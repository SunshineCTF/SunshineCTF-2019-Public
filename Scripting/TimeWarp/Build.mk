# Name of the challenge executable to build
TARGETS := timewarp numbergen

CFLAGS := -Wall -Wextra -Wno-unused-parameter

timewarp_SRCS := TimeWarp.c
numbergen_SRCS := numbergen.c

# Build a Docker image named "timewarp" that exposes the challenge on port 19004
DOCKER_IMAGE := timewarp
DOCKER_PORTS := 19004

# For archive.sunshinectf.org: Publish the port number as port.txt
$(call publish_port,$(DIR))
