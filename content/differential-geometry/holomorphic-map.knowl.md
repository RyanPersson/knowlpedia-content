+++
id = "differential-geometry/holomorphic-map"
title = "Holomorphic map"
kind = "definition"
summary = "A complex-differentiable map between open subsets or complex manifolds."
aliases = ["holomorphic", "analytic map"]
domains = ["differential-geometry", "complex-analysis"]
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/complex-coordinate-chart", "differential-geometry/biholomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A map \(f:U\to\mathbb C^m\), where \(U\subseteq\mathbb C^n\) is open, is **holomorphic** if each component is complex differentiable in every variable in a neighborhood of every point. Equivalently, each component is locally represented by a convergent complex power series in \(n\) variables.

For [[differential-geometry/complex-manifold|complex manifolds]], a map is holomorphic when its expression in every pair of [[differential-geometry/complex-coordinate-chart|complex coordinate charts]] is holomorphic in this Euclidean sense. A bijective holomorphic map with holomorphic inverse is a [[differential-geometry/biholomorphism|biholomorphism]].

## Scalar-valued and one-variable cases

A holomorphic map \(f:U\to\mathbb C\) is a **holomorphic function**. When \(U\subseteq\mathbb C\), holomorphicity means that the [[complex-analysis/complex-derivative|complex derivative]]
\[
f'(z)=\lim_{h\to0}\frac{f(z+h)-f(z)}h
\]
exists at every \(z\in U\). The [[complex-analysis/cauchy-riemann-criterion|Cauchy–Riemann criterion]] converts this condition into real partial differential equations under an explicit regularity hypothesis.

## Why the analytic description is equivalent

In one variable, the [[complex-analysis/cauchy-integral-formula|Cauchy integral formula]] proves that [[complex-analysis/holomorphic-functions-are-analytic|holomorphic functions are analytic]]. In several variables, holomorphicity in all variables likewise implies a local convergent multivariable power series; separate holomorphicity is also enough by Hartogs' theorem. These are theorems, not additional clauses in the definition.

## Chart invariance

It is enough to check the coordinate condition in one chart around each source point and one chart around its image. If another pair is chosen, the new expression is obtained by composing with holomorphic transition maps, and compositions of holomorphic maps are holomorphic. Thus the definition depends only on the complex atlases, not on chosen coordinates.

## Differential

The real differential of a holomorphic map intertwines the complex structures:
\[
df\circ J_M=J_N\circ df.
\]
For maps between open subsets of complex Euclidean spaces, this says that the real derivative is complex linear. In complex dimension one it is exactly the matrix condition encoded by the [[complex-analysis/cauchy-riemann-equations|Cauchy–Riemann equations]].

## Terminology and scope

“Analytic map” is a common synonym in complex geometry. It should not be confused with a real-analytic map, and complex differentiability at only one isolated point does not make a function holomorphic.

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§1–2.
2. R. C. Gunning and H. Rossi, *Analytic Functions of Several Complex Variables*, AMS Chelsea, 2009. [AMS record](https://bookstore.ams.org/chel-368). Relevant: Chapter I.
