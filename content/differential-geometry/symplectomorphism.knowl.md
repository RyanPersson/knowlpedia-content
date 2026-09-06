+++
id = "differential-geometry/symplectomorphism"
title = "Symplectomorphism"
kind = "definition"
summary = "A diffeomorphism between symplectic manifolds that preserves their symplectic forms by pullback."
aliases = ["symplectic diffeomorphism"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-manifold", "fiber-bundles/diffeomorphism", "fiber-bundles/pullback-of-differential-forms", "differential-geometry/symplectic-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega_M)\) and \((N,\omega_N)\) be [[differential-geometry/symplectic-manifold|symplectic manifolds]]. A **symplectomorphism** from \(M\) to \(N\) is a [[fiber-bundles/diffeomorphism|diffeomorphism]] \(\varphi:M\to N\) satisfying
\[
\varphi^*\omega_N=\omega_M,
\]
where \(\varphi^*\) denotes [[fiber-bundles/pullback-of-differential-forms|pullback of differential forms]]. Equivalently, \(\varphi\) is an invertible [[differential-geometry/symplectic-map|symplectic map]]. Pointwise, its differential is a [[differential-geometry/linear-symplectomorphism|symplectic linear isomorphism]]:
\[
\omega_N(d\varphi_pu,d\varphi_pv)=\omega_M(u,v)
\]
for every \(p\in M\) and \(u,v\in T_pM\). Thus a symplectomorphism preserves the full symplectic form, not merely the topology, orientation, or associated volume.

## Group and local structure

The identity is a symplectomorphism, composites of symplectomorphisms are symplectomorphisms, and the inverse of a symplectomorphism is symplectic. Hence the self-symplectomorphisms of \((M,\omega)\) form the [[differential-geometry/symplectomorphism-group|symplectomorphism group]] \(\operatorname{Symp}(M,\omega)\). They are also the isomorphisms in the [[differential-geometry/category-of-symplectic-manifolds|category of symplectic manifolds]]. The [[differential-geometry/darboux-theorem-symplectic|symplectic Darboux theorem]] says every two symplectic manifolds of the same dimension are locally symplectomorphic, although global symplectomorphism can be obstructed.

## Dynamics

Whenever a Hamiltonian [[fiber-bundles/vector-field|vector field]] has a flow defined through time \(t\), its time-\(t\) map is a symplectomorphism. More generally, a vector field \(X\) generates local symplectomorphisms exactly when \(\mathcal L_X\omega=0\). [[differential-geometry/hamiltonian-flow|Hamiltonian flows]] are a distinguished subclass because \(\iota_X\omega\) is exact, not merely closed.

A path of self-symplectomorphisms beginning at the identity is a [[differential-geometry/symplectic-isotopy|symplectic isotopy]]. Its endpoint lies in \(\operatorname{Symp}_0(M,\omega)\); requiring an exact generating contraction form gives a [[differential-geometry/hamiltonian-isotopy|Hamiltonian isotopy]].

## Examples and non-examples

Every [[linear-algebra/linear-map|linear map]] \(A:\mathbb R^{2n}\to\mathbb R^{2n}\) satisfying \(A^{\mathsf T}JA=J\) is a symplectomorphism for the standard form. A dilation \(x\mapsto cx\) pulls the standard form back to \(c^2\omega\), so it is symplectic only when \(c^2=1\). An orientation-preserving, volume-preserving diffeomorphism in dimension greater than two need not preserve the symplectic form.

## Conventions and scope

In Hamiltonian mechanics, “canonical transformation” commonly means symplectomorphism, though conventions involving time-dependent or contact transformations may broaden the term.

## References

1. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: §1.1, symplectic manifolds, maps, and diffeomorphisms.
2. Vladimir I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: chapters on symplectic geometry and canonical transformations.
