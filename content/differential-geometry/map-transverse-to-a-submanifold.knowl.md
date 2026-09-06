+++
id = "differential-geometry/map-transverse-to-a-submanifold"
title = "Map transverse to a submanifold"
kind = "definition"
summary = "A smooth map whose differential and the submanifold tangent space span the target at every inverse-image point."
aliases = ["transversality to a submanifold", "f transverse to S"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-map", "fiber-bundles/smooth-manifold", "differential-geometry/embedded-submanifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(f:M\to N\) be a [[fiber-bundles/smooth-map|smooth map]] between finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]] without boundary, and let \(S\subseteq N\) be an [[differential-geometry/embedded-submanifold|embedded submanifold]]. The map \(f\) is **transverse to \(S\) at \(x\in M\)**, written \(f\pitchfork_xS\), if either \(f(x)\notin S\), or
\[
df_x(T_xM)+T_{f(x)}S=T_{f(x)}N.
\]
It is **transverse to \(S\)**, written \(f\pitchfork S\), if it is transverse at every \(x\in M\). Equivalently, \(f\) and the inclusion \(S\hookrightarrow N\) are [[differential-geometry/transverse-smooth-maps|transverse smooth maps]].

## Normal-space formulation

At \(x\in f^{-1}(S)\), compose the [[fiber-bundles/differential-of-a-smooth-map|differential]] \(df_x:T_xM\to T_{f(x)}N\) with the quotient map to \(T_{f(x)}N/T_{f(x)}S\). Transversality is equivalent to surjectivity of this composite. This says that \(f\) supplies every direction normal to \(S\), even though \(df_x\) need not be surjective onto all of \(T_{f(x)}N\).

## Preimage theorem

If \(f\pitchfork S\), then \(f^{-1}(S)\) is an embedded submanifold of \(M\), with
\[
T_xf^{-1}(S)=(df_x)^{-1}(T_{f(x)}S)
\]
and codimension equal to \(\operatorname{codim}_N S\). This is the transverse-preimage theorem.

## Examples and non-examples

Every submersion is transverse to every embedded submanifold of its target. A constant map whose value lies in a positive-codimension submanifold is not transverse, because its differential contributes no normal directions. A map whose image misses \(S\) is transverse by the vacuous clause.

## Conventions and scope

Some authors state the condition only at points of \(f^{-1}(S)\); declaring it automatic elsewhere yields the same global notion. Boundary and corner versions require additional compatibility conditions not included here.

## References

1. M. W. Hirsch, *Differential Topology*, Springer, 1976. [Springer DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 3, transversality and the inverse-image theorem.
2. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 6, transversality.
