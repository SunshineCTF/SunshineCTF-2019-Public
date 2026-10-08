# Name of program to build
TARGET := return-to-mania

# Build as a 32-bit binary (solve expects 32-bit addresses / 4-byte p32)
BITS := 32

# Compiler mitigations and other settings
NX := 1
ASLR := 1

# Originally ran on the default PwnableHarness base image (ubuntu 16.04)
UBUNTU_VERSION := 16.04

# Deployment settings
DOCKER_IMAGE := sun19-return-to-mania
DOCKER_PORTS := 19001
DOCKER_TIMELIMIT := 30

# Files to publish
PUBLISH_BUILD := $(TARGET)

# Publish the port number as port.txt
$(call publish_port,$(DIR))

# `pwnmake check`: run the exploit and verify it prints the flag
$(call ctf_check,$(DIR),$(DOCKER_PORTS),python3 solve.py)
