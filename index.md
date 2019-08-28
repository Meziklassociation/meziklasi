---
layout: default
title: Úvodní stránka
order: 0
---

## Vítejte v Meziklasí!

{{ site.description }}

### Nedávno přidané články
{% for post in site.posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) ({{ post.category | downcase }}; {{ post.date | date: "%-d. %-m. %Y" }})
{% endfor %}

[Více článků...](/clanky/)
