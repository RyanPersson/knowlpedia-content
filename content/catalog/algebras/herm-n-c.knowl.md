+++
id = "catalog/algebras/herm-n-c"
title = "Herm_n(C) Jordan algebra"
kind = "definition"
summary = "Catalogue object: Herm_n(C) Jordan algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/complex-numbers-c", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For integers \(n\geq1\), The **Herm_n(C) Jordan algebra** is the \(\mathbb R\)-vector space
\[
\operatorname{Herm}_{n}(\mathbb C)=\{X\in M_{n}(\mathbb C):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{n}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[shared-foundations/complex-numbers-c|the coefficient algebra]].

## Coordinates and dimension

There are \(n\) diagonal scalar coordinates and \(n(n-1)/2\) independent coefficient-algebra entries. Thus the dimension over \(\mathbb R\) is \(n+2n(n-1)/2\). In particular, the usual Hermitian complex matrices form a real [[linear-algebra/vector-space|vector space]]; multiplication by \(i\) does not preserve self-adjointness.

## Jordan identity and range

The fixed subspace is closed under \(X\circ Y\), because \((XY)^*=Y^*X^*\). Associativity of the ambient matrix algebra proves the Jordan identity, so the construction works in every positive size.
