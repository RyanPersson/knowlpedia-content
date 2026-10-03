+++
id = "catalog/lie-algebras/so-1-r"
title = "so(1,R) — real orthogonal Lie algebra"
kind = "definition"
summary = "so(1,R) — real orthogonal Lie algebra."
aliases = ["so(1,R) — real orthogonal Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real orthogonal [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{so}(1,\mathbb R)\) consists of skew-symmetric \(1\times1\) matrices, with commutator bracket:

\[
\mathfrak{so}(1,\mathbb R)=\{X\in M_{1}(\mathbb R):X^T+X=0\},\qquad [X,Y]=XY-YX.
\]


The form preserved here is the positive-definite real form \(x_1^2+\cdots+x_1^2\).

## Dimension and structure

The independent entries above the diagonal give real dimension \(0\); a basis is \(E_{ij}-E_{ji}\ (1\leq i<j\leq 1)\). There are no such pairs, so the algebra is zero.

[[lie-groups/orthogonal-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb R\) as its defining field. Its complexification is a different catalogue object; a matrix presentation over complex numbers does not change this field automatically.
