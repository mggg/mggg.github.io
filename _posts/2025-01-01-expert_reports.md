---
title: Expert Reports
date: 2025-01-01 00:00:00 Z
categories:
  - reports
permalink: /expert-reports
featured: true
---
Moon has served as an expert witness in a variety of court cases related to race, redistricting, and the VRA. 
What role does mathematics and data science play in the court?

## Reports
<ul class="card-list">
  {% assign post_titles = "Texas congressional <i>(LULAC v. Abbott)</i> | Pennsylvania congressional <i>(Carter v. Chapman)</i> | North Carolina congressional and legislative <i>(Moore v. Harper)</i> | Alabama congressional <i>(Allen v. Milligan)</i>" |split: " | " %}

  {% for post_title in post_titles %}
    {% assign post = site.posts | where: "title", post_title | first %}
    {% if post %}
      {% include post_card.html work=post %}
    {% endif %}
  {% endfor %}
</ul>

For more expert reports, please contact the Lab directly.