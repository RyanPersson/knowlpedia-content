+++
id = "catalog/algebras/herm-n-split-h"
title = "Herm_n(H_s) Jordan algebra"
kind = "definition"
summary = "Catalogue object: Herm_n(H_s) Jordan algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/split-quaternions", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For integers \(n\geq1\), The **Herm_n(H_s) Jordan algebra** is the \(\mathbb R\)-vector space
\[
\operatorname{Herm}_{n}(\mathbb H_s)=\{X\in M_{n}(\mathbb H_s):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{n}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[catalog/algebras/split-quaternions|the coefficient algebra]].

## Coordinates and dimension

There are \(n\) diagonal scalar coordinates and \(n(n-1)/2\) independent coefficient-algebra entries. Thus the dimension over \(\mathbb R\) is \(n+4n(n-1)/2\).

## Jordan identity and range

The fixed subspace is closed under \(X\circ Y\), because \((XY)^*=Y^*X^*\). Associativity of the ambient matrix algebra proves the Jordan identity, so the construction works in every positive size. The composition norm is indefinite. No Euclidean or formally real property is asserted from the word “Hermitian.”
