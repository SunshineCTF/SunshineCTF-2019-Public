# For the SunshineCTF 2019 archive (ctf.hackucf.org)
PUBLISH := ports.md

#####
# publish_port($1: directory)
#
# Generate build rules to publish a port.txt file that contains the challenge's port number.
# This is used by the archive site to display each challenge's connection port.
#####
define _publish_port

# Publish port.txt, which needs to be rebuilt if this Build.mk file changes
publish/$1/port.txt: $1/Build.mk
	$$(_V)echo "Publishing $1/port.txt with port $$($1+DOCKER_PORTS)"
	$$(_v)mkdir -p $$(@D) && echo "$$($1+DOCKER_PORTS)" > $$@

publish[$1]: publish/$1/port.txt

endef #_publish_port
publish_port = $(eval $(call _publish_port,$1))


# SunshineCTF archive: top-level `check` support.
#
# `pwnmake check`      runs the QUICK challenge solvers and verifies each prints its flag.
# `pwnmake check-full` runs ALL solvers, including slow ones (padding oracles, genetic /
#                      brute-force / probabilistic exploits, etc.).
# `pwnmake check[<dir>]` checks a single challenge (slow ones included).
# Pass `REMOTE=1` to test against the real archive server instead of local containers.
#
#     pwnmake check              # quick solvers only, local
#     pwnmake check-full         # everything, including slow solvers
#     pwnmake check REMOTE=1     # quick solvers against the live server
#     pwnmake check[Pwn/flock]   # just one challenge
#
# Locally a check brings its challenge up itself (PwnableHarness challenges via docker
# run, docker-compose challenges via `docker compose up`), waits for it to answer, runs
# the solver, then tears it back down -- so `pwnmake check[-full]` is self-contained and
# needs no separate deploy step. (To HOST the challenges for players instead, use
# `pwnmake docker-start` / `docker-stop`, which leave them running.)
#
# Each hosted challenge's Build.mk registers itself with one of:
#   $(call ctf_check,$(DIR),$(DOCKER_PORTS),<cmd>)        PwnableHarness TCP challenge
#   $(call ctf_check_tcp,$(DIR),<port>,<cmd>)             docker-compose TCP challenge
#   $(call ctf_check_web,$(DIR),<port>,<subdomain>,<cmd>) docker-compose web challenge
# and the matching *_slow variants for slow solvers (registered under check-full only).
#
# The solve command runs from the challenge dir with $HOST/$PORT (and $URL for web) set;
# it must print the flag to stdout. The check passes iff the output contains flag.txt.
# The challenge's own build/ and published files are reachable from the solver via the
# `.build/` and `publish/` symlinks the check creates in the challenge dir (so solvers
# read `.build/<binary>` and `publish/<libc>` rather than needing artifacts copied in).
# CHECK_TIMEOUT (default 120s) bounds each solver run; slow challenges raise it.

.PHONY: check check-full
check:
check-full:

# Hostname used for REMOTE=1 TCP checks (web challenges pass their own subdomain).
CTF_REMOTE_HOST ?= ctf.hackucf.org

# Per-solver time limit (seconds).
CHECK_TIMEOUT ?= 120

# Default so `$(if $(REMOTE),...)` doesn't warn when REMOTE is unset.
REMOTE ?=

