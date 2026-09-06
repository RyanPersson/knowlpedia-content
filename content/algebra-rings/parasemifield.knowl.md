+++
id = "algebra-rings/parasemifield"
title = "Parasemifield"
kind = "definition"
summary = "A semiring-like algebra whose multiplicative reduct is a group but which has no required additive zero."
aliases = ["semifield without zero"]
domains = ["algebra-rings", "algebra-hyperstructures"]
section_mode = "progressive"
prerequisites = ["algebra-groups/abelian-group", "algebra-rings/semifield"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **parasemifield** is a set \(S\) with associative, commutative operations
\(+\) and \(\cdot\) such that multiplication distributes over addition and
\((S,\cdot,1)\) is an [[algebra-groups/abelian-group|abelian group]]. No additive identity is required.

Thus a parasemifield differs from a [[algebra-rings/semifield|semifield]]:
a semifield has an additive zero \(0\), which is absorbing for
multiplication, and only its nonzero elements form a multiplicative group.
Removing the additive zero from an idempotent semifield produces an
idempotent parasemifield.

## References
Jonathan S. Golan, *Semirings and their Applications*, Kluwer, 1999.
[DOI](https://doi.org/10.1007/978-94-015-9333-5).
