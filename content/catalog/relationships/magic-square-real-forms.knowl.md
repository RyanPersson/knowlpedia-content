+++
id = "catalog/relationships/magic-square-real-forms"
title = "Real-form conventions for magic squares"
kind = "document"
summary = "Compact, split and complex magic-square inputs must remain separate catalogue choices."
aliases = ["Real-form conventions for magic squares"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "continuous"
prerequisites = ["catalog/relationships/vinberg-magic-square-construction"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

The [[catalog/relationships/compact-freudenthal-magic-square|compact Freudenthal magic square]] uses the real division composition algebras \(\mathbb R,\mathbb C,\mathbb H,\mathbb O\) and returns compact real Lie algebras. Here \(\mathbb C\) is a two-dimensional **real input algebra**, not the base field of the construction.

## Changing the input form

The [[catalog/algebras/split-complex-numbers|split complex numbers]], [[catalog/algebras/split-quaternions|split quaternions]] and [[catalog/algebras/split-octonions|split octonions]] are separate real composition algebras. Their [[linear-algebra/quadratic-form|quadratic forms]] are indefinite, and they have [[algebra-rings/zero-divisor|zero divisors]]. Inserting them into the [[catalog/relationships/vinberg-magic-square-construction|same construction]] changes the real forms of its outputs. Using split inputs along only one axis need not give the split form of every output.

## Changing the scalar field

Complexifying a compact real output produces a complex Lie algebra. This is different from viewing that real algebra as a complex vector space: a scalar extension is required. The compact and split real forms of a given complex type can have isomorphic complexifications without being isomorphic over \(\mathbb R\).

## Catalogue convention

The machine table is named `compact-real-freudenthal`; each axis references the actual input object IDs, and each cell references a real output object. Split scalar objects and complex exceptional objects have their own records. A missing split-square cell means the construction is not yet catalogued in that table, not that no such construction exists. The [[catalog/algebras/sedenions|sedenions]] are not composition algebras and are not a fifth input to this square.

## References

1. C. H. Barton and A. Sudbery, “Magic squares and matrix models of Lie algebras,” §§2–3, especially pp. 4 and 10–12, division versus split composition algebras and the real magic-square tables. [Paper](https://arxiv.org/pdf/math/0203010).
