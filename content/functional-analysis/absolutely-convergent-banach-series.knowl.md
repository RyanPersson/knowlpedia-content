+++
id = "functional-analysis/absolutely-convergent-banach-series"
title = "Absolutely convergent series in a Banach space"
kind = "theorem"
summary = "Summability of the norms ensures convergence of a vector-valued series in a complete normed space."
aliases = ["absolute convergence in a Banach space", "norm-summable series"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/banach-space", "real-analysis/series", "real-analysis/comparison-test"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If \(X\) is a [[linear-algebra/banach-space|Banach space]] and \(\sum_{n=0}^\infty\|x_n\|_X<\infty\), then \(\sum_nx_n\) converges in \(X\). Moreover,
\[
\left\|\sum_{n=N}^\infty x_n\right\|_X
\le\sum_{n=N}^\infty\|x_n\|_X.
\]

## Proof and operator series

The triangle inequality bounds differences of partial sums by tails of the scalar series, so the partial sums are Cauchy. Completeness supplies the limit, and continuity of the norm gives the tail bound. In particular this applies in a Banach space of bounded operators. Convergence can follow from summable bounds on powers of an operator even when its first power has norm at least one.
