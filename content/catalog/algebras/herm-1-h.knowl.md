+++
id = "catalog/algebras/herm-1-h"
title = "Herm_1(H) Jordan algebra"
kind = "definition"
summary = "Catalogue object: Herm_1(H) Jordan algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quaternion-division-algebra", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **Herm_1(H) Jordan algebra** is the \(\mathbb R\)-vector space
\[
\operatorname{Herm}_{1}(\mathbb H)=\{X\in M_{1}(\mathbb H):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{1}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[linear-algebra/quaternion-division-algebra|the coefficient algebra]].

## Coordinates and dimension

The diagonal contributes \(1\) scalar coordinates, and the off-diagonal pairs contribute \(0\), giving dimension \(1\) over \(\mathbb R\).

## Jordan identity and range

The fixed subspace is closed under \(X\circ Y\), because \((XY)^*=Y^*X^*\). Associativity of the ambient matrix algebra proves the Jordan identity, so the construction works in every positive size. Conjugation-fixed coefficients are exactly \(\mathbb R1\), so \([a]\mapsto a\) identifies this one-dimensional [[nonassociative-algebra/jordan-algebra|Jordan algebra]] with \(\mathbb R\).
