---
title: How Geocoded Voterfiles Can Inform the Collection of Precinct Boundary Data
date:  2020-04-8 00:00:00 Z
authors: MGGG
categories:
  - data
authors: MGGG
layout: post
image: "/uploads/CT-geocode.png"
---

Our research at the MGGG Redistricting Lab requires election data at the finest spatial resolutions possible. This generally is the voting precinct, also sometimes called voting tabulation districts (VTDs), wards, and election districts. Unfortunately for our research purposes, many states either do not keep track of their precinct boundaries at all or have significant discrepancies between their precinct boundary data and tabular election results. While we can contact individual municipalities to collect data or clear up these discrepancies, this is incredibly time consuming and sometimes local election administrators are unable or unwilling to help. In these instances, a geocoded voterfile can be used to help determine precinct boundaries. Voterfiles are lists kept by state elections officials of registered voters. The information in them varies state by state, but generally they include address information and precinct assignments for all registered voters.

For example, using the Texas A&M Geocoder, we were able to geocode around 1500 addresses of registered voters in Avon, CT. We know from the precinct-level election returns for the 2018 midterm elections, the town of Avon had three precincts but the shapefile we have only had two. Using the geocoded voterfile we were able to confirm that one of the town’s precincts had been split along the boundary between State House District 17 and 19. While the method is not a cure all for the precinct problem (voterfiles in some states are prohibitively expensive or inaccurate and it can be difficult to reasonably delineate boundaries in more sparsely populated areas), geocoded voterfiles can be incredibly helpful in determining precinct splits as in this example or in checking the accuracy of precinct boundaries.