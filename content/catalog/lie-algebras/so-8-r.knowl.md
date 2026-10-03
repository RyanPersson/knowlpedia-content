+++
id = "catalog/lie-algebras/so-8-r"
title = "so(8,R) — real orthogonal Lie algebra"
kind = "definition"
summary = "so(8,R) — real orthogonal Lie algebra."
aliases = ["so(8,R) — real orthogonal Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real orthogonal [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{so}(8,\mathbb R)\) consists of skew-symmetric \(8\times8\) matrices, with commutator bracket:

\[
\mathfrak{so}(8,\mathbb R)=\{X\in M_{8}(\mathbb R):X^T+X=0\},\qquad [X,Y]=XY-YX.
\]


The form preserved here is the positive-definite real form \(x_1^2+\cdots+x_8^2\).

## Dimension and structure

The independent entries above the diagonal give real dimension \(28\); a basis is \(E_{ij}-E_{ji}\ (1\leq i<j\leq 8)\). This is the type \(D_4\) algebra whose vector and [[lie-groups/half-spin-representation|half-spin representations]] participate in [[lie-groups/spin8-triality|triality]].

[[lie-groups/orthogonal-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb R\) as its defining field. Its complexification is a different catalogue object; a matrix presentation over complex numbers does not change this field automatically.
