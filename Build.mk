# For archive.sunshinectf.org
PUBLISH := ports.md

#####
# publish_port($1: directory)
#
# Generate build rules to publish a port.txt file that contains the challenge's port number.
#####
define _publish_port

# Publish port.txt, which needs to be rebuilt if this Build.mk file changes
publish/$1/port.txt: $1/Build.mk
	$$(_V)echo "Publishing $1/port.txt with port $$($1+DOCKER_PORTS)"
	$$(_v)mkdir -p $$(@D) && echo "$$($1+DOCKER_PORTS)" > $$@

publish[$1]: publish/$1/port.txt

endef #_publish_port
publish_port = $(eval $(call _publish_port,$1))


# List of nginx config files
NGINX_CONFIGS :=

#####
# nginx_conf($1: nginx config file)
#
# Upon deployment, this nginx config file will be used by nginx.
#####
define _nginx_conf

NGINX_CONFIGS := $$(NGINX_CONFIGS) $1

endef #_nginx_conf
nginx_conf = $(eval $(call _nginx_conf,$1))
