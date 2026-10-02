+++
id = "catalog/algebras/herm-n-r-complexified"
title = "Symmetric n-by-n complex Jordan algebra"
kind = "definition"
summary = "Catalogue object: Symmetric n-by-n complex Jordan algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/complex-numbers-c", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For integers \(n\geq1\), The **Symmetric n-by-n complex Jordan algebra** is the \(\mathbb C\)-vector space
\[
\operatorname{Herm}_{n}((\mathbb R\otimes_{\mathbb R}\mathbb C))=\{X\in M_{n}((\mathbb R\otimes_{\mathbb R}\mathbb C)):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{n}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[shared-foundations/complex-numbers-c|the coefficient algebra]]. That conjugation is extended complex-linearly, so it fixes the newly adjoined complex scalars.

## Coordinates and dimension

There are \(n\) diagonal scalar coordinates and \(n(n-1)/2\) independent coefficient-algebra entries. Thus the dimension over \(\mathbb C\) is \(n+1n(n-1)/2\). Here the coefficient involution is the identity, so the condition is \(X^T=X\), not \(\overline X^T=X\) with ordinary complex conjugation.

## Jordan identity and range

The fixed subspace is closed under \(X\circ Y\), because \((XY)^*=Y^*X^*\). Associativity of the ambient matrix algebra proves the Jordan identity, so the construction works in every positive size.

## Scalar convention

This is the complexification of the corresponding real Hermitian [[nonassociative-algebra/jordan-algebra|Jordan algebra]]. Its complex-bilinear product and real restriction give different category views; it is not the space of ordinary self-adjoint matrices on a complex Hilbert space.
