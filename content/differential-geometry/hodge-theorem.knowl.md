+++
id = "differential-geometry/hodge-theorem"
title = "Hodge theorem"
kind = "theorem"
summary = "Every de Rham cohomology class on a compact oriented Riemannian manifold has a unique harmonic representative."
aliases = ["Hodge isomorphism theorem", "harmonic representative theorem"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/de-rham-cohomology-group", "differential-geometry/harmonic-differential-form", "differential-geometry/hodge-laplacian", "linear-algebra/vector-space", "fiber-bundles/smooth-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,g)\) be a compact oriented
[[differential-geometry/riemannian-manifold|Riemannian manifold]] without boundary.
The **Hodge theorem** states that every class in the real
[[fiber-bundles/de-rham-cohomology-group|de Rham cohomology group]]
\(H^k_{\mathrm{dR}}(M;\mathbb R)\) contains a unique
[[differential-geometry/harmonic-differential-form|harmonic \(k\)-form]].
Equivalently, the map
\[
\mathcal H^k(M,g)\longrightarrow H^k_{\mathrm{dR}}(M;\mathbb R),
\qquad \alpha\longmapsto[\alpha],
\]
is an isomorphism of finite-dimensional real [[linear-algebra/vector-space|vector spaces]]. The harmonic
representative and the displayed isomorphism depend on \(g\), whereas de
Rham cohomology itself depends only on the [[fiber-bundles/smooth-manifold|smooth manifold]].

## Why existence and uniqueness hold

The Hodge orthogonal decomposition writes every smooth \(k\)-form as
\[
\omega=h+d\beta+\delta\gamma
\]
with \(h\) harmonic. If \(\omega\) is closed, orthogonality forces its
coexact component \(\delta\gamma\) to vanish, so \([\omega]=[h]\). This
gives existence.

If two harmonic forms represent the same class, their difference is both
harmonic and exact. Exact forms are orthogonal to harmonic forms, so the
difference has zero \(L^2\)-norm and vanishes. This gives uniqueness. The
analytic input is ellipticity of the
[[differential-geometry/hodge-laplacian|Hodge Laplacian]] on the compact
manifold; the cohomological conclusion is not a purely formal property of
the [[differential-geometry/de-rham-complex|de Rham complex]].

## Consequences

Because \(\mathcal H^k(M,g)\) is the kernel of an
[[differential-geometry/elliptic-differential-operator|elliptic operator]]
on a compact manifold, it is finite-dimensional. The theorem therefore proves
finite-dimensionality of \(H^k_{\mathrm{dR}}(M;\mathbb R)\). It also turns
cohomology questions into equations for differential forms: a cohomology
class is zero exactly when its harmonic representative is zero.

The [[differential-geometry/hodge-star-operator|Hodge star]] commutes with
the Hodge Laplacian and maps harmonic \(k\)-forms to harmonic
\((n-k)\)-forms. Together with the theorem, this supplies the analytic
realization of Poincaré duality for an oriented compact manifold.

## Conventions and scope

“Compact” here includes absence of boundary only because that hypothesis is
stated separately. On a
[[differential-geometry/manifold-with-boundary|manifold with boundary]],
absolute or relative boundary conditions lead to different Hodge theorems.
On a noncompact
manifold, unrestricted smooth harmonic forms generally do not provide
unique representatives of ordinary de Rham cohomology; \(L^2\), compactly
supported, or weighted variants require additional analytic hypotheses.

## References

1. Mark Andrea A. de Cataldo, *The Hodge Theory of Projective Manifolds*, Imperial College Press, 2007. [Author-hosted book PDF](https://www.math.stonybrook.edu/~mde/papers/MyHodgeTheoryBook.pdf). Relevant: Theorem 2.3.3 and Corollary 2.3.7.
2. Raymond O. Wells, Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter IV, §2 on the Hodge theorem.
