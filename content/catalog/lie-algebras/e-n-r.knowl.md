+++
id = "catalog/lie-algebras/e-n-r"
title = "e(n) — Euclidean motion Lie algebra"
kind = "definition"
summary = "e(n) — Euclidean motion Lie algebra."
aliases = ["e(n) — Euclidean motion Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "lie-groups/orthogonal-lie-algebra", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **Euclidean motion [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak e(n)\) is the real [[linear-algebra/vector-space|vector space]] [[lie-groups/orthogonal-lie-algebra|\(\mathfrak{so}(n)\)]]\(\oplus\mathbb R^{n}\) with bracket

\[
[(A,v),(B,w)]=(AB-BA,Aw-Bv).
\]

## Rotations and translations

Rotations act on the translation vectors by ordinary matrix multiplication. The translations form an abelian ideal; quotienting by them gives the orthogonal Lie algebra. The block-matrix realization \((A,v)\mapsto\begin{pmatrix}A&v\\0&0\end{pmatrix}\) verifies the bracket and Jacobi identity.

The full Euclidean group and its orientation-preserving subgroup have this same tangent [[lie-groups/lie-algebra|Lie algebra]]; their disconnected components are invisible infinitesimally.
