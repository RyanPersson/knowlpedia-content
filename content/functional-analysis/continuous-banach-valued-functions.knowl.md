+++
id = "functional-analysis/continuous-banach-valued-functions"
title = "Continuous Banach-valued functions on a compact space"
kind = "definition"
summary = "Continuous functions into a Banach space form a Banach space under the uniform norm."
aliases = ["C(K;X)", "uniform Banach function space"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/banach-space", "topology/compact-set", "topology/continuous-map", "real-analysis/supremum-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(K\) be a [[topology/compact-set|compact]] topological space and \(X\) a [[linear-algebra/banach-space|Banach space]]. The space \(C(K;X)\) of continuous maps is normed by
\[
\|u\|_{C(K;X)}=\sup_{t\in K}\|u(t)\|_X.
\]
It is complete. A uniformly Cauchy sequence has a limit at each point by completeness of \(X\); the same uniform Cauchy bound gives uniform convergence, and a uniform limit of continuous maps is continuous.

## Closed balls

A closed ball in this space is a complete metric space. An integral equation can therefore use such a ball as the domain of a contraction, provided the integral map is shown to preserve the ball and to have Lipschitz constant less than one. Completeness alone gives neither of these two bounds.
