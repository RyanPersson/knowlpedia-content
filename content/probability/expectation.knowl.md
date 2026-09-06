+++
id = "probability/expectation"
title = "Expectation"
kind = "knowl"
summary = "The integral of a random variable with respect to the underlying probability measure."
aliases = ["expectation"]
domains = ["probability"]
prerequisites = ["probability/random-variable", "measure-theory/lebesgue-integral", "measure-theory/lebesgue-integrable-function"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
legacy_source_path = "probability/expectation.md"
+++

The **expectation** of an integrable [[probability/random-variable|random variable]] \(X\) is
\[
\mathbb E[X]=\int_\Omega X(\omega)\,d\mathbb P(\omega),
\]
where integrability means \(\int_\Omega |X|\,d\mathbb P<\infty\).

## Remarks

This definition uses the [[measure-theory/lebesgue-integral|Lebesgue integral]] on the underlying [[probability/probability-space|probability space]]; expectation is the basic averaging operation underlying [[probability/variance|variance]], [[probability/covariance|covariance]], and many limit theorems.

## Examples

- If \(X\) takes values \(x_k\) with probabilities \(p_k\) (countably many), then \(\mathbb E[X]=\sum_k x_k p_k\) whenever \(\sum_k |x_k|p_k<\infty\).
- If \(X\) is uniform on \([0,1]\), then \(\mathbb E[X]=\int_0^1 x\,dx=\tfrac12\).