#####
# _ctf_check_impl($1: dir, $2: port, $3: cmd, $4: remote host, $5: start deps, $6: url,
#                 $7: slow?, $8: teardown command, $9: kind [ph|ctcp|web])
#####
define _ctf_check_impl
.PHONY: check[$1]
check-full: check[$1]
$(if $7,,check: check[$1])
check[$1]: $5
	$$(_V)echo "===== [check] $1 ($(if $(REMOTE),$4,localhost):$2)"
	$$(_v)flag="$$$$(cat $1/flag.txt 2>/dev/null | tr -d '\n')"; \
		$(if $(REMOTE),,ws="$$$$(pwd)"; \
			ln -srfn "$$$$ws/$$($1+BUILD)" "$1/.build" 2>/dev/null || true; \
			ln -srfn "$$$$ws/$(PUB_DIR)/$1" "$1/publish" 2>/dev/null || true; \
			$(if $(filter web,$9),\
				for _i in $$$$(seq 1 90); do code=$$$$(curl -s -o /dev/null -w '%{http_code}' --max-time 3 http://localhost:$2); echo "$$$$code" | grep -qE '^[234]' && break; sleep 1; done,\
				for _i in $$$$(seq 1 45); do python3 -c "import socket; socket.create_connection(('localhost'$(COMMA)$2)$(COMMA)1).close()" >/dev/null 2>&1 && break; sleep 1; done$(if $(filter ctcp,$9),; sleep 4)) ;) \
		out="$$$$(cd $1 && HOST=$(if $(REMOTE),$4,localhost) PORT=$2 URL=$6 timeout $$(CHECK_TIMEOUT) $3 2>&1)" || true; \
		$(if $(REMOTE),,$8 || true;) \
		if [ -n "$$$$flag" ] && printf '%s' "$$$$out" | grep -qF "$$$$flag"; then \
			echo "[PASS] $1"; \
		else \
			echo "[FAIL] $1 — flag not found in solver output:"; \
			printf '%s\n' "$$$$out" | tail -25; \
			exit 1; \
		fi
endef

# PwnableHarness TCP challenge: built + started (docker run) and torn down automatically.
ctf_check      = $(eval $(call _ctf_check_impl,$1,$2,$3,$$(CTF_REMOTE_HOST),$(if $(REMOTE),,publish-one[$1] docker-start-one[$1]),$(if $(REMOTE),https://$$(CTF_REMOTE_HOST),http://localhost:$2),,$$(DOCKER) rm -f $$($1+DOCKER_CONTAINER) >/dev/null 2>&1,ph))
ctf_check_slow = $(eval $(call _ctf_check_impl,$1,$2,$3,$$(CTF_REMOTE_HOST),$(if $(REMOTE),,publish-one[$1] docker-start-one[$1]),$(if $(REMOTE),https://$$(CTF_REMOTE_HOST),http://localhost:$2),slow,$$(DOCKER) rm -f $$($1+DOCKER_CONTAINER) >/dev/null 2>&1,ph))

# docker-compose TCP challenge: `docker compose up/down` automatically (+grace for warmup).
ctf_check_tcp      = $(eval $(call _ctf_check_impl,$1,$2,$3,$$(CTF_REMOTE_HOST),$(if $(REMOTE),,docker-start-one[$1]),$(if $(REMOTE),https://$$(CTF_REMOTE_HOST),http://localhost:$2),,cd $1 && docker compose down >/dev/null 2>&1,ctcp))
ctf_check_tcp_slow = $(eval $(call _ctf_check_impl,$1,$2,$3,$$(CTF_REMOTE_HOST),$(if $(REMOTE),,docker-start-one[$1]),$(if $(REMOTE),https://$$(CTF_REMOTE_HOST),http://localhost:$2),slow,cd $1 && docker compose down >/dev/null 2>&1,ctcp))

# docker-compose web challenge ($4 = remote subdomain): `docker compose up/down`.
ctf_check_web      = $(eval $(call _ctf_check_impl,$1,$2,$4,$3,$(if $(REMOTE),,docker-start-one[$1]),$(if $(REMOTE),https://$3,http://localhost:$2),,cd $1 && docker compose down >/dev/null 2>&1,web))
ctf_check_web_slow = $(eval $(call _ctf_check_impl,$1,$2,$4,$3,$(if $(REMOTE),,docker-start-one[$1]),$(if $(REMOTE),https://$3,http://localhost:$2),slow,cd $1 && docker compose down >/dev/null 2>&1,web))
