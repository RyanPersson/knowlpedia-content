+++
id = "catalog/lie-algebras/e-3-r"
title = "e(3) — Euclidean motion Lie algebra"
kind = "definition"
summary = "e(3) — Euclidean motion Lie algebra."
aliases = ["e(3) — Euclidean motion Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "catalog/lie-algebras/so-3-r", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **Euclidean motion [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak e(3)\) is the real [[linear-algebra/vector-space|vector space]] [[catalog/lie-algebras/so-3-r|\(\mathfrak{so}(3)\)]]\(\oplus\mathbb R^{3}\) with bracket

\[
[(A,v),(B,w)]=(AB-BA,Aw-Bv).
\]

## Rotations and translations

Rotations act on the translation vectors by ordinary matrix multiplication. The translations form an abelian ideal; quotienting by them gives the [[lie-groups/orthogonal-lie-algebra|orthogonal Lie algebra]]. The block-matrix realization \((A,v)\mapsto\begin{pmatrix}A&v\\0&0\end{pmatrix}\) verifies the bracket and Jacobi identity.

The full Euclidean group and its orientation-preserving subgroup have this same tangent [[lie-groups/lie-algebra|Lie algebra]]; their disconnected components are invisible infinitesimally.
