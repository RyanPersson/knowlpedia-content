+++
id = "algebra-rings/commutative-semiring"
title = "Commutative semiring"
kind = "definition"
summary = "A semiring whose multiplication is commutative."
aliases = ["commutative unital semiring"]
domains = ["algebra-rings", "algebra-hyperstructures"]
section_mode = "progressive"
prerequisites = ["algebra-rings/semiring"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **commutative semiring** is a [[algebra-rings/semiring|semiring]] \(S\) in
which \(ab=ba\) for all \(a,b\in S\). Thus both addition and multiplication
are commutative, \(1\) is part of the structure, and \(0\) is multiplicatively
absorbing.

## Scope

Unless a page says otherwise, semirings in the tropical and hyperstructure
parts of this corpus are commutative and unital. This convention makes their
multiplicative monoids compatible with the [[algebra-hyperstructures/hyperring|commutative hyperrings]] and
hyperfields used there.

## Examples

Every [[algebra-rings/commutative-ring|commutative ring]] is a commutative
semiring. The natural numbers, the [[algebra-rings/boolean-semifield|Boolean semifield]], and the max-plus tropical
semifield are commutative semirings. A matrix semiring over a commutative
semiring is generally not commutative when the matrix size exceeds one.

## References

1. Jonathan S. Golan, *Semirings and their Applications*, Kluwer, 1999. [Publisher DOI record](https://doi.org/10.1007/978-94-015-9333-5). Relevant: Chapter 1.
