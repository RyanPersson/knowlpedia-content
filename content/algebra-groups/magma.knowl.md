+++
id = "algebra-groups/magma"
title = "Magma"
kind = "knowl"
summary = "A set with a binary operation (no other axioms)"
aliases = ["magma"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/magma.md"
prerequisites = ["shared-foundations/set", "shared-foundations/binary-operation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **magma** is a set \(M\) together with a binary operation \(\cdot : M \times M \to M\). No additional axioms are required—the operation need not be associative, commutative, or have an identity.

## Examples

- Any set with any binary operation
- \((\mathbb{Z}, -)\) — integers under subtraction (not associative)
- Rock-paper-scissors with the "winner" operation

## Remarks

This is the most general algebraic structure with a single binary operation. All [[algebra-groups/semigroup|semigroups]], [[algebra-groups/monoid|monoids]], and [[algebra-groups/group|groups]] are magmas.
