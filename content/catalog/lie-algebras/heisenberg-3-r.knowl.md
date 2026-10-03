+++
id = "catalog/lie-algebras/heisenberg-3-r"
title = "Heisenberg Lie algebra h7(R)"
kind = "definition"
summary = "Heisenberg Lie algebra h7(R)."
aliases = ["Heisenberg Lie algebra h7(R)"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real Heisenberg [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak h_{7}(\mathbb R)\) is the [[linear-algebra/vector-space|vector space]] with basis \(x_1,\ldots,x_{3},y_1,\ldots,y_{3},z\) and bilinear alternating bracket determined by

\[
[x_i,y_j]=\delta_{ij}z,\qquad [x_i,x_j]=[y_i,y_j]=[z,x_i]=[z,y_i]=0.
\]

## Center and matrix model

Its center and derived algebra are both the line \(\mathbb Rz\). Every nested bracket of length three is zero, so Jacobi is immediate and the algebra is nilpotent of class two. The quotient by its center is abelian of dimension \(6\).

A faithful matrix model sends \(x_i\mapsto E_{1,i+1},\ y_i\mapsto E_{i+1,3+2},\ z\mapsto E_{1,3+2}\) in matrices of size \(3+2\). The subscript records dimension, whereas the catalogue parameter \(n\) counts pairs of generators.
