DOCKER_IMAGE := wrestlerbook
DOCKER_IMAGE_CUSTOM := 1
DOCKER_PORT_ARGS := -p 127.0.0.1:19506:80
DOCKER_RUN_ARGS := -v /var/run

PUBLISH := port.txt

$(call nginx_conf,$(DIR)/nginx.conf)
