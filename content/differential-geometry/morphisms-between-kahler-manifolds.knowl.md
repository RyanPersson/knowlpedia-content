+++
id = "differential-geometry/morphisms-between-kahler-manifolds"
title = "Morphisms between Kähler manifolds"
kind = "definition"
summary = "A convention guide separating holomorphic maps, Kähler immersions, and strict Kähler isomorphisms."
aliases = ["Kähler morphism conventions", "maps of Kähler manifolds"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
+++

A [[differential-geometry/kahler-manifold|Kähler manifold]] carries three compatible kinds of data: a complex structure \(J\), a Riemannian metric \(g\), and a symplectic form
\[
\omega(X,Y)=g(JX,Y).
\]
The phrase **morphism of Kähler manifolds** is not unambiguous until one states which of these data the map must preserve.

On this page, the house category of Kähler manifolds uses holomorphic maps as
morphisms: Kählerness is a property of each object, while only the complex
structures are required to be preserved. Metric-preserving maps are always
called Kähler immersions or strict Kähler isomorphisms.

## Three standard levels

Let \(f:(M,J_M,g_M)\to(N,J_N,g_N)\) be smooth.

1. A **holomorphic map** satisfies
   \[
   df\circ J_M=J_N\circ df.
   \]
   It preserves the complex structures but need not preserve either metric or Kähler form. Kähler manifolds with these maps form the category obtained by forgetting the metrics.

2. A **Kähler immersion** or [[differential-geometry/holomorphic-isometric-immersion|holomorphic isometric immersion]] additionally satisfies
   \[
   f^*g_N=g_M.
   \]
   Equivalently, for a holomorphic map, it satisfies \(f^*\omega_N=\omega_M\). Such maps are both Riemannian isometric immersions and symplectic maps, and they compose.

3. A **strict Kähler isomorphism** is a Kähler immersion that is a diffeomorphism. It is simultaneously a [[differential-geometry/biholomorphism|biholomorphism]], a Riemannian isometry, and a [[differential-geometry/symplectomorphism|symplectomorphism]]. These maps form the maximal subgroupoid for the strict structure-preserving convention.

## Why there is no single default

A constant map is holomorphic but cannot be an isometric immersion from a positive-dimensional source. Conversely, a symplectomorphism between the underlying symplectic manifolds need not be holomorphic. Requiring only a biholomorphism preserves the complex structure but allows the metric to change.

For this reason, a statement outside the declared house category that uses
“Kähler morphism” should replace it by one of the explicit levels above. The
strict immersion convention is useful when the metric and form are selected
data; the holomorphic house convention is natural when Kählerness is treated
as a property of the objects and only complex geometry is functorial.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §3.1, compatibility of complex, metric, and symplectic data.
2. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II*, Wiley, 1969. [Publisher record](https://www.wiley.com/en-us/Foundations+of+Differential+Geometry%2C+Volume+2-p-9780471157328). Relevant: Chapter IX, Kähler manifolds and transformations.
