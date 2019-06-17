---
title: "maup: the geospatial toolkit for redistricting data"
authors: Max Hully and MGGG
categories:
  - code
description:
  "`maup` is our attempt to make working with redistricting data easier for
  everyone. It is a Python package that streamlines the basic workflows that
  arise when working with blocks, precincts, and district shapefiles."
---

Anyone who has done research or data science about redistricting can tell you
that one of the most difficult (and important!) steps in the process is
collecting, cleaning, and processing the geospatial data that underpins
everything: shapefiles of precincts and census blocks.

[`maup`](https://github.com/mggg/maup) is our attempt to make working with
redistricting data easier for everyone. It is a Python package that streamlines
the basic workflows that arise when working with blocks, precincts, and
districts, such as:

- Assigning precincts to districts,
- Aggregating block data to precincts,
- Disaggregating data from precincts down to blocks, and
- Prorating data when units do not nest neatly.

The project's priorities are to be efficient by using spatial indices whenever
possible and to integrate well with the existing ecosystem around
[pandas](https://pandas.pydata.org/), [geopandas](https://geopandas.org) and
[shapely](https://shapely.readthedocs.io/en/latest/). The package is distributed
under the MIT License.

The name of the package comes from the
[modifiable areal unit problem (MAUP)](https://en.wikipedia.org/wiki/Modifiable_areal_unit_problem),
the fact that the same spatial data will look different depending on how you
divide up the space. Since `maup` is all about changing the way your data is
aggregated and partitioned, we have named it after the MAUP to encourage users
to use the toolkit thoughtfully and responsibly.

For more information on the package, including examples of how to use it on real
data, check out [the project's GitHub repo](https://github.com/mggg/maup).
