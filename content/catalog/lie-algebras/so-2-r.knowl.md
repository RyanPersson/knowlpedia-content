+++
id = "catalog/lie-algebras/so-2-r"
title = "so(2,R) — real orthogonal Lie algebra"
kind = "definition"
summary = "so(2,R) — real orthogonal Lie algebra."
aliases = ["so(2,R) — real orthogonal Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real orthogonal [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{so}(2,\mathbb R)\) consists of skew-symmetric \(2\times2\) matrices, with commutator bracket:

\[
\mathfrak{so}(2,\mathbb R)=\{X\in M_{2}(\mathbb R):X^T+X=0\},\qquad [X,Y]=XY-YX.
\]


The form preserved here is the positive-definite real form \(x_1^2+\cdots+x_2^2\).

## Dimension and structure

The independent entries above the diagonal give real dimension \(1\); a basis is \(E_{ij}-E_{ji}\ (1\leq i<j\leq 2)\). There is one generator and its self-bracket is zero, so this algebra is abelian.

[[lie-groups/orthogonal-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb R\) as its defining field. Its complexification is a different catalogue object; a matrix presentation over complex numbers does not change this field automatically.
