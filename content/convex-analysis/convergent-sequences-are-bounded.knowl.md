+++
id = "convex-analysis/convergent-sequences-are-bounded"
title = "Convergent sequences are bounded"
kind = "knowl"
summary = "A convergent sequence in a metric space must lie in some ball"
aliases = ["convergent-sequences-are-bounded", "Convergent sequences are bounded"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convergent-sequences-are-bounded.md"
prerequisites = ["convex-analysis/convergence-of-a-sequence"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Proposition.**
Any [[convex-analysis/convergence-of-a-sequence|convergent sequence]] in a metric space is bounded.

## Proof

If \(x_n\to a\), then \(d(x_n,a)<1\) for all sufficiently large \(n\). The finitely many remaining values \(d(x_n,a)\) are also bounded, so there is \(R<\infty\) such that \(d(x_n,a)\le R\) for every \(n\). Thus the sequence is [[convex-analysis/bounded-set-and-bounded-sequence|bounded]].
