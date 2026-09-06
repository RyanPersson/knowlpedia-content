+++
id = "analysis/quantitative-unique-continuation"
title = "Quantitative unique continuation"
kind = "definition"
summary = "An estimate that gives an explicit lower bound for the mass of a function on an observation set from analytic or spectral constraints."
aliases = ["quantitative uniqueness estimate", "observability inequality"]
domains = ["analysis", "partial-differential-equations", "harmonic-analysis"]
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **quantitative unique-continuation estimate** for a class
\(\mathcal F\subseteq L^2(\mathbb R^d)\) and an observation set
\(U\subseteq\mathbb R^d\) is an inequality
\[
\|f\mathbf 1_U\|_2\ge c\|f\|_2,
\qquad f\in\mathcal F,
\]
with an explicit constant \(c>0\) determined by stated geometric and analytic
parameters. It strengthens qualitative unique continuation, which would only
say that vanishing on \(U\) forces \(f=0\).

## Spectral version used in fractal uncertainty

The class \(\mathcal F\) may consist of functions whose Fourier transforms are
supported in a prescribed set and whose frequency-side decay is controlled by
a [[harmonic-analysis/damping-function|damping function]]. Observation sets
formed by placing one small cube in each unit cube then give a uniform lower
bound. Iterating the resulting single-scale estimate across the holes of a
porous set produces a [[harmonic-analysis/fractal-uncertainty-principle|fractal
uncertainty principle]].

## Scope

The name also covers Carleman-estimate and spectral-inequality results in PDE.
The defining feature is quantitative control, not one particular proof method.

## References

1. Benjamin Jaye and Mishko Mitkovski, “Quantitative uniqueness properties for (L^2) functions with fast decaying, or sparsely supported, Fourier transform,” *IMRN* (2022). [DOI record](https://doi.org/10.1093/imrn/rnab140).
2. Rui Han and Wilhelm Schlag, “A higher-dimensional Bourgain–Dyatlov fractal uncertainty principle,” *Analysis & PDE* 13 (2020). [DOI record](https://doi.org/10.2140/apde.2020.13.813).
