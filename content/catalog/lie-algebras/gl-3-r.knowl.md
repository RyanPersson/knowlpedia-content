+++
id = "catalog/lie-algebras/gl-3-r"
title = "gl(3,R) — real general linear Lie algebra"
kind = "definition"
summary = "gl(3,R) — real general linear Lie algebra."
aliases = ["gl(3,R) — real general linear Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real general linear [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{gl}(3,\mathbb R)\) is the real [[linear-algebra/vector-space|vector space]] of all \(3\times3\) matrices over \(\mathbb R\), with commutator bracket.

\[
\mathfrak{gl}(3,\mathbb R)=M_{3}(\mathbb R),\qquad [X,Y]=XY-YX.
\]

## Dimension and structure

The matrix units \(E_{ij}\) form a basis, so its real dimension is \(9\). The commutator of an associative matrix algebra satisfies the Jacobi identity by expansion.

Its center is the scalar matrices; the trace-zero subspace is an ideal because \(\operatorname{tr}[X,Y]=0\).

[[lie-groups/general-linear-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb R\) as its defining field. Its complexification is a different catalogue object; a matrix presentation over complex numbers does not change this field automatically.
