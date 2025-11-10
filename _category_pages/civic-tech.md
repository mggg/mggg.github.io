---
title: Civic Tech
key: civic-tech
index: 4
output: true
layout: category
show_categories: true
---

## Tools for Democratic Participation
Democracy works best when everyone can participate in shaping it. This section brings together the software, data, code, and interactive tools the Lab has built and collected to democratize access to sophisticated methods for redistricting and electoral analysis.

All our tools are **open-source and freely available.** We believe the methods for analyzing democracy should be democratic themselves: transparent, accessible, and community-owned. Whether you're a community member who wants to draw your own district map, a researcher analyzing voting patterns, a journalist covering redistricting, or an advocate building a voting rights case, these tools put computational methods in your hands.

## Our Tools:
- **Districtr:** This mapping tool lets you draw and share redistricting plans as well as draw and describe your “community of interest.” Districtr has been used by tens of thousands of people and was adopted as the official public mapping platform in big cities like New York and Los Angeles all the way down to tiny Grand County, Utah. Draw a map, explain why your community should stay together, and share your vision of fair representation.
- **GerryChain:** This is the open-source Python library powering our redistricting analyses. GerryChain is tech for ensemble analysis that’s been used in major redistricting cases. Generate thousands of alternative redistricting plans using Markov chain Monte Carlo methods to establish baselines for what "typical" maps look like under various constraints. GerryChain has been used by researchers, advocates, and expert witnesses nationwide.
- **VoteKit:** VoteKit is our “Swiss army knife for computational social choice research.” This Python package provides an end-to-end pipeline for reading in ballot data, running ballots through a voting rule to get election outcomes, and then visualizing and analyzing the preferences and winners. It also implements a suite of statistical models for generating realistic ballots given voter preferences. We use this package to compare different electoral systems for communities and advocates.
- **VoteKit Lite:** Don’t want to touch Python code yourself? VoteKit Lite is a web app that replicates some of the basic features of VoteKit, allowing you to compare electoral outcomes under a variety of assumptions through a more user-friendly interface.
- **PyEI:** Since ballots don't actually include demographic information, statistical inference methods are needed to estimate whether different demographic groups have different voting patterns.  We can use this to identify polarized voting, which is required by courts in Voting Rights Act cases. PyEI is a Python toolkit that lets users apply a range of methods (especially variants of ER and EI) via an easy-to-use interface, with flexible options for saving and visualizing the outputs. Under the hood, the EI uses state-of-the-art PyMC.
- **Interactives:** These visualizations allow you to explore concepts like compactness, and proportionality.

