+++
id = "topology/contractible-space"
title = "Contractible space"
kind = "definition"
summary = "A space whose identity map is homotopic to a constant map."
aliases = ["contractible", "contraction"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "topology/homotopy"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A [[topology/topological-space|topological space]] \(X\) is **contractible** if there exist a point \(x_0\in X\) and a [[topology/homotopy|homotopy]]
\[
H:X\times[0,1]\to X,\qquad H(x,0)=x,\quad H(x,1)=x_0
\]
for every \(x\in X\). Thus the identity map of \(X\) is homotopic to a constant map. The homotopy is not required to keep \(x_0\) fixed at intermediate times.

## Examples and scope

Every nonempty convex subset of \(\mathbb R^n\) is contractible: choose \(x_0\) in it and use \(H(x,t)=(1-t)x+tx_0\). A one-point space is contractible. The empty space is not contractible under this convention, because no point \(x_0\) exists.

Contractibility is a property of the space with its given topology; an ambient deformation that leaves the space is not a contraction of that space.
