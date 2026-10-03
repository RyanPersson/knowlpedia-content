+++
id = "catalog/lie-algebras/u-p-q-r"
title = "u(p,q) — indefinite unitary real Lie algebra"
kind = "definition"
summary = "u(p,q) — indefinite unitary real Lie algebra."
aliases = ["u(p,q) — indefinite unitary real Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For nonnegative integers \(p,q\) with \(p+q\geq1\), the **indefinite unitary real [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{u}(p,q)\) is defined by

\[
\mathfrak{u}(p,q)=\{X\in M_{p+q}(\mathbb C):X^*\eta+\eta X=0\},\qquad \eta=\operatorname{diag}(I_{p},-I_{q}).
\]


Its bracket is \([X,Y]=XY-YX\). The star is conjugate transpose.

## Signature, dimension and scalars

The signature convention is \(p\) positive and \(q\) negative directions. Negating the entire form leaves the matrix [[lie-groups/lie-algebra|Lie algebra]] unchanged, and exchanging the two coordinate blocks identifies signatures \((p,q)\) and \((q,p)\). The matrix \(\eta X\) is skew-Hermitian over \(\mathbb C\), giving \((p+q)^2\) real parameters.

The scalar field of this Lie algebra is \(\mathbb R\). Its complex matrix entries do not make its defining bracket space closed under complex scalar multiplication.

## References

1. [Barton and Sudbery, Magic squares and matrix models of Lie algebras](https://arxiv.org/pdf/math/0203010), §2, pp. 5–8, equations (2.19)–(2.27); quaternionic and indefinite matrix conventions.
