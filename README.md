# [meziklasi.cz](http://meziklasi.cz/)

This repository contains the source code to [meziklasi.cz](http://meziklasi.cz/), dedicated to the legendary Czech village [Meziklasí](https://en.wikipedia.org/wiki/Meziklas%C3%AD). Code of site is published under GPLv3 license and site content
under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Local setup

### Prerequisites
- Ruby (tested on 2.7)
- Bundler (`gem install bundler`)
- Jekyll (`gem install jekyll`)
- Gems that Meziklasí relies on (`bundle update`)
- Node.js

For image generation, `libvips` is required. This can be installed with `apt` by executing `sudo apt install libvips libvips-dev libvips-tools` or on other platforms as described in [`libvips`'s docs](https://www.libvips.org/install.html).

### Development
To start the development server, you can run the following command and then go to [localhost:4000](http://localhost:4000/).
```
bundle exec jekyll serve
```

Commits are automatically deployed using GitHub actions.
