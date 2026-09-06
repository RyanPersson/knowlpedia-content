+++
id = "real-analysis/limit-superior-lim-sup"
title = "Limit superior (lim sup)"
kind = "knowl"
summary = "The largest limit point of a bounded sequence, or equivalently the infimum of suprema of tails."
aliases = ["limit-superior-lim-sup", "Limit superior (lim sup)"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-superior-lim-sup.md"
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **limit superior** (or **lim sup**) of a bounded sequence \((x_n)\) in \(\mathbb{R}\) is
\[
\limsup_{n \to \infty} x_n = \lim_{n \to \infty} \sup_{k \geq n} x_k = \inf_{n \geq 1} \sup_{k \geq n} x_k.
\]

## Characterizations
For a [[real-analysis/bounded-sequence|bounded sequence]] \((x_n)\), the lim sup equals:

1. The largest subsequential limit (when the sequence is bounded; this includes limits of eventually constant subsequences).
2. The supremum of the set of all [[real-analysis/subsequence|subsequential]] limits.

## Properties
- \(\liminf x_n \leq \limsup x_n\) always.
- The sequence converges if and only if \(\liminf x_n = \limsup x_n\), and then the limit equals this common value.
- \(\limsup(-x_n) = -\liminf(x_n)\).

## Extended values
For an unbounded sequence, the lim sup is determined by the tail behavior: it is \(+\infty\) when every tail is unbounded above. A finite initial outlier does not affect the lim sup. If \(x_n\to -\infty\), then \(\limsup x_n=-\infty\).

## Examples
For \(x_n = (-1)^n(1 + 1/n)\): \(\limsup x_n = 1\), \(\liminf x_n = -1\).
