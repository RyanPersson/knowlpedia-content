+++
id = "differential-geometry/boundary-orientation"
title = "Boundary orientation"
kind = "definition"
summary = "The orientation on a manifold boundary determined by placing an outward normal before a positive boundary basis."
aliases = ["induced orientation on the boundary", "outward-normal-first convention"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be an [[differential-geometry/orientation-of-a-smooth-manifold|oriented]] \(n\)-dimensional [[differential-geometry/manifold-with-boundary|smooth manifold with boundary]]. Its [[differential-geometry/boundary-and-interior-of-a-manifold|boundary]] \(\partial M\) has the **boundary orientation** defined as follows. At \(p\in\partial M\), an ordered basis \((v_1,\ldots,v_{n-1})\) of \(T_p\partial M\) is positive exactly when
\[
(\nu,v_1,\ldots,v_{n-1})
\]
is a positive basis of \(T_pM\) for any outward-pointing vector \(\nu\in T_pM\). Replacing \(\nu\) by another outward-pointing vector does not change the sign, so the rule is well defined. This is the outward-normal-first convention.

## Role in Stokes' theorem

With this convention, [[differential-geometry/stokes-theorem|Stokes' theorem]] has no additional sign:
\[
\int_M d\omega=\int_{\partial M}\omega
\]
for every compactly supported \((n-1)\)-form \(\omega\). The orientation is therefore not decorative data: reversing it changes the boundary integral and breaks this formula [Lee, Chapter 16](https://doi.org/10.1007/978-1-4419-9982-5).

## Basic examples

Give the interval \([a,b]\) its orientation from the increasing coordinate. Its oriented boundary is \(\{b\}-\{a\}\): the positive orientation at \(b\) is \(+1\), while at \(a\) it is \(-1\). For an oriented product \([a,b]\times N\), the two boundary faces inherit opposite orientations, with the precise product sign determined by the order of the interval and \(N\) factors.

## Conventions and scope

Some texts use inward-normal-last or outward-normal-last conventions. These are equivalent only after the appropriate dimension-dependent sign is inserted. A boundary orientation requires an orientation of \(M\); an orientable but unoriented manifold does not determine one canonically.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 16, boundary orientations and Stokes' theorem.
2. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: Chapter 23, orientation of the boundary.
