+++
id = "topology/connectedness-criteria-r"
title = "Connectedness criteria in R"
kind = "knowl"
summary = "Equivalent ways to recognize when a subset of the real line is connected."
aliases = ["connectedness-criteria-r", "Connectedness criteria in R"]
domains = ["topology"]
legacy_source_path = "topology/connectedness-criteria-r.md"
prerequisites = ["topology/connected-set", "real-analysis/interval", "topology/continuous-image-of-connected-set-is-connected"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Connectedness criteria in \(\mathbb{R}\).** Let \(E\subseteq\mathbb{R}\) have the subspace topology. The following are equivalent:

1. \(E\) is [[topology/connected-set|connected]].
2. \(E\) is an [[real-analysis/interval|interval]], with the empty set and one-point sets allowed.
3. \(E\) is order-convex: whenever \(a,b\in E\) and \(a<c<b\), one has \(c\in E\).

These criteria are all manifestations of the same phenomenon: in \(\mathbb{R}\), connectedness is completely controlled by order. They are often paired with [[topology/continuous-image-of-connected-set-is-connected|continuity preserves connectedness]] to pin down real-valued images.
