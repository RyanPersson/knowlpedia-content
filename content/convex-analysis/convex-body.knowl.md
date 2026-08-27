+++
id = "convex-analysis/convex-body"
title = "Convex body"
kind = "definition"
summary = "A nonempty compact convex subset of a finite-dimensional real vector space."
aliases = ["compact convex set", "convex compact set"]
domains = ["convex-analysis", "integral-geometry"]
section_mode = "progressive"
+++

Let \(V\) be a finite-dimensional real
[[linear-algebra/vector-space|vector space]]. A **convex body** is a
nonempty [[topology/compact-set|compact]] [[convex-analysis/convex-set|convex
set]] \(K\subseteq V\). The family of all convex bodies in \(V\) is commonly
denoted \(\mathcal K(V)\).

## Operations

If \(K,L\in\mathcal K(V)\) and \(s,t\ge0\), then
\[
sK+tL=\{sx+ty:x\in K,\ y\in L\}
\]
is again a convex body. This is the
[[convex-analysis/minkowski-sum|Minkowski sum]] operation used to polarize
volume and define [[convex-analysis/mixed-volume|mixed volumes]].

## Topology and dual description

The [[topology/hausdorff-distance|Hausdorff distance]] metrizes convergence of
convex bodies. Equivalently, \(K_m\to K\) exactly when their
[[convex-analysis/support-function|support functions]] converge uniformly on
compact subsets of \(V^*\), or uniformly on the
[[linear-algebra/unit-sphere|unit sphere]] after an
[[linear-algebra/inner-product|inner product]] is chosen.

## Convention

Some authors require a convex body to have nonempty interior. This knowl uses
the broader convention standard in valuation theory, allowing lower-dimensional
compact convex sets. A statement needing full dimension must say so.

## References

1. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press, 2014. [DOI record](https://doi.org/10.1017/CBO9781139003858). Relevant: §1.1.
