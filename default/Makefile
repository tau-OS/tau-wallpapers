WP_DIR=$(DESTDIR)/usr/share/backgrounds/tauos
GNOME_BG_DIR=$(DESTDIR)/usr/share/gnome-background-properties
# PLASMA_BG_DIR=$(DESTDIR)/usr/share/plasma/desktoptheme
# KDE_BG_DIR=$(DESTDIR)/usr/share/wallpapers
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

	for name in *.jpg *.png; do \
		$(INSTALL) $${name}	$(WP_DIR)/default/$${name} ; \
    done;
	
	#~ GNOME background
	$(MKDIR) $(GNOME_BG_DIR)
	$(INSTALL) gnome-backgrounds-tau.xml	$(GNOME_BG_DIR)/tau.xml

	#~ KDE and Plasma background
	# $(MKDIR) $(KDE_BG_DIR)/tauos/contents/images
	# $(INSTALL) tau-metadata.desktop $(KDE_BG_DIR)/tauos/metadata.desktop
	# for res in 1280x1024 \
	# 	     640x480 800x600 1024x768 1152x864 1200x900 1280x960 1440x1080 1600x1200 1600x1280 1920x1440 2048x1536 \
	# 	     800x480 1024x600 1152x720 1280x720 1280x768 1280x800 1366x768 1440x900 1680x1050 1920x1080 1920x1200 1920x1280 \
	# 	     2160x1440 2304x1440 2560x1440 2560x1600 2960x1440 3000x2000 3200x1800  3440x1440 3840x2160; do \
	# 		 $(LN_S) ../../../../backgrounds/tauos/default/tau.png \
	#          	$(KDE_BG_DIR)/tauos/contents/images/$${res}.png ; \
	# done; \
	# $(MKDIR) $(PLASMA_BG_DIR)/tauos
	# $(INSTALL) tau-metadata.desktop	$(PLASMA_BG_DIR)/tauos/metadata.desktop

	# for name in *.jpg *png; do \
	# 	$(LN_S) ../../../../backgrounds/tauos/default/$${name} \
	# 			$(KDE_BG_DIR)/tauos/contents/images/$${name} ; \
    # done;
