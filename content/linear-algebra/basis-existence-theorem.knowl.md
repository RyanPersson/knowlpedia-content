+++
id = "linear-algebra/basis-existence-theorem"
title = "Basis existence theorem"
kind = "knowl"
summary = "Every vector space has a basis."
aliases = ["basis-existence-theorem", "Basis existence theorem"]
domains = ["linear-algebra"]
prerequisites = ["linear-algebra/vector-space"]
dependency_review_count = 1
legacy_source_path = "linear-algebra/basis-existence-theorem.md"
+++

**Basis existence theorem.** Assuming the axiom of choice, every [[linear-algebra/vector-space|vector space]] \(V\) has a subset \(B\subseteq V\) such that every \(v\in V\) has a unique expression as a finite linear combination of distinct elements of \(B\).

## Remarks

The standard proof applies Zorn's lemma to the partially ordered set of linearly independent subsets of \(V\). In set theory without choice, the assertion that every vector space has a basis is not provable.
