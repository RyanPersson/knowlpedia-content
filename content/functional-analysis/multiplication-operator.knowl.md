+++
id = "functional-analysis/multiplication-operator"
title = "Multiplication operator"
kind = "definition"
summary = "The linear operator that multiplies a function by a fixed coefficient."
aliases = []
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["measure-theory/lp-space", "measure-theory/measurable-function", "functional-analysis/bounded-linear-operator"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a measurable scalar coefficient \(a\), the **multiplication operator** \(M_a\) acts by \(M_af=af\) on functions for which the product belongs to the chosen function space. On \(L^p\), a bounded coefficient defines a bounded operator with
\[
\|M_af\|_p\le\|a\|_\infty\|f\|_p.
\]
These are [[measure-theory/lp-space|Lebesgue norms]].

## Domains

For an unbounded coefficient, one must specify the domain, such as \(\{f\in L^p:af\in L^p\}\). Multiplication of a distribution instead requires a smooth coefficient, or additional hypotheses that make the product meaningful.
