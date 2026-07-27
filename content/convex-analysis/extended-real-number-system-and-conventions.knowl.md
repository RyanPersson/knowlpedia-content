+++
id = "convex-analysis/extended-real-number-system-and-conventions"
title = "Extended real number system and conventions"
kind = "knowl"
summary = "The ordered real line with positive and negative infinity, together with standard infimum and supremum conventions."
aliases = ["extended-real-number-system-and-conventions", "Extended real number system and conventions"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/extended-real-number-system-and-conventions.md"
+++

The **extended real number system** is
\[
\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\},
\]
ordered by \(-\infty<x<+\infty\) for every \(x\in\mathbb R\). Convex analysis often uses the one-sided extension
\[
\mathbb R\cup\{+\infty\}=(-\infty,+\infty]
\]
for functions that encode infeasible points by the value \(+\infty\).

## Infimum and supremum conventions

For \(A\subseteq\overline{\mathbb R}\), an unbounded-below nonempty set has \(\inf A=-\infty\), and an unbounded-above nonempty set has \(\sup A=+\infty\). For the empty set, the conventions are
\[
\inf\varnothing=+\infty,
\qquad
\sup\varnothing=-\infty.
\]

## Remarks

Allowing the value \(+\infty\) lets an [[convex-analysis/indicator-function-of-a-set|indicator function]] encode a constraint without repeatedly restricting the domain.
