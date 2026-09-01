+++
id = "fiber-bundles/fiber-coordinates"
title = "Fiber coordinates"
kind = "definition"
summary = "Coordinates in the typical-fiber factor supplied by a local bundle trivialization."
aliases = ["local fiber coordinates", "bundle fiber coordinates"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/local-trivialization"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\Phi:\pi^{-1}(U)\to U\times F\) be a
[[fiber-bundles/local-trivialization|local trivialization]] of a fiber bundle.
Writing

\[
\Phi(p)=(\pi(p),f(p)),
\]

the value \(f(p)\in F\), or ordinary coordinates on \(F\) applied to it, is
the **fiber coordinate** of \(p\) in this trivialization.

## Change of fiber coordinates

On the overlap of two trivializations, the base point remains fixed while the
fiber coordinate changes by the associated
[[fiber-bundles/transition-function|transition function]]. Fiber coordinates
therefore depend on a local trivialization and are not usually intrinsic to a
point of the total space.

## Principal bundles

For a principal \(G\)-bundle, a local section chooses an origin in each
[[fiber-bundles/g-torsor|fiber torsor]] and supplies a coordinate \(h\in G\).
Changing the local section changes \(h\) by multiplication with the
principal-bundle transition function.

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: bundle coordinates and transition functions.
