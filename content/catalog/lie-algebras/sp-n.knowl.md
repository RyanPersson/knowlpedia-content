+++
id = "catalog/lie-algebras/sp-n"
title = "sp(n) — compact symplectic Lie algebra"
kind = "definition"
summary = "sp(n) — compact symplectic Lie algebra."
aliases = ["sp(n) — compact symplectic Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **compact symplectic [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{sp}(n)\) is the real [[linear-algebra/vector-space|vector space]]

\[
\mathfrak{sp}(n)=\{X\in M_{n}(\mathbb H):X^*+X=0\}.
\]

with commutator bracket \([X,Y]=XY-YX\). Here \(X^*\) means conjugate transpose using quaternionic conjugation.

## Dimension and scalar field

Each diagonal entry is an imaginary quaternion with three real coordinates; each pair of off-diagonal entries contributes four. The real dimension is \(3n+4\frac{n(n-1)}2=n(2n+1)\). The size parameter counts quaternionic rows, not complex rows.

This object is a **real** [[lie-groups/lie-algebra|Lie algebra]]. Multiplication by \(i\) does not generally preserve the defining skew-adjoint condition; there is no inherited complex-linear category membership.

## References

1. [Barton and Sudbery, Magic squares and matrix models of Lie algebras](https://arxiv.org/pdf/math/0203010), §2, pp. 5–8, equations (2.19)–(2.27); quaternionic and indefinite matrix conventions.
