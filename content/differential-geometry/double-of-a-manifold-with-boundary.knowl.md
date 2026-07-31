+++
id = "differential-geometry/double-of-a-manifold-with-boundary"
title = "Double of a manifold with boundary"
kind = "definition"
summary = "The boundaryless smooth manifold formed by gluing two copies of a manifold along their common boundary."
aliases = ["doubling a manifold", "double manifold"]
domains = ["differential-geometry", "topology"]
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

Choose a collar \(c:\partial M\times[0,\varepsilon)\to M\). Use \(t\) on the positive copy and \(-t\) on the negative copy to form charts across the seam. Different choices of collar produce diffeomorphic smooth doubles, so the diffeomorphism type depends only on \(M\). The collar is essential: the bare quotient describes the topology but does not by itself specify compatible smooth charts [Lee, Chapter 9].

## Examples and consequences

The double of \([0,1]\) is \(S^1\), and the double of the closed \(n\)-ball is \(S^n\). The double of a cylinder \(N\times[0,1]\) is \(N\times S^1\). If \(M\) is compact, then \(DM\) is compact; if \(M\) is oriented, the two copies are given opposite orientations so that the orientation extends across the seam.

## Scope

The construction does not require compactness or connected boundary. If \(\partial M=\varnothing\), the displayed quotient is the disjoint union of two copies of \(M\), although some authors reserve “double” for the nonempty-boundary case. Gluing two different manifolds along a boundary diffeomorphism is a broader construction and may require additional collar data.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 9, collar neighborhoods and the double construction.
2. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [Springer DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 4, collars and boundary constructions.
