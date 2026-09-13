+++
id = "discrete-structures/directed-graph"
title = "Directed graph"
kind = "definition"
summary = "A vertex set equipped with a specified set of ordered edges."
aliases = ["digraph"]
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["shared-foundations/ordered-pair", "shared-foundations/cartesian-product", "shared-foundations/set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **directed graph** is a pair \(G=(V,E)\) with \(E\subseteq V\times V\). An [[shared-foundations/ordered-pair|ordered edge]] \((u,v)\), written \(u\to v\), has source \(u\) and target \(v\). This convention allows loops and allows both \(u\to v\) and \(v\to u\); additional hypotheses can exclude them. There are no parallel copies of an edge when \(E\) is a set.

## Paths

[[discrete-structures/directed-path|Directed paths]] follow successive arrows; a [[discrete-structures/directed-cycle|directed cycle]] returns to its starting vertex. Edge orientation must be stated when the graph describes dependencies: “requires” and “is used by” give opposite conventions.
