+++
id = "catalog/algebras/split-complex-hermitian-isomorphism"
title = "Split-complex Hermitian matrices as full-matrix Jordan algebras"
kind = "theorem"
summary = "Split-complex Hermitian matrices as full-matrix Jordan algebras."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/split-complex-numbers", "catalog/algebras/c-complexified", "nonassociative-algebra/jordan-algebra-homomorphism"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For \(F=\mathbb R\) or \(\mathbb C\), equip \(D=F\times F\) with conjugation \(\overline{(a,b)}=(b,a)\). Projection onto the first matrix component defines a unital Jordan isomorphism
\[
\operatorname{Herm}_n(D)\ \cong\ M_n(F)^+,
\qquad (X,X^T)\longmapsto X,
\]
for every integer \(n\geq1\). On the right, the product is \(X\circ Y=(XY+YX)/2\).

## Verification

The equation \((X,Y)^*=(X,Y)\) is exactly \(Y=X^T\). Thus the inverse map is \(X\mapsto(X,X^T)\). Symmetrization of the product in the second component gives \((XY+YX)^T/2\), so projection preserves the Jordan product and the unit.

## Catalogue instances

Over \(\mathbb R\), the coefficient algebra is [[catalog/algebras/split-complex-numbers|\(\mathbb C_s\)]]. Over \(\mathbb C\), it is [[catalog/algebras/c-complexified|\(\mathbb C\otimes_{\mathbb R}\mathbb C\)]], whose composition conjugation exchanges the two factors. Consequently the complexification of the ordinary real [[nonassociative-algebra/jordan-algebra|Jordan algebra]] \(\operatorname{Herm}_n(\mathbb C)\) is \(M_n(\mathbb C)^+\). It is not the ordinary conjugate-self-adjoint subspace over \(\mathbb C\).
