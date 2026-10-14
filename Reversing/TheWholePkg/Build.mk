# Handout-only challenge: no build or server, just the packaged Windows binary
# players download (served from publish/ at /files/...).
#
# Strategy_Vault-win.exe (22 MB) is kept xz-compressed in git; publishing
# decompresses it so players download the .exe itself (the web server
# compresses in transit).
$(BUILD_DIR)/Strategy_Vault-win.exe: $(DIR)/attachments/Strategy_Vault-win.exe.xz
	$(_V)echo "Unpacking $(@F)"
	$(_v)mkdir -p $(@D) && xz -dc $< > $@

PUBLISH_BUILD := Strategy_Vault-win.exe
