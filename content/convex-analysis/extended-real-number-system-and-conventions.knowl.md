+++
id = "convex-analysis/extended-real-number-system-and-conventions"
title = "Extended real number system and conventions"
kind = "knowl"
summary = "The ordered real line with positive and negative infinity, together with standard infimum and supremum conventions."
aliases = ["extended-real-number-system-and-conventions", "Extended real number system and conventions"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/extended-real-number-system-and-conventions.md"
prerequisites = ["shared-foundations/real-numbers", "shared-foundations/total-order", "shared-foundations/upper-bound", "shared-foundations/lower-bound", "real-analysis/infimum", "real-analysis/supremum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

The **extended real number system** adjoins two formal endpoints to the [[shared-foundations/real-numbers|real numbers]]:
\[
\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\},
\]
ordered by \(-\infty<x<+\infty\) for every \(x\in\mathbb R\). Convex analysis often uses the one-sided extension
\[
\mathbb R\cup\{+\infty\}=(-\infty,+\infty]
\]
for functions that encode infeasible points by the value \(+\infty\).

## Infimum and supremum conventions

Every nonempty \(A\subseteq\overline{\mathbb R}\) has a greatest lower bound and a least upper bound in the extended order, extending the real [[real-analysis/infimum|infimum]] and [[real-analysis/supremum|supremum]]. If \(A\) has no real lower bound then \(\inf A=-\infty\); if it has no real upper bound then \(\sup A=+\infty\). The distinction between real and extended bounds matters: \(-\infty\) is an extended lower bound for every subset. For the empty set, the conventions are
\[
\inf\varnothing=+\infty,
\qquad
\sup\varnothing=-\infty.
\]

## Remarks

Allowing the value \(+\infty\) lets an [[convex-analysis/indicator-function-of-a-set|indicator function]] encode a constraint without repeatedly restricting the domain.
