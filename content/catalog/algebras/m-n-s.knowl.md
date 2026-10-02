+++
id = "catalog/algebras/m-n-s"
title = "M_n(S) matrix algebra"
kind = "definition"
summary = "Catalogue object: M_n(S) matrix algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/sedenions", "linear-algebra/matrix"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For each integer \(n\geq1\), **\(M_{n}(\mathbb S)\)** consists of \(n\)-by-\(n\) matrices with entries in [[catalog/algebras/sedenions|S]], with entrywise addition and scalar multiplication and product
\[
(XY)_{ij}=\sum_{r=1}^{n}X_{ir}Y_{rj}.
\]
Its unit is \(I_{n}\). The scalar field for this catalogue object is \(\mathbb R\).

## Dimension and multiplication

Each of the \(n^2\) entries contributes \(16\) real coordinates, so the real dimension is \(16n^2\).

Two-factor matrix products are unambiguous, but multiplication is not associative: the coefficient algebra embeds in a diagonal corner, so its nonzero associators survive. No associative-algebra or ring view is assigned. Symmetrizing this product must not be assumed to give a [[nonassociative-algebra/jordan-algebra|Jordan algebra]].

## Size convention

The entries for sizes one, two, and three are separate catalogue objects; this record is the parameterized family. Matrix size is not the dimension of the algebra.
