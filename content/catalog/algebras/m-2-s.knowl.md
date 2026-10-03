+++
id = "catalog/algebras/m-2-s"
title = "M_2(S) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_2(S) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/sedenions", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

**\(M_{2}(\mathbb S)\)** consists of \(2\)-by-\(2\) matrices with entries in [[catalog/algebras/sedenions|S]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{2}X_{ir}Y_{rj}.
\]
Its unit is \(I_{2}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

The real dimension is \(64\), since there are \(4\) entries with \(16\) real coordinates each.

Two-factor matrix products are unambiguous, but multiplication is not associative: the coefficient algebra embeds in a diagonal corner, so its nonzero associators survive. No associative-algebra or ring view is assigned. Symmetrizing this product must not be assumed to give a [[nonassociative-algebra/jordan-algebra|Jordan algebra]].

## Size convention

For every size at least two, \(E_{11}E_{22}=0\) exhibits nonzero zero divisors. Matrix size is not the dimension of the whole algebra.
