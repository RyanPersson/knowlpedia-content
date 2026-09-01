+++
id = "convex-analysis/closure-characterized-by-convergent-sequences"
title = "Closure via sequences"
kind = "knowl"
summary = "In a metric space, a point lies in a set's closure exactly when a sequence from the set converges to it."
aliases = ["closure-characterized-by-convergent-sequences", "Closure via sequences"]
domains = ["convex-analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/closure-characterized-by-convergent-sequences.md"
+++

Let \((X,d)\) be a metric space and \(A\subseteq X\). For \(a\in X\),
\[
a\in \overline{A}\quad\Longleftrightarrow\quad \exists\ (a_n)\subset A \text{ with } a_n\to a.
\]

## Remarks

**Context.** This is a specifically metric phenomenon (first-countability): the topological notion of [[convex-analysis/closure-of-a-set|closure]] can be detected by sequences.

**Proof sketch.**
- If \(a\in\overline{A}\), then by [[convex-analysis/closure-characterized-by-ball-intersections|ball intersections]] each ball \(B(a;1/n)\) meets \(A\); pick \(a_n\in A\cap B(a;1/n)\) to get \(a_n\to a\).
- Conversely, if \(a_n\in A\) and \(a_n\to a\), then every ball around \(a\) contains some \(a_n\), hence meets \(A\), so \(a\in\overline{A}\).
