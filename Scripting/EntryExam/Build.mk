# docker-compose web challenge (Flask; no build product, so this Build.mk only
# registers the check). `pwnmake check` starts it, runs the solver, and tears it down.
$(call ctf_check_web,$(DIR),19202,entryexam.ctf.hackucf.org,python3 solve.py)
