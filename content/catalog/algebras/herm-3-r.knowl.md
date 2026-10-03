+++
id = "catalog/algebras/herm-3-r"
title = "Herm_3(R) Jordan algebra"
kind = "definition"
summary = "Catalogue object: Herm_3(R) Jordan algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/real-numbers", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **Herm_3(R) Jordan algebra** is the \(\mathbb R\)-vector space
\[
\operatorname{Herm}_{3}(\mathbb R)=\{X\in M_{3}(\mathbb R):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{3}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[shared-foundations/real-numbers|the coefficient algebra]].

## Coordinates and dimension

The diagonal contributes \(3\) scalar coordinates, and the off-diagonal pairs contribute \(3\), giving dimension \(6\) over \(\mathbb R\).

## Jordan identity and range

The fixed subspace is closed under \(X\circ Y\), because \((XY)^*=Y^*X^*\). Associativity of the ambient matrix algebra proves the Jordan identity, so the construction works in every positive size.
