+++
id = "measure-theory/radon-nikodym-derivative"
title = "Radon–Nikodym Derivative"
kind = "knowl"
summary = "The almost-everywhere unique density dν/dμ representing an absolutely continuous measure ν relative to μ."
aliases = ["radon-nikodym-derivative", "Radon–Nikodym Derivative"]
domains = ["measure-theory"]
legacy_source_path = "shale-paper/radon-nikodym-derivative.md"
prerequisites = ["measure-theory/measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mu\) and \(\nu\) be \(\sigma\)-finite positive measures on the same [[measure-theory/measurable-space|measurable space]]. If \(\nu\ll\mu\), the **Radon–Nikodym derivative** \(d\nu/d\mu\) is the \(\mu\)-almost-everywhere unique [[measure-theory/measurable-function|measurable function]] \(X\geq 0\) such that
\[
\nu(S)=\int_S X\,d\mu
\]
for every [[measure-theory/measurable-set|measurable set]] \(S\).

## Remarks

Existence and almost-everywhere uniqueness follow from the
[[probability/radon-nikodym-theorem|Radon–Nikodym theorem]].

In Shale's notation for a Gaussian pushforward, \(X(T)=dn(T)/dn\) plays the role of a measure-theoretic Jacobian.

## Examples

- For \(\nu=f\mu\) with \(f\ge0\), one has \(d\nu/d\mu=f\).
