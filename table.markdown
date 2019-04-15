---
title: The Known Sizes of Grid Metagraphs
layout: freeform
---

<div class="l-content l-center" markdown="1">

# The Known Sizes of Grid Metagraphs

At MGGG, we think that one of the reasons that redistricting is hard to study is
that the space of possibilities (i.e., valid districting plans) is so huge it's
unthinkable by humans. And relatedly, the number of ways to achieve any simple
objective is overwhelmingly large.

We think that to study districting plans in context, you need to understand the
space of alternatives. So we are working on the science of sampling from these
universes of districting plans. As a simplified warmup problem, we can ask how
many ways there would be to district a jurisdiction made up of a small number of
units with equal population arranged in a perfect grid. We can then build up the
complexity from there. But this problem is already formidable!

In this table, the row marked **nxn → d** shows the number of ways to partition
an n by n grid into d districts (or connected pieces). The columns describe how
much size difference is tolerated among the districts. The two halves of the
table distinguish whether, to be considered contiguous, the districts would have
to be transitable by a chess rook (making only NSEW moves) or a chess queen
(which can also move diagonally). Queen contiguity allows many more district
shapes.

</div>{% include metagraph-table.html %}<div class="l-center l-content" markdown="1">
The generation of the numbers in this table was overseen by MGGG's Zach Schutzman and Daryl DeFord. We used a combination of [our own python code](https://github.com/zschutzman/enumerator) and an algorithm coded by Bob Harris ([code](http://www.bumblebeagle.org/polyominoes/tilingcounting/), [writeup](http://www.bumblebeagle.org/polyominoes/tilingcounting/counting_9x9_tilings.pdf); [OEIS](https://oeis.org/A172477)) in C in 2010. We've checked the math behind both algorithms and are confident in both implementations.

As of October 2018, we've got runs going on MIT's
[OpenStack](https://tig.csail.mit.edu/shared-computing/open-stack/) to extend
the coverage of this table. Each missing value is expected to take at least a
day, and sometimes weeks or more, of computer time.

An earlier version of the table, which appears in November's print version of
Scientific American, used partition enumeration code that was included with the
R package redist— that code turns out to be buggy. As a result, some of the
numbers have since been corrected.

</div>
