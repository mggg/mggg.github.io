---
title: Data & Data Practices
date: 2025-01-02 00:00:00 Z
categories:
  - reports
description: With years of experience in electoral and demographic data, explore how the Lab answers questions about the best ways to use the data we have.
permalink: /data-practices
featured: true
---

With years of experience in electoral and demographic data, explore how the Lab answers questions about the best ways to use the data we have.

## Reports

<ul class="card-list">
  {% assign disagg_post = site.posts | where: "title", "Disaggregation of Unsorted Votes" | first %}
  {% if disagg_post %}
    {% include post_card.html work=disagg_post %}
  {% endif %}
  {% assign vap_post = site.posts | where: "title", "Conventions for Constructing Demographic Categories" | first %}
  {% if vap_post %}
    {% include post_card.html work=vap_post %}
  {% endif %}
  {% assign mggg_states_post = site.posts | where: "title", "MGGG States" | first %}
  {% if mggg_states_post %}
    {% include post_card.html work=mggg_states_post %}
  {% endif %}
</ul>

