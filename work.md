---
title: Our Work
layout: default
show_categories: true
---

{% assign categories = site.category_pages |
    where_exp:"item","item.show_categories != false" | sort: "index" %}

# Our Work

{% for category in categories %}
{% include category_preview.html category=category %} {% endfor %}
