---
title: "Differential Privacy and Redistricting"
date: 2022-06-24 00:00:00 Z
categories:
  - research
authors: MGGG
featured: true
permalink: /DP
image: "/uploads/dp_tree.png"
excerpt_separator: "<!--more-->"
---

In order to protect the privacy of individual Census respondents, Census data is released only at aggregate levels, typically combining records for hundreds of individuals or more and just reporting the overall counts. Unfortunately, on its own, this does not provide enough protection to prevent privacy attacks; simple mathematics of linear combinations easily allows people to reconstruct a full individual-level table that is perfectly compatible with the aggregate data. 

To handle this privacy threat, the 2020 Decennial Census was released with a new disclosure avoidance system in place &mdash; a differentially private system called **TopDown** &mdash; in order to thwart reconstruction. In short, TopDown adds random noise that cancels out at the aggregate level of cities or districts, but makes individual blocks very noisy.

The Census Bureau released their TopDown code in a public github, but to our knowledge, MGGG was the only group outside of the Bureau to work out how to run it.  This enabled several studies that examined whether the noising of Census data would be destructive of its uses for redistricting and voting rights enforcement.

<!--more-->

## Private numbers in public policy
This piece, which appeared in the Harvard Data Science Review, gives the background on how 
Census data is used, and how it is regarded by courts, before outlining several experiments to measure impacts on redistricting and voting rights.  

[HDSR 2022](https://hdsr.mitpress.mit.edu/pub/954ycugm/release/2)

The HDSR paper expanded on an earlier piece in FORC (Foundations of Responsible Computing) that includes more mathematical explorations of how "off-spine" redistricting might impact accuracy.

[FORC 2021](https://drops.dagstuhl.de/opus/volltexte/2021/13873/pdf/LIPIcs-FORC-2021-5.pdf)


## Study for Arizona Independent Redistricting Commission
In Arizona, the independent redistricting commission brought us in to advise them about whether their work would be negatively impacted by DP in the Census.  We presented work that showed that (a) the reconstruction threat is real, and (b)  both in large counties like Pima and in small counties like Navajo, the impact of TopDown noising on their work would be minimal.  

 [AIRC 2021](/publications/AZ-DP.pdf)
