# Handout-only challenge: no build or server, just the SD card image players
# download (served from publish/ at /files/...).
#
# file.img (50 MB) is kept xz-compressed in git; publishing decompresses it so
# players download the image itself (the web server compresses in transit).
$(BUILD_DIR)/file.img: $(DIR)/attachments/file.img.xz
	$(_V)echo "Unpacking $(@F)"
	$(_v)mkdir -p $(@D) && xz -dc $< > $@

PUBLISH_BUILD := file.img
