+++
id = "catalog/algebras/herm-2-c-complexified"
title = "Herm_2(C) complexification"
kind = "definition"
summary = "Catalogue object: Herm_2(C) complexification; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/c-complexified", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **Herm_2(C) complexification** is the \(\mathbb C\)-vector space
\[
\operatorname{Herm}_{2}((\mathbb C\otimes_{\mathbb R}\mathbb C))=\{X\in M_{2}((\mathbb C\otimes_{\mathbb R}\mathbb C)):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{2}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[catalog/algebras/c-complexified|the coefficient algebra]]. That conjugation is extended complex-linearly, so it fixes the newly adjoined complex scalars.

## Coordinates and dimension

The diagonal contributes \(2\) scalar coordinates, and the off-diagonal pairs contribute \(2\), giving dimension \(4\) over \(\mathbb C\).

## Jordan identity and range

The fixed subspace is closed under \(X\circ Y\), because \((XY)^*=Y^*X^*\). Associativity of the ambient matrix algebra proves the Jordan identity, so the construction works in every positive size.

## Scalar convention

This is the complexification of the corresponding real Hermitian [[nonassociative-algebra/jordan-algebra|Jordan algebra]]. Its complex-bilinear product and real restriction give different category views; it is not the space of ordinary self-adjoint matrices on a complex Hilbert space.
