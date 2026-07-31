+++
id = "differential-geometry/hodge-laplacian"
title = "Hodge Laplacian"
kind = "definition"
summary = "The Hodge Laplacian is the degree-preserving elliptic operator obtained by anticommuting the exterior derivative and codifferential."
aliases = ["Laplace–de Rham operator", "de Rham Laplacian", "Hodge–de Rham Laplacian"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be an oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]]. The **Hodge Laplacian** on differential \(k\)-forms is
\[
\Delta=d\delta+\delta d:\Omega^k(M)\longrightarrow\Omega^k(M),
\]
where \(d\) is the [[fiber-bundles/exterior-derivative|exterior derivative]] and \(\delta\) is the [[differential-geometry/codifferential|codifferential]], its formal \(L^2\)-adjoint. This convention makes \(\Delta\) nonnegative: for compactly supported \(\alpha\),
\[
\langle\Delta\alpha,\alpha\rangle
=\|d\alpha\|^2+\|\delta\alpha\|^2.
\]
The operator preserves form degree, is formally self-adjoint, and is elliptic with principal symbol \(|\xi|^2\operatorname{id}\).
The same differential expression applies in every degree, including functions; its analytic realization depends on an operator domain and, when present, boundary conditions.

## Harmonic forms and cohomology

A form is **harmonic** when \(\Delta\alpha=0\). On a compact manifold without boundary, the energy identity implies
\[
\Delta\alpha=0
\quad\Longleftrightarrow\quad
d\alpha=0\ \text{and}\ \delta\alpha=0.
\]
The [[differential-geometry/hodge-theorem|Hodge theorem]] then identifies each de Rham cohomology class with a unique harmonic representative [Wells, chapter IV, §2].

On a noncompact manifold or a [[differential-geometry/manifold-with-boundary|manifold with boundary]], the differential expression is unchanged, but kernel, self-adjointness, and cohomological conclusions depend on domains, completeness, and boundary conditions.

## Basic identities

The relations \(d^2=0\) and \(\delta^2=0\) imply
\[
d\Delta=\Delta d,
\qquad
\delta\Delta=\Delta\delta.
\]
The [[differential-geometry/hodge-star-operator|Hodge star]] also intertwines the Laplacian in complementary degrees. These identities let harmonicity pass naturally between closed forms, coclosed forms, and their Hodge duals.

The Weitzenböck formula compares \(\Delta\) with the rough Laplacian:
\[
\Delta=\nabla^*\nabla+\mathcal R,
\]
where \(\mathcal R\) is a zeroth-order curvature action. On functions, \(\mathcal R=0\), and in Euclidean coordinates the nonnegative convention gives \(\Delta f=-\sum_j\partial_j^2f\).

## Conventions

Some analysis texts define the scalar Laplacian with the opposite sign. The formula \(d\delta+\delta d\) fixes the sign used here and makes the operator nonnegative in the \(L^2\) pairing. The [[fiber-bundles/covariant-hodge-laplacian|covariant Hodge Laplacian]] on bundle-valued forms is a related operator with additional coefficient curvature.

## References

1. Raymond O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: chapter IV, §2, harmonic forms, Hodge Laplacians, and Hodge theory.
2. Shigeyuki Morita, *Geometry of Differential Forms*, American Mathematical Society, 2001. [DOI record](https://doi.org/10.1090/mmono/201). Relevant: the chapter “Laplacian and harmonic forms.”
