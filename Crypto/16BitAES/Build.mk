DOCKER_IMAGE := 16-bit-aes
DOCKER_IMAGE_CUSTOM := 1
DOCKER_PORTS := 19003

# For archive.sunshinectf.org: Publish the port number as port.txt
$(call publish_port,$(DIR))
