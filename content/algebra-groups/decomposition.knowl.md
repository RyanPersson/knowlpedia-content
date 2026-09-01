+++
id = "algebra-groups/decomposition"
title = "Group decomposition"
kind = "knowl"
summary = "Ways to describe a group in terms of simpler subgroups, factors, or extensions."
aliases = ["decomposition", "Group decomposition"]
domains = ["algebra-groups"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-groups/decomposition.md"
+++

A **group decomposition** describes a group in terms of simpler groups and the maps that assemble them. The precise form depends on how the constituent subgroups interact.

## Common forms

- An [[algebra-groups/internal-direct-product|internal direct product]] expresses a group as a product of commuting normal subgroups with trivial intersection.
- An [[algebra-groups/internal-semidirect-product|internal semidirect product]] relaxes the commutativity requirement and records an action of one factor on the other.
- A [[algebra-groups/group-extension|group extension]] describes a group \(G\) through an exact sequence
  \[
  1\longrightarrow N\longrightarrow G\longrightarrow Q\longrightarrow 1.
  \]
  When the extension splits, \(G\) is a [[algebra-groups/semidirect-product|semidirect product]] of \(N\) by \(Q\).

## Structural results

The available decomposition and its uniqueness depend on the class of groups under consideration. For example, the [[algebra-groups/classification-finite-abelian-groups|classification of finite abelian groups]] gives a direct-product decomposition into cyclic prime-power groups, while the [[algebra-groups/krull-remak-schmidt-theorem-groups|Krull–Remak–Schmidt theorem]] gives uniqueness results for certain decompositions into directly indecomposable factors.
