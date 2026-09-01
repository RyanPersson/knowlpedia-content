+++
id = "nonassociative-algebra/octonionic-spin-factor"
title = "Octonionic spin factor"
kind = "definition"
summary = "The ten-dimensional Euclidean Jordan algebra of two-by-two Hermitian octonionic matrices."
aliases = ["octonionic spin factor", "h_2(O)", "octonionic qubit"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/jordan-algebra", "nonassociative-algebra/euclidean-jordan-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

The **octonionic spin factor** is the ten-dimensional real [[nonassociative-algebra/jordan-algebra|Jordan algebra]]
\[
\mathfrak h_2(\mathbb O)
=\left\{
\begin{pmatrix}\alpha&z\\ \bar z&\beta\end{pmatrix}
:\alpha,\beta\in\mathbb R,\ z\in\mathbb O
\right\},
\qquad X\circ Y=\frac12(XY+YX).
\]
It is a [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan
algebra]] despite the nonassociativity of the octonions.

## Spin-factor identification

Set \(\lambda=(\alpha+\beta)/2\) and
\[
u=((\alpha-\beta)/2,z)\in\mathbb R\oplus\mathbb O\cong\mathbb R^9.
\]
The matrix corresponds to \((\lambda,u)\), and its Jordan product becomes the
spin-factor product. Consequently
\[
\mathfrak h_2(\mathbb O)\cong J(\mathbb R^9).
\]
It is simple, has rank \(2\), dimension \(10\), and abstract automorphism group
\(O(9)\).

## Embedding in the exceptional algebra

The upper-left corner gives a Jordan embedding
\[
\mathfrak h_2(\mathbb O)\hookrightarrow\mathfrak h_3(\mathbb O),
\qquad
X\longmapsto
\begin{pmatrix}X&0\\0&0\end{pmatrix}.
\]
It is not unital: the source unit becomes
\(\operatorname{diag}(1,1,0)\), a proper idempotent of the [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]].

The setwise stabilizer of this corner inside
\(\operatorname{Aut}(\mathfrak h_3(\mathbb O))\cong F_4\) is
\(\operatorname{Spin}(9)\). This ambient stabilizer is not the abstract
automorphism group \(O(9)\) of the [[nonassociative-algebra/spin-factor-jordan-algebra|spin factor]]: its action on the whole
27-dimensional Albert algebra contains additional information.

## Degree caveat

Alternativity is enough for the degree-two product to satisfy the Jordan
identity. Degree three also works and gives the Albert algebra, but the same
Hermitian-matrix construction fails to be Jordan in degrees at least four.

## References

1. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-12622-6).
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
