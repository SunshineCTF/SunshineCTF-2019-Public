TARGET := CyberRumble

BITS := 64
ASLR := 1
NX := 1
CANARY := 1
RELRO := 1
# DEBUG := 1
STRIP := 1

DOCKER_IMAGE := cyberrumble
DOCKER_PORTS := 19002
DOCKER_TIMELIMIT := 30
DOCKER_BUILD_DEPS := $(DIR)/flag

PUBLISH := $(TARGET)

# For archive.sunshinectf.org: Publish the port number as port.txt
$(call publish_port,$(DIR))
