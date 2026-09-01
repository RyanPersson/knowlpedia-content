+++
id = "probability/variance"
title = "Variance"
kind = "knowl"
summary = "A measure of how spread out a random variable is around its mean."
aliases = ["variance"]
domains = ["probability"]
prerequisites = ["probability/random-variable", "probability/expectation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "probability/variance.md"
+++

A **variance** of a [[probability/random-variable|random variable]] \(X\) is the quantity
\[
\operatorname{Var}(X)=\mathbb E\big[(X-\mathbb E[X])^2\big],
\]
defined when \(\mathbb E[X^2]<\infty\) (so in particular the [[probability/expectation|expectation]] \(\mathbb E[X]\) is finite).

## Equivalent characterizations

Equivalently,
\[
\operatorname{Var}(X)=\mathbb E[X^2]-\big(\mathbb E[X]\big)^2.
\]

## Remarks

Variance is the second centered [[probability/moment|moment]] of \(X\). It is also the special case \(\operatorname{Var}(X)=\operatorname{Cov}(X,X)\) of [[probability/covariance|covariance]], and it is used to normalize [[probability/covariance|covariance]] into the [[probability/correlation-coefficient|correlation coefficient]].

## Examples

- If \(X\) is Bernoulli\((p)\) (so \(\mathbb P(X=1)=p\), \(\mathbb P(X=0)=1-p\)), then \(\operatorname{Var}(X)=p(1-p)\).
- If \(X\sim N(\mu,\sigma^2)\), then \(\operatorname{Var}(X)=\sigma^2\).
