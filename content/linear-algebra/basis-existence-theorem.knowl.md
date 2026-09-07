+++
id = "linear-algebra/basis-existence-theorem"
title = "Basis existence theorem"
kind = "knowl"
summary = "Every vector space has a basis."
aliases = ["basis-existence-theorem", "Basis existence theorem"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/basis-existence-theorem.md"
prerequisites = ["linear-algebra/vector-space", "convex-analysis/basis-hamel-basis-and-dimension", "shared-foundations/axiom-of-choice"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
+++

**Basis existence theorem.** Assuming the axiom of choice, every [[linear-algebra/vector-space|vector space]] \(V\) has a [[convex-analysis/basis-hamel-basis-and-dimension|Hamel basis]] \(B\subseteq V\): every \(v\in V\) has a unique finitely supported coefficient family \((c_b)_{b\in B}\) such that \(v=\sum_{b\in B}c_b b\).

## Remarks

The standard proof applies Zorn's lemma to the partially ordered set of linearly independent subsets of \(V\). In set theory without choice, the assertion that every vector space has a basis is not provable.
