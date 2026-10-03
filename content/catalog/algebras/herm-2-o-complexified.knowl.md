+++
id = "catalog/algebras/herm-2-o-complexified"
title = "Herm_2(O) complexification"
kind = "definition"
summary = "Catalogue object: Herm_2(O) complexification; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/o-complexified", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **Herm_2(O) complexification** is the \(\mathbb C\)-vector space
\[
\operatorname{Herm}_{2}((\mathbb O\otimes_{\mathbb R}\mathbb C))=\{X\in M_{2}((\mathbb O\otimes_{\mathbb R}\mathbb C)):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{2}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[catalog/algebras/o-complexified|the coefficient algebra]]. That conjugation is extended complex-linearly, so it fixes the newly adjoined complex scalars.

## Coordinates and dimension

The diagonal contributes \(2\) scalar coordinates, and the off-diagonal pairs contribute \(8\), giving dimension \(10\) over \(\mathbb C\).

## Jordan identity and range

Sizes one, two, and three satisfy the Jordan identity. The symbolic family in this catalogue is restricted to those sizes; ordinary Hermitian octonionic matrices in arbitrary size are not a uniform Jordan-algebra family.

## Scalar convention

This is the complexification of the corresponding real Hermitian [[nonassociative-algebra/jordan-algebra|Jordan algebra]]. Its complex-bilinear product and real restriction give different category views; it is not the space of ordinary self-adjoint matrices on a complex Hilbert space.

## References

1. [Holger P. Petersson, A survey on Albert algebras](https://www.fernuni-hagen.de/mi/fakultaet/emeriti/docs/petersson/alb.-alg.-tg.-survey.pdf), Sections 2.2, 2.5–2.7 and 7.8; printed pages 2–3 and 19.
