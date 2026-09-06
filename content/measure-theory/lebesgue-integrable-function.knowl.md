+++
id = "measure-theory/lebesgue-integrable-function"
title = "Lebesgue integrable function"
kind = "knowl"
summary = "A measurable function whose absolute value has finite Lebesgue integral."
aliases = ["lebesgue-integrable-function", "Lebesgue integrable function"]
domains = ["measure-theory"]
prerequisites = ["measure-theory/measure-space","measure-theory/measurable-function","real-analysis/absolute-value","measure-theory/lebesgue-integral"]
dependency_review_count = 1
legacy_source_path = "measure-theory/lebesgue-integrable-function.md"
+++

A **Lebesgue integrable function** on a [[measure-theory/measure-space|measure space]] \((X,\Sigma,\mu)\) is a real- or complex-valued [[measure-theory/measurable-function|measurable function]] \(f\) such that
\[
\int_X |f|\,d\mu<\infty,
\]
where \(|f|\) denotes the [[real-analysis/absolute-value|absolute value]] applied pointwise.

Its [[measure-theory/lebesgue-integral|Lebesgue integral]] is finite and depends only on the [[measure-theory/ae-equality|almost-everywhere equivalence class]] of \(f\). These equivalence classes form the space [[measure-theory/l1-function|\(L^1(X,\mu)\)]].

## Examples

- On \(\mathbb R\) with [[measure-theory/lebesgue-measure|Lebesgue measure]], the function \(f(x)=\frac{1}{1+x^2}\) is Lebesgue integrable.
- If \(E\) is a [[measure-theory/measurable-set|measurable set]] with \(\mu(E)<\infty\), then the [[measure-theory/indicator-function|indicator function]] \(\mathbf{1}_E\) is Lebesgue integrable.
