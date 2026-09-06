+++
id = "convex-analysis/semialgebraic-set"
title = "Semialgebraic set"
kind = "knowl"
summary = "A subset of real affine space described by finitely many polynomial equalities and inequalities."
aliases = ["semialgebraic", "semialgebraic set"]
domains = ["convex-analysis", "algebraic-geometry-foundations"]
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A subset \(S\subseteq\mathbb R^n\) is **semialgebraic** if it can be obtained from finitely many sets of the form
\[
\{x:p(x)=0\}\quad\text{and}\quad\{x:q(x)>0\},
\]
where \(p,q\in\mathbb R[x_1,\ldots,x_n]\), using finitely many unions, intersections, and complements. Equivalently, membership in \(S\) is given by a finite Boolean combination of polynomial sign conditions.

Semialgebraic sets are closed under products, projections, closure, and taking connected components. They form the basic class of sets in real algebraic geometry.
