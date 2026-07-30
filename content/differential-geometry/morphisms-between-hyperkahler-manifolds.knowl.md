+++
id = "differential-geometry/morphisms-between-hyperkahler-manifolds"
title = "Morphisms between hyperkähler manifolds"
kind = "definition"
summary = "A convention guide separating hypercomplex maps, metric-preserving maps, and strict or rotating hyperkähler isomorphisms."
aliases = ["hyperkähler morphism conventions", "maps of hyperkähler manifolds", "hyper-Kähler morphisms"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
+++

A [[differential-geometry/hyperkahler-manifold|hyperkähler manifold]]
\[
(M,g,I,J,K)
\]
combines an ordered hypercomplex triple, a Riemannian metric, and three Kähler forms. There is no single universally intended meaning of **hyperkähler morphism**; the preserved data must be stated.

The house category on this page uses triholomorphic maps, preserving the
specified ordered triple. Whenever the metric must also be preserved, this
corpus says **strict hyperkähler isometric immersion** or **strict
hyperkähler isometry** explicitly.

## Common choices

1. A [[differential-geometry/triholomorphic-map|triholomorphic map]] preserves the ordered triple:
   \[
   df\circ I_M=I_N\circ df,\quad
   df\circ J_M=J_N\circ df,\quad
   df\circ K_M=K_N\circ df.
   \]
   It need not preserve the metric. These maps form the natural category after retaining the hypercomplex structures and forgetting the metrics.

2. A **strict hyperkähler isometric immersion** is triholomorphic and satisfies \(f^*g_N=g_M\). It consequently pulls back each target Kähler form to its corresponding source form. These maps compose and may have positive codimension.

3. A [[differential-geometry/hyperkahler-isometry|strict hyperkähler isometry]] is a strict hyperkähler isometric immersion that is a diffeomorphism. Such isometries are the arrows of the maximal strict groupoid.

4. A **rotating hyperkähler isometry** is allowed to carry the ordered triple to one constant \(SO(3)\)-rotation of the target triple. These isometries form a broader groupoid when the rotation is remembered; they are not strict morphisms unless the rotation is the identity.

## Structures that should not be conflated

A map holomorphic only for \(I\) need not preserve \(J\) or \(K\). A triholomorphic map need not preserve \(g\). A Riemannian isometry need not fix the selected ordered triple. Finally, a map preserving only the rank-three bundle
\[
Q=\operatorname{span}_{\mathbb R}\{I,J,K\}
\]
belongs naturally to quaternionic rather than strict hypercomplex geometry.

Accordingly, categorical statements use triholomorphic maps for the house
category, strict isometries for the ordered-triple groupoid, or rotating
isometries for its explicitly enlarged version.

## References

1. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: Chapters 6–7, hypercomplex and hyperkähler structures.
2. Simon Salamon, “Quaternionic Kähler Manifolds,” *Inventiones Mathematicae* 67 (1982), 143–171. [EuDML record](https://eudml.org/doc/142941). Relevant: the distinction between chosen hypercomplex triples and quaternionic structures.
