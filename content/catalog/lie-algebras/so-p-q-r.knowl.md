+++
id = "catalog/lie-algebras/so-p-q-r"
title = "so(p,q) — indefinite orthogonal real Lie algebra"
kind = "definition"
summary = "so(p,q) — indefinite orthogonal real Lie algebra."
aliases = ["so(p,q) — indefinite orthogonal real Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For nonnegative integers \(p,q\) with \(p+q\geq1\), the **indefinite orthogonal real [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{so}(p,q)\) is defined by

\[
\mathfrak{so}(p,q)=\{X\in M_{p+q}(\mathbb R):X^T\eta+\eta X=0\},\qquad \eta=\operatorname{diag}(I_{p},-I_{q}).
\]


Its bracket is \([X,Y]=XY-YX\). The transpose is real transpose.

## Signature, dimension and scalars

The signature convention is \(p\) positive and \(q\) negative directions. Negating the entire form leaves the matrix [[lie-groups/lie-algebra|Lie algebra]] unchanged, and exchanging the two coordinate blocks identifies signatures \((p,q)\) and \((q,p)\). The matrix \(\eta X\) is skew-symmetric, so counting entries above its diagonal gives the real dimension.

The scalar field of this Lie algebra is \(\mathbb R\).

## References

1. [Barton and Sudbery, Magic squares and matrix models of Lie algebras](https://arxiv.org/pdf/math/0203010), §2, pp. 5–8, equations (2.19)–(2.27); quaternionic and indefinite matrix conventions.
