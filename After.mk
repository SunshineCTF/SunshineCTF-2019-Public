# Generate rules for merging the nginx configs if there are any present
ifdef NGINX_CONFIGS

NGINX_CONF := $(BUILD)/$(DIR)/nginx.conf
NGINX_DEST := /etc/nginx/conf.d/sunshinectf-2019.conf

$(NGINX_CONF): $(NGINX_CONFIGS)
	$(_V)echo "Merging nginx configs"
	$(_v)cat $^ > $@

$(NGINX_DEST): $(NGINX_CONF)
	$(_V)echo "Applying merged nginx config"
	$(_v)cat $< | sudo tee $@ >/dev/null && sudo systemctl reload nginx

deploy-nginx: $(NGINX_DEST)

.PHONY: deploy-nginx

deploy: deploy-nginx

else #NGINX_CONFIGS

$(warning NGINX_CONFIGS is empty)

endif #NGINX_CONFIGS
