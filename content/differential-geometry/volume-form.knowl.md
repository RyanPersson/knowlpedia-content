+++
id = "differential-geometry/volume-form"
title = "Volume form"
kind = "definition"
summary = "A nowhere-vanishing top-degree differential form that specifies oriented volume on a smooth manifold."
aliases = ["volume element", "volume differential form"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/differential-k-form", "differential-geometry/orientation-of-a-smooth-manifold"]
dependency_heuristic = "semantic-full-review-v1"
+++

Let \(M\) be an [[differential-geometry/orientation-of-a-smooth-manifold|oriented]] [[fiber-bundles/smooth-manifold|smooth \(n\)-manifold]]. A **volume form** on \(M\) is a smooth nowhere-vanishing [[fiber-bundles/differential-k-form|differential \(n\)-form]] \(\mu\) that is positive on every positively oriented basis of each tangent space.

## Riemannian volume form

An oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]] \((M,g)\) has a canonical volume form \(\operatorname{vol}_g\), characterized in every positively oriented \(g\)-orthonormal coframe \((\theta^1,\ldots,\theta^n)\) by
\[
\operatorname{vol}_g=\theta^1\wedge\cdots\wedge\theta^n.
\]
In oriented coordinates, \(\operatorname{vol}_g=\sqrt{\det(g_{ij})}\,dx^1\wedge\cdots\wedge dx^n\). Reversing the orientation changes its sign.

## Existence and scope

An \(n\)-manifold admits a volume form exactly when it is orientable. A volume form itself chooses an orientation, so no orientation is needed in advance to state the equivalent unoriented version: a smooth nowhere-vanishing top form determines the orientation for which it is positive. A Riemannian metric without an orientation canonically determines a volume density, while a volume form requires a choice of orientation.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: the chapters on orientations and integration.
2. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [Publisher record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapter 2, Riemannian volume.
