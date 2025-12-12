---
title: Redistricting Reports
date: 2025-01-04 00:00:00 Z
categories:
  - reports
description: How the Lab has used the power of computational redistricting to analyze enacted, proposed, and challenged legislative maps.
permalink: /redistricting-reports
featured: true
image: "/uploads/gridlandia.svg"
---

How the Lab has used the power of computational redistricting to analyze enacted, proposed, and challenged legislative maps.

## Reports
<ul class="card-list">
  {% assign post_titles = "UK Boundaries | Modeling electoral dynamics for the Portland, Oregon city council | Michigan Independent Citizens Redistricting Commission Post-Mortem | Privacy, Census Data, and Arizona Redistricting | The Mathematicians' Brief in Rucho v. Common Cause | Comparison of Districting Plans for the Virginia House of Delegates" | split: " | " %}

  {% for post_title in post_titles %}
    {% assign post = site.posts | where: "title", post_title | first %}
    {% if post %}
      {% include post_card.html work=post %}
    {% endif %}
  {% endfor %}
</ul>

