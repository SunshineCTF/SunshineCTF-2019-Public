# Name of program to build
TARGET := return-to-mania

# Compiler mitigations and other settings
NX := 1
ASLR := 1

# Deployment settings
DOCKER_IMAGE := return-to-mania
DOCKER_PORTS := 19001
DOCKER_TIMELIMIT := 30

# Files to publish
PUBLISH := $(TARGET)

# For archive.sunshinectf.org: Publish the port number as port.txt
$(call publish_port,$(DIR))
