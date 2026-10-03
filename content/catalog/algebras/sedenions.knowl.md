+++
id = "catalog/algebras/sedenions"
title = "Real sedenions S"
kind = "definition"
summary = "Catalogue object: Real sedenions S; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/octonion-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **real sedenions** \(\mathbb S\) are the real [[linear-algebra/vector-space|vector space]] \(\mathbb O\oplus\mathbb O\), with [[nonassociative-algebra/octonion-algebra|octonionic]] coordinates, componentwise addition, and multiplication
\[
(a,b)(c,d)=(ac-\overline d b,\; da+b\overline c).
\]
The unit is \((1,0)\), and conjugation is \(\overline{(a,b)}=(\overline a,-b)\). This is the 16-dimensional fourth Cayley–Dickson algebra over \(\mathbb R\).

## Algebraic boundaries

The product is neither associative nor alternative. Nonzero zero divisors exist, so this is not a division algebra and the positive [[linear-algebra/quadratic-form|quadratic form]] \(N(a,b)=|a|^2+|b|^2\) is not multiplicative. The formula \(x^{-1}=\overline x/N(x)\) still gives a two-sided inverse for each nonzero element; without associativity, that fact does not imply cancellation. Thus inverse formulas must not be used to register \(\mathbb S\) as a field, ring, or [[nonassociative-algebra/composition-algebra|composition algebra]].

## Catalogue convention

Here \(\mathbb S\) always denotes sedenions, not a sphere or the split octonions. Its real vector-space and nonassociative-algebra views are distinct choices of morphisms on the same object.

## References

1. [John C. Baez, The Octonions](https://math.ucr.edu/home/baez/octonions/node5.html), Section 2.2, Cayley–Dickson construction, Propositions 1–5 and the sedenion paragraph.
