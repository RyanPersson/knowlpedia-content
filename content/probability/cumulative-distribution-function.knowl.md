+++
id = "probability/cumulative-distribution-function"
title = "Cumulative distribution function"
kind = "definition"
summary = "The function assigning to each real threshold the probability of a value at or below it."
aliases = ["cumulative distribution function", "CDF"]
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/probability-measure"]
dependency_heuristic = "probability-foundations-review-v1"
dependency_review_count = 1
+++

The **cumulative distribution function** of a [[probability/probability-measure|probability measure]] \(P\) on \(\mathbb R\) is
\[
F:\mathbb R\to[0,1],\qquad F(t)=P(({-\infty},t]).
\]

## Random variables

For a real-valued [[probability/random-variable|random variable]] \(X\), this is the cumulative distribution function of its [[probability/distribution-law|law]]: \(F_X(t)=\mathbb P(X\le t)\).

## Properties

The function is nondecreasing and right-continuous, with limits zero at \(-\infty\) and one at \(+\infty\). It determines the measure through \(P((a,b])=F(b)-F(a)\) for \(a<b\).

## Masses and densities

For a [[probability/probability-mass-function|mass function]] on a countable subset of \(\mathbb R\), \(F(t)=\sum_{x\le t}p(x)\). If \(P\) has a [[probability/probability-density-function|density]] \(f\), then \(F(t)=\int_{-\infty}^t f(x)\,dx\). A cumulative distribution function exists even when neither representation applies.
