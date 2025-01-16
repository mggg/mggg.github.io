---
title: "Jobs at D/D"
date: 1800-01-16 00:00:00 Z
authors: MGGG
categories:
    - news
layout: post
permalink: /jobs
excerpt_separator: "<!--more-->"
featured: true
---

The Data and Democracy Lab (née MGGG Redistricting Lab) is a research group led by PI Moon Duchin in the Department of Mathematics and Brooks School of Public Policy at Cornell.  Members of the lab engage in interdisciplinary research, drawing on approaches from geometry, topology, graphs and networks, probability/statistics, and algorithm design, in conversation with geography, political science, policy, and law.  The lab is deeply engaged with civil rights and good-government work in representative democracy.

Major activities of the lab include:
- researching ranked choice voting, redistricting, or other topics at the intersection of mathematics and democracy; 
- software development of our open-source packages in Python and various other languages; and
- collaborating with community partners and civil rights organizations.

Below are our open job opportunities.

## Summer Internship 2025

We invite applications from undergraduate and graduate students for full-time Data/Democracy summer intern positions for five weeks (June 16th to July 18th, 2025).  Applications should be completed by February 7th, 2025 and notification of decisions will be made by February 21st. Interns will work in-person in Ithaca, NY. Interns should expect to arrive in Ithaca by June 15th and depart on or after July 19th. The stipend is $5000 for the five weeks, and there is additional funding support for travel and lodging. 

This internship will be built around a research problem that you develop in conjunction with other members of the lab.  Many projects combine skills from mathematics and computation, though the balance depends on the individual.  There are opportunities for primarily solo research or for work in groups.  We hold a one hour weekly lab meeting for all members.

The application should include the following elements.

(1) a one-page cover letter explaining your background and interests, and including general project directions if you have ideas in mind;
(2) a CV or resume; and
(3) the contact information for one recommender, most likely a professor who knows you and your work.

### To apply
Application materials should be submitted [here](https://forms.gle/DnigNZgsS7LfoL5z5). Any questions about the application process should be sent to <sd-interns@mggg.org>.

## Programmers, Developers, Engineers

We are always looking to hear from programmers, developers, or engineers who are interested in the intersection of computation, software, and society. Please contact <code@mggg.org> to inquire about a position.


<!-- The MGGG Redistricting Lab is a non-profit research organization based at Tufts University studying
applications of geometry and computing to U.S. redistricting. Our mission is both technical
and civic, and we aim to drive cutting-edge research, amplify the voices of the public and the civil
rights community, and improve accountability in the redistricting process.

As of January 2023, we have filled our Senior Web Developer position. We anticipate more developer and researcher positions in the coming year, so please reach out to [jobs@mggg.org](mailto:jobs@mggg.org) to inquire.

This semester we seek to hire 1-2 postdoctoral scholars with experience in mathematics, computing, statistics, geography, politics, and/or law.  The positions are for 1 year, with possibility of renewal to 3 years. For more information, contact us at [jobs@mggg.org](mailto:jobs@mggg.org).
 
Access to voting rights for communities of color and other marginalized groups
is central to our mission, and we strive to build a team that is diverse in as
many ways as possible. -->

<!-- We are not currently hiring.  Please check this page in the future for any updates to our openings. -->


<ul class="card-list">
{% assign jobs = site.jobs | sort: "position" %}
{% for job in jobs %}
    {% if job.hidden == false %}
        {% include job.html job=job %}
    {% endif %}
{% endfor %}
</ul>
