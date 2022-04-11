SUBDIRS = default
VERSION = 1.1
NAME =  tau-wallpapers-$(VERSION)

all:
	@for i in $(SUBDIRS) ; do \
		(cd $$i; $(MAKE)) ;\
	done;

install:
	@for i in $(SUBDIRS) ; do \
		(cd $$i; $(MAKE) install) ; \
	done;