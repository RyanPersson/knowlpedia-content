+++
id = "probability/event-probability"
title = "Probability of an event"
kind = "knowl"
summary = "The number assigned by a probability measure to an event."
aliases = ["event-probability", "Probability of an event"]
domains = ["probability"]
prerequisites = ["probability/probability-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "probability/event-probability.md"
+++

Let \((\Omega,\mathcal F,\mathbb P)\) be a [[probability/probability-space|probability space]]. The **probability of an event** \(A\in\mathcal F\) is the number \(\mathbb P(A)\in[0,1]\).

## Remarks

Because events are [[measure-theory/measurable-set|measurable sets]] and \(\mathbb P\) is a [[probability/probability-measure|probability measure]], event probabilities are countably additive on pairwise disjoint events, with \(\mathbb P(\varnothing)=0\) and \(\mathbb P(\Omega)=1\).

## Examples

- In a fair coin-toss space, the event \(A=\{H\}\) has probability \(\mathbb P(A)=1/2\).
- Under the uniform probability measure on \([0,1]\), the event \(A=[0,1/2]\) has probability \(\mathbb P(A)=1/2\).
