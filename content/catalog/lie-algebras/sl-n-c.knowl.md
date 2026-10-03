+++
id = "catalog/lie-algebras/sl-n-c"
title = "sl(n,C) — complex special linear Lie algebra"
kind = "definition"
summary = "sl(n,C) — complex special linear Lie algebra."
aliases = ["sl(n,C) — complex special linear Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "lie-groups/general-linear-lie-algebra"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **complex special linear [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{sl}(n,\mathbb C)\) is the trace-zero subspace of [[lie-groups/general-linear-lie-algebra|the general linear Lie algebra]], with bracket

\[
\mathfrak{sl}(n,\mathbb C)=\{X\in M_{n}(\mathbb C):\operatorname{tr}X=0\},\qquad [X,Y]=XY-YX.
\]

## Dimension and structure

Trace is one nonzero linear equation, so the complex dimension is \(n^2-1\). Closure follows from \(\operatorname{tr}(XY)=\operatorname{tr}(YX)\). The off-diagonal matrix units together with \(E_{jj}-E_{nn}\ (1\leq j<n)\) give a basis.

[[lie-groups/special-linear-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb C\) as its defining field. Its [[linear-algebra/realification-of-a-complex-vector-space|underlying real vector space]] has twice the complex dimension; real-linear maps need not be complex-linear.
