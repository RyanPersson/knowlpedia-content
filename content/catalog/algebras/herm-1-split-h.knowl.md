+++
id = "catalog/algebras/herm-1-split-h"
title = "Herm_1(H_s) Jordan algebra"
kind = "definition"
summary = "Catalogue object: Herm_1(H_s) Jordan algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/split-quaternions", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **Herm_1(H_s) Jordan algebra** is the \(\mathbb R\)-vector space
\[
\operatorname{Herm}_{1}(\mathbb H_s)=\{X\in M_{1}(\mathbb H_s):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{1}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[catalog/algebras/split-quaternions|the coefficient algebra]].

## Coordinates and dimension

The diagonal contributes \(1\) scalar coordinates, and the off-diagonal pairs contribute \(0\), giving dimension \(1\) over \(\mathbb R\).

## Jordan identity and range

The fixed subspace is closed under \(X\circ Y\), because \((XY)^*=Y^*X^*\). Associativity of the ambient matrix algebra proves the Jordan identity, so the construction works in every positive size. Conjugation-fixed coefficients are exactly \(\mathbb R1\), so \([a]\mapsto a\) identifies this one-dimensional [[nonassociative-algebra/jordan-algebra|Jordan algebra]] with \(\mathbb R\).
