+++
id = "catalog/algebras/herm-n-o-complexified"
title = "Herm_n(O) complexification"
kind = "definition"
summary = "Catalogue object: Herm_n(O) complexification; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/o-complexified", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For integers \(1\leq n\leq3\), The **Herm_n(O) complexification** is the \(\mathbb C\)-vector space
\[
\operatorname{Herm}_{n}((\mathbb O\otimes_{\mathbb R}\mathbb C))=\{X\in M_{n}((\mathbb O\otimes_{\mathbb R}\mathbb C)):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{n}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[catalog/algebras/o-complexified|the coefficient algebra]]. That conjugation is extended complex-linearly, so it fixes the newly adjoined complex scalars.

## Coordinates and dimension

There are \(n\) diagonal scalar coordinates and \(n(n-1)/2\) independent coefficient-algebra entries. Thus the dimension over \(\mathbb C\) is \(n+8n(n-1)/2\).

## Jordan identity and range

Sizes one, two, and three satisfy the Jordan identity. The symbolic family in this catalogue is restricted to those sizes; ordinary Hermitian octonionic matrices in arbitrary size are not a uniform Jordan-algebra family.

## Scalar convention

This is the complexification of the corresponding real Hermitian [[nonassociative-algebra/jordan-algebra|Jordan algebra]]. Its complex-bilinear product and real restriction give different category views; it is not the space of ordinary self-adjoint matrices on a complex Hilbert space.

## References

1. [Holger P. Petersson, A survey on Albert algebras](https://www.fernuni-hagen.de/mi/fakultaet/emeriti/docs/petersson/alb.-alg.-tg.-survey.pdf), Sections 2.2, 2.5–2.7 and 7.8; printed pages 2–3 and 19.
