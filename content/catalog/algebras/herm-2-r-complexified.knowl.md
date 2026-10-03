+++
id = "catalog/algebras/herm-2-r-complexified"
title = "Symmetric 2-by-2 complex Jordan algebra"
kind = "definition"
summary = "Catalogue object: Symmetric 2-by-2 complex Jordan algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/complex-numbers-c", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **Symmetric 2-by-2 complex Jordan algebra** is the \(\mathbb C\)-vector space
\[
\operatorname{Herm}_{2}((\mathbb R\otimes_{\mathbb R}\mathbb C))=\{X\in M_{2}((\mathbb R\otimes_{\mathbb R}\mathbb C)):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{2}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[shared-foundations/complex-numbers-c|the coefficient algebra]]. That conjugation is extended complex-linearly, so it fixes the newly adjoined complex scalars.

## Coordinates and dimension

The diagonal contributes \(2\) scalar coordinates, and the off-diagonal pairs contribute \(1\), giving dimension \(3\) over \(\mathbb C\). Here the coefficient involution is the identity, so the condition is \(X^T=X\), not \(\overline X^T=X\) with ordinary complex conjugation.

## Jordan identity and range

The fixed subspace is closed under \(X\circ Y\), because \((XY)^*=Y^*X^*\). Associativity of the ambient matrix algebra proves the Jordan identity, so the construction works in every positive size.

## Scalar convention

This is the complexification of the corresponding real Hermitian [[nonassociative-algebra/jordan-algebra|Jordan algebra]]. Its complex-bilinear product and real restriction give different category views; it is not the space of ordinary self-adjoint matrices on a complex Hilbert space.
