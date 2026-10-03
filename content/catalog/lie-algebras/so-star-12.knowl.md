+++
id = "catalog/lie-algebras/so-star-12"
title = "so*(12) — quaternionic orthogonal real form"
kind = "definition"
summary = "so*(12) — quaternionic orthogonal real form."
aliases = ["so*(12) — quaternionic orthogonal real form"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real Lie algebra** \(\mathfrak{so}^*(12)\) can be realized using quaternionic matrices as

\[
\{X\in M_6(\mathbb H):X^*J+JX=0\},\qquad J=\begin{pmatrix}0&I_3\\-I_3&0\end{pmatrix},\qquad [X,Y]=XY-YX.
\]


Conjugate transpose uses quaternionic conjugation, and the scalar field of this [[lie-groups/lie-algebra|Lie algebra]] is \(\mathbb R\).

## Block count and naming

Writing \(X=\begin{pmatrix}A&B\\C&D\end{pmatrix}\) gives \(D=-A^*,\ B=B^*,\ C=C^*\). The block \(A\) contributes 36 real parameters; each Hermitian quaternionic 3-by-3 block contributes 15. Hence the dimension is \(36+15+15=66\). The real part of the trace vanishes automatically. The complexification is \(\mathfrak{so}(12,\mathbb C)\).

## References

1. [Barton and Sudbery, Magic squares and matrix models of Lie algebras](https://arxiv.org/pdf/math/0203010), §2, pp. 5–8, equations (2.19)–(2.27); quaternionic and indefinite matrix conventions.
