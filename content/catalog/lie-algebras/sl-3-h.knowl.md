+++
id = "catalog/lie-algebras/sl-3-h"
title = "sl(3,H) — quaternionic special linear Lie algebra"
kind = "definition"
summary = "sl(3,H) — quaternionic special linear Lie algebra."
aliases = ["sl(3,H) — quaternionic special linear Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **quaternionic special linear [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{sl}(3,\mathbb H)\) is the real [[linear-algebra/vector-space|vector space]]

\[
\mathfrak{sl}(3,\mathbb H)=\{X\in M_{3}(\mathbb H):\operatorname{Re}\operatorname{tr}X=0\},\qquad [X,Y]=XY-YX.
\]

## Trace and scalar conventions

Quaternionic matrix multiplication is associative, so its commutator is a real [[fiber-bundles/lie-bracket|Lie bracket]]. The **real part** of the trace is essential: the full quaternionic trace need not be cyclic, but its real part is. Thus the displayed subspace is closed under brackets and has real codimension one. Its conventional complex-matrix name is \(\mathfrak{su}^*(6)\).

Quaternionic entries do not make this a [[lie-groups/lie-algebra|Lie algebra]] over a commutative field \(\mathbb H\). All scalar-linear categories in this record are over \(\mathbb R\).

## References

1. [Barton and Sudbery, Magic squares and matrix models of Lie algebras](https://arxiv.org/pdf/math/0203010), §2, pp. 5–8, equations (2.19)–(2.27); quaternionic and indefinite matrix conventions.
