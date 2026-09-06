+++
id = "measure-theory/change-of-variables-pushforward"
title = "Change of variables for pushforward measures"
kind = "knowl"
summary = "Identity relating integrals with respect to a pushforward measure to composition with the underlying map."
aliases = ["change-of-variables-pushforward", "Change of variables for pushforward measures"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/change-of-variables-pushforward.md"
prerequisites = ["measure-theory/measure-space", "measure-theory/measurable-space", "measure-theory/measurable-function", "measure-theory/pushforward-measure", "measure-theory/lebesgue-integrable-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Change of variables for pushforward measures:** Let \((X,\Sigma,\mu)\) be a [[measure-theory/measure-space|measure space]], let \((Y,\mathcal T)\) be a [[measure-theory/measurable-space|measurable space]], and let \(T:X\to Y\) be a [[measure-theory/measurable-function|measurable function]]. Let \(\nu = T_*\mu\) be the [[measure-theory/pushforward-measure|pushforward measure]] of \(\mu\) by \(T\). Then for every nonnegative measurable function \(g:Y\to[0,\infty]\),
\[
\int_Y g\,d\nu \;=\; \int_X (g\circ T)\,d\mu.
\]
If \(g\) is [[measure-theory/lebesgue-integrable-function|Lebesgue integrable]] with respect to \(\nu\), then \(g\circ T\) is Lebesgue integrable with respect to \(\mu\) and the same identity holds with finite values.

## Interpretation

This formula packages the defining property of the pushforward measure into an equality of [[measure-theory/lebesgue-integral|Lebesgue integrals]] and is a standard “change of variables” principle for transporting a [[measure-theory/measure|measure]] along a map. It is frequently used together with constructions such as the [[measure-theory/product-measure|product measure]].
