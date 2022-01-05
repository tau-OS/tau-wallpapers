WP_NAME=tau-wallpapers
WP_DIR=$(DESTDIR)/usr/share/backgrounds/$(WP_NAME)
GNOME_BG_DIR=$(DESTDIR)/usr/share/gnome-background-properties
MKDIR=/bin/mkdir -p
INSTALL=/usr/bin/install -p -m644 -D

all:

install:
	$(MKDIR) $(WP_DIR)/default
	#~ Base background
	# for tod in 01-day 02-night; do \
	#    $(INSTALL) $(WP_NAME)-$${tod}.png	$(WP_DIR)/default/$(WP_NAME)-$${tod}.png ; \
	# done;
	$(INSTALL) $(WP_NAME).png	$(WP_DIR)/default/$(WP_NAME).png
	
	#~ GNOME background
	$(MKDIR) $(GNOME_BG_DIR)
	$(INSTALL) gnome-backgrounds-$(WP_NAME).xml	$(GNOME_BG_DIR)/$(WP_NAME).xml