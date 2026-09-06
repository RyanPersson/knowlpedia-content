+++
id = "measure-theory/pushforward-measure"
title = "Pushforward measure"
kind = "knowl"
summary = "The measure obtained by transporting a measure through a measurable map."
aliases = ["pushforward-measure", "Pushforward measure"]
domains = ["measure-theory"]
prerequisites = ["measure-theory/measure-space", "measure-theory/measurable-space", "measure-theory/measurable-function", "measure-theory/measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "measure-theory/pushforward-measure.md"
+++

A **pushforward measure** transports a measure along a measurable map. Let \((X,\mathcal A,\mu)\) be a [[measure-theory/measure-space|measure space]], let \((Y,\mathcal B)\) be a [[measure-theory/measurable-space|measurable space]], and let \(T:X\to Y\) be a [[measure-theory/measurable-function|measurable function]]. The **pushforward** of \(\mu\) by \(T\), denoted \(T_\#\mu\) or \(T_*\mu\), is the [[measure-theory/measure|measure]] on \((Y,\mathcal B)\) defined by
\[
(T_\#\mu)(B)=\mu(T^{-1}(B))\qquad(B\in\mathcal B).
\]

The definition measures subsets of \(Y\) by pulling them back to \(X\). Pushforwards are the natural language for the [[measure-theory/change-of-variables-pushforward|change-of-variables formula]].

## Examples

- Let \(\lambda\) be Lebesgue measure on \([0,1]\) and let \(T(x)=x^2\). Then \(\nu=T_\#\lambda\) satisfies \(\nu([0,t])=\sqrt t\) for \(0\le t\le1\), so \(\nu\) has density \(1/(2\sqrt y)\) on \((0,1]\).
- If \(\pi_X:X\times Y\to X\) is projection and \(\mu\otimes\nu\) is a [[measure-theory/product-measure|product measure]], then
  \[
  (\pi_X)_\#(\mu\otimes\nu)(A)=(\mu\otimes\nu)(A\times Y)=\mu(A)\nu(Y)
  \]
  for \(A\in\mathcal A\). Thus \((\pi_X)_\#(\mu\otimes\nu)=\nu(Y)\mu\); in particular, it equals \(\mu\) when \(\nu\) is a probability measure.
