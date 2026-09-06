+++
id = "fiber-bundles/smooth-structure"
title = "Smooth structure"
kind = "definition"
summary = "A choice of mutually compatible smooth coordinate charts on a topological manifold, represented by their maximal smooth atlas."
aliases = ["smooth manifold structure", "differentiable structure", "C-infinity structure"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/maximal-smooth-atlas", "fiber-bundles/smooth-atlas", "fiber-bundles/smooth-compatibility-of-charts-and-atlases"]
dependency_heuristic = "semantic-foundations-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a topological manifold. A **smooth structure** on \(M\) is a
[[fiber-bundles/maximal-smooth-atlas|maximal smooth atlas]] on \(M\).
Equivalently, it is an equivalence class of [[fiber-bundles/smooth-atlas|smooth
atlases]], where two atlases are equivalent when they are
[[fiber-bundles/smooth-compatibility-of-charts-and-atlases|compatible]].

A [[fiber-bundles/smooth-manifold|smooth manifold]] is a topological manifold
together with a chosen smooth structure.

## Specifying a smooth structure

It is unnecessary to write down every chart in the maximal atlas. Any smooth
atlas determines a unique smooth structure by adjoining every chart smoothly
compatible with it. For example, the identity chart on \(\mathbb R^n\)
generates its standard smooth structure.

## Dependence on the choice

The topology of \(M\) does not always determine its smooth structure up to
diffeomorphism. Distinct smooth structures on the same underlying topological
manifold can therefore produce non-diffeomorphic smooth manifolds.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: smooth structures and smooth manifolds.
