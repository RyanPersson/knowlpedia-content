+++
id = "topology/extreme-value-theorem"
title = "Extreme value theorem"
kind = "theorem"
summary = "A continuous real-valued function on a nonempty compact set attains its maximum and minimum."
aliases = ["extreme-value-theorem", "Extreme value theorem"]
domains = ["topology"]
legacy_source_path = "topology/extreme-value-theorem.md"
prerequisites = ["topology/compact-set", "topology/continuous-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **extreme value theorem** states: if \(K\) is a nonempty
[[topology/compact-set|compact set]] and
\(f:K\to\mathbb R\) is a [[topology/continuous-map|continuous function]],
then \(f\) attains its maximum and minimum values.

That is, there exist \(x_{\max}, x_{\min} \in K\) such that
\[
f(x_{\min}) \leq f(x) \leq f(x_{\max}) \quad \text{for all } x \in K.
\]

## Classical version

If \(a\leq b\), every continuous function \(f:[a,b]\to\mathbb R\) attains
a maximum and a minimum on \([a,b]\).

## Why compactness matters

- The function \(f(x)=x\) on \((0,1)\) has neither a maximum nor a minimum.
- The function \(f(x)=x\) on \([1,\infty)\) has no maximum.
