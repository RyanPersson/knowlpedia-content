+++
id = "discrete-structures/directed-path"
title = "Directed path"
kind = "definition"
summary = "A finite sequence of vertices joined by edges in their prescribed direction."
aliases = ["directed walk"]
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/directed-graph", "shared-foundations/function", "shared-foundations/natural-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **directed path of length \(k\)** in a [[discrete-structures/directed-graph|directed graph]] is a sequence \(v_0,\ldots,v_k\) with \(v_{j-1}\to v_j\) for \(1\le j\le k\). A length-zero path consists of a single vertex.

## Convention and reachability

Here repeated vertices are permitted; some texts call this a directed walk and reserve “path” for sequences with no repeated vertices. A path with no repeated vertices is called simple. A vertex \(v\) is reachable from \(u\) if a directed path starts at \(u\) and ends at \(v\). Paths with matching endpoints can be concatenated.
