+++
id = "analysis/unique-ergodicity"
title = "Unique ergodicity"
kind = "definition"
summary = "The property that a continuous dynamical system has exactly one invariant probability measure."
aliases = ["uniquely ergodic system", "uniquely ergodic flow"]
domains = ["analysis", "dynamical-systems", "ergodic-theory"]
prerequisites = ["topology/continuous-map", "probability/probability-measure"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A [[topology/continuous-map|continuous map]] \(T:X\to X\) of a compact space is **uniquely ergodic** if it
has exactly one \(T\)-invariant Borel [[probability/probability-measure|probability measure]]. A continuous flow
\((\varphi_t)_{t\in\mathbb R}\) is uniquely ergodic if there is exactly one
probability measure invariant under every \(\varphi_t\).

## Uniform time averages

If \(T\) is uniquely ergodic with invariant measure \(\mu\), then for every
continuous \(f:X\to\mathbb R\),
\[
\frac1N\sum_{k=0}^{N-1}f(T^kx)
\longrightarrow \int_Xf\,d\mu
\]
uniformly in \(x\). An analogous statement holds for continuous-time averages
of a uniquely ergodic flow.

## Warning

Unique ergodicity is stronger than ergodicity with respect to one chosen
measure. It is a topological assertion about the uniqueness of all invariant
probability measures.

## References

1. Peter Walters, *An Introduction to Ergodic Theory*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4612-5775-2).
