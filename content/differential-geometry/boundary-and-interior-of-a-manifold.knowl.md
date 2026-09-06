+++
id = "differential-geometry/boundary-and-interior-of-a-manifold"
title = "Boundary and interior of a manifold with boundary"
kind = "definition"
summary = "The boundary and interior of a manifold with boundary are the points represented respectively on and off the bounding hyperplane in half-space coordinates."
aliases = ["manifold boundary", "manifold interior", "boundary point", "interior point"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/manifold-with-boundary", "differential-geometry/boundary-chart"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be an \(n\)-dimensional [[differential-geometry/manifold-with-boundary|smooth manifold with boundary]]. A point \(p\in M\) is a **boundary point** if a [[differential-geometry/boundary-chart|boundary chart]] \(\varphi:U\to V\subseteq\mathbb H^n\) sends it to the bounding hyperplane \(x^n=0\). It is an **interior point** if \(\varphi(p)\) has \(x^n>0\). These conditions do not depend on the chart. The **boundary** and **interior** are
\[
\partial M=\{p\in M:p\text{ is a boundary point}\},
\qquad
\operatorname{Int}M=M\setminus\partial M.
\]
Here \(\partial M\) is intrinsic to the manifold-with-boundary structure, not the boundary of \(M\) inside an unspecified ambient space.

## Intrinsic structure

The invariance-of-boundary theorem makes the chart-based definition intrinsic. The interior is an open \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]] without boundary. When \(\partial M\) is nonempty, it inherits a canonical smooth structure of dimension \(n-1\) by restricting boundary charts to \(x^n=0\). In particular, the boundary of a smooth manifold with boundary is itself a smooth manifold without boundary.

Every diffeomorphism of manifolds with boundary preserves the two strata: it sends \(\partial M\) to the target boundary and \(\operatorname{Int}M\) to the target interior.

## Examples and contrasts

For the [[topology/closed-ball|closed ball]] \(B^n\), the intrinsic boundary is \(S^{n-1}\) and the interior is the [[topology/open-ball|open ball]]. For the interval \([0,1]\), the boundary is \(\{0,1\}\), a \(0\)-manifold. A manifold without boundary is allowed: then \(\partial M=\varnothing\) and \(\operatorname{Int}M=M\).

Intrinsic boundary need not agree with an ambient topological boundary. The embedded circle \(S^1\subset\mathbb R^2\) has ambient boundary \(S^1\) as a subset of \(\mathbb R^2\), but as a \(1\)-manifold it has empty intrinsic boundary.

## Conventions and scope

**Warning.** The notation \(\partial A\) in topology usually means the closure of \(A\) minus its interior in a specified ambient space. The same symbol \(\partial M\) here records a local half-space model and requires no embedding. For manifolds with corners, points have several possible boundary depths, so the two-stratum decomposition above is not the complete structure.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2012. [Publisher record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 1, “Smooth Manifolds,” especially invariance of the boundary and the induced boundary structure.
2. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Universitext, Springer, 2011. [Publisher record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: the chapter “Manifolds with Boundary.”
