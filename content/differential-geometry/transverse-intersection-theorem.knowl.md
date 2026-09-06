+++
id = "differential-geometry/transverse-intersection-theorem"
title = "Transverse intersection theorem"
kind = "theorem"
summary = "Transverse embedded submanifolds intersect in an embedded submanifold of the expected codimension."
aliases = ["intersection theorem for transverse submanifolds"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/embedded-submanifold", "fiber-bundles/smooth-manifold", "differential-geometry/transverse-submanifolds"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(S\) and \(T\) be [[differential-geometry/embedded-submanifold|embedded submanifolds]] of a finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\) without boundary. If \(S\) and \(T\) are [[differential-geometry/transverse-submanifolds|transverse]], then \(S\cap T\) is an embedded submanifold of \(M\). At every \(p\in S\cap T\),
\[
T_p(S\cap T)=T_pS\cap T_pT,
\]
\[
\operatorname{codim}_M(S\cap T)
=\operatorname{codim}_M S+\operatorname{codim}_M T.
\]
Equivalently, every nonempty component has dimension \(\dim S+\dim T-\dim M\).
No metric or orthogonality hypothesis is involved.

## Proof idea

Near an intersection point, choose defining coordinates for one submanifold. Restricting its normal-coordinate map to the other submanifold gives a submersion because transversality supplies every normal direction. The submersion level-set theorem then makes the common zero set an embedded submanifold. Its [[differential-geometry/tangent-space|tangent space]] is the kernel of the restricted differential, which is exactly \(T_pS\cap T_pT\).

## Consequences and examples

The coordinate axes in \(\mathbb R^2\) intersect transversely, so their intersection is the zero-dimensional submanifold \(\{0\}\). More generally, complementary-dimensional transverse submanifolds meet in a discrete submanifold.

The theorem also shows that every transverse intersection is a [[differential-geometry/clean-intersection|clean intersection]]. The converse fails: a proper embedded submanifold intersects itself cleanly but not transversely.

## Scope

The empty intersection is an embedded submanifold and satisfies the conclusion vacuously. For manifolds with boundary or corners, transversality in the ambient tangent spaces alone may not control the boundary strata; an appropriate stratified or neat version is required.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 6, transverse intersections.
2. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 2, transversality and intersection theory.
