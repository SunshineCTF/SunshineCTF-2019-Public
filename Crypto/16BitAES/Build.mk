# docker-compose TCP challenge (no build product, so this Build.mk only registers
# the check). `pwnmake check` starts it, runs the solver, and tears it down.
$(call ctf_check_tcp,$(DIR),19401,python3 solve.py)
