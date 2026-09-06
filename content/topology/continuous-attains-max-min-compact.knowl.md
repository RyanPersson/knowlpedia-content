+++
id = "topology/continuous-attains-max-min-compact"
title = "Continuous attains max/min on compact set"
kind = "knowl"
summary = "A continuous real-valued function on a compact set achieves a maximum and a minimum"
aliases = ["continuous-attains-max-min-compact", "Continuous attains max/min on compact set"]
domains = ["topology"]
prerequisites = ["topology/compact-set", "topology/continuous-map", "topology/continuous-image-of-compact-set-is-compact"]
dependency_review_count = 1
legacy_source_path = "topology/continuous-attains-max-min-compact.md"
+++

**Extreme-value theorem.** Let \(K\) be a nonempty [[topology/compact-set|compact set]] and let \(f:K\to\mathbb R\) be [[topology/continuous-map|continuous]]. Then there exist \(x_{\min},x_{\max}\in K\) such that
\(f(x_{\min})\le f(x)\le f(x_{\max})\) for all \(x\in K\).

## Equivalent characterizations

Equivalently, the subset \(f(K)\subseteq\mathbb{R}\) has both a [[real-analysis/minimum|minimum]] and a [[real-analysis/maximum|maximum]].

## Remarks

This can be seen by combining [[topology/continuous-image-of-compact-set-is-compact|compactness of continuous images]] with basic order properties of compact subsets of \(\mathbb{R}\).
