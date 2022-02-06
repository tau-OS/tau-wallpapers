SUBDIRS = default
VERSION = 1.0.0
NAME =  tau-wallpapers
TAG=$(NAME)-$(VERSION)

all:
	@for i in $(SUBDIRS) ; do \
		(cd $$i; $(MAKE)) ;\
	done;

install:
	@for i in $(SUBDIRS) ; do \
		(cd $$i; $(MAKE) install) ; \
	done;

tag:
	@git tag -a -f -m "Tag as $(TAG)" -f $(TAG)
	@echo "Tagged as $(TAG)"

archive: tag
	@git archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD > $(TAG).tar
	@gzip -f $(TAG).tar
	@echo "$(TAG).tar.gz created" 
	@sha1sum $(TAG).tar.gz > $(TAG).sha1sum

