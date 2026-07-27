+++
id = "differential-geometry/symplectic-map"
title = "Symplectic map"
kind = "definition"
summary = "A smooth map between symplectic manifolds that pulls the target symplectic form back to the source symplectic form."
aliases = ["symplectic morphism", "form-preserving smooth map"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,\omega_M)\) and \((N,\omega_N)\) be [[differential-geometry/symplectic-manifold|symplectic manifolds]]. A **symplectic map** is a [[fiber-bundles/smooth-map|smooth map]] \(f:M\to N\) such that
\[
f^*\omega_N=\omega_M,
\]
where \(f^*\omega_N\) is the [[fiber-bundles/pullback-of-differential-forms|pullback of the differential form]] \(\omega_N\). This definition does not require \(f\) to be injective, surjective, or a diffeomorphism. Nondegeneracy of \(\omega_M\) implies that \(d f_x:T_xM\to T_{f(x)}N\) is injective at every \(x\), so every symplectic map is a [[fiber-bundles/smooth-immersion|smooth immersion]] and necessarily \(\dim M\leq \dim N\).

## Basic consequences

The identity map is symplectic, and a composite of symplectic maps is symplectic by functoriality of pullback. If \(M\) and \(N\) have the same dimension, a symplectic map is a local diffeomorphism. A [[fiber-bundles/diffeomorphism|diffeomorphism]] satisfying the pullback equation is a [[differential-geometry/symplectomorphism|symplectomorphism]]; its inverse also preserves the symplectic forms.

These facts follow directly from the definition and the linear nondegeneracy argument in [Cannas da Silva, §1.1](https://doi.org/10.1007/978-3-540-45330-7).

## Examples and non-examples

The inclusion of a [[differential-geometry/symplectic-submanifold|symplectic submanifold]] with its restricted form is a symplectic map. A constant map from a positive-dimensional symplectic manifold is not symplectic, because its pullback of every positive-degree form vanishes. A diffeomorphism need not be symplectic: it must satisfy the displayed pullback identity, not merely preserve orientation or volume.

## Conventions and scope

**Warning.** Some authors use “symplectic map” only for a form-preserving diffeomorphism, making it synonymous with “symplectomorphism.” Here the term allows maps between manifolds of different dimensions and does not include bijectivity. Under this convention a [[differential-geometry/symplectic-embedding|symplectic embedding]] is a symplectic map that is also an embedding.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §§1.1–1.2, symplectic linear algebra and symplectic maps.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [Publisher record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 1, conventions for symplectic manifolds and maps.
