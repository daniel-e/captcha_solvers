DST = $(CAPTCHA_SOLVER_G)

# ------------------------------------

# CONSTANT INPUT DATA
CAPTCHA_IMAGE = data/captcha/cactus.jpeg

# BINARIES, SCRIPTS
FROM_CAPTCHA_BIN = bin/from_captcha.py

# GENRATED OUTPUTS / INPUTS
CAPTCHA_IMAGES_PATH = $(DST)/unknown_images

# ------------------------------------

all: check from_captcha

check:
	@if [ -z $(DST) ]; then echo "Please set the CAPTCHA_SOLVER_G environment variable"; exit 1; fi
	@mkdir -p $(DST)

# -----------------------------------------------------------------------------------------------------

from_captcha: $(CAPTCHA_IMAGES_PATH)

$(CAPTCHA_IMAGES_PATH): $(FROM_CAPTCHA_BIN) $(CAPTCHA_IMAGE)
	@rm -rf $(CAPTCHA_IMAGES_PATH)
	@mkdir -p $(CAPTCHA_IMAGES_PATH)
	@echo "Extracting images from captcha ..."
	@for y in 0 1 2; do \
		for x in 0 1 2; do \
		$(FROM_CAPTCHA_BIN) -i $(CAPTCHA_IMAGE) -o $(CAPTCHA_IMAGES_PATH)/y$$y.x$$x.jpg -y $$y -x $$x; done; \
	done
