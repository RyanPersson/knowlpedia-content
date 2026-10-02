+++
id = "catalog/algebras/herm-3-split-o"
title = "Split real Albert algebra"
kind = "definition"
summary = "Catalogue object: Split real Albert algebra; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/split-octonions", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **Split real Albert algebra** is the \(\mathbb R\)-vector space
\[
\operatorname{Herm}_{3}(\mathbb O_s)=\{X\in M_{3}(\mathbb O_s):X^*=X\},
\qquad X\circ Y=\tfrac12(XY+YX),
\]
with unit \(I_{3}\). Here \(X^*=\overline X^T\), using the standard conjugation of [[catalog/algebras/split-octonions|the coefficient algebra]].

## Coordinates and dimension

The diagonal contributes \(3\) scalar coordinates, and the off-diagonal pairs contribute \(24\), giving dimension \(27\) over \(\mathbb R\).

## Jordan identity and range

Sizes one, two, and three satisfy the Jordan identity. The symbolic family in this catalogue is restricted to those sizes; ordinary Hermitian octonionic matrices in arbitrary size are not a uniform Jordan-algebra family. This degree-three algebra is exceptional: it is not a [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] of any symmetrized associative algebra. The composition norm is indefinite. No Euclidean or formally real property is asserted from the word “Hermitian.”

## References

1. [Holger P. Petersson, A survey on Albert algebras](https://www.fernuni-hagen.de/mi/fakultaet/emeriti/docs/petersson/alb.-alg.-tg.-survey.pdf), Sections 2.2, 2.5–2.7 and 7.8; printed pages 2–3 and 19.
