# Handout-only challenge: no build or server, just the packaged Windows binary
# players download (served from publish/ at /files/...).
#
# Strategy_Vault-win.exe (22 MB) is kept xz-compressed in git; publishing
# decompresses it so players download the .exe itself. A pre-compressed .gz is
# published next to it: the web server serves it transparently
# (Content-Encoding: gzip) to clients that accept gzip, cutting the transfer
# to ~8 MB while the browser still saves a plain .exe.
$(BUILD_DIR)/Strategy_Vault-win.exe: $(DIR)/attachments/Strategy_Vault-win.exe.xz
	$(_V)echo "Unpacking $(@F)"
	$(_v)mkdir -p $(@D) && xz -dc $< > $@

$(BUILD_DIR)/Strategy_Vault-win.exe.gz: $(BUILD_DIR)/Strategy_Vault-win.exe
	$(_V)echo "Pre-compressing $(@F) for the web server"
	$(_v)gzip -9n -c $< > $@

PUBLISH_BUILD := Strategy_Vault-win.exe Strategy_Vault-win.exe.gz
