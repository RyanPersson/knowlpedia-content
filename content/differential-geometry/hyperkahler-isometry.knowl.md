+++
id = "differential-geometry/hyperkahler-isometry"
title = "Hyperkähler isometry"
kind = "definition"
summary = "A diffeomorphism of hyperkähler manifolds that preserves the metric and each member of the specified quaternionic triple."
aliases = ["hyper-Kähler isometry", "strict hyperkähler isometry"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/hyperkahler-manifold", "differential-geometry/triholomorphic-map", "differential-geometry/kahler-form", "differential-geometry/hyperkahler-isometric-immersion"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let
\[
(M,g_M,I_M,J_M,K_M),\qquad
(N,g_N,I_N,J_N,K_N)
\]
be [[differential-geometry/hyperkahler-manifold|hyperkähler manifolds]] with
specified ordered triples. A **hyperkähler isometry**, in the strict
ordered-triple sense, is a diffeomorphism \(f:M\to N\) such that
\[
f^*g_N=g_M
\]
and
\[
df\circ I_M=I_N\circ df,\qquad
df\circ J_M=J_N\circ df,\qquad
df\circ K_M=K_N\circ df.
\]
It is therefore both a Riemannian isometry and a [[differential-geometry/triholomorphic-map|triholomorphic map]]. Equivalently, it preserves the metric and each of the three [[differential-geometry/kahler-form|Kähler forms]].

It is equivalently a
[[differential-geometry/hyperkahler-isometric-immersion|hyperkähler
isometric immersion]] that is a diffeomorphism. Hyperkähler isometries are
the isomorphisms in the category with hyperkähler isometric immersions as
morphisms.

## Strict preservation

A Riemannian isometry of the underlying metrics need not fix a selected
ordered hyperkähler triple. An isometry that instead carries the triple to
one constant \(SO(3)\)-rotation is a
[[differential-geometry/rotating-hyperkahler-isometry|rotating hyperkähler
isometry]], a distinct definition. The unqualified term on this page always
means strict preservation.

## References

1. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: Chapter 7, parallel quaternionic triples and their Kähler forms.
2. Daniel Huybrechts, “Compact Hyperkähler Manifolds: Basic Results,” *Inventiones Mathematicae* 135 (1999), 63–113. [DOI record](https://doi.org/10.1007/s002220050280). Relevant: §1, hyperkähler structures and the sphere of induced complex structures.
