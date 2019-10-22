---
layout: default
title: Články
order: 2
---

{% assign sorted_categories = site.categories | sort %}
{% for category in sorted_categories %}
<div id="{{ category | first | downcase }}">
  <h2>{{ category | first }}</h2>
</div>
  {% assign sorted_posts = category.last | sort: "date" | reverse %}
  {% for post in sorted_posts %}
- [{{ post.title }}]({{ post.url }}) ({{ post.date | date: "%-d. %-m. %Y" }})
  {% endfor %}
{% endfor %}
