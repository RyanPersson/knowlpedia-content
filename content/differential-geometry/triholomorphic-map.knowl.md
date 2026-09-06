+++
id = "differential-geometry/triholomorphic-map"
title = "Triholomorphic map"
kind = "definition"
summary = "A smooth map between hypercomplex manifolds that preserves each member of the ordered quaternionic triple."
aliases = ["hypercomplex map", "triholomorphic morphism"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/hypercomplex-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,I_M,J_M,K_M)\) and \((N,I_N,J_N,K_N)\) be [[differential-geometry/hypercomplex-manifold|hypercomplex manifolds]]. A **triholomorphic map** is a smooth map \(f:M\to N\) satisfying
\[
\begin{aligned}
df\circ I_M&=I_N\circ df,\\
df\circ J_M&=J_N\circ df,\\
df\circ K_M&=K_N\circ df.
\end{aligned}
\]
Thus \(f\) is holomorphic for each member of the specified ordered triples. Because \(K=IJ\), any two of these equations imply the third, but writing all three makes the symmetry and convention explicit.

The equation also holds for every induced complex structure
\[
L=aI+bJ+cK,\qquad a^2+b^2+c^2=1,
\]
using the same coefficients on source and target. Identities and composites are triholomorphic, so hypercomplex manifolds with ordered triples and triholomorphic maps form a category.

## Metric independence

Triholomorphicity does not require a metric. Between
[[differential-geometry/hyperkahler-manifold|hyperkähler manifolds]], a
triholomorphic map need not preserve the hyperkähler metrics or two-forms.
Adding the pullback equation \(f^*g_N=g_M\) makes it a
[[differential-geometry/hyperkahler-isometric-immersion|hyperkähler
isometric immersion]]; if it is also a diffeomorphism, it is a
[[differential-geometry/hyperkahler-isometry|hyperkähler isometry]].

## Convention warning

The ordered triples matter. A
[[differential-geometry/rotating-hyperkahler-isometry|rotating hyperkähler
isometry]] with nontrivial rotation is not triholomorphic under this strict
definition.

## References

1. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: Chapters 6–7, hypercomplex and hyperkähler structures.
2. Daniel Huybrechts, “Compact Hyperkähler Manifolds: Basic Results,” *Inventiones Mathematicae* 135 (1999), 63–113. [DOI record](https://doi.org/10.1007/s002220050280). Relevant: §1, induced complex structures and hyperkähler data.
