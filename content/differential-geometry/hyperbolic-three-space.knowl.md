+++
id = "differential-geometry/hyperbolic-three-space"
title = "Hyperbolic three-space"
kind = "definition"
summary = "The simply connected complete three-dimensional Riemannian manifold of constant sectional curvature −1."
aliases = ["hyperbolic 3-space", "H3", "three-dimensional hyperbolic space"]
domains = ["differential-geometry", "lie-groups"]
section_mode = "progressive"
+++

**Hyperbolic three-space** \(\mathbb H^3\) is the simply connected complete \(3\)-dimensional [[differential-geometry/riemannian-manifold|Riemannian manifold]] of constant sectional curvature \(-1\), unique up to isometry.

## Standard models

In the upper-half-space model,
\[
\mathbb H^3=\{(z,r):z\in\mathbb C,\ r>0\},
\qquad
ds^2=\frac{|dz|^2+dr^2}{r^2}.
\]
In the hyperboloid model, using the \((-+++)\) form fixed for [[linear-algebra/minkowski-vector-space|Minkowski space]],
\[
\mathbb H^3=\{v\in\mathbb R^{1,3}:q(v)=-1,\ t>0\},
\]
with Riemannian metric \(\eta\) restricted to tangent spaces.

A third model is the space of positive-definite Hermitian \(2\times2\) matrices \(H\) with \(\det H=1\). The identification with the hyperboloid uses the [[lie-groups/hermitian-matrix-model-of-minkowski-space|Hermitian matrix model]].

## Boundary and symmetry

The ideal or conformal boundary is
\[
\partial_\infty\mathbb H^3\cong S^2\cong\mathbb{CP}^1.
\]
The orientation-preserving isometry group is \(PSL(2,\mathbb C)\), and its boundary action is the Möbius action. Discrete subgroups of this group are Kleinian groups; torsion-free discrete subgroups give hyperbolic \(3\)-manifolds as quotients.

## References

1. John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 3rd ed., Springer, 2019, Chapters 3–4. [Publisher record](https://doi.org/10.1007/978-3-030-31597-9).
2. Alan F. Beardon, *The Geometry of Discrete Groups*, Springer, 1983, Chapter 7. [Publisher record](https://doi.org/10.1007/978-1-4612-1146-4).
