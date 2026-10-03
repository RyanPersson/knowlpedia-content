+++
id = "catalog/lie-algebras/aff-n-r"
title = "Affine transformation Lie algebra aff(n,R)"
kind = "definition"
summary = "Affine transformation Lie algebra aff(n,R)."
aliases = ["Affine transformation Lie algebra aff(n,R)"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **real affine transformation [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{aff}(n,\mathbb R)\) is \(M_{n}(\mathbb R)\oplus \mathbb R^{n}\) with bracket

\[
[(A,v),(B,w)]=(AB-BA,Aw-Bv).
\]


It describes infinitesimal affine transformations of \(\mathbb R^{n}\).

## Matrix model and convention

The block-matrix embedding \[
(A,v)\longmapsto\begin{pmatrix}A&v\\0&0\end{pmatrix}
\]
turns the displayed bracket into a matrix commutator, proving the Lie axioms. The translation vectors form an abelian ideal, and the quotient is the [[lie-groups/general-linear-lie-algebra|general linear Lie algebra]].

This finite-dimensional algebra of affine transformations is not an affine Kac–Moody algebra.
