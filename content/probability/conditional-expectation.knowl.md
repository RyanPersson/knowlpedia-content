+++
id = "probability/conditional-expectation"
title = "Conditional expectation"
kind = "knowl"
summary = "An integrable random variable characterized by its averages over events in a given sigma-algebra."
aliases = ["conditional-expectation", "Conditional expectation"]
domains = ["probability"]
prerequisites = ["probability/random-variable", "probability/probability-space", "measure-theory/measurable-function", "probability/expectation", "measure-theory/indicator-function"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
legacy_source_path = "probability/conditional-expectation.md"
+++

A **conditional expectation** of an integrable [[probability/random-variable|random variable]] \(X\) given a sub-\(\sigma\)-algebra \(\mathcal G\subseteq\mathcal F\) on a [[probability/probability-space|probability space]] \((\Omega,\mathcal F,\mathbb P)\) is an integrable, \(\mathcal G\)-[[measure-theory/measurable-function|measurable function]] \(Y\) such that
\[
\mathbb E\!\left[Y\,\mathbf 1_G\right] \;=\; \mathbb E\!\left[X\,\mathbf 1_G\right]\quad\text{for every }G\in\mathcal G.
\]

Such a \(Y\) exists and is unique up to almost-sure equality; it is denoted \(\mathbb E[X\mid\mathcal G]\).

## Remarks

The special case \(X=\mathbf1_A\) gives the [[probability/conditional-probability|conditional probability]] of \(A\) given \(\mathcal G\).

## Examples

- If \(\mathcal G=\{\varnothing,\Omega\}\), then \(\mathbb E[X\mid\mathcal G]=\mathbb E[X]\) almost surely.
- If \(X\) is \(\mathcal G\)-measurable, then \(\mathbb E[X\mid\mathcal G]=X\) almost surely.
- If \(B\in\mathcal F\), \(\mathbb P(B)\in(0,1)\), and \(\mathcal G=\sigma(B)\), then
  \[
  \mathbb E[X\mid \mathcal G]
  \;=\;
  \frac{\mathbb E[X\,\mathbf 1_B]}{\mathbb P(B)}\,\mathbf 1_B
  \;+\;
  \frac{\mathbb E[X\,\mathbf 1_{B^c}]}{\mathbb P(B^c)}\,\mathbf 1_{B^c}.
  \]
