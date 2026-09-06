+++
id = "real-analysis/uniqueness-of-sup-inf"
title = "Uniqueness of Supremum and Infimum"
kind = "knowl"
summary = "A set has at most one least upper bound and at most one greatest lower bound."
aliases = ["uniqueness-of-sup-inf", "Uniqueness of Supremum and Infimum"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/supremum", "real-analysis/infimum", "real-analysis/completeness-axiom"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "real-analysis/uniqueness-of-sup-inf.md"
+++

**Uniqueness of supremum/infimum:** Let \(A \subseteq \mathbb{R}\) be nonempty.

- If \(s\) and \(t\) are both [[real-analysis/supremum|suprema]] of \(A\), then \(s=t\).
- If \(u\) and \(v\) are both [[real-analysis/infimum|infima]] of \(A\), then \(u=v\).

This guarantees that the notation \(\sup A\) and \(\inf A\) is unambiguous whenever these numbers exist, which is ensured under the hypotheses of the [[real-analysis/completeness-axiom|completeness axiom]] (for \(\sup\)) and its dual (for \(\inf\)).
