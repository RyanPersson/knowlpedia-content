+++
id = "differential-geometry/hyperkahler-isometry"
title = "Hyperkähler isometry"
kind = "definition"
summary = "An isometry of hyperkähler manifolds, with strict and rotating conventions distinguished."
aliases = ["hyper-Kähler isometry", "rotating hyperkähler isometry"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let
\[
(M,g_M,I_M,J_M,K_M),\qquad
(N,g_N,I_N,J_N,K_N)
\]
be [[differential-geometry/hyperkahler-manifold|hyperkähler manifolds]] with specified ordered triples. A **strict hyperkähler isometry** is a diffeomorphism \(f:M\to N\) such that
\[
f^*g_N=g_M
\]
and
\[
df\circ I_M=I_N\circ df,\qquad
df\circ J_M=J_N\circ df,\qquad
df\circ K_M=K_N\circ df.
\]
It is therefore both a Riemannian isometry and a [[differential-geometry/triholomorphic-map|triholomorphic map]]. Equivalently, it preserves the metric and each of the three Kähler forms.

## Rotating convention

A broader **rotating hyperkähler isometry** is a Riemannian isometry for which there is one constant matrix \(A=(A_{ba})\in SO(3)\) satisfying
\[
df\circ (J_M)_a
=\sum_{b=1}^3 A_{ba}(J_N)_b\circ df,
\]
where \(((J)_1,(J)_2,(J)_3)=(I,J,K)\). Equivalently,
\[
f^*(\omega_N)_b
=\sum_{a=1}^3A_{ba}(\omega_M)_a.
\]
The matrix must be constant and orientation-preserving so that it respects the quaternion multiplication on the sphere of induced complex structures. The strict convention is the special case \(A=I_3\).

Rotating isometries compose, with their rotation matrices composing. They form a broader groupoid if the rotation is permitted as part of the morphism data. They are not morphisms in the strict ordered-triple groupoid unless their rotation is the identity.

## Scope warning

A Riemannian isometry of the underlying metrics is not automatically strict with respect to a chosen hyperkähler triple. Depending on the geometry, it may rotate the parallel three-plane, act more generally on parallel structures, or fail to preserve the selected triple. Every use of “hyperkähler isometry” should therefore declare whether strict or rotating preservation is intended.

## References

1. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: Chapter 7, parallel quaternionic triples and their Kähler forms.
2. Daniel Huybrechts, “Compact Hyperkähler Manifolds: Basic Results,” *Inventiones Mathematicae* 135 (1999), 63–113. [DOI record](https://doi.org/10.1007/s002220050280). Relevant: §1, hyperkähler structures and the sphere of induced complex structures.
