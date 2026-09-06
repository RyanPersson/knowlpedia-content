+++
id = "algebraic-geometry-foundations/projective-line"
title = "Projective line"
kind = "definition"
summary = "The one-dimensional projective space formed by lines in a two-dimensional vector space."
aliases = ["projective 1-space", "projective one-space", "P1"]
domains = ["algebraic-geometry-foundations", "linear-algebra"]
prerequisites = ["algebraic-geometry-foundations/projective-space"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a field \(k\), the **projective line over \(k\)** is
\[
\mathbb P_k^1=\operatorname{Proj}k[x_0,x_1].
\]
Its \(k\)-points are the one-dimensional subspaces of \(k^2\), written in [[algebraic-geometry-foundations/projective-space|homogeneous coordinates]] as \([x_0:x_1]\), with \([x_0:x_1]=[\lambda x_0:\lambda x_1]\) for \(\lambda\in k^\times\).

## Two affine charts

The open set \(U_1=\{x_1\ne0\}\) has coordinate \(z=x_0/x_1\) and is isomorphic to the [[algebraic-geometry-foundations/affine-line|affine line]] \(\mathbb A_k^1\). The other open set \(U_0=\{x_0\ne0\}\) has coordinate \(w=x_1/x_0\). On their overlap,
\[
w=z^{-1}.
\]
Thus \(\mathbb P_k^1\) is obtained by gluing two affine lines along their punctured affine lines by inversion. This choice of \(z\) is the one used in the [[complex-analysis/riemann-sphere|Riemann sphere]] and in the standard matrix formula for [[complex-analysis/mobius-transformation|Möbius transformations]].

## The point at infinity

In the \(z\)-chart, the complement is the single \(k\)-point
\[
\infty=[1:0],
\]
so at the level of \(k\)-points one often writes \(\mathbb P^1(k)=k\cup\{\infty\}\). The label \(\infty\) depends on the chosen affine chart: no point of the projective line is intrinsically distinguished.

For \(k=\mathbb C\), the associated [[differential-geometry/complex-manifold|complex manifold]] is the [[complex-analysis/riemann-sphere|Riemann sphere]]. Projective linear transformations act on \(\mathbb P_k^1\); after coordinates are chosen, these are fractional linear transformations.

## References

1. Robin Hartshorne, *Algebraic Geometry*, Springer, 1977. [Publisher record](https://doi.org/10.1007/978-1-4757-3849-0). Relevant: Chapter I, §2 and Chapter II, §2.
2. Joe Harris, *Algebraic Geometry: A First Course*, Springer, 1992. [Publisher record](https://doi.org/10.1007/978-1-4757-2189-8). Relevant: Lecture 1.
