+++
id = "discrete-structures/directed-cycle"
title = "Directed cycle"
kind = "definition"
summary = "A positive-length closed directed path with no repetitions except its common initial and final vertex."
aliases = []
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/directed-path"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **directed cycle** is a [[discrete-structures/directed-path|directed path]] \(v_0,\ldots,v_k\), \(k\ge1\), such that \(v_k=v_0\) and \(v_0,\ldots,v_{k-1}\) are distinct. A loop is a cycle of length one.

## Closed paths

Every positive-length closed directed path contains a directed cycle: if vertices repeat before the final return, select a shortest positive closed subpath. Minimality excludes an internal repetition. Consequently, excluding directed cycles also excludes all positive-length paths from a vertex to itself.
