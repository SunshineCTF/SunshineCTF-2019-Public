# docker-compose web challenge (Django/nginx/postgres/rabbitmq; this Build.mk only
# registers the check). Two flags: solve.py checks flag 2 (flag.txt holds flag 2);
# flag 1's solve needs external infrastructure, so it is not checked here.
# `pwnmake check` starts the stack, runs the solver, and tears it down.
$(call ctf_check_web,$(DIR),19303,enterthepolygon.ctf.hackucf.org,python3 solve.py)
