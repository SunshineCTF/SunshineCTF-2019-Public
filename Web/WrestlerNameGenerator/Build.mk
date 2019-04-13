DOCKER_IMAGE := namegen
DOCKER_IMAGE_CUSTOM := 1
DOCKER_BUILD_ARGS := --build-arg "FLAG=`cat $(DIR)/flag.txt`"
DOCKER_PORT_ARGS := -p 127.0.0.1:19507:80
DOCKER_RUN_ARGS := -v /var/run

PUBLISH := port.txt

$(call nginx_conf,$(DIR)/nginx.conf)
