# Don't recurse into build/publish output. `pwnmake check` leaves `.build` and
# `publish` symlinks in each challenge dir, and published copies of a challenge
# (including its Build.mk) would otherwise be picked up as duplicate projects.
RECURSION_BLACKLIST += %/publish %/.build

# Resource limits for the PwnableHarness challenge containers. PwnableHarness
# already caps CPU (0.5) and memory (500m) by default; also cap the number of
# processes, since many challenges hand players a shell. PwnableHarness has no
# setting of its own for that, so the flag rides along with the CPU limit
# (passed as `--cpus=$(DOCKER_CPULIMIT)`). A challenge that sets its own
# DOCKER_CPULIMIT must add --pids-limit itself.
DEFAULT_DOCKER_CPULIMIT := 0.5 --pids-limit=512
