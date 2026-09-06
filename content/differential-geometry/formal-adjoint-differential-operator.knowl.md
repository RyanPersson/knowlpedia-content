+++
id = "differential-geometry/formal-adjoint-differential-operator"
title = "Formal adjoint of a differential operator"
kind = "definition"
summary = "The formal adjoint is the differential operator obtained by transferring derivatives across an integral pairing without boundary terms."
aliases = ["formal adjoint"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/complex-vector-bundle", "fiber-bundles/bundle-metric", "differential-geometry/differential-operator-vector-bundles"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be an oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]] without boundary, let \(E,F\to M\) be real or [[fiber-bundles/complex-vector-bundle|complex vector bundles]] with [[fiber-bundles/bundle-metric|bundle metrics]], and let
\[
P:\Gamma(E)\longrightarrow\Gamma(F)
\]
be a linear [[differential-geometry/differential-operator-vector-bundles|differential operator]]. Its **formal adjoint** is the unique differential operator \(P^\dagger:\Gamma(F)\to\Gamma(E)\) satisfying
\[
\int_M\langle Pu,v\rangle_F\,\operatorname{vol}_g
=\int_M\langle u,P^\dagger v\rangle_E\,\operatorname{vol}_g
\]
for all compactly supported smooth sections \(u\) and \(v\). In the complex
case the bundle pairings are Hermitian, conjugate-linear in the first
argument, and linear in the second. The identity is algebraic integration by
parts and specifies no Hilbert-space domain.

## Construction and properties

In a [[fiber-bundles/local-trivialization|local trivialization]], move each derivative in \(P\) from \(u\) to the coefficient multiplying \(v\), reversing its sign and conjugating matrix coefficients in the complex case. A partition of unity shows that the resulting local operators assemble into \(P^\dagger\). The construction gives
\[
(PQ)^\dagger=Q^\dagger P^\dagger,
\qquad
(P^\dagger)^\dagger=P.
\]
The formal adjoint has the same order as \(P\). Its principal symbol is the fiberwise adjoint of the principal symbol of \(P\), with the sign dictated by the chosen symbol convention.

## Differential forms

For the [[fiber-bundles/exterior-derivative|exterior derivative]] \(d:\Omega^{k-1}(M)\to\Omega^k(M)\), the formal adjoint is the [[differential-geometry/codifferential|codifferential]]
\[
d^\dagger=(-1)^{n(k+1)+1}*d*
\]
on \(k\)-forms under the [[differential-geometry/hodge-star-operator|Hodge-star]] convention of an oriented \(n\)-dimensional Riemannian manifold. The [[differential-geometry/hodge-laplacian|Hodge Laplacian]] \(dd^\dagger+d^\dagger d\) is therefore formally self-adjoint.

For functions of compact support on [[linear-algebra/euclidean-space|Euclidean space]], the formal adjoint of \(\partial/\partial x^j\) is \(-\partial/\partial x^j\). Multiplication by a real-valued function is formally self-adjoint.

## Boundary terms and analytic adjoints

**Warning.** On a [[differential-geometry/manifold-with-boundary|manifold with boundary]], [[real-analysis/integration-by-parts|integration by parts]] produces a boundary term unless supports avoid the boundary or boundary conditions make it vanish. The same differential expression can consequently have different operator adjoints for Dirichlet, Neumann, or other domains.

The formal adjoint is not automatically the adjoint of an unbounded operator on an \(L^2\) [[linear-algebra/hilbert-space|Hilbert space]]. The latter depends on a specified dense domain and on completeness or boundary conditions. Formal self-adjointness is therefore necessary but not sufficient for self-adjointness of an analytic realization.

## References

1. Raymond O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Graduate Texts in Mathematics 65, Springer, 2008. [Publisher record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter III, Hodge-star identities, and Chapter IV, “Elliptic Operator Theory.”
2. Shigeyuki Morita, *Geometry of Differential Forms*, Translations of Mathematical Monographs 201, American Mathematical Society, 2001. [Publisher record](https://doi.org/10.1090/mmono/201). Relevant: “Laplacian and harmonic forms.”
