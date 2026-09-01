+++
id = "differential-geometry/rotating-hyperkahler-isometry"
title = "Rotating hyperkähler isometry"
kind = "definition"
summary = "A Riemannian isometry that carries one specified hyperkähler triple to a constant SO(3)-rotation of the other."
aliases = ["rotating hyper-Kähler isometry", "SO(3)-rotating hyperkähler isometry"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/hyperkahler-manifold"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let
\[
(M,g_M,(J_M)_1,(J_M)_2,(J_M)_3),\qquad
(N,g_N,(J_N)_1,(J_N)_2,(J_N)_3)
\]
be [[differential-geometry/hyperkahler-manifold|hyperkähler manifolds]] with
specified ordered triples. A **rotating hyperkähler isometry** is a
Riemannian isometry \(f:M\to N\) for which there is a constant matrix
\(A=(A_{ba})\in SO(3)\) satisfying
\[
df\circ (J_M)_a
=\sum_{b=1}^3 A_{ba}(J_N)_b\circ df
\qquad(a=1,2,3).
\]
For disconnected manifolds, the rotation may instead be specified separately
and constantly on each connected component.

## Kähler-form formulation

If \((\omega_M)_a\) and \((\omega_N)_b\) are the three [[differential-geometry/kahler-form|Kähler forms]], the
definition is equivalently
\[
f^*(\omega_N)_b
=\sum_{a=1}^3 A_{ba}(\omega_M)_a.
\]
The matrix is orientation-preserving because it must respect quaternion
multiplication on the sphere of induced complex structures.

Rotating hyperkähler isometries compose, with their rotation matrices
composing. The special case \(A=I_3\) is a
[[differential-geometry/hyperkahler-isometry|hyperkähler isometry]] in the
strict ordered-triple sense.

## Distinction from metric isometries

A Riemannian isometry of the underlying metrics need not preserve the
parallel three-plane spanned by \(I,J,K\), so it need not be rotating
hyperkähler. Conversely, a rotating isometry with \(A\ne I_3\) is not
[[differential-geometry/triholomorphic-map|triholomorphic]] for the specified
ordered triples.

## References

1. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: Chapter 7, parallel quaternionic triples and their Kähler forms.
2. Daniel Huybrechts, “Compact Hyperkähler Manifolds: Basic Results,” *Inventiones Mathematicae* 135 (1999), 63–113. [DOI record](https://doi.org/10.1007/s002220050280). Relevant: §1, hyperkähler structures and the sphere of induced complex structures.
