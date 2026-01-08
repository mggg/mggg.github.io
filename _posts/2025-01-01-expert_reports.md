---
title: Export Reports
date: 2025-01-01 00:00:00 Z
categories:
  - reports
permalink: /export-reports
featured: true
---
Moon has served as an expert witness in a variety of court cases related to race, redistricting, and the VRA. 
What role does mathematics and data science play in the court?

## Reports
<ul class="card-list">
  {% assign post_titles = "Report on Congressional Plan C2333 | Comparison of Congressional Districting Plans in Pennsylvania | North Carolina Rebuttal Report | Presentation of Alternative Congressional Districting Plans for Alabama" | split: " | " %}

  {% for post_title in post_titles %}
    {% assign post = site.posts | where: "title", post_title | first %}
    {% if post %}
      {% include post_card.html work=post %}
    {% endif %}
  {% endfor %}
</ul>

For more expert reports, please contact the Lab directly.