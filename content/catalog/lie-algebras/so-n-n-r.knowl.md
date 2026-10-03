+++
id = "catalog/lie-algebras/so-n-n-r"
title = "so(n,n) — indefinite orthogonal real Lie algebra"
kind = "definition"
summary = "so(n,n) — indefinite orthogonal real Lie algebra."
aliases = ["so(n,n) — indefinite orthogonal real Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/orthogonal-lie-algebra", "lie-groups/lie-algebra", "linear-algebra/bilinear-form"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **indefinite orthogonal real [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{so}(n,n)\) preserves a symmetric [[linear-algebra/bilinear-form|bilinear form]] with \(n\) positive and \(n\) negative directions infinitesimally:

\[
\mathfrak{so}(n,n)=\{X\in M_{2n}(\mathbb R):X^T\eta+\eta X=0\},\qquad \eta=\operatorname{diag}(I_{n},-I_{n}).
\]


The bracket is the matrix commutator.

## Dimension and real form

Multiplication by \(\eta\) identifies the defining [[linear-algebra/vector-space|vector space]] with skew-symmetric matrices, so its real dimension is \(n(2n-1)\). This is a vector-space count, not an assertion that compact and indefinite brackets are isomorphic. The equal-signature form is split.

Exchanging the positive and negative coordinates gives an isomorphic [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak{so}(n,n)\).
