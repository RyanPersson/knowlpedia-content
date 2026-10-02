+++
id = "catalog/lie-algebras/so-2-2-r"
title = "so(2,2) — indefinite orthogonal real Lie algebra"
kind = "definition"
summary = "so(2,2) — indefinite orthogonal real Lie algebra."
aliases = ["so(2,2) — indefinite orthogonal real Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/orthogonal-lie-algebra", "lie-groups/lie-algebra", "linear-algebra/bilinear-form"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **indefinite orthogonal real [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{so}(2,2)\) preserves a symmetric [[linear-algebra/bilinear-form|bilinear form]] with \(2\) positive and \(2\) negative directions infinitesimally:

\[
\mathfrak{so}(2,2)=\{X\in M_{4}(\mathbb R):X^T\eta+\eta X=0\},\qquad \eta=\operatorname{diag}(I_{2},-I_{2}).
\]


The bracket is the matrix commutator.

## Dimension and real form

Multiplication by \(\eta\) identifies the defining [[linear-algebra/vector-space|vector space]] with skew-symmetric matrices, so its real dimension is \(6\). This is a vector-space count, not an assertion that compact and indefinite brackets are isomorphic. The equal-signature form is split.

Exchanging the positive and negative coordinates gives an isomorphic [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak{so}(2,2)\).
