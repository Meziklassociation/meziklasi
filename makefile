SHELL=/bin/fish

clean:
	bundle exec jekyll clean --trace

deploy: clean
	bundle exec jekyll build --trace
	tree -C -d
	scripts/upload
