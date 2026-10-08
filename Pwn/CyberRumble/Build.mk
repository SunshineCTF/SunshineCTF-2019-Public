TARGET := CyberRumble

BITS := 64
ASLR := 1
NX := 1
CANARY := 1
RELRO := 1
# DEBUG := 1
STRIP := 1

# Originally ran on the default PwnableHarness base image (ubuntu 16.04)
UBUNTU_VERSION := 16.04

DOCKER_IMAGE := sun19-cyberrumble
DOCKER_PORTS := 19002
DOCKER_TIMELIMIT := 30

PUBLISH_BUILD := $(TARGET)

# Publish the port number as port.txt
$(call publish_port,$(DIR))

# `pwnmake check`: run the exploit and verify it prints the flag
$(call ctf_check,$(DIR),$(DOCKER_PORTS),python3 solve.py)
