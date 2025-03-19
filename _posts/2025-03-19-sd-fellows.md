---
title: "Structural Democracy Fellows"
date: 2025-03-19 00:00:00 Z
categories:
  - news
authors: MGGG
featured: true
permalink: /sd-fellows
excerpt_separator: "<!--more-->"
---

The Data and Democracy Lab announces an initial cohort in the **Structural Democracy Faculty Fellow Program**, funded by the [Crankstart Foundation](https://crankstart.org/programs).

These 16 researchers from universities in the U.S., the U.K., and Chile are funded to build and strengthen a research community in Structural Democracy, which is meant to include a range of practically applicable areas in the study of systems of election.
Topics in scope include (computational) social choice, mechanism design, computational redistricting, statistical models of elections, data visualization for elections, behavioral psychology of ranking and voting, dynamics of turnout and engagement, and the design of law and policy around voting.

<!--more-->

The fellows have proposed the following projects for the 2025 calendar year.


## Algorithmic Challenges in Apportionment
### Jose Correa, Universidad de Chile, and Victor Verdugo, Pontificia Universidad Católica de Chile

This project addresses algorithmic challenges in electoral apportionment, focusing on improving democratic systems through proportional representation. The apportionment problem involves allocating seats in representative bodies to regions or parties based on population or vote shares while adhering to the principles of fairness and proportionality. Despite extensive historical developments, existing methods often encounter paradoxes or fail to balance competing fairness criteria. We propose leveraging randomized algorithms and optimization tools to overcome these challenges. Randomization offers a promising approach to reconcile incompatible apportionment properties while providing provable fairness guarantees. Additionally, we will investigate online frameworks to ensure proportionality over time, aiming at dynamically accommodating multidimensional representation needs, such as gender and ethnicity.

## Bayesian Small-Area Estimation for Structural Democracy
### Aaron Schein, University of Chicago

Enforcement of the 1965 Voting Right Act’s stipulation against racial gerrymandering relies heavily on lawsuits that are routinely brought against state officials by political parties and civil rights advocacy groups. Legal arguments in such cases hinge on claims about the racial/ethnic composition of the citizen voting-age population (CVAP)—i.e., the population of eligible voters. Although critically important for the protection of minority groups’ rights to representation, there are no authoritative sources for this data at the level of Census blocks, which is the spatial resolution required to argue gerrymandering cases. Litigants in such cases appeal instead to estimates of block-level CVAP by race/ethnicity, typically supplied by expert witnesses. Despite the role of such estimates, there are no accepted best practices for producing them, and competing methods can yield substantially different results. This project seeks to 1) develop a family of novel methods for CVAP estimation, 2) understand trade-offs in the downstream effects of different methods’ deployment in gerrymandering cases, and 3) advocate for a single “best practice” method and release its estimates as a public resource.

## Central Advantage: a Measure of Partisan Fairness in Redistricting
### Jon X. Eguia, Michigan State University

The first project explores the Central Advantage, a measure of partisan (un)fairness in redistricting. The Central Advantage compares a party’s number of seats to a fair geographic baseline based on the premise that each voter’s ideal unit of representation is the community of her closest neighbors. This project is co-developed with Jeff Barton. We seek to study the relation between this “central” geographic baseline number of seats, and the seat results derived from appropriate ReComb ensembles, to check to what extent the Central Advantage, in its simplicity, can capture the insights on the effect of geography that one can learn from from ReComb ensembles. 
The second project studies the properties of a “quadratic” voting mechanism in which agents express their preference intensities by casting a different number of votes for each alternative and paying a cost that is the square of the votes they cast for each alternative.


## The Central Advantage and Related Neighborhood-Based Metrics in Redistricting
### Jeff Barton, Hampshire College

The first part of this project is co-developed with Jon Eguia and extends our joint work on the Central Advantage, a geographic measure of partisan fairness in redistricting. For a given redistricting plan, the Central Advantage compares a party's actual number of seats to a geographic baseline number of seats that the party would receive if every resident were at the center of their own ideal district. We will explore the relationship between this geographic baseline and results generated by appropriate ensembles constructed using the ReCom algorithm.
 
The second part of the project extends the neighborhood framework that is used to define the Central Advantage. By varying the way we define neighborhoods and the measures we apply to them, we can gain insights into how a given districting plan affects different notions of community. Applications to compactness as well as racial gerrymandering will be considered.

## Data-driven Democracy in Noisy and Adversarial Settings
### Teodora Baluta and Juba Ziani, Georgia Tech

The goal of this proposal is to investigate the role of privacy-preserving techniques, particularly differential privacy (DP), in data-driven problems for social choice and structural democracy. Voting or demographic data are inherently sensitive, necessitating robust privacy protections in their use for auditing voting systems, redesigning election rules, apportionment and redistricting, and optimizing political targeting. Techniques like DP, which is currently implemented in the US Census, ensure data privacy but can introduce biases and distortions with potentially serious consequences for downstream applications of relevance to structural democracy. The proposed research focuses on the following key applications: designing elections systems using DP data, apportionment and redistricting, and adversarial attacks on election systems.

