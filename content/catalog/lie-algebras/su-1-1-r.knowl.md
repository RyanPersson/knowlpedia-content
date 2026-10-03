+++
id = "catalog/lie-algebras/su-1-1-r"
title = "su(1,1) — indefinite special unitary real Lie algebra"
kind = "definition"
summary = "su(1,1) — indefinite special unitary real Lie algebra."
aliases = ["su(1,1) — indefinite special unitary real Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **indefinite special unitary real [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{su}(1,1)\) is defined by

\[
\mathfrak{su}(1,1)=\{X\in M_{2}(\mathbb C):X^*\eta+\eta X=0,\ \operatorname{tr}X=0\},\qquad \eta=\operatorname{diag}(I_{1},-I_{1}).
\]


Its bracket is \([X,Y]=XY-YX\). The star is conjugate transpose.

## Signature, dimension and scalars

The signature convention is \(p\) positive and \(q\) negative directions. Negating the entire form leaves the matrix [[lie-groups/lie-algebra|Lie algebra]] unchanged, and exchanging the two coordinate blocks identifies signatures \((p,q)\) and \((q,p)\). The matrix \(\eta X\) is skew-Hermitian over \(\mathbb C\), giving \((p+q)^2\) real parameters. Its purely imaginary trace must also vanish, imposing one real equation.

The scalar field of this Lie algebra is \(\mathbb R\). Its complex matrix entries do not make its defining bracket space closed under complex scalar multiplication.

## References

1. [Barton and Sudbery, Magic squares and matrix models of Lie algebras](https://arxiv.org/pdf/math/0203010), §2, pp. 5–8, equations (2.19)–(2.27); quaternionic and indefinite matrix conventions.
