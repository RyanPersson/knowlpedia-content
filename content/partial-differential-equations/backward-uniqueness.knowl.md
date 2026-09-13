+++
id = "partial-differential-equations/backward-uniqueness"
title = "Backward uniqueness"
kind = "definition"
summary = "Coincidence at a later time determines equality at earlier times within a specified evolution class."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/cauchy-problem", "shared-foundations/injective-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 3
+++

An evolution [[partial-differential-equations/cauchy-problem|problem]] has **backward uniqueness** in a specified class if any two solutions that agree at a time \(T\) agree throughout their common earlier time interval. For a linear evolution family \(S(T,s)\), this is [[shared-foundations/injective-function|injectivity]] of \(S(T,s)\).

## Heat equation example

For the [[partial-differential-equations/heat-semigroup|heat semigroup]] on \(L^2(\mathbb R^n)\), the [[functional-analysis/fourier-transform-schwartz-space|Fourier multiplier]] is \(e^{-4\pi^2\nu(T-s)|\xi|^2}>0\). Thus \(S(T,s)v=0\) implies \(v=0\). Inverting this multiplier is unbounded on \(L^2\): uniqueness of past values does not give existence or continuous dependence for arbitrary terminal data. Backward uniqueness for equations with variable coefficients requires additional hypotheses.
