+++
id = "catalog/lie-algebras/gl-2-c"
title = "gl(2,C) — complex general linear Lie algebra"
kind = "definition"
summary = "gl(2,C) — complex general linear Lie algebra."
aliases = ["gl(2,C) — complex general linear Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **complex general linear [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{gl}(2,\mathbb C)\) is the complex [[linear-algebra/vector-space|vector space]] of all \(2\times2\) matrices over \(\mathbb C\), with commutator bracket.

\[
\mathfrak{gl}(2,\mathbb C)=M_{2}(\mathbb C),\qquad [X,Y]=XY-YX.
\]

## Dimension and structure

The matrix units \(E_{ij}\) form a basis, so its complex dimension is \(4\). The commutator of an associative matrix algebra satisfies the Jacobi identity by expansion.

Its center is the scalar matrices; the trace-zero subspace is an ideal because \(\operatorname{tr}[X,Y]=0\).

[[lie-groups/general-linear-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb C\) as its defining field. Its [[linear-algebra/realification-of-a-complex-vector-space|underlying real vector space]] has twice the complex dimension; real-linear maps need not be complex-linear.
