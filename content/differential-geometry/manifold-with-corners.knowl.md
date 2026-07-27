+++
id = "differential-geometry/manifold-with-corners"
title = "Smooth manifold with corners"
kind = "definition"
summary = "A smooth space locally modeled on Euclidean orthants of possibly varying codimension."
aliases = ["manifold with corners", "cornered manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

An \(n\)-dimensional **smooth manifold with corners** is a Hausdorff, second-countable space \(M\) with a maximal compatible atlas of charts onto open subsets of
\[
\mathbb R_k^n=[0,\infty)^k\times\mathbb R^{n-k},\qquad 0\leq k\leq n.
\]
Two corner charts are compatible when each transition map and its inverse locally extend to [[fiber-bundles/smooth-map|smooth maps]] between open subsets of \(\mathbb R^n\). The integer \(k\) may vary between charts; at a particular point, only the number of vanishing boundary coordinates is intrinsic. Ordinary [[fiber-bundles/smooth-manifold|smooth manifolds]] use \(k=0\), while [[differential-geometry/manifold-with-boundary|manifolds with boundary]] require at most one vanishing boundary coordinate locally.

## Depth strata

The number of vanishing boundary coordinates at a point is independent of the chart and is its [[differential-geometry/depth-of-a-point-in-a-manifold-with-corners|depth]]. Points of depth \(r\) form a smooth \((n-r)\)-dimensional stratum without boundary. This canonical stratification distinguishes the interior, open boundary faces, and higher-codimension corners.

## Products and examples

Products of manifolds with corners inherit product corner charts, and depths add:
\[
\operatorname{depth}_{M\times N}(x,y)
=\operatorname{depth}_M(x)+\operatorname{depth}_N(y).
\]
The cube \([0,1]^n\), a product of compact intervals, is the basic example. A closed disk is a manifold with boundary and hence also a manifold with corners, but its [[differential-geometry/boundary-and-interior-of-a-manifold|boundary points]] all have depth one and it has no higher-depth points.

## Conventions and scope

**Warning.** The literature contains inequivalent notions of boundary and of [[differential-geometry/smooth-map-of-manifolds-with-corners|smooth map between manifolds with corners]]. The core specifies the common extension-based smooth structure on each object; a category of cornered manifolds must additionally choose its morphisms. Joyce compares these choices and develops one functorial convention in [Joyce, §§2–3](https://arxiv.org/abs/0910.3518).

## References

1. Dominic Joyce, “On Manifolds with Corners,” final preprint version, 2010. [arXiv record](https://arxiv.org/abs/0910.3518). Relevant: §2, Definition 2.1 and the comparison of conventions; §3, smooth maps.
