+++
id = "differential-geometry/double-of-a-manifold-with-boundary"
title = "Double of a manifold with boundary"
kind = "definition"
summary = "The boundaryless smooth manifold formed by gluing two copies of a manifold along their common boundary."
aliases = ["doubling a manifold", "double manifold"]
domains = ["differential-geometry", "topology"]
prerequisites = ["differential-geometry/manifold-with-boundary", "differential-geometry/collar-neighborhood-theorem", "fiber-bundles/smooth-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a smooth [[differential-geometry/manifold-with-boundary|manifold with boundary]]. Its **double** is the quotient
\[
DM=(M\times\{+,-\})/{\sim},
\qquad (x,+)\sim(x,-)\ \text{for }x\in\partial M,
\]
equipped with the smooth structure obtained from a [[differential-geometry/collar-neighborhood-theorem|collar]] of \(\partial M\). In collar coordinates, the two inward parameters \(t\geq0\) are joined as the signed coordinate \(t\in\mathbb R\). The result is a [[fiber-bundles/smooth-manifold|smooth manifold]] without boundary containing two copies of \(M\), whose intersection is their common embedded hypersurface \(\partial M\).
Reflection exchanges the two copies and fixes this hypersurface pointwise.

## Smooth construction

Choose a collar
\[
c:\partial M\times[0,\varepsilon)\longrightarrow M.
\]
It gives a chart across the seam by
\[
\widetilde c(x,t)=
\begin{cases}
[(c(x,t),+)],&t\geq0,\\
[(c(x,-t),-)],&t\leq0,
\end{cases}
\qquad
(x,t)\in\partial M\times(-\varepsilon,\varepsilon).
\]
Together with the original smooth charts away from the seam, these maps define
the smooth structure on \(DM\). Different collar choices produce
diffeomorphic smooth structures, so the smooth double is well defined up to
diffeomorphism.

## Examples and consequences

The double of \([0,1]\) is \(S^1\), and the double of the closed \(n\)-ball is \(S^n\). The double of a cylinder \(N\times[0,1]\) is \(N\times S^1\). If \(M\) is compact, then \(DM\) is compact; if \(M\) is oriented, the two copies are given opposite orientations so that the orientation extends across the seam.

## Scope

The construction does not require compactness or connected boundary. If \(\partial M=\varnothing\), the displayed quotient is the disjoint union of two copies of \(M\), although some authors reserve “double” for the nonempty-boundary case. Gluing two different manifolds along a boundary diffeomorphism is a broader construction and may require additional collar data.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 9, collar neighborhoods and the double construction.
2. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [Springer DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 4, collars and boundary constructions.
