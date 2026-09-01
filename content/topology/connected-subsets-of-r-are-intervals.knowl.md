+++
id = "topology/connected-subsets-of-r-are-intervals"
title = "Connected subsets of R are intervals"
kind = "knowl"
summary = "A subset of the real line is connected exactly when it is an interval."
aliases = ["connected-subsets-of-r-are-intervals", "Connected subsets of R are intervals"]
domains = ["topology"]
prerequisites = ["topology/connected-set", "real-analysis/interval", "topology/continuous-image-of-connected-set-is-connected"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "topology/connected-subsets-of-r-are-intervals.md"
+++

**Connected subsets of \(\mathbb{R}\) are intervals:** View \(\mathbb{R}\) with its usual topology. If \(E\subseteq \mathbb{R}\) is [[topology/connected-set|connected]], then \(E\) is an [[real-analysis/interval|interval]]: whenever \(a,b\in E\) with \(a<b\) and \(c\in\mathbb{R}\) satisfies \(a<c<b\), one has \(c\in E\). Conversely, every interval in \(\mathbb{R}\) is connected.

This classification is frequently combined with [[topology/continuous-image-of-connected-set-is-connected|continuous images preserve connectedness]] to identify images of connected sets under real-valued continuous functions.

## Examples

The usual topology on \(\mathbb R\) is the topology induced by the standard metric \(d(x,y)=|x-y|\).
