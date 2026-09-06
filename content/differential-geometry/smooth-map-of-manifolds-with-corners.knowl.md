+++
id = "differential-geometry/smooth-map-of-manifolds-with-corners"
title = "Smooth map between manifolds with corners"
kind = "definition"
summary = "In Joyce's convention, a coordinate-smooth map that pulls each target boundary defining function back either to zero or to one source boundary defining function."
aliases = ["smooth map of cornered manifolds", "corner-smooth map"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/manifold-with-corners", "topology/continuous-map", "differential-geometry/boundary-face-of-a-manifold-with-corners", "differential-geometry/boundary-defining-function"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) and \(Y\) be
[[differential-geometry/manifold-with-corners|manifolds with corners]], locally
modeled on \([0,\infty)^k\times\mathbb R^{n-k}\). In Joyce's convention, a
[[topology/continuous-map|continuous map]] \(f:X\to Y\) is **smooth** if it is smooth in corner charts
and satisfies a boundary condition: for every
[[differential-geometry/boundary-face-of-a-manifold-with-corners|local
boundary component]] \(\beta\) of \(Y\) at \(f(x)\), and every boundary
defining function \(b\) for \(\beta\), either \(b\circ f\) vanishes on a
neighborhood of \(x\), or \(b\circ f\) is a [[differential-geometry/boundary-defining-function|boundary defining function]] for a
unique local boundary component of \(X\) at \(x\).

## Coordinate smoothness

“Smooth in corner charts,” called **weakly smooth** by Joyce, means that each coordinate representative extends locally to a smooth map between open subsets of [[linear-algebra/euclidean-space|Euclidean spaces]]. If the target has no boundary, the extra boundary condition is vacuous, so this reduces to the ordinary notion of a [[fiber-bundles/smooth-map|smooth map]].

The boundary condition is independent of the chosen defining function. It ensures that a target boundary hypersurface either contains the local image or pulls back with first-order vanishing along one source boundary hypersurface.

## Category and examples

Identity maps, composites, products, boundary inclusions, and projections are smooth in this sense; hence these maps form Joyce's category \(\mathbf{Man}^c\). The inclusion \([0,\infty)\hookrightarrow\mathbb R\) is smooth because the target has no boundary.

The map
\[
\mathbb R\longrightarrow[0,\infty),\qquad x\longmapsto x^2,
\]
is weakly smooth but not smooth in Joyce's sense: the target defining function pulls back to \(x^2\), which is neither locally zero nor a boundary defining function at \(0\). Similarly, \((x,y)\mapsto xy\) from \([0,\infty)^2\) to \([0,\infty)\) fails the one-source-boundary condition.

## Conventions and scope

There is no universal convention for morphisms of manifolds with corners. Many authors use “smooth” for Joyce's weakly smooth maps; Melrose's \(b\)-maps allow products of powers of source boundary functions. Therefore a statement involving smooth maps, transversality, or fiber products of cornered manifolds must specify its convention. The definition here is deliberately Joyce's and should not be silently substituted into another corner calculus.

## References

1. Dominic Joyce, “On manifolds with corners,” *Advances in Geometric Analysis*, Advanced Lectures in Mathematics 21, International Press, 2012, pp. 225–258. [Author manuscript](https://arxiv.org/abs/0910.3518). Relevant: §3, especially Definition 3.1, Remark 3.3, and Theorem 3.4; §4 describes the induced action on corners.
