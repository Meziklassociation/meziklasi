# [meziklasi.cz](http://meziklasi.cz/)

This repository contains the source code to [meziklasi.cz](http://meziklasi.cz/), dedicated to the legendary Czech village [Meziklasí](https://en.wikipedia.org/wiki/Meziklas%C3%AD).

## Local setup

### Prerequisites
- Ruby (tested on 2.7)
- Bundler (`gem install bundler`)
- Jekyll (`gem install jekyll`)

### Development
To start the development server, you can simple execute the following command and then go to [localhost:4000](http://localhost:4000/).
```
bundle exec jekyll serve
```

### Production
To build the site, execute

```
bundle exec jekyll build
```

and Jekyll will create a `_site` directory in which will be all the static assets. This is the directory which should be deployed to production.