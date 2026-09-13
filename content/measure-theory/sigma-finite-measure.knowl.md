+++
id = "measure-theory/sigma-finite-measure"
title = "Sigma-finite measure"
kind = "definition"
summary = "A measure space covered by countably many measurable sets of finite measure."
aliases = ["sigma-finiteness", "σ-finite measure"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/measure-space", "shared-foundations/countable-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A [[measure-theory/measure-space|measure space]] \((X,\Sigma,\mu)\) is **sigma-finite** if there are measurable sets \(E_1,E_2,\ldots\) with \(X=\bigcup_jE_j\) and \(\mu(E_j)<\infty\) for every \(j\).

## Examples and use

Lebesgue measure on \(\mathbb R^n\) is sigma-finite: use bounded cubes of increasing size. A finite measure is sigma-finite. Counting measure on an uncountable set is not, since a countable union of finite sets is countable. Sigma-finiteness is a hypothesis of the standard product-measure uniqueness and [[measure-theory/tonellis-theorem|Tonelli]] statements; it does not mean that the whole space has finite measure.
