+++
id = "catalog/algebras/herm-2-split-c"
title = "Herm_2(C_s) Jordan algebra"
kind = "definition"
summary = "Catalogue object: Herm_2(C_s) Jordan algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/split-complex-numbers", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **Herm_2(C_s) Jordan algebra** is the \(\mathbb R\)-vector space
\[
\operatorname{Herm}_{2}(\mathbb C_s)=\{X\in M_{2}(\mathbb C_s):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{2}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[catalog/algebras/split-complex-numbers|the coefficient algebra]].

## Coordinates and dimension

The diagonal contributes \(2\) scalar coordinates, and the off-diagonal pairs contribute \(2\), giving dimension \(4\) over \(\mathbb R\).

## Jordan identity and range

The fixed subspace is closed under \(X\circ Y\), because \((XY)^*=Y^*X^*\). Associativity of the ambient matrix algebra proves the Jordan identity, so the construction works in every positive size. The composition norm is indefinite. No Euclidean or formally real property is asserted from the word “Hermitian.”
