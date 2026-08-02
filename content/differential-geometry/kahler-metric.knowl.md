+++
id = "differential-geometry/kahler-metric"
title = "Kähler metric"
kind = "definition"
summary = "A Hermitian metric whose associated fundamental two-form is closed."
aliases = []
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]] with complex structure \(J\). A **Kähler metric** is a [[differential-geometry/hermitian-manifold|Hermitian]] Riemannian metric \(g\) whose associated real fundamental \(2\)-form
\[
\omega(X,Y)=g(JX,Y)
\]
is closed:
\[
d\omega=0.
\]
Equivalently, \(\omega\) is a [[differential-geometry/kahler-form|Kähler form]], and \((X,J,g)\) is a [[differential-geometry/kahler-manifold|Kähler manifold]] with specified metric data. The positivity and \(J\)-invariance belong to the Hermitian hypothesis, while closedness is the additional Kähler condition. The metric \(g\) is real bilinear; the corresponding Hermitian form on the [[differential-geometry/holomorphic-tangent-bundle|complex tangent bundle]] is sesquilinear.

## Equivalent characterizations

For a [[fiber-bundles/hermitian-metric|Hermitian metric]], the Kähler condition is equivalent to \(\nabla J=0\) for the Levi–Civita connection. It is also equivalent to the Levi–Civita and [[fiber-bundles/chern-connection|Chern connections]] on the holomorphic tangent bundle agreeing. In holomorphic coordinates, the Hermitian coefficient matrix \((g_{j\bar k})\) satisfies
\[
\frac{\partial g_{j\bar k}}{\partial z^\ell}
=
\frac{\partial g_{\ell\bar k}}{\partial z^j}.
\]

## Structure and consequences

The fundamental form of a Kähler metric is nondegenerate, so it also makes \(X\) a [[differential-geometry/symplectic-manifold|symplectic manifold]]. The Levi–Civita connection preserves \(g\), \(J\), and \(\omega\), and its holonomy is contained in \(U(n)\). Locally, the metric coefficients are complex Hessians of real [[differential-geometry/local-kahler-potential|Kähler potentials]]. These compatibilities are special: an arbitrary Hermitian metric need not have closed [[differential-geometry/fundamental-form-almost-hermitian|fundamental form]].

## Examples and non-examples

The Euclidean metric on \(\mathbb C^n\), flat Hermitian metrics on complex tori, and the [[differential-geometry/fubini-study-metric|Fubini–Study metric]] on [[algebraic-geometry-foundations/projective-space|complex projective space]] are Kähler. If \(n>1\), multiplying a Kähler metric by \(e^f\) for a nonconstant real function \(f\) usually gives only a Hermitian metric, because its fundamental form is \(e^f\omega\) and
\[
d(e^f\omega)=e^f\,df\wedge\omega
\]
need not vanish.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: §3.1, Kähler metrics and their fundamental forms.
2. Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, 2012. [Author-hosted text](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Relevant: Chapter VI, §4, especially Definition 4.1 and Theorem 4.8.
