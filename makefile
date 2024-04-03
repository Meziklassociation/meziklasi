SHELL=/bin/fish

.PHONY: run

run:
	bundle exec jekyll serve --trace --drafts

deploy: clean build upload

clean:
	bundle exec jekyll clean --trace

build:
	bundle exec jekyll build --trace
	tree -C -d | sed 's/^/                    /'

upload:
	scripts/upload

install:
	gem install bundler
	bundle config set --local path '.vendor/bundle'
	bundle install

