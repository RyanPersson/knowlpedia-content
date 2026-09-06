+++
id = "differential-geometry/isotropic-submanifold"
title = "Isotropic submanifold"
kind = "definition"
summary = "An immersed submanifold on which the ambient symplectic form pulls back to zero."
aliases = ["isotropic immersed submanifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/symplectic-manifold", "fiber-bundles/smooth-immersion", "differential-geometry/isotropic-subspace", "differential-geometry/symplectic-vector-space", "differential-geometry/tangent-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]]. A [[fiber-bundles/smooth-immersion|smooth immersion]] \(\iota:L\to M\) is an **isotropic submanifold** if
\[
\iota^*\omega=0.
\]
Equivalently, for every \(p\in L\), the image \(d\iota_p(T_pL)\) is an [[differential-geometry/isotropic-subspace|isotropic subspace]] of the [[differential-geometry/symplectic-vector-space|symplectic vector space]] \(T_{\iota(p)}M\). When \(L\subseteq M\) is embedded, \(\iota\) is the inclusion and the condition says \(\omega_p(u,v)=0\) for all \(u,v\in T_pL\). The definition concerns the pullback to \(L\); self-intersections of an isotropic immersion do not alter it.

## Dimension bound and the Lagrangian case

If \(\dim M=2n\), isotropic linear algebra gives
\[
\dim L\leq n.
\]
An isotropic submanifold of dimension \(n\) is Lagrangian. Thus isotropic submanifolds range from curves, which are automatically isotropic, up to the maximal half-dimensional case. The zero pullback condition is much stronger than the automatic identity \(\omega(v,v)=0\) for an individual tangent vector.

## Examples and non-examples

Every immersed curve in a symplectic manifold is isotropic because a two-form vanishes on a one-dimensional [[differential-geometry/tangent-space|tangent space]]. In standard \(\mathbb R^{2n}\) with coordinates \((q_i,p_i)\), the coordinate submanifold
\[
\{p_1=\cdots=p_n=0,\ q_{k+1}=\cdots=q_n=0\}
\]
is isotropic of dimension \(k\leq n\).

By contrast, an open subset of a positive-dimensional symplectic manifold is not isotropic: its pulled-back form remains nondegenerate rather than vanishing. A surface in a symplectic four-manifold is isotropic exactly when it is Lagrangian.

## Immersed versus embedded terminology

Some authors say “isotropic immersion” for the map \(\iota\) and reserve “isotropic submanifold” for an embedded image. The defining equation is the same. When an immersed image has self-intersections, tangent planes coming from different preimages need not be mutually symplectically orthogonal; only each individual tangent plane must be isotropic.

## References

1. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [Oxford DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: §3.3, isotropic and Lagrangian submanifolds.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008. [Chapter DOI record](https://doi.org/10.1007/978-3-540-45330-7_3). Relevant: “Lagrangian Submanifolds,” pp. 17–23.
