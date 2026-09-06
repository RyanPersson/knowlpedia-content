+++
id = "differential-geometry/transverse-submanifolds"
title = "Transverse submanifolds"
kind = "definition"
summary = "Submanifolds whose tangent spaces together span the ambient tangent space at every intersection point."
aliases = ["transversely intersecting submanifolds", "transverse intersection"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/embedded-submanifold", "fiber-bundles/smooth-manifold", "linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(S\) and \(T\) be [[differential-geometry/embedded-submanifold|embedded submanifolds]] of a [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\). They are **transverse at \(p\in S\cap T\)** if
\[
T_pS+T_pT=T_pM.
\]
They are **transverse**, written \(S\pitchfork T\), if this condition holds at every point of \(S\cap T\). Equivalently, the [[linear-algebra/linear-map|linear map]] \(T_pS\oplus T_pT\to T_pM\), \((v,w)\mapsto v-w\), is surjective for each intersection point. Disjoint submanifolds are transverse by convention because there are no intersection points at which the condition can fail.

## Transverse intersection theorem

If \(S\pitchfork T\), then \(S\cap T\) is an embedded submanifold of \(M\) with
\[
T_p(S\cap T)=T_pS\cap T_pT
\]
and codimension \(\operatorname{codim}(S\cap T)=\operatorname{codim}S+\operatorname{codim}T\). Equivalently, its dimension is \(\dim S+\dim T-\dim M\).

## Examples and non-examples

The coordinate axes in \(\mathbb R^2\) meet transversely at the origin. The \(x\)-axis and the parabola \(y=x^2\) do not: at their intersection both [[fiber-bundles/tangent-space-at-a-point|tangent spaces]] are the \(x\)-axis, so their sum does not fill \(\mathbb R^2\).

## Conventions and scope

Transversality is a condition only along the actual intersection. It is stronger than the set-theoretic statement that the intersection has the expected dimension, and it is distinct from orthogonality: no metric is required.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 6, transversality and intersections.
2. V. Guillemin and A. Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [AMS DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 2, transversality and intersection theory.
