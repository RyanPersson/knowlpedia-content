+++
id = "probability/bernoulli-distribution"
title = "Bernoulli distribution"
kind = "definition"
summary = "The distribution on zero and one with a specified probability of one."
aliases = ["Bernoulli distribution", "Bernoulli law"]
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/probability-mass-function"]
dependency_heuristic = "probability-foundations-review-v1"
dependency_review_count = 1
+++

For \(\theta\in[0,1]\), the **Bernoulli distribution** \(\operatorname{Bernoulli}(\theta)\) is the distribution on \(\{0,1\}\) with [[probability/probability-mass-function|probability mass function]]
\[
p(1)=\theta,\qquad p(0)=1-\theta.
\]

## Interpretation

The value one denotes success and zero denotes failure. The indicator of an event of probability \(\theta\) has this distribution, including the deterministic cases \(\theta=0\) and \(\theta=1\).

## Moments

If \(X\) has this law, its [[probability/expectation|expectation]] is \(\theta\) and its [[probability/variance|variance]] is \(\theta(1-\theta)\).
