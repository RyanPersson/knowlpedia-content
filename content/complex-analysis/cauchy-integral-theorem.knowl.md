+++
id = "complex-analysis/cauchy-integral-theorem"
title = "Cauchy integral theorem"
kind = "theorem"
summary = "Holomorphic functions have zero integral around null-homologous closed contours."
aliases = ["Cauchy's theorem", "Cauchy–Goursat theorem"]
domains = ["complex-analysis"]
prerequisites = ["complex-analysis/complex-domain", "complex-analysis/complex-contour-integral", "topology/simply-connected-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(D\subseteq\mathbb C\) be a [[complex-analysis/complex-domain|domain]], let \(f:D\to\mathbb C\) be holomorphic, and let \(\gamma\) be a closed piecewise \(C^1\) contour in \(D\). If \(\gamma\) is null-homotopic in \(D\), then
\[
\int_\gamma f(z)\,dz=0.
\]
In particular, this holds for every closed contour when \(D\) is [[topology/simply-connected-space|simply connected]].

## Homological form

A stronger standard formulation replaces null-homotopy by the requirement that \(\operatorname{Ind}(\gamma,a)=0\) for every \(a\notin D\). Equivalently, the cycle represented by \(\gamma\) is null-homologous in \(D\). This version handles sums of contours and multiply connected domains cleanly.

## Local and primitive forms

On a disc, the theorem follows from the Cauchy–Goursat theorem without assuming continuity of \(f'\). On a domain, all closed [[complex-analysis/complex-contour-integral|contour integrals]] of \(f\) vanish exactly when \(f\) has a holomorphic primitive. The local theorem drives the [[complex-analysis/cauchy-integral-formula|Cauchy integral formula]].

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 4, §§1–2.
