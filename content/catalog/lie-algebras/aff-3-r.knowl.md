+++
id = "catalog/lie-algebras/aff-3-r"
title = "Affine transformation Lie algebra aff(3,R)"
kind = "definition"
summary = "Affine transformation Lie algebra aff(3,R)."
aliases = ["Affine transformation Lie algebra aff(3,R)"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real affine transformation [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{aff}(3,\mathbb R)\) is \(M_{3}(\mathbb R)\oplus \mathbb R^{3}\) with bracket

\[
[(A,v),(B,w)]=(AB-BA,Aw-Bv).
\]


It describes infinitesimal affine transformations of \(\mathbb R^{3}\).

## Matrix model and convention

The block-matrix embedding \[
(A,v)\longmapsto\begin{pmatrix}A&v\\0&0\end{pmatrix}
\]
turns the displayed bracket into a matrix commutator, proving the Lie axioms. The translation vectors form an abelian ideal, and the quotient is the [[lie-groups/general-linear-lie-algebra|general linear Lie algebra]].

This finite-dimensional algebra of affine transformations is not an affine Kac–Moody algebra.
