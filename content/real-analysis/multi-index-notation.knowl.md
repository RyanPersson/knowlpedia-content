+++
id = "real-analysis/multi-index-notation"
title = "Multi-index notation"
kind = "notation"
summary = "Compact notation for products, factorials, and iterated partial derivatives in several variables."
aliases = ["multiindex notation", "multi-index derivative"]
domains = ["real-analysis", "partial-differential-equations"]
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **multi-index** is a tuple \(\alpha=(\alpha_1,\ldots,\alpha_d)\in\mathbb N_0^d\).
The standard notation is
\[
|\alpha|=\alpha_1+\cdots+\alpha_d,
\quad \alpha!=\alpha_1!\cdots\alpha_d!,
\quad x^\alpha=x_1^{\alpha_1}\cdots x_d^{\alpha_d},
\]
\[
\partial^\alpha
=\partial_{x_1}^{\alpha_1}\cdots\partial_{x_d}^{\alpha_d}.
\]

## Derivative families

The symbol \(D^a f\) may denote the family
\((\partial^\alpha f)_{|\alpha|=a}\). A scalar size such as
\(|D^a f(x)|=\sup_{|\alpha|=a}|\partial^\alpha f(x)|\) must be stated because
other texts use Euclidean or summed norms on this finite family.

## Uses

Multi-indices compress Taylor formulas, symbol estimates, [[functional-analysis/schwartz-space|Schwartz seminorms]],
and [[functional-analysis/distributional-derivative|distributional
derivatives]] in several variables.

## References

1. Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., AMS, 2010. [Publisher record](https://bookstore.ams.org/gsm-19-r/).
