+++
id = "discrete-structures/support-intersection-graph"
title = "Support intersection graph"
kind = "definition"
summary = "The graph connecting distinct labels whose assigned support sets intersect."
aliases = ["overlap graph", "intersection graph"]
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/graph-vertex-edge", "shared-foundations/indexed-family-of-sets", "shared-foundations/intersection"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an [[shared-foundations/indexed-family-of-sets|indexed family of sets]] \((K_\gamma)_{\gamma\in\Gamma}\), its **intersection graph** has vertex set \(\Gamma\) and an edge between distinct labels \(\gamma,\gamma'\) exactly when
\[
K_\gamma\cap K_{\gamma'}\ne\varnothing.
\]
When the sets are supports, this is a **support intersection graph**. Enlarged supports may be used to account for later localization or differentiation.

## Checking a degree bound

A uniform bound on the number of sets through a point does not by itself bound this graph's degree. One large set may meet arbitrarily many mutually disjoint small sets. Degree estimates typically also require comparable diameters and separation of centers, as in a fixed mesh or finitely many neighboring scales. The edge rule must include every interaction that a subsequent coloring is intended to separate.
