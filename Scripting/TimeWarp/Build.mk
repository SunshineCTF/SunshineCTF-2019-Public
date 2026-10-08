# Name of the challenge executable to build
TARGETS := timewarp numbergen

CFLAGS := -Wall -Wextra -Wno-unused-parameter

timewarp_SRCS := TimeWarp.c
numbergen_SRCS := numbergen.c

# Originally ran on the default PwnableHarness base image (ubuntu 16.04).
# The solver's numbergen helper depends on this runtime.
UBUNTU_VERSION := 16.04

# Build a Docker image that exposes the challenge on port 19201
DOCKER_IMAGE := sun19-timewarp
# Only the challenge itself is served; numbergen is a local solver helper
DOCKER_RUNTIME_NAME := timewarp
DOCKER_PORTS := 19201

# Publish the port number as port.txt
$(call publish_port,$(DIR))

# `pwnmake check`: run the solver (uses the built numbergen helper) and verify the flag
$(call ctf_check,$(DIR),$(DOCKER_PORTS),python3 solve.py)
