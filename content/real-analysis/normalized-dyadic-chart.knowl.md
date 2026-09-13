+++
id = "real-analysis/normalized-dyadic-chart"
title = "Normalized dyadic chart"
kind = "definition"
summary = "Coordinates divided by a fixed band scale so that a scale-localized region has order-one size."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/dyadic-scale-partition", "real-analysis/anisotropic-dilation", "real-analysis/chain-rule-multivariable", "real-analysis/multi-index-notation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Fix a [[real-analysis/dyadic-scale-partition|dyadic band]] with scale \(Q>0\). For exponents \(b_i\), **normalized coordinates** are \(y_i=x_i/Q^{b_i}\); for a time distance \(\tau\), one may also set \(s=\tau/Q\). The number \(Q\) is constant within the chart.

## Derivatives

For \(F(x)=A\widetilde F(y)\), where \(A\) is constant on this chart,
\[
\partial_x^I F=AQ^{-\sum_i b_i I_i}\partial_y^I\widetilde F.
\]
Even if a variable scale \(q(x)\) is comparable to \(Q\) on the band, differentiating a normalized chart holds \(Q\) fixed. Replacing \(Q\) by \(q(x)\) defines a different coordinate change and introduces chain-rule terms. Auxiliary parameters are held fixed unless their derivatives are explicitly included.
