+++
id = "differential-geometry/quaternionic-hermitian-manifold"
title = "Quaternionic-Hermitian manifold"
kind = "definition"
summary = "An almost-quaternionic manifold with a Riemannian metric invariant under every admissible local complex structure."
aliases = ["almost quaternion-Hermitian manifold"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/almost-quaternionic-manifold", "differential-geometry/riemannian-manifold"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **quaternionic-Hermitian manifold** is an [[differential-geometry/almost-quaternionic-manifold|almost-quaternionic manifold]] \((M,Q)\) of real dimension \(4n\) together with a [[differential-geometry/riemannian-manifold|Riemannian metric]] \(g\) such that
\[
g(AX,AY)=g(X,Y)
\]
for every local section \(A\) of \(Q\) satisfying \(A^2=-\operatorname{id}_{TM}\), and all tangent vectors \(X,Y\) at the same point. Equivalently, for every local admissible frame \((I,J,K)\) of \(Q\), the metric is Hermitian with respect to \(I\), \(J\), and \(K\). This compatibility is pointwise: it imposes no integrability condition on \(Q\) and no parallelism condition on \(g\).

## Structure-group interpretation

An almost-quaternionic structure reduces the frame bundle to \(GL(n,\mathbb H)Sp(1)\). Choosing a compatible metric reduces it further to the compact [[lie-groups/compact-symplectic-product-group|group \(Sp(n)Sp(1)\)]],
\[
Sp(n)Sp(1)=(Sp(n)\times Sp(1))/\{\pm(1,1)\}.
\]
This is the natural Riemannian structure group of quaternionic geometry. The formulation is independent of the chosen admissible frame because two such frames differ by an \(SO(3)\)-valued change of basis in \(Q\).

## Fundamental four-form

For a local admissible orthonormal frame \((I,J,K)\), define two-forms
\[
\omega_I(X,Y)=g(IX,Y),\qquad
\omega_J(X,Y)=g(JX,Y),\qquad
\omega_K(X,Y)=g(KX,Y).
\]
The combination
\[
\Omega=\omega_I\wedge\omega_I+\omega_J\wedge\omega_J+\omega_K\wedge\omega_K
\]
is unchanged by rotating the admissible frame, so it defines a global differential four-form. Its normalization varies in the literature, but its stabilizer encodes the \(Sp(n)Sp(1)\)-reduction.

## Relationship to quaternion-Kähler geometry

The quaternionic-Hermitian condition is algebraic. A quaternion-Kähler metric additionally requires its [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] to preserve \(Q\), or equivalently that its holonomy lie in \(Sp(n)Sp(1)\). Thus a compatible metric need not be quaternion-Kähler. A [[differential-geometry/hyperhermitian-manifold|hyper-Hermitian manifold]] provides a quaternionic-Hermitian example by taking \(Q=\operatorname{span}\{I,J,K\}\), but the global triple is extra data invisible to \((Q,g)\).

## Conventions and scope

**Warning.** Some authors use “quaternionic-Hermitian” only when the underlying \(Q\) is integrable, and use “almost quaternion-Hermitian” for the definition in the core. Here the terms are aliases and no integrability is assumed. In real dimension four, an \(Sp(1)Sp(1)\)-structure is essentially an oriented Riemannian conformal structure, so quaternion-Kähler terminology requires an additional convention.

## References

1. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [Springer DOI record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: Chapter 14, especially quaternionic-Hermitian structures and quaternion-Kähler metrics.
2. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [Oxford DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: quaternionic, hypercomplex, and hyperkähler structures.
