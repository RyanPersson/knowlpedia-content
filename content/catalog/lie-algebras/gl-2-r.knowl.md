+++
id = "catalog/lie-algebras/gl-2-r"
title = "gl(2,R) — real general linear Lie algebra"
kind = "definition"
summary = "gl(2,R) — real general linear Lie algebra."
aliases = ["gl(2,R) — real general linear Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real general linear [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{gl}(2,\mathbb R)\) is the real [[linear-algebra/vector-space|vector space]] of all \(2\times2\) matrices over \(\mathbb R\), with commutator bracket.

\[
\mathfrak{gl}(2,\mathbb R)=M_{2}(\mathbb R),\qquad [X,Y]=XY-YX.
\]

## Dimension and structure

The matrix units \(E_{ij}\) form a basis, so its real dimension is \(4\). The commutator of an associative matrix algebra satisfies the Jacobi identity by expansion.

Its center is the scalar matrices; the trace-zero subspace is an ideal because \(\operatorname{tr}[X,Y]=0\).

[[lie-groups/general-linear-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb R\) as its defining field. Its complexification is a different catalogue object; a matrix presentation over complex numbers does not change this field automatically.
