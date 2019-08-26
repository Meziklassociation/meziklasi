# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "meziklasi"
  spec.version       = "0.1.0"
  spec.authors       = ["Tomas Slama", "Jan Cerny"]
  spec.email         = ["tomas@slama.dev"]

  spec.summary       = "A theme developed for the meziklasi.cz website."
  spec.homepage      = "http://meziklasi.cz/"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README)!i) }

  spec.add_runtime_dependency "jekyll", "~> 3.8"

  spec.add_development_dependency "bundler", "~> 1.16"
  spec.add_development_dependency "rake", "~> 12.0"
end
