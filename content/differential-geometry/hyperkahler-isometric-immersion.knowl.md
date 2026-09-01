+++
id = "differential-geometry/hyperkahler-isometric-immersion"
title = "Hyperkähler isometric immersion"
kind = "definition"
summary = "A triholomorphic map of hyperkähler manifolds that pulls the target metric back to the source metric."
aliases = ["strict hyperkähler isometric immersion", "hyper-Kähler isometric immersion"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/hyperkahler-manifold", "differential-geometry/triholomorphic-map", "differential-geometry/riemannian-isometric-immersion"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let
\[
(M,g_M,I_M,J_M,K_M),\qquad
(N,g_N,I_N,J_N,K_N)
\]
be [[differential-geometry/hyperkahler-manifold|hyperkähler manifolds]] with
specified ordered triples. A **hyperkähler isometric immersion** is a smooth
map \(f:M\to N\) satisfying
\[
f^*g_N=g_M
\]
and
\[
df\circ I_M=I_N\circ df,\qquad
df\circ J_M=J_N\circ df,\qquad
df\circ K_M=K_N\circ df.
\]
Thus it is both a
[[differential-geometry/triholomorphic-map|triholomorphic map]] and a
[[differential-geometry/riemannian-isometric-immersion|Riemannian isometric
immersion]]. No separate immersion hypothesis is needed, because the metric
pullback equation makes \(df\) injective.

## Kähler forms

Let \((\omega_M)_I,(\omega_M)_J,(\omega_M)_K\) and
\((\omega_N)_I,(\omega_N)_J,(\omega_N)_K\) be the corresponding Kähler
forms. The defining equations imply
\[
f^*(\omega_N)_I=(\omega_M)_I,\qquad
f^*(\omega_N)_J=(\omega_M)_J,\qquad
f^*(\omega_N)_K=(\omega_M)_K.
\]
Conversely, preservation of the metric and any two members of the ordered
triple implies preservation of the third, since \(K=IJ\).

## Isomorphisms

Hyperkähler isometric immersions compose. If \(f\) is a diffeomorphism, it is
a [[differential-geometry/hyperkahler-isometry|hyperkähler isometry]].
Allowing an \(SO(3)\)-rotation of the target triple gives the distinct notion
of a [[differential-geometry/rotating-hyperkahler-isometry|rotating
hyperkähler isometry]].

## References

1. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: Chapters 6–7, hypercomplex and hyperkähler structures.
2. Daniel Huybrechts, “Compact Hyperkähler Manifolds: Basic Results,” *Inventiones Mathematicae* 135 (1999), 63–113. [DOI record](https://doi.org/10.1007/s002220050280). Relevant: §1, hyperkähler metrics and induced complex structures.
