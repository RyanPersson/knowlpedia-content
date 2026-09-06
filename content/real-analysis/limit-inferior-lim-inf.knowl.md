+++
id = "real-analysis/limit-inferior-lim-inf"
title = "Limit inferior (lim inf)"
kind = "knowl"
summary = "The smallest limit point of a bounded sequence, or equivalently the supremum of infima of tails."
aliases = ["limit-inferior-lim-inf", "Limit inferior (lim inf)"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-inferior-lim-inf.md"
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **limit inferior** (or **lim inf**) of a bounded sequence \((x_n)\) in \(\mathbb{R}\) is
\[
\liminf_{n \to \infty} x_n = \lim_{n \to \infty} \inf_{k \geq n} x_k = \sup_{n \geq 1} \inf_{k \geq n} x_k.
\]

## Characterizations
For a [[real-analysis/bounded-sequence|bounded sequence]] \((x_n)\), the lim inf equals:

1. The smallest subsequential limit (when the sequence is bounded; this includes limits of eventually constant subsequences).
2. The infimum of the set of all [[real-analysis/subsequence|subsequential]] limits.

## Properties
- \(\liminf x_n \leq \limsup x_n\) always.
- The sequence converges if and only if \(\liminf x_n = \limsup x_n\).
- \(\liminf(-x_n) = -\limsup(x_n)\).
- \(\liminf(x_n + y_n) \geq \liminf x_n + \liminf y_n\) (superadditivity).

## Extended values
For an unbounded sequence, the lim inf is determined by the tail behavior: it is \(-\infty\) when every tail is unbounded below. A finite initial outlier does not affect the lim inf. If \(x_n\to +\infty\), then \(\liminf x_n=+\infty\).

## Examples
For \(x_n = (-1)^n + 1/n\): \(\liminf x_n = -1\), \(\limsup x_n = 1\).
