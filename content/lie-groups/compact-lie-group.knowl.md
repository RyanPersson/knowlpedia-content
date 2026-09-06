+++
id = "lie-groups/compact-lie-group"
title = "Compact Lie group"
kind = "knowl"
summary = "A Lie group that is compact as a manifold (equivalently, as a topological group)."
aliases = ["compact-lie-group", "Compact Lie group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/compact-lie-group.md"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Definition.** A [[fiber-bundles/lie-group|Lie group]] \(G\) is **compact** if its underlying topological space is compact.

## Remarks

**Core structural features.**
- Compactness implies the existence of a bi-invariant [[harmonic-analysis/haar-measure|Haar measure]], enabling averaging arguments throughout geometry and representation theory.
- Every compact Lie group admits a [[lie-groups/bi-invariant-metric|bi-invariant Riemannian metric]]; see [[lie-groups/compact-lie-group-bi-invariant-metric|bi-invariant metrics on compact Lie groups]].
- For a connected compact Lie group, maximal tori control much of the structure: every element lies in some maximal torus, and conjugacy classes intersect a fixed maximal torus in Weyl-group orbits (see [[lie-groups/maximal-torus-theorem|the maximal torus theorem]] and [[lie-groups/weyl-group|the Weyl group]]). For disconnected compact groups, component-group data require a separate qualification.

**Representation-theoretic context.** Finite-dimensional continuous representations of compact Lie groups are [[lie-groups/completely-reducible-representation-lie|completely reducible]], and the regular representation on \(L^2(G)\) decomposes discretely (compare [[lie-groups/peter-weyl-theorem|the Peter–Weyl theorem]]).

For a global decomposition of compact connected groups into torus and semisimple parts, see [[lie-groups/compact-lie-group-structure|structure of compact Lie groups]].