## Fairness and Representation in Permanent Citizens' Assemblies
### Evi Micha, University of Southern California

As citizens' assemblies gain increasing acceptance, the establishment of permanent citizens' assemblies, such as the Ostbelgien Model in Belgium and the Paris Citizens' Assembly, is becoming more common. Unlike temporary or ad hoc assemblies, which are convened for specific purposes and dissolved after delivering their recommendations, permanent citizens' assemblies operate continuously. However, “permanent” does not mean that the same members serve indefinitely. For instance, in the Paris Citizens' Assembly, 100 Parisians are selected by lottery each year to participate. Permanent citizens' assemblies introduce new challenges in achieving proportional representation. Our goal is to design selection algorithms that ensure proportional representation within each panel and cumulatively over time, guaranteeing fair representation for smaller groups across iterations.


## Improved Sampling Methods for Political Redistricting
### Sarah Cannon, Claremont McKenna College

Detecting when gerrymandering is occurring is a hard problem.  Many people point to crazily drawn districts or disproportionate election outcomes as evidence of gerrymandering, but these don’t tell the whole story.  One approach that's been developed is to use random sampling to understand the space of possible districting plans, assess proposed plans, and study rule changes or alternative districting systems. This project will study tree-based sampling methods and their applications to political districting, with the goal of advancing the state-of-the-art and coupling new algorithms with proofs that they perform as desired. Constraints and insights developed from considering applied problems will drive algorithmic exploration. There are also connections to broader theoretical questions about the combinatorial and probabilistic structure of random trees and random walks; subgraphs with constrained sizes; Markov chain mixing under non-local constraints; and duality in non-planar graphs.

## Panelot 2.0
### Bailey Flanigan and Paul Gölz

The website Panelot.org is a widely used tool for selecting the members of deliberative minipublics, based on a selection algorithm with mathematical guarantees that we and our coauthors developed in 2021. However, the widespread use of Panelot.org at this point exceeds the limits of the site’s current technical realization, which has additionally limited us in providing recently developed algorithmic tools to minipublic practitioners.
In this project, we will expand Panelot into an open-source, publicly available “one-stop-shop” for conducting civic lotteries. We will add new functionalities to the website — based both on cutting-edge research and user requests — and will generally make the website more user friendly and extensible for future additions.

## Participatory budgeting for building cohesive communities
### Edith Elkind, Northwestern University

The project will explore three emerging directions in computational social choice: fairness in urban planning and infrastructure, design of multiwinner voting rules that promote social cohesion, and proportionality in temporal voting.

## Proportional Representation: Axioms, Measures, and Applications
## Markus Brill, University of Warwick

This project focuses on the mathematical study of proportional representation in multiwinner voting and participatory budgeting. It investigates quantitative measures of proportionality to assess election outcomes, examines trade-offs between proportionality and efficiency in participatory budgeting, and addresses the impact of incomplete voter preferences on decision-making processes.

## Reducibility and irreducibility of recombination Markov chains
### Matthew Kahle, The Ohio State University

Recombination Markov chains are a popular tool. They are particularly important for sampling random (or ‘typical’) maps in the study of redistricting plans. Although such Markov chains are widely applied, so far little is known about them mathematically. For example, not much is known about their mixing times. Even worse, it is not even known in general whether these Markov chains are irreducible, i.e. whether the state-space graph is connected. We will study problems related to reducibility and irreducibility of these kinds of Markov chains.

## Spanning Tree Methods for Independent Sampling of District Plans
## Jeanne Clelland, University of Colorado Boulder

Spanning tree-based methods have rapidly become the standard for sampling district plans, largely due to their affinity for creating plans with relatively compact districts.  Most of these methods rely on Markov chains, where new plans are created from prior plans by changing only a small number of districts at a time.  In most cases this works very well, but some states (e.g., Ohio) impose restrictive requirements on district plans that make it difficult for such a Markov chain to make meaningful changes to a plan while remaining legally compliant.  The goals of this project are: (1) to develop a spanning tree-based method for independent sampling of plans that could be used to create a diverse ensemble of plans without relying on Markov chains, and (2) to derive theoretical and empirical results about the corresponding sampling distribution.  This is joint work with Kristopher Tapp.


## Spanning Tree Methods for Sampling Balanced Partitions
### Kristopher Tapp, St. Joseph's University

Modern redistricting algorithms obtain balanced partitions of graphs by splitting random spanning trees.  This approach leads to several important mathematical questions whose resolutions could help improve the algorithms and more precisely characterize their output.  For example, I propose to study the probability that a (UST or MST) random spanning tree of an n-by-n grid can be split.  Additionally, I propose an improvement of the popular SMC algorithm that recursively divides regions in half, rather than repeatedly biting off single districts.  


