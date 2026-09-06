+++
id = "measure-theory/measurable-space"
title = "Measurable space"
kind = "knowl"
summary = "A set equipped with a sigma-algebra of measurable subsets."
aliases = ["measurable-space", "Measurable space"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/measurable-space.md"
prerequisites = ["shared-foundations/set", "measure-theory/sigma-algebra"]
dependency_heuristic = "semantic-foundations-review-v1"
dependency_review_count = 1
+++

A **measurable space** is a pair \((X,\Sigma)\) consisting of a [[shared-foundations/set|set]] \(X\) and a [[measure-theory/sigma-algebra|sigma-algebra]] \(\Sigma\) on \(X\).

Measurable spaces are the domains and codomains for [[measure-theory/measurable-function|measurable functions]]; adding a [[measure-theory/measure|measure]] produces a [[measure-theory/measure-space|measure space]].

## Examples

- \((\mathbb R,\mathcal B(\mathbb R))\), where \(\mathcal B(\mathbb R)\) is the [[measure-theory/borel-sigma-algebra|Borel sigma-algebra]] on \(\mathbb R\).
- \((X,\mathcal P(X))\), where \(\mathcal P(X)\) is the [[shared-foundations/power-set|power set]] of \(X\).
