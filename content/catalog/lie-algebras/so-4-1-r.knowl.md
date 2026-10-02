+++
id = "catalog/lie-algebras/so-4-1-r"
title = "so(4,1) — indefinite orthogonal real Lie algebra"
kind = "definition"
summary = "so(4,1) — indefinite orthogonal real Lie algebra."
aliases = ["so(4,1) — indefinite orthogonal real Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/orthogonal-lie-algebra", "lie-groups/lie-algebra", "linear-algebra/bilinear-form"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **indefinite orthogonal real [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{so}(4,1)\) preserves a symmetric [[linear-algebra/bilinear-form|bilinear form]] with \(4\) positive and \(1\) negative directions infinitesimally:

\[
\mathfrak{so}(4,1)=\{X\in M_{5}(\mathbb R):X^T\eta+\eta X=0\},\qquad \eta=\operatorname{diag}(I_{4},-I_{1}).
\]


The bracket is the matrix commutator.

## Dimension and real form

Multiplication by \(\eta\) identifies the defining [[linear-algebra/vector-space|vector space]] with skew-symmetric matrices, so its real dimension is \(10\). This is a vector-space count, not an assertion that compact and indefinite brackets are isomorphic.

Exchanging the positive and negative coordinates gives an isomorphic [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak{so}(1,4)\).
