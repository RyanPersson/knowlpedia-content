+++
id = "catalog/lie-algebras/e-2-r"
title = "e(2) — Euclidean motion Lie algebra"
kind = "definition"
summary = "e(2) — Euclidean motion Lie algebra."
aliases = ["e(2) — Euclidean motion Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "catalog/lie-algebras/so-2-r", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **Euclidean motion [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak e(2)\) is the real [[linear-algebra/vector-space|vector space]] [[catalog/lie-algebras/so-2-r|\(\mathfrak{so}(2)\)]]\(\oplus\mathbb R^{2}\) with bracket

\[
[(A,v),(B,w)]=(AB-BA,Aw-Bv).
\]

## Rotations and translations

Rotations act on the translation vectors by ordinary matrix multiplication. The translations form an abelian ideal; quotienting by them gives the [[lie-groups/orthogonal-lie-algebra|orthogonal Lie algebra]]. The block-matrix realization \((A,v)\mapsto\begin{pmatrix}A&v\\0&0\end{pmatrix}\) verifies the bracket and Jacobi identity.

The full Euclidean group and its orientation-preserving subgroup have this same tangent [[lie-groups/lie-algebra|Lie algebra]]; their disconnected components are invisible infinitesimally.
