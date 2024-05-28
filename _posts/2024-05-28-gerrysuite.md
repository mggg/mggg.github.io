---
title: "Major updates to Gerry-Suite"
date: 2024-05-28
authors: MGGG
categories:
    - news
layout: post
image: "/uploads/triple-PA.gif"
featured: true
---



Since the beginning of the year, we’ve made several major updates to our main suite of redistricting analysis tools.

## GerryChain

Our [GerryChain](https://gerrychain.readthedocs.io/) library has several new features that help catch the
public releases up to the code we’ve been using in Lab projects.  In particular, users can now run
what we call "region-aware" chains (e.g., prioritizing county intactness) and 
“exploratory” chains that heuristically optimize a particular metric or score.

To accompany these new features, we have also made a concerted effort
to overhaul the package's documentation. This includes
adding tutorials, re-working the old tutorials to make
sure that they are up to date with current best practices, and adding a complete, searchable package reference.

### Region-Aware Chains

When redistricting a specific locality, it is often a stated preference
that smaller regions (such as counties or cities or neighborhoods) are preserved un-split as much as possible. 
The newest version of GerryChain allows the user to select a parameter interpolating from no 
region-awareness to a maximal level of priority on region preservation.

For those curious about the math: this is accomplished by using a shifted Kruskal’s algorithm.  The splitting step in a 
recombination train is done by drawing a random spanning tree and deleting an edge of that in a balanced fashion.
One fast algorithm for randomizing spanning trees is MST, or minimum spanning tree, given a set of edge weights.
Instead of drawing all weights from the same distribution (as in standard Kruskal), we “surcharge” the weights
on edges between different regions.  This makes us more likely to choose a spanning tree that restricts to one tree 
within each region; when the tree is split, the region is then split at most once.  To learn more, please see our new
[documentation](https://gerrychain.readthedocs.io/en/v0.3.2/user/recom/#region-aware-recom)


### Exploratory Chains

[Version 0.3.2](https://github.com/mggg/GerryChain/releases/tag/v0.3.2) of GerryChain
came with the addition of two optimizer classes:

1. `SingleMetricOptimizer` This is a general-purpose class that is designed to
   seek higher-scoring plans with respect to a single metric.
2. `Gingleator` This is a subclass of the `SingleMetricOptimizer` class, specifically
   designed to search for plans with increased numbers of majority-minority districts. The class is named 
   for the Supreme Court case _Thornburg v. Gingles_ which set a requirement to find these when bringing VRA cases.

Each of these optimization classes has three different modes:

1. **Tilted Runs:**  In a tilted run, we always accept a proposed plan with a better score, and we accept a worse-scoring plan with a user-chosen probability $p$.
2. **Short Bursts:** The short bursts heuristic—originally proposed for redistricting by Zach Schutzman and then 
studied in the paper
   ["Voting Rights, Markov Chains, and Optimization by Short Bursts"](https://arxiv.org/abs/2011.02288) by MGGG collaborators
(Cannon, Goldbloom-Helzner, Gupta, Matthews, and Suwal)—starts from some plan and then performs $b$ steps of an unbiased random walk (the user sets the number
   $b$, known as the _burst length_). A new burst of length $b$ is then run starting from the most extreme
   configuration found in the previous burst, and we iterate.
3. **Simulated Annealing:** This is an optimization technique borrowed from statistical physics. The basic
   idea is to start a chain "hot,” meaning that every proposed new plan is accepted. 
   As time passes, the chain "cools,” making it less and less likely for lower scores to be 
   accepted.  The probability is governed by a value called $\beta$, which varies on a user-chosen temperature schedule, creating a heating and cooling cycle that repeats over the life of the chain.



## GerryTools

In addition to the major updates to GerryChain, we have been working hard to help improve
the functionality of its companion library [GerryTools](https://gerrytools.readthedocs.io/en/v1.2.0/), which 
contains auxiliary functions meant to facilitate analysis and visualization.
GerryTools will continue to evolve throughout Summer 2024, but has two exciting new features in this release.

### A new compression scheme called Binary Ensemble (BEN)

When it comes to ensemble analysis work, reproducibility and auditability are vital. 
Ideally, we can preserve and publish the exact data that was used in any given analytical project.
However, when the data itself is tens or hundreds of millions of districting plans, each consisting of an assignment of
potentially millions of geographical units.  This creates massive data files that are costly to store and hard to manipulate.

In previous years, MGGG made substantial progress towards solving this issue with the
[PCompress](https://github.com/mggg/pcompress) package due to Lab alum Max Fan, which successfully reduced
the storage burden for large ensembles where the differences from one plan to the next are small relative to the size of 
the plan, as in common MCMC methods.  But for chains run on the census-block level or for ensembles of less correlated 
plans, the resulting files can still be quite unwieldy.

The new BEN file format tackles both of these issues. The  [BEN module](https://gerrytools.readthedocs.io/en/v1.2.0/user/ben/)
in GerryTools comes with a suite of tools that allows users to compress ensembles
of districting plans down by 1-2 orders of magnitude (depending on the type of plan
and how conveniently the nodes are indexed). There’s also an extreme compression tool and
file format known as XBEN, letting users see up to a **4000-fold improvement** in the
compression of their files. This means that many ensembles of plans can now be compressed small
enough to fit into an email, and several hundred can now fit on a thumb drive.

The documentation contains an example 
[here](https://gerrytools.readthedocs.io/en/v1.2.0/user/ben/#compression)
where we reduce a 27Gb file containing
100,000 block-level Colorado plans down to a slim 6Mb, small enough for GitHub.


### Wrappers for diverse sampling methods

The main Markov chain technique provided in GerryChain is called ReCom, or recombination, first introduced by DeFord, 
Duchin, Najt, and Solomon.  Lab alum Parker Rule created a blazingly fast implementation of both regular ReCom and of a 
reversible variant called RevReCom in the high-performance programming language Rust.  The Rust implementation lets users 
do bigger and more complicated runs than are possible in Python alone, for instance enabling block-level runs on large 
states in a matter of hours.  In the lab, we use the Rust implementation for our resesarch and consulting work.  This new 
release of GerryTools includes a Python wrapper for the Rust code, so that Python users of GerryChain can now access the 
power of the faster implementation without needing any knowledge of Rust syntax.  

MGGG is one group in a larger ecosystem of researchers building mathematical and computational approaches
to redistricting.  For example, teams led by Jonathan Mattingly at 
[Duke](https://sites.duke.edu/quantifyinggerrymandering/) and by Kosuke Imai at 
[Harvard](https://alarm-redist.org/) have built highly-cited tools for sampling districting plans, called 
_Forest ReCom_ and _Sequential Monte Carlo_ (or SMC), respectively.  Forest ReCom is a Metropolis Markov chain
implemented in Julia and SMC is a re-weighted recursive splitting technique implemented in R/C++.  Both are based on the spanning tree partitioning idea first introduced in ReCom.

The differences in programming language and file format can make it challenging
for users to benchmark differences in the samplers, so we have also added Python wrappers to GerryTools that let you 
run Forest ReCom and SMC without setting up the original development pipelines.  (We also have some supporting documentation
to help users understand the methods.)  This is available in the [MGRP](https://gerrytools.readthedocs.io/en/v1.2.0/user/mgrp/)
module of GerryTools.

The contact person and main developer for all of these innovations and improvements is Peter Rock (peter@mggg.org), who would love to hear from you!
