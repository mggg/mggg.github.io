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

{% assign post = site.posts | where: "title", "Top 100 city council structures" | first %}
  {% if post %}
    {% include post_card.html work=post %}
  {% endif %}

  {% assign post = site.posts | where: "title", "Study of the 2024 STV City Council Election in Portland, Oregon" | first %}
  {% if post %}
    {% include post_card.html work=post %}
  {% endif %}

   {% assign post = site.posts | where: "title", "Comparing Electoral Systems for the Massachusetts Legislature" | first %}
  {% if post %}
    {% include post_card.html work=post %}
  {% endif %}

{% assign post = site.posts | where: "title", "Modeling the Fair Representation Act" | first %}
  {% if post %}
    {% include post_card.html work=post %}
  {% endif %}


  {% assign post = site.posts | where: "title", "Analysis of County Commission Elections in Yakima County, WA" | first %}
  {% if post %}
    {% include post_card.html work=post %}
  {% endif %}

{% assign post = site.posts | where: "title", "STV Reports in the Pacific Northwest" | first %}
  {% if post %}
    {% include post_card.html work=post %}
  {% endif %}


{% assign post = site.posts | where: "title", "Election Reform in Lowell, MA" | first %}
  {% if post %}
    {% include post_card.html work=post %}
  {% endif %}

{% assign post = site.posts | where: "title", "Study of Reform Proposals for Chicago City Council" | first %}
  {% if post %}
    {% include post_card.html work=post %}
  {% endif %}

  {% assign post = site.posts | where: "title", "Study of voting systems for Santa Clara, CA" | first %}
  {% if post %}
    {% include post_card.html work=post %}
  {% endif %}
</ul>
