+++
id = "catalog/lie-algebras/so-3-1-r"
title = "so(3,1) — indefinite orthogonal real Lie algebra"
kind = "definition"
summary = "so(3,1) — indefinite orthogonal real Lie algebra."
aliases = ["so(3,1) — indefinite orthogonal real Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/orthogonal-lie-algebra", "lie-groups/lie-algebra", "linear-algebra/bilinear-form"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **indefinite orthogonal real [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{so}(3,1)\) preserves a symmetric [[linear-algebra/bilinear-form|bilinear form]] with \(3\) positive and \(1\) negative directions infinitesimally:

\[
\mathfrak{so}(3,1)=\{X\in M_{4}(\mathbb R):X^T\eta+\eta X=0\},\qquad \eta=\operatorname{diag}(I_{3},-I_{1}).
\]


The bracket is the matrix commutator.

## Dimension and real form

Multiplication by \(\eta\) identifies the defining [[linear-algebra/vector-space|vector space]] with skew-symmetric matrices, so its real dimension is \(6\). This is a vector-space count, not an assertion that compact and indefinite brackets are isomorphic. It is the six-dimensional Lorentz algebra, isomorphic to \(\mathfrak{sl}(2,\mathbb C)_{\mathbb R}\) as a **real** [[lie-groups/lie-algebra|Lie algebra]].

Exchanging the positive and negative coordinates gives an isomorphic Lie algebra \(\mathfrak{so}(1,3)\).
