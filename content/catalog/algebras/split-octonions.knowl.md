+++
id = "catalog/algebras/split-octonions"
title = "Split octonions O_s"
kind = "definition"
summary = "Catalogue object: Split octonions O_s; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quaternion-division-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **real split octonion algebra** \(\mathbb O_s\) is \(\mathbb H\oplus\mathbb H\), with [[linear-algebra/quaternion-division-algebra|quaternionic]] coordinates, componentwise addition, and multiplication
\[
(a,b)(c,d)=(ac+\overline d b,\;da+b\overline c).
\]
Its unit is \((1,0)\), conjugation is \(\overline{(a,b)}=(\overline a,-b)\), and its multiplicative [[linear-algebra/quadratic-form|quadratic form]] is \(N(a,b)=|a|^2-|b|^2\).

## Split form

This is an eight-dimensional alternative, nonassociative real [[nonassociative-algebra/composition-algebra|composition algebra]]. Its norm has signature \((4,4)\). The elements \((1,1)\) and \((1,-1)\) are nonzero and their product is zero, so it is not a division algebra. The plus sign in the first component distinguishes this construction from the real division octonions.

## Hermitian matrices

The [[catalog/algebras/herm-3-split-o|Hermitian degree-three construction]] gives the split Albert algebra. Its scalar field is real, even though some notation for its coefficient algebra resembles complex notation. “Split” records the algebra and norm form, not a change of scalar field.

## References

1. [Alberto Elduque, Composition algebras](https://arxiv.org/html/1810.09979), Section 2.1, equation (7); Theorem 2.11 and Corollary 2.12.
