+++
id = "differential-geometry/hodge-decomposition-riemannian"
title = "Hodge decomposition on a compact Riemannian manifold"
kind = "theorem"
summary = "Smooth forms on a compact oriented Riemannian manifold split orthogonally into harmonic, exact, and coexact parts."
aliases = ["orthogonal Hodge decomposition"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "differential-geometry/harmonic-differential-form"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,g)\) be a compact oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]] without boundary.
The **Hodge decomposition** in degree \(k\) is the \(L^2\)-orthogonal direct
sum
\[
\Omega^k(M)
=\mathcal H^k(M,g)
\oplus d\Omega^{k-1}(M)
\oplus\delta\Omega^{k+1}(M),
\]
where \(\mathcal H^k(M,g)=\ker\Delta\) is the space of
[[differential-geometry/harmonic-differential-form|harmonic forms]],
\(d\Omega^{k-1}(M)\) consists of exact forms, and
\(\delta\Omega^{k+1}(M)\) consists of coexact forms. Thus every smooth
\(k\)-form has a unique harmonic, exact, and coexact component. The
decomposition depends on \(g\) and uses compactness and the absence of a
boundary.

## Orthogonality and uniqueness

Exact and coexact forms are orthogonal because
\[
\langle d\beta,\delta\gamma\rangle_{L^2}
=\langle d^2\beta,\gamma\rangle_{L^2}=0.
\]
Harmonic forms are closed and coclosed, so they are orthogonal to both
summands. These identities show uniqueness once existence is known.
Existence is the analytic part: elliptic theory for the
[[differential-geometry/hodge-laplacian|Hodge Laplacian]] gives a Green
operator on the [[linear-algebra/orthogonal-complement|orthogonal complement]] of its finite-dimensional kernel.

Equivalently,
\[
\Omega^k(M)=\ker\Delta\oplus\operatorname{im}\Delta.
\]
Indeed, \(\operatorname{im}\Delta\) is the orthogonal sum of the exact and
coexact subspaces in the displayed decomposition.

## Cohomological meaning

If \(\omega\) is closed, its coexact component vanishes, leaving
\[
\omega=h+d\beta.
\]
The harmonic component \(h\) is therefore the unique harmonic
representative of \([\omega]\). This recovers the
[[differential-geometry/hodge-theorem|Hodge theorem]] and identifies
\(\mathcal H^k(M,g)\) with de Rham cohomology.

The decomposition is sometimes compared with the Helmholtz decomposition of
[[fiber-bundles/vector-field|vector fields]]: the exact and coexact pieces generalize gradient and
curl-type contributions. The analogy concerns orthogonal splitting; the
actual objects here are differential forms in every degree.

## Conventions and scope

This Riemannian decomposition should not be confused with the
\((p,q)\)-decomposition of complex differential forms or the Hodge
decomposition of cohomology on a compact
[[differential-geometry/kahler-manifold|Kähler manifold]]. Those use complex
type and additional
[[differential-geometry/kahler-identities|Kähler identities]]. On manifolds
with boundary, boundary conditions add further summands or modify the
domains; on noncompact
manifolds, closures of images and the chosen \(L^2\) realization become
essential.

## References

1. Mark Andrea A. de Cataldo, *The Hodge Theory of Projective Manifolds*, Imperial College Press, 2007. [Author-hosted book PDF](https://www.math.stonybrook.edu/~mde/papers/MyHodgeTheoryBook.pdf). Relevant: Theorem 2.3.3, the Hodge orthogonal decomposition theorem.
2. Raymond O. Wells, Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter IV, §2 on harmonic forms and Hodge decomposition.
