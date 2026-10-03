+++
id = "catalog/relationships/hermitian-cubic-derivation-algebras"
title = "Derivation algebras of cubic Hermitian Jordan algebras"
kind = "theorem"
summary = "The first compact magic-square row records the derivations of H3 over the division algebras."
aliases = ["Derivation algebras of cubic Hermitian Jordan algebras"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/derivation-of-a-jordan-algebra"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

For \(A=\mathbb R,\mathbb C,\mathbb H,\mathbb O\), give \(H_3(A)\) the real Jordan product \(X\circ Y=(XY+YX)/2\). Its [[nonassociative-algebra/derivation-of-a-jordan-algebra|derivation Lie algebra]] is respectively
\[
\begin{array}{c|cccc}
 A&\mathbb R&\mathbb C&\mathbb H&\mathbb O\\\hline
 \operatorname{Der}_{\mathbb R}(H_3(A))&
 \mathfrak{so}(3)&\mathfrak{su}(3)&\mathfrak{sp}(3)&\mathfrak f_{4,\mathrm{compact}}
\end{array}
\]
The dimensions are \(3,8,21,52\). These are compact real Lie algebras; \(\mathfrak{sp}(3)\) here uses quaternionic matrix size three.

## Why this is the first row

The [[catalog/relationships/tits-magic-square-decomposition|Tits decomposition]] gives \(\mathfrak M(\mathbb R,A)=\operatorname{Der}(H_3(A))\). Thus Jordan products determine the first row of the [[catalog/relationships/compact-freudenthal-magic-square|compact square]].

## Derivations and automorphisms

Derivations are infinitesimal automorphisms, with commutator bracket. They are not arbitrary Jordan endomorphisms: a derivation obeys a Leibniz rule, while a [[nonassociative-algebra/jordan-algebra-homomorphism|Jordan homomorphism]] preserves the product itself.

## References

1. C. H. Barton and A. Sudbery, “Magic squares and matrix models of Lie algebras,” §2, equations (2.19)–(2.23); §3 compact square; §5 Theorem 5.1(a). [Paper](https://arxiv.org/pdf/math/0203010).
2. John C. Baez, “The Octonions,” §4.2, Theorem 5. [Checked section](https://math.ucr.edu/home/baez/octonions/node15.html).
