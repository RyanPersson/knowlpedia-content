+++
id = "topology/relatively-compact-set"
title = "Relatively compact set"
kind = "knowl"
summary = "A subset whose closure is compact in the ambient space."
aliases = ["relatively-compact-set", "Relatively compact set"]
domains = ["topology"]
legacy_source_path = "topology/relatively-compact-set.md"
prerequisites = ["topology/topological-space", "topology/closure", "topology/compact-set"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

A **relatively compact set** is a subset \(A\subseteq X\) of a [[topology/topological-space|topological space]] \(X\) such that its [[topology/closure|closure]] \(\overline{A}\) is [[topology/compact-set|compact]] in \(X\).

## Ambient space and terminology

Relative compactness depends on the ambient space and topology (it is not purely an intrinsic property of \(A\)). Some authors use “precompact” for relative compactness; in metric and uniform spaces it commonly means [[topology/totally-bounded-set|totally bounded]], which is equivalent to relative compactness when the ambient metric space is complete. These notions can differ in an incomplete ambient space.

## Examples

- In \(\mathbb{R}\) with the usual topology, \((0,1)\) is relatively compact because its closure is \([0,1]\), which is compact.
- In an infinite discrete space, an infinite subset is not relatively compact since its closure is itself and it is not compact.
