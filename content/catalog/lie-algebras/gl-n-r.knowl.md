+++
id = "catalog/lie-algebras/gl-n-r"
title = "gl(n,R) — real general linear Lie algebra"
kind = "definition"
summary = "gl(n,R) — real general linear Lie algebra."
aliases = ["gl(n,R) — real general linear Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **real general linear [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{gl}(n,\mathbb R)\) is the real [[linear-algebra/vector-space|vector space]] of all \(n\times n\) matrices over \(\mathbb R\), with commutator bracket.

\[
\mathfrak{gl}(n,\mathbb R)=M_{n}(\mathbb R),\qquad [X,Y]=XY-YX.
\]

## Dimension and structure

The matrix units \(E_{ij}\) form a basis, so its real dimension is \(n^2\). The commutator of an associative matrix algebra satisfies the Jacobi identity by expansion.

Its center is the scalar matrices; the trace-zero subspace is an ideal because \(\operatorname{tr}[X,Y]=0\).

[[lie-groups/general-linear-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb R\) as its defining field. Its complexification is a different catalogue object; a matrix presentation over complex numbers does not change this field automatically.
