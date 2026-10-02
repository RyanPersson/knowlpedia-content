+++
id = "catalog/lie-algebras/heisenberg-n-r"
title = "Heisenberg Lie algebra h2n+1(R)"
kind = "definition"
summary = "Heisenberg Lie algebra h2n+1(R)."
aliases = ["Heisenberg Lie algebra h2n+1(R)"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **real Heisenberg [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak h_{2n+1}(\mathbb R)\) is the [[linear-algebra/vector-space|vector space]] with basis \(x_1,\ldots,x_{n},y_1,\ldots,y_{n},z\) and bilinear alternating bracket determined by

\[
[x_i,y_j]=\delta_{ij}z,\qquad [x_i,x_j]=[y_i,y_j]=[z,x_i]=[z,y_i]=0.
\]

## Center and matrix model

Its center and derived algebra are both the line \(\mathbb Rz\). Every nested bracket of length three is zero, so Jacobi is immediate and the algebra is nilpotent of class two. The quotient by its center is abelian of dimension \(2n\).

A faithful matrix model sends \(x_i\mapsto E_{1,i+1},\ y_i\mapsto E_{i+1,n+2},\ z\mapsto E_{1,n+2}\) in matrices of size \(n+2\). The subscript records dimension, whereas the catalogue parameter \(n\) counts pairs of generators.
