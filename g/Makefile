DST = /tmp/gdata

# -----------------------------------------------------------------------------

# CONSTANT INPUT DATA
CAPTCHA_IMAGE = data/captcha/cactus.jpeg
IMAGES = data/images

# BINARIES, SCRIPTS
FROM_CAPTCHA_BIN = bin/from_captcha.py
DATASET_BIN = bin/build_dataset.py

# GENERATED OUTPUTS / INPUTS
CAPTCHA_IMAGES_PATH = $(DST)/unknown_images
DATASET_PATH = $(DST)/dataset

# -----------------------------------------------------------------------------

all: from_captcha dataset

clean:
	rm -rf $(DST)

# -----------------------------------------------------------------------------

from_captcha: $(CAPTCHA_IMAGES_PATH)

$(CAPTCHA_IMAGES_PATH): $(FROM_CAPTCHA_BIN) $(CAPTCHA_IMAGE)
	@rm -rf $@
	@mkdir -p $@
	@echo "Extracting images from captcha ..."
	@for y in 0 1 2; do \
		for x in 0 1 2; do \
		$(FROM_CAPTCHA_BIN) -i $(CAPTCHA_IMAGE) -o $(CAPTCHA_IMAGES_PATH)/y$$y.x$$x.jpg -y $$y -x $$x; done; \
	done

# -----------------------------------------------------------------------------

dataset: $(DATASET_PATH)

$(DATASET_PATH): $(DATASET_BIN) $(IMAGES)
	@echo "Creating dataset ..."
	@rm -rf $@
	@$(DATASET_BIN) -i $(IMAGES) -o $@
