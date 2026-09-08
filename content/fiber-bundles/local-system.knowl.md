+++
id = "fiber-bundles/local-system"
title = "Local system"
kind = "definition"
summary = "A locally constant sheaf, equivalently on a suitable space a representation of its fundamental groupoid."
aliases = ["locally constant sheaf"]
domains = ["fiber-bundles", "topology", "langlands"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/sheaf", "algebra-rings/ring", "algebra-modules/module", "topology/topological-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(R\) be a ring. A **local system** of \(R\)-modules on a [[topology/topological-space|topological space]] \(X\) is a
[[algebraic-geometry-foundations/sheaf|sheaf]] \(\mathcal L\) of \(R\)-modules
that is locally isomorphic to a constant sheaf of \(R\)-modules; equivalently, around each point its sections are locally constant functions with values in a fixed \(R\)-module \(L\), with pointwise module operations and restriction maps given by restricting functions. More generally, a local system
may take values in sets, groups, vector spaces, or another category.

## Monodromy

On a path-connected, locally path-connected, and semilocally simply connected
space, choosing \(x\in X\) identifies local systems with fixed fiber module \(L\) with
representations
\[
\pi_1(X,x)\longrightarrow \operatorname{Aut}_R(L),
\]
up to isomorphism of the fiber module. If \(L\cong R^r\) is finite free, this automorphism group is \(GL_r(R)\).

## Fundamental-groupoid form

Without choosing a base point, parallel continuation gives a functor from the
fundamental groupoid of \(X\). This formulation handles disconnected spaces
and makes transport along paths intrinsic.

## Relation to flat bundles

On a smooth manifold, a finite-rank complex local system determines a [[fiber-bundles/vector-bundle|vector bundle]] with a
[[fiber-bundles/flat-vector-bundle-connection|flat connection]]. Conversely,
horizontal sections of a flat bundle form a local system. This analytic
correspondence should not be confused with the algebraic de Rham formulation
of a [[langlands/g-local-system|\(G\)-local system]].

## References

1. Alexander Grothendieck, *Revêtements étales et groupe fondamental (SGA 1)*,
   Lecture Notes in Mathematics 224, Springer, 1971.
   [DOI](https://doi.org/10.1007/BFb0058656).
