outputs := html epub

course := $(shell cat course.txt)
repo := $(shell git config --get remote.origin.url)
index := src/index.md
welcome := src/welcome.md
markdown := $(filter-out $(welcome) $(index), $(shell find src -name "*.md" | sort -t- -k2 -n))
includes := src/includes.html
metadata := src/metadata.yml

# basic rules
all: $(outputs)

clean:
	rm -rf build

.PHONY: all clean deploy $(outputs)

define \n


endef

define INSTALL_TARGET
$(1): $(2)
	@mkdir -p $$(@D)
	install -m$(3) $$< $$@
endef

# mathjax rules
MathJax/.git:
	git submodule update --init $(@D)

MathJax: MathJax/.git

# simple directories
copy_directories := stylesheets media images

$(foreach directory, $(copy_directories), \
	$(eval $(directory) := $(wildcard $(directory)/*)))

$(foreach directory, $(copy_directories), \
	$(foreach output, $(outputs), \
		$(eval $(call INSTALL_TARGET, \
			build/$(output)/$(directory)/%, $(directory)/%, 644))))

$(foreach directory, $(copy_directories), \
	$(foreach output, $(outputs), \
		$(eval $(output)_$(directory) := $(addprefix build/$(output)/, $($(directory))))))

# javascript/coffeescript rules
js_source := $(wildcard js-src/*.js)
cs_source := $(wildcard js-src/*.coffee)
javascript := $(patsubst js-src/%, build/js/%, $(js_source)) $(patsubst js-src/%.coffee, build/js/%.js, $(cs_source))

ifeq ($(shell command -v uglifyjs),)
$(eval $(call INSTALL_TARGET, build/js/%.js, js-src/%.js, 644))

build/js/%.js: js-src/%.coffee
	coffee --output $(@D) --compile $<
else
build/js/%.js: js-src/%.js
	@mkdir -p $(@D)
	uglifyjs $< --output $@ --mangle

build/js/%.js: js-src/%.coffee
	@mkdir -p $(@D)
	coffee --print --compile $< | uglifyjs - --output $@ --mangle
endif

$(foreach output, $(outputs), \
	$(eval $(call INSTALL_TARGET, build/$(output)/js/%, build/js/%, 644)))

$(foreach output, $(outputs), \
	$(eval $(output)_js := $(patsubst build/js/%, build/$(output)/js/%, $(javascript))))

# so we don't have to rebuild them for different outputs
.PRECIOUS: build/js/%.js

# html rules
html_files := $(patsubst src/%.md, build/html/%.html, $(index) $(welcome) $(markdown))
standalone_html_files := $(patsubst src/%.md, build/html/%-st.html, $(markdown))

build/welcome.md: $(welcome) $(markdown)
	@mkdir -p $(@D)
	install -m 644 $< $@
	echo "\n### Contents" >> $@
	$(foreach file, $(markdown), \
		head -1 $(file) | sed 's/^\#*[[:space:]]*\(.*\)/1. [\1](#$(patsubst src/%.md,%.html, $(file)))/' >> $@${\n}\
	)

build/html/welcome.html: build/welcome.md
	@mkdir -p $(@D)
	pandoc --write=html5 --output=$@ --smart --mathjax $<

build/html/index.html: $(index) src/index.layout
	@mkdir -p $(@D)
	pandoc --template=src/index.layout --write=html5 --output=$@ --smart --standalone $<

build/html/%.html: src/%.md
	@mkdir -p $(@D)
	pandoc --write=html5 --output=$@ --smart --mathjax $<

build/html/%-st.html: src/%.md src/includes.html
	@mkdir -p $(@D)
	pandoc --write=html5 --output=$@ --smart --standalone \
		--mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML" \
		--css=stylesheets/pandoc.css --include-in-header=src/includes.html $<

html: $(html_stylesheets) $(html_media) $(html_images) $(html_js) $(html_files) $(standalone_html_files)

# epub rules
# build/epub/intermediate.epub: $(metadata) stylesheets/pandoc.css $(markdown)
# 	@mkdir -p $(@D)
# 	pandoc --write=epub3 --output=$@ --smart --mathml --epub-stylesheet=stylesheets/pandoc.css $(metadata) $(markdown)

# build/epub/output.epub: build/epub/intermediate.epub MathJax $(includes) $(javascript) utils/post-process-epub.py
# 	python utils/post-process-epub.py --output=$@ --input=$< --include-in-headers=$(includes) --mathjax=MathJax $(javascript)

# epub: build/epub/output.epub

# deploy targets
# EPUB := build/html/downloads/$(course)-$(shell date +%Y%m%d).epub
# $(EPUB): build/epub/output.epub
# 	@mkdir -p $(@D)
# 	@rm -f $(@D)/$(course)-*.epub
# 	install -m 644 $< $@

downloadepubjs := build/html/js/downloadepub.js

$(downloadepubjs):
	@mkdir -p $(@D)
	echo "function DownloadEpub(){window.open(\"$(patsubst build/html/%, %, $(EPUB))\");}" > $@

gotorepojs := build/html/js/gotorepo.js
$(gotorepojs):
	@mkdir -p $(@D)
	echo "function GotoRepo(){window.location=\"$(shell echo $(repo) | sed -e 's+^git@github.com:+https://github.com/+' -e 's+.git$$++')\";}" > $@

deploy: html $(EPUB) $(downloadepubjs) $(gotorepojs)
	rm -rf build/html/.git
	git init build/html
	git --git-dir=build/html/.git remote add origin $(repo)
	git --git-dir=build/html/.git --work-tree=build/html add .
	git --git-dir=build/html/.git commit -m 'Update Website'
	git --git-dir=build/html/.git push --force origin master:gh-pages
