SHELL=/bin/fish

.PHONY: clean build deploy upload

deploy: clean build upload

clean:
	bundle exec jekyll clean --trace

build:
	bundle exec jekyll build --trace
	tree -C -d | sed 's/^/                    /'

upload:
	scripts/upload
