+++
id = "catalog/lie-algebras/aff-1-r"
title = "Affine transformation Lie algebra aff(1,R)"
kind = "definition"
summary = "Affine transformation Lie algebra aff(1,R)."
aliases = ["Affine transformation Lie algebra aff(1,R)"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real affine transformation [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{aff}(1,\mathbb R)\) is \(M_{1}(\mathbb R)\oplus \mathbb R^{1}\) with bracket

\[
[(A,v),(B,w)]=(AB-BA,Aw-Bv).
\]


It describes infinitesimal affine transformations of \(\mathbb R^{1}\).

## Matrix model and convention

The block-matrix embedding \[
(A,v)\longmapsto\begin{pmatrix}A&v\\0&0\end{pmatrix}
\]
turns the displayed bracket into a matrix commutator, proving the Lie axioms. The translation vectors form an abelian ideal, and the quotient is the [[lie-groups/general-linear-lie-algebra|general linear Lie algebra]]. Here a basis \(h,x\) has \([h,x]=x\): this is a two-dimensional solvable, nonnilpotent [[lie-groups/lie-algebra|Lie algebra]].

This finite-dimensional algebra of affine transformations is not an affine Kac–Moody algebra.
