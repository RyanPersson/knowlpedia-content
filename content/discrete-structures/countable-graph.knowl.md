+++
id = "discrete-structures/countable-graph"
title = "Countable graph"
kind = "definition"
summary = "A graph whose vertex set is finite or countably infinite."
aliases = []
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/graph-vertex-edge", "shared-foundations/countable-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **countable graph** is a [[discrete-structures/graph-vertex-edge|graph]] whose vertex set is [[shared-foundations/countable-set|countable]], meaning finite or countably infinite. Its vertices can therefore be processed in a finite list or a sequence \(v_1,v_2,\ldots\) containing each vertex exactly once.

## Sequential constructions

For a simple graph on a countable vertex set, the edge set is countable too, since edges are unordered pairs of distinct vertices. Countability supports sequential choices such as greedy coloring. It does not bound the degree: a vertex may have infinitely many neighbors.
