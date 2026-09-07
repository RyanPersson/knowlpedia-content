+++
id = "topology/second-countable-space"
title = "Second-countable space"
kind = "definition"
summary = "A topological space whose topology has a countable basis."
aliases = ["second countable", "second-countable", "second countability"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/basis-of-topology", "shared-foundations/countable-set"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 1
+++

A [[topology/topological-space|topological space]] is **second-countable** if its topology admits a [[shared-foundations/countable-set|countable]] [[topology/basis-of-topology|basis]].

## Meaning

There is one countable collection of open sets whose unions give every open set in the space. The same collection works at every point.

## Examples

- Euclidean space \(\mathbb R^n\) has a countable basis of open balls with rational centers and positive rational radii.
- A discrete space is second-countable exactly when its underlying set is countable: every singleton must occur in any basis.

## Manifolds

Second countability is part of the convention used here for a [[topology/topological-manifold|topological manifold]]. Local Euclidean structure and Hausdorffness alone do not imply it; an uncountable disjoint union of copies of \(\mathbb R\) is a counterexample.
