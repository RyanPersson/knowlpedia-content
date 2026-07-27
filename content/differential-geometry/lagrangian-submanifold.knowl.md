+++
id = "differential-geometry/lagrangian-submanifold"
title = "Lagrangian submanifold"
kind = "definition"
summary = "A half-dimensional submanifold on which the ambient symplectic form vanishes."
aliases = ["Lagrangian embedding", "maximal isotropic submanifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]] of dimension \(2n\). An [[differential-geometry/embedded-submanifold|embedded submanifold]] \(L\subset M\) is a **Lagrangian submanifold** if \(\dim L=n\) and the pullback of \(\omega\) along the inclusion \(i:L\hookrightarrow M\) vanishes:
\[
i^*\omega=0.
\]
Equivalently, every [[differential-geometry/tangent-space|tangent space]] \(T_xL\) is a [[differential-geometry/lagrangian-subspace|Lagrangian subspace]] of the [[differential-geometry/symplectic-vector-space|symplectic vector space]] \(T_xM\). A Lagrangian embedding is an embedding \(f:L\to M\) with \(f^*\omega=0\) and \(\dim L=\frac12\dim M\).
The vanishing condition is pointwise: every pair of tangent vectors to the submanifold has zero symplectic pairing. Both vanishing and the half-dimension condition are essential.

## Equivalent formulations

An \(n\)-dimensional submanifold of a \(2n\)-dimensional symplectic manifold is Lagrangian exactly when it is [[differential-geometry/isotropic-submanifold|isotropic]]. Equivalently,
\[
(T_xL)^\omega=T_xL
\]
for every \(x\in L\). The dimension hypothesis matters: lower-dimensional isotropic submanifolds are not Lagrangian, even though the symplectic form also restricts to zero on them.

## Standard local model

The [[fiber-bundles/zero-section|zero section]] of a [[fiber-bundles/cotangent-bundle|cotangent bundle]] \(T^*Q\), equipped with its canonical symplectic form, is Lagrangian. More generally, the graph of a one-form \(\alpha\) on \(Q\) is Lagrangian precisely when \(d\alpha=0\); it is the graph of \(df\) when \(\alpha\) is exact. The [[differential-geometry/lagrangian-neighborhood-theorem|Lagrangian neighborhood theorem]] says a neighborhood of any Lagrangian is symplectomorphic to a neighborhood of the zero section in \(T^*L\) [Cannas da Silva, §2.3](https://doi.org/10.1007/978-3-540-45330-7).

## Constructions and examples

The graph of a [[differential-geometry/symplectomorphism|symplectomorphism]] \(M\to N\) is Lagrangian in \(M^{-}\times N\), where \(M^{-}\) carries \(-\omega_M\). This converts [[differential-geometry/symplectic-map|symplectic maps]] into Lagrangian correspondences. A smooth curve in a symplectic surface is automatically Lagrangian. By contrast, a [[differential-geometry/symplectic-submanifold|symplectic submanifold]] of positive dimension cannot be Lagrangian because its restricted form is nondegenerate rather than zero.

## Conventions and scope

Some literature permits immersed Lagrangians, defining them by a Lagrangian immersion rather than an embedded image. Unless explicitly qualified, this knowl uses embedded submanifolds. “Maximal isotropic” here means maximal by dimension in a symplectic vector space; maximality by set inclusion without regularity assumptions is not a substitute for the smooth half-dimensional condition.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §2.3, Lagrangian submanifolds and the neighborhood theorem.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 3, Lagrangian submanifolds.
