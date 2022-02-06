WP_DIR=$(DESTDIR)/usr/share/backgrounds/tauos
GNOME_BG_DIR=$(DESTDIR)/usr/share/gnome-background-properties
MKDIR=/bin/mkdir -p
INSTALL=/usr/bin/install -p -m644 -D
LN_S=/bin/ln -s

all:

install:
	$(MKDIR) $(WP_DIR)/default
	#~ Base background
	# for tod in 01-day 02-night; do \
	#    $(INSTALL) $(WP_NAME)-$${tod}.png	$(WP_DIR)/default/$(WP_NAME)-$${tod}.png ; \
	# done;

	for name in *.jpg; do \
		$(INSTALL) $${name}	$(WP_DIR)/default/$${name} ; \
    done;
	
	$(INSTALL) tau.png	$(WP_DIR)/default/tau.png
	
	#~ GNOME background
	$(MKDIR) $(GNOME_BG_DIR)
	$(INSTALL) gnome-backgrounds-tau.xml	$(GNOME_BG_DIR)/tau.xml