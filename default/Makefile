WP_DIR=$(DESTDIR)/usr/share/backgrounds/tauos
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
	$(INSTALL) tau.png	$(WP_DIR)/default/tau.png
	
	#~ GNOME background
	$(MKDIR) $(GNOME_BG_DIR)
	$(INSTALL) gnome-backgrounds-tau.xml	$(GNOME_BG_DIR)/tau.xml