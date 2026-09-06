+++
id = "topology/continuous-on-compact-bounded-corollary"
title = "Continuous function on a compact set is bounded"
kind = "knowl"
summary = "Continuous functions on compact domains have finite upper and lower bounds"
aliases = ["continuous-on-compact-bounded-corollary", "Continuous function on a compact set is bounded"]
domains = ["topology"]
prerequisites = ["topology/compact-set", "topology/continuous-map", "topology/continuous-attains-max-min-compact"]
dependency_review_count = 1
legacy_source_path = "topology/continuous-on-compact-bounded-corollary.md"
+++

**Corollary**: Let \((X,d)\) be a [[topology/compact-set|compact]] [[topology/metric-space|metric space]] and let \(f:X\to\mathbb{R}\) be a [[topology/continuous-map|continuous map]]. Then \(f\) is bounded: there exists \(M<\infty\) such that \(|f(x)|\le M\) for all \(x\in X\).

## Remarks

**Connection to parent theorem**:
By the [[topology/continuous-attains-max-min-compact|extreme-value theorem]], \(f\) attains a maximum \(M_+\) and a minimum \(M_-\). Then \(|f(x)|\le \max\{|M_+|,|M_-|\}\).
