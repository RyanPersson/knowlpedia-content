+++
id = "fiber-bundles/coordinate-transition-map"
title = "Coordinate transition map"
kind = "definition"
summary = "The change-of-coordinates map between the Euclidean images of two overlapping manifold charts."
aliases = ["change of coordinates", "coordinate change", "chart transition map", "coordinate transformation"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/smooth-chart-coordinate-chart", "shared-foundations/composition", "shared-foundations/inverse-function"]
dependency_heuristic = "semantic-foundations-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((U,\varphi)\) and \((V,\psi)\) be coordinate charts on the same
\(n\)-dimensional manifold with \(U\cap V\ne\varnothing\). Their **coordinate
transition map**, from \(\varphi\)-coordinates to \(\psi\)-coordinates, is

\[
\psi\circ\varphi^{-1}:
\varphi(U\cap V)\longrightarrow\psi(U\cap V).
\]

It is a homeomorphism between open subsets of \(\mathbb R^n\). The charts are
[[fiber-bundles/smooth-compatibility-of-charts-and-atlases|smoothly compatible]]
exactly when this map is a [[fiber-bundles/diffeomorphism|diffeomorphism]].

## Role in an atlas

The transition maps record how local coordinate descriptions agree on
overlaps. Pairwise smoothness of these maps is the compatibility axiom in a
[[fiber-bundles/smooth-atlas|smooth atlas]]. Their derivatives give the
transition functions of the [[fiber-bundles/tangent-bundle|tangent bundle]].

## Distinction from bundle transition functions

A coordinate transition map changes coordinates on the base manifold and is
a map between open subsets of Euclidean space. A
[[fiber-bundles/transition-function|bundle transition function]] instead
records how two local trivializations change fiber coordinates over the same
base point.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: coordinate charts and transition maps.
