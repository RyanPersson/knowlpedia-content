+++
id = "topology/simply-connected-space"
title = "Simply connected space"
kind = "definition"
summary = "A path-connected topological space with trivial fundamental group."
aliases = ["simply connected", "simple connectivity"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "topology/fundamental-group", "topology/path-connected-set"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

A [[topology/topological-space|topological space]] \(X\) is **simply connected** if it is nonempty and [[topology/path-connected-set|path-connected]] and, for one—and hence every—basepoint \(x_0\in X\), its [[topology/fundamental-group|fundamental group]] is trivial:
\[
\pi_1(X,x_0)=\{1\}.
\]

## Loop formulation

Equivalently, a nonempty path-connected space is simply connected if every loop in \(X\) can be continuously contracted to a constant loop while its basepoint remains fixed.

## Basepoint and hypotheses

Path-connectedness makes fundamental groups at different basepoints isomorphic, so the definition does not depend on the chosen point. No local path-connectedness or semilocal simple-connectivity hypothesis is part of the definition; those additional conditions enter standard existence and classification theorems for covering spaces.

## Examples

Nonempty convex subsets of real vector spaces, spheres \(S^n\) for \(n\geq2\), and Euclidean spaces are simply connected. The circle and punctured plane are not simply connected: each has fundamental group isomorphic to \(\mathbb Z\).

## References

1. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002. [Author-hosted text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf). Relevant: §1.1.
