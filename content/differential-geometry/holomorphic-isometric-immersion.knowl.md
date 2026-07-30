+++
id = "differential-geometry/holomorphic-isometric-immersion"
title = "Holomorphic isometric immersion"
kind = "definition"
summary = "A holomorphic map between Hermitian manifolds that pulls the target metric back to the source metric."
aliases = ["Kähler immersion", "Hermitian isometric immersion", "holomorphic Riemannian immersion"]
domains = ["differential-geometry", "complex-analysis"]
section_mode = "progressive"
+++

Let \((M,J_M,g_M)\) and \((N,J_N,g_N)\) be [[differential-geometry/hermitian-manifold|Hermitian manifolds]]. A **holomorphic isometric immersion** is a smooth map \(f:M\to N\) satisfying
\[
df\circ J_M=J_N\circ df
\qquad\text{and}\qquad
f^*g_N=g_M.
\]
The first equation says that \(f\) is [[differential-geometry/holomorphic-map|holomorphic]], while the second makes it a [[differential-geometry/riemannian-isometric-immersion|Riemannian isometric immersion]]. No separate immersion hypothesis is needed because the metric pullback equation makes \(df\) injective.

## Preservation of the fundamental form

Write
\[
\omega_M(X,Y)=g_M(J_MX,Y),\qquad
\omega_N(U,V)=g_N(J_NU,V).
\]
The two defining equations imply
\[
f^*\omega_N=\omega_M.
\]
Hence a holomorphic isometric immersion between [[differential-geometry/kahler-manifold|Kähler manifolds]] is also a [[differential-geometry/symplectic-map|symplectic map]]. Conversely, a holomorphic map between Kähler manifolds that pulls back \(\omega_N\) to \(\omega_M\) also pulls back \(g_N\) to \(g_M\). In this setting the terms **Kähler immersion** and holomorphic isometric immersion are commonly synonymous.

## Isomorphisms and near misses

If \(f\) is a diffeomorphism, it is a biholomorphic Riemannian isometry and therefore a strict isomorphism of the Kähler data. A holomorphic map alone need not preserve either metric or Kähler form. A Riemannian isometric immersion alone need not be holomorphic.

The definition is strict: a homothetic holomorphic immersion satisfying \(f^*g_N=cg_M\) for \(c\neq1\) is not isometric unless the metrics are rescaled.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §3.1, Hermitian metrics and Kähler forms.
2. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II*, Wiley, 1969. [Publisher record](https://www.wiley.com/en-us/Foundations+of+Differential+Geometry%2C+Volume+2-p-9780471157328). Relevant: Chapter IX, Hermitian and Kähler geometry.
