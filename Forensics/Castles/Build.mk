# Handout-only challenge: no build or server, just the disk image players
# download (served from publish/ at /files/...).
#
# Castles.001 is a 119 MB raw disk image. In git it is kept xz-compressed and
# split into parts under 50 MB; publishing joins the parts and decompresses it,
# so players download the image itself (the web server compresses in transit).
CASTLES_PARTS := $(sort $(wildcard $(DIR)/attachments/Castles.001.xz.part-*))

$(BUILD_DIR)/Castles.001: $(CASTLES_PARTS)
	$(_V)echo "Unpacking $(@F) from $(words $^) xz parts"
	$(_v)mkdir -p $(@D) && cat $^ | xz -dc > $@

PUBLISH_BUILD := Castles.001
