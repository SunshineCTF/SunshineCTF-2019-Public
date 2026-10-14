# Handout-only challenge: no build or server, just the SD card image players
# download (served from publish/ at /files/...).
#
# file.img (50 MB) is kept xz-compressed in git; publishing decompresses it so
# players download the image itself. A pre-compressed file.img.gz is published
# next to it: the web server serves it transparently (Content-Encoding: gzip)
# to clients that accept gzip, which cuts the transfer to ~19 MB while the
# browser still saves a plain file.img.
$(BUILD_DIR)/file.img: $(DIR)/attachments/file.img.xz
	$(_V)echo "Unpacking $(@F)"
	$(_v)mkdir -p $(@D) && xz -dc $< > $@

$(BUILD_DIR)/file.img.gz: $(BUILD_DIR)/file.img
	$(_V)echo "Pre-compressing $(@F) for the web server"
	$(_v)gzip -9n -c $< > $@

PUBLISH_BUILD := file.img file.img.gz
