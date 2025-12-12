---
title: Election System Case Studies
date: 2025-01-03 00:00:00 Z
categories:
  - reports
description: Deep dives into the consequences of changing the electoral system in specific jurisdictions, commissioned by cities and advocacy groups exploring electoral alternatives.
permalink: /election-system-case-studies
featured: true
---
Deep dives into the consequences of changing the electoral system in specific jurisdictions, commissioned by cities and advocacy groups exploring electoral alternatives.

## Reports
<ul class="card-list">
  {% assign post_titles = "Top 100 city council structures | Study of the 2024 STV City Council Election in Portland, Oregon | Comparing Electoral Systems for the Massachusetts Legislature | Modeling the Fair Representation Act | Analysis of County Commission Elections in Yakima County, WA | STV Reports in the Pacific Northwest | Election Reform in Lowell, MA | Study of Reform Proposals for Chicago City Council | Study of voting systems for Santa Clara, CA" | split: " | " %}

  {% for post_title in post_titles %}
    {% assign post = site.posts | where: "title", post_title | first %}
    {% if post %}
      {% include post_card.html work=post %}
    {% endif %}
  {% endfor %}
</ul>
