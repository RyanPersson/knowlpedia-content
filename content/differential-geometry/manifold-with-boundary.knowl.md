+++
id = "differential-geometry/manifold-with-boundary"
title = "Smooth manifold with boundary"
kind = "definition"
summary = "A smooth manifold with boundary is locally modeled on open subsets of a closed Euclidean half-space."
aliases = ["manifold with boundary"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-atlas", "fiber-bundles/smooth-chart", "topology/topological-manifold"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

An \(n\)-dimensional **smooth manifold with boundary** is a Hausdorff, second-countable space \(M\) equipped with a maximal [[fiber-bundles/smooth-atlas|smooth atlas]] of [[fiber-bundles/smooth-chart|charts]] onto relatively open subsets of
\[
\mathbb{H}^n=\{(x^1,\ldots,x^n)\in\mathbb{R}^n:x^n\geq0\}.
\]
Coordinate changes must extend smoothly to open Euclidean neighborhoods of their domains. The separation and countability axioms are the same as for a [[topology/topological-manifold|topological manifold]], but the local model is the half-space. A point belongs to \(\partial M\) when one, and hence every, chart sends it to \(x^n=0\); all remaining points form the interior \(\operatorname{Int}M\).

## Intrinsic boundary and interior

The invariance of the boundary under coordinate changes is a theorem, not an additional chart choice. The interior is an open smooth \(n\)-manifold without boundary. In the induced charts, \(\partial M\) is a smooth \((n-1)\)-manifold without boundary. A diffeomorphism of manifolds with boundary necessarily maps boundary to boundary and interior to interior.

## Smooth maps

A map \(F:M\to N\) is smooth when its coordinate representatives extend smoothly to maps on open subsets of [[linear-algebra/euclidean-space|Euclidean space]]. This definition permits a [[fiber-bundles/smooth-map|smooth map]] to send interior points to boundary points. A smooth [[fiber-bundles/vector-field|vector field]] at a [[differential-geometry/boundary-and-interior-of-a-manifold|boundary point]] is a vector in the full \(n\)-dimensional [[differential-geometry/tangent-space|tangent space]]; it need not be tangent to \(\partial M\).

## Examples and scope

The [[topology/closed-ball|closed ball]], the closed upper half-space, and a compact interval are manifolds with boundary. Their boundaries are respectively a sphere, a Euclidean hyperplane, and two points. A product of two manifolds with nonempty boundary naturally has corner points, so its product atlas belongs to the broader theory of manifolds with corners rather than to this half-space definition.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 1 and the treatment of manifolds with boundary.
2. M. W. Hirsch, *Differential Topology*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 1.
