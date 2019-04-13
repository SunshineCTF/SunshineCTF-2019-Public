DOCKER_IMAGE := portfolio
DOCKER_IMAGE_CUSTOM := 1
DOCKER_PORT_ARGS := -p 127.0.0.1:19509:5000
DOCKER_RUN_ARGS := -v /var/run

PUBLISH := port.txt

$(call nginx_conf,$(DIR)/nginx.conf)
