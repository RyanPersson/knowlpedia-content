+++
id = "topology/simply-connected-space"
title = "Simply connected space"
kind = "definition"
summary = "A path-connected topological space with trivial fundamental group."
aliases = ["simply connected", "simple connectivity"]
domains = ["topology"]
prerequisites = ["topology/topological-space", "topology/fundamental-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

A [[topology/topological-space|topological space]] \(X\) is **simply connected** if it is path-connected and, for one—and hence every—basepoint \(x_0\in X\), its [[topology/fundamental-group|fundamental group]] is trivial:
\[
\pi_1(X,x_0)=\{1\}.
\]
Equivalently, every loop in \(X\) can be continuously contracted to a constant loop while its basepoint remains fixed.

## Basepoint and hypotheses

Path-connectedness makes fundamental groups at different basepoints isomorphic, so the definition does not depend on the chosen point. No local path-connectedness or semilocal simple-connectivity hypothesis is part of the definition; those additional conditions enter standard existence and classification theorems for covering spaces.

## Examples

Convex subsets of real vector spaces, spheres \(S^n\) for \(n\geq2\), and Euclidean spaces are simply connected. The circle and punctured plane are not simply connected: each has fundamental group isomorphic to \(\mathbb Z\).

## References

1. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002. [Author-hosted text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf). Relevant: §1.1.
