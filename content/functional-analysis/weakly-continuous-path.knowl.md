+++
id = "functional-analysis/weakly-continuous-path"
title = "Weakly continuous path"
kind = "definition"
summary = "A time-dependent vector whose value under every continuous linear functional depends continuously on time."
aliases = []
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/weak-topology", "functional-analysis/topological-dual", "topology/continuous-map", "real-analysis/interval"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(I\) be a real [[real-analysis/interval|interval]] and \(X\) a topological vector space. A map \(u:I\to X\) is **weakly continuous**, written \(u\in C_w(I;X)\), if it is [[topology/continuous-map|continuous]] for the [[functional-analysis/weak-topology|weak topology]] on \(X\). Equivalently, \(t\mapsto\ell(u(t))\) is continuous for every \(\ell\) in the [[functional-analysis/topological-dual|continuous dual]] \(X'\).

## Hilbert spaces

For a Hilbert space this means continuity of \(t\mapsto\langle u(t),v\rangle\) for every fixed \(v\). It specifies a value at every time, unlike an equivalence class in a time Lebesgue space. Weak continuity need not imply norm continuity.
