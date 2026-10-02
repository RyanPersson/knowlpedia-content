+++
id = "catalog/lie-algebras/so-1-c"
title = "so(1,C) — complex orthogonal Lie algebra"
kind = "definition"
summary = "so(1,C) — complex orthogonal Lie algebra."
aliases = ["so(1,C) — complex orthogonal Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **complex orthogonal [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{so}(1,\mathbb C)\) consists of skew-symmetric \(1\times1\) matrices, with commutator bracket:

\[
\mathfrak{so}(1,\mathbb C)=\{X\in M_{1}(\mathbb C):X^T+X=0\},\qquad [X,Y]=XY-YX.
\]


The transpose has no complex conjugation: the preserved form is complex bilinear, not Hermitian.

## Dimension and structure

The independent entries above the diagonal give complex dimension \(0\); a basis is \(E_{ij}-E_{ji}\ (1\leq i<j\leq 1)\). There are no such pairs, so the algebra is zero.

[[lie-groups/orthogonal-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb C\) as its defining field. Its [[linear-algebra/realification-of-a-complex-vector-space|underlying real vector space]] has twice the complex dimension; real-linear maps need not be complex-linear.
