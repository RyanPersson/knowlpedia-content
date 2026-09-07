+++
id = "probability/probability-mass-function"
title = "Probability mass function"
kind = "definition"
summary = "The point probabilities of a probability measure on a countable state space."
aliases = ["mass function", "probability mass function", "PMF"]
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/probability-measure", "shared-foundations/countable-set"]
dependency_heuristic = "probability-foundations-review-v1"
dependency_review_count = 1
+++

The **probability mass function** of a [[probability/probability-measure|probability measure]] \(P\) on a [[shared-foundations/countable-set|countable set]] \(S\), equipped with all its subsets, is the function
\[
p:S\to[0,1],\qquad p(x)=P(\{x\}).
\]

## Characterization

The masses satisfy \(\sum_{x\in S}p(x)=1\), and \(P(A)=\sum_{x\in A}p(x)\) for every \(A\subseteq S\). Conversely, any nonnegative function on \(S\) whose sum is one defines a probability measure by this formula.

For a [[probability/random-variable|random variable]] \(X\) taking values in \(S\), its mass function is that of its [[probability/distribution-law|law]]: \(p_X(x)=\mathbb P(X=x)\).

## Example

A [[probability/bernoulli-distribution|Bernoulli distribution]] with parameter \(\theta\) has masses \(p(1)=\theta\) and \(p(0)=1-\theta\).

## Mass versus density

A mass is a point probability. A [[probability/probability-density-function|density with respect to Lebesgue measure]] gives probabilities by integration, not by evaluating the density at a point.
