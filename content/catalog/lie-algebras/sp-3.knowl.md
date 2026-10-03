+++
id = "catalog/lie-algebras/sp-3"
title = "sp(3) — compact symplectic Lie algebra"
kind = "definition"
summary = "sp(3) — compact symplectic Lie algebra."
aliases = ["sp(3) — compact symplectic Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **compact symplectic [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{sp}(3)\) is the real [[linear-algebra/vector-space|vector space]]

\[
\mathfrak{sp}(3)=\{X\in M_{3}(\mathbb H):X^*+X=0\}.
\]

with commutator bracket \([X,Y]=XY-YX\). Here \(X^*\) means conjugate transpose using quaternionic conjugation.

## Dimension and scalar field

Each diagonal entry is an imaginary quaternion with three real coordinates; each pair of off-diagonal entries contributes four. The real dimension is \(21\). The size parameter counts quaternionic rows, not complex rows.

This object is a **real** [[lie-groups/lie-algebra|Lie algebra]]. Multiplication by \(i\) does not generally preserve the defining skew-adjoint condition; there is no inherited complex-linear category membership.

## References

1. [Barton and Sudbery, Magic squares and matrix models of Lie algebras](https://arxiv.org/pdf/math/0203010), §2, pp. 5–8, equations (2.19)–(2.27); quaternionic and indefinite matrix conventions.
