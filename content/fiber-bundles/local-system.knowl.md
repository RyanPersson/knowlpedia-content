+++
id = "fiber-bundles/local-system"
title = "Local system"
kind = "definition"
summary = "A locally constant sheaf, equivalently on a suitable space a representation of its fundamental groupoid."
aliases = ["locally constant sheaf"]
domains = ["fiber-bundles", "topology", "langlands"]
section_mode = "progressive"
+++

A **local system** of \(R\)-modules on a topological space \(X\) is a
[[algebraic-geometry-foundations/sheaf|sheaf]] \(\mathcal L\) of \(R\)-modules
that is locally isomorphic to a constant sheaf. More generally, a local system
may take values in sets, groups, vector spaces, or another category.

On a path-connected, locally path-connected, and semilocally simply connected
space, choosing \(x\in X\) identifies finite-rank local systems with
representations
\[
\pi_1(X,x)\longrightarrow GL(\mathcal L_x),
\]
up to change of basis.

## Fundamental-groupoid form

Without choosing a base point, parallel continuation gives a functor from the
fundamental groupoid of \(X\). This formulation handles disconnected spaces
and makes transport along paths intrinsic.

## Relation to flat bundles

A finite-rank complex local system determines a [[fiber-bundles/vector-bundle|vector bundle]] with a
[[fiber-bundles/flat-vector-bundle-connection|flat connection]]. Conversely,
horizontal sections of a flat bundle form a local system. This analytic
correspondence should not be confused with the algebraic de Rham formulation
of a [[langlands/g-local-system|\(G\)-local system]].

## References

1. Alexander Grothendieck, *Revêtements étales et groupe fondamental (SGA 1)*,
   Lecture Notes in Mathematics 224, Springer, 1971.
   [DOI](https://doi.org/10.1007/BFb0058656).
