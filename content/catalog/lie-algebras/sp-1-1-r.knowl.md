+++
id = "catalog/lie-algebras/sp-1-1-r"
title = "sp(1,1) — indefinite quaternionic symplectic real Lie algebra"
kind = "definition"
summary = "sp(1,1) — indefinite quaternionic symplectic real Lie algebra."
aliases = ["sp(1,1) — indefinite quaternionic symplectic real Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **indefinite quaternionic symplectic real [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{sp}(1,1)\) is defined by

\[
\mathfrak{sp}(1,1)=\{X\in M_{2}(\mathbb H):X^*\eta+\eta X=0\},\qquad \eta=\operatorname{diag}(I_{1},-I_{1}).
\]


Its bracket is \([X,Y]=XY-YX\). The star is conjugate transpose using quaternionic conjugation.

## Signature, dimension and scalars

The signature convention is \(p\) positive and \(q\) negative directions. Negating the entire form leaves the matrix [[lie-groups/lie-algebra|Lie algebra]] unchanged, and exchanging the two coordinate blocks identifies signatures \((p,q)\) and \((q,p)\). The matrix \(\eta X\) is skew-Hermitian over the quaternions. Counting three real coordinates on each diagonal entry and four on each off-diagonal pair gives \((p+q)(2(p+q)+1)\) real dimensions. The parameters count quaternionic coordinates, not complex coordinates.

The scalar field of this Lie algebra is \(\mathbb R\).

## References

1. [Barton and Sudbery, Magic squares and matrix models of Lie algebras](https://arxiv.org/pdf/math/0203010), §2, pp. 5–8, equations (2.19)–(2.27); quaternionic and indefinite matrix conventions.
