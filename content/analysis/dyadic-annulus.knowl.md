+++
id = "analysis/dyadic-annulus"
title = "Dyadic annulus"
kind = "definition"
summary = "A radial shell whose outer radius is twice its inner radius, used to organize estimates by scale."
aliases = ["dyadic shell"]
domains = ["analysis", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For an integer \(k\), a **dyadic annulus** in \(\mathbb R^d\) is a set of the
form
\[
A_k=\{x\in\mathbb R^d:2^k\le |x|<2^{k+1}\}.
\]
Changing open or closed endpoints, or multiplying both radii by a fixed
constant, gives an equivalent convention for most estimates.

## Scale decomposition

The annuli are pairwise disjoint and cover
\(\mathbb R^d\setminus\{0\}\). A sum or integral over large radii can therefore
be estimated by summing its contributions over \(k\).

## Smooth localization

Scaled [[differential-geometry/bump-function|bump functions]] produce a smooth
dyadic partition in which each point belongs to only boundedly many enlarged
annuli. Derivatives of a cutoff at radius \(2^k\) gain factors of \(2^{-k}\).

## References

1. Loukas Grafakos, *Classical Fourier Analysis*, 3rd ed., Springer, 2014. [DOI record](https://doi.org/10.1007/978-1-4939-1194-3).
