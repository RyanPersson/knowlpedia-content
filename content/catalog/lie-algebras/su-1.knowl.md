+++
id = "catalog/lie-algebras/su-1"
title = "su(1) — compact special unitary Lie algebra"
kind = "definition"
summary = "su(1) — compact special unitary Lie algebra."
aliases = ["su(1) — compact special unitary Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **special unitary [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{su}(1)\) is the real [[linear-algebra/vector-space|vector space]]

\[
\mathfrak{su}(1)=\{X\in M_{1}(\mathbb C):X^*+X=0,\ \operatorname{tr}X=0\}.
\]

with commutator bracket \([X,Y]=XY-YX\). Here \(X^*\) means conjugate transpose.

## Dimension and scalar field

A skew-Hermitian diagonal has one real parameter per entry, while each off-diagonal pair has two. The trace-zero condition removes one real parameter. Consequently the real dimension is \(0\). The algebra is zero.

This object is a **real** [[lie-groups/lie-algebra|Lie algebra]]. Multiplication by \(i\) does not generally preserve the defining skew-adjoint condition; there is no inherited complex-linear category membership.
