#!/bin/bash
# Runs during pwnmake image initialization. Installs the python modules the
# challenge solver scripts need so `pwnmake check` can run them in the container.
set -e
apt-get update
apt-get install -y --no-install-recommends \
	python3-pwntools \
	python3-requests \
	python3-pil \
	python3-pycryptodome

# docker compose v2 plugin + a `docker-compose` shim, so `pwnmake` can bring the
# docker-compose challenges up/down from inside the pwnmake container (used by the
# compose check macros' auto-start/teardown).
COMPOSE_VERSION=v2.29.7
PLUGIN_DIR=/usr/libexec/docker/cli-plugins
mkdir -p "$PLUGIN_DIR"
if [ ! -x "$PLUGIN_DIR/docker-compose" ]; then
	curl -fsSL "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-linux-x86_64" \
		-o "$PLUGIN_DIR/docker-compose"
	chmod +x "$PLUGIN_DIR/docker-compose"
fi
cat > /usr/local/bin/docker-compose <<'SH'
#!/bin/sh
exec docker compose "$@"
SH
chmod +x /usr/local/bin/docker-compose
