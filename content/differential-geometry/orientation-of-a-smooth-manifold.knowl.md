+++
id = "differential-geometry/orientation-of-a-smooth-manifold"
title = "Orientation of a smooth manifold"
kind = "definition"
summary = "An orientation of a smooth manifold is a continuous choice of orientation for all of its tangent spaces."
aliases = ["manifold orientation"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/orientation-of-a-real-vector-bundle", "fiber-bundles/tangent-bundle", "fiber-bundles/smooth-atlas", "real-analysis/jacobian-determinant", "topology/connected-component"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be an \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]]. An **orientation of \(M\)** is an [[fiber-bundles/orientation-of-a-real-vector-bundle|orientation]] of its [[fiber-bundles/tangent-bundle|tangent bundle]] \(TM\): at each \(p\in M\), one chooses one of the two orientation classes of ordered bases of \(T_pM\), and the choice must vary continuously. Equivalently, an orientation is a maximal [[fiber-bundles/smooth-atlas|smooth atlas]] whose coordinate changes have positive [[real-analysis/jacobian-determinant|Jacobian determinant]]. A manifold together with such a choice is **oriented**; a manifold admitting a choice is **orientable**. On each [[topology/connected-component|connected component]] of a positive-dimensional [[differential-geometry/orientability-of-a-smooth-manifold|orientable manifold]], exactly two orientations exist.

## Equivalent descriptions

For a smooth manifold, the following data determine the same orientation:

1. an orientation of \(TM\);
2. an [[shared-foundations/equivalence-class|equivalence class]] of positively oriented atlases; or
3. a nowhere-vanishing smooth \(n\)-form, where two such forms are equivalent when one is a positive smooth multiple of the other.

The equivalence uses smooth partitions of unity to construct a global positive top-degree form from compatible local choices.

## Maps and boundaries

A [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]] between oriented \(n\)-manifolds is orientation-preserving when its differential sends positive bases to positive bases, equivalently when its Jacobian in oriented charts is positive. If \(M\) has boundary, the [[differential-geometry/boundary-orientation|outward-normal-first convention]] orients \(\partial M\): a boundary basis \((v_1,\ldots,v_{n-1})\) is positive when \((\nu,v_1,\ldots,v_{n-1})\) is positive for an outward-pointing \(\nu\).

## Examples and scope

The standard ordered coordinates orient \(\mathbb{R}^n\). Every [[differential-geometry/complex-manifold|complex manifold]] has a canonical orientation because a complex basis gives a real basis \((v_1,iv_1,\ldots,v_m,iv_m)\). The Möbius band is not orientable. Orientability is a property; an orientation is one of the possible choices, so an orientable manifold is not automatically an oriented manifold.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 15.
2. L. W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: §21.3.
