+++
id = "algebra-groups/perfect-group"
title = "Perfect Group"
kind = "knowl"
summary = "A group equal to its commutator subgroup."
aliases = ["perfect-group", "Perfect Group"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/commutator-subgroup"]
dependency_review_count = 1
legacy_source_path = "algebra-groups/perfect-group.md"
+++

A **perfect group** is a [[algebra-groups/group|group]] \(G\) such that
\[
[G,G]=G,
\]
where \([G,G]\) is its [[algebra-groups/commutator-subgroup|commutator subgroup]].

## Examples

- The alternating group \(A_n\) is perfect for \(n\ge 5\).
- The trivial group is perfect.
- A nontrivial abelian group is not perfect because its commutator subgroup is trivial.

## Equivalent characterizations

Equivalently, \(G\) is perfect if and only if its abelianization \(G/[G,G]\) is trivial, or, equivalently, every homomorphism from \(G\) to an [[algebra-groups/abelian-group|abelian group]] is trivial. Every nonabelian [[algebra-groups/simple-group|simple group]] is therefore perfect.
