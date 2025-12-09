---
title: Interactives
date: 2024-03-01 00:01:00 Z
categories:
  - civic-tech
description: These visualizations allow you to explore concepts like compactness and proportionality.
image: "/uploads/dsf.gif"

---

These visualizations allow you to explore concepts like compactness and proportionality.

<ul class="card-list">
  {% assign interactive_posts = site.categories.interactives %}
  {% for work in interactive_posts %}
    {% include post_card.html work=work %}
  {% endfor %}
</ul>
