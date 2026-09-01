+++
id = "differential-geometry/coadjoint-orbit"
title = "Coadjoint orbit"
kind = "definition"
summary = "An orbit of a Lie group acting on the dual of its Lie algebra by the coadjoint action."
aliases = ["co-adjoint orbit"]
domains = ["differential-geometry", "lie-groups"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/lie-algebra", "lie-groups/orbit-lie-group", "fiber-bundles/coadjoint-action-of-a-lie-group", "lie-groups/stabilizer-lie-group", "fiber-bundles/diffeomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let [[fiber-bundles/lie-group|\(G\)]] be a finite-dimensional Lie group with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), and let \(\lambda\in\mathfrak g^*\). The **coadjoint orbit through \(\lambda\)** is the [[lie-groups/orbit-lie-group|orbit]]
\[
\mathcal O_\lambda=G\cdot\lambda
=\{\operatorname{Ad}_g^*\lambda:g\in G\}\subseteq\mathfrak g^*
\]
for the [[fiber-bundles/coadjoint-action-of-a-lie-group|coadjoint action]]. If \(G_\lambda=\{g\in G:\operatorname{Ad}_g^*\lambda=\lambda\}\) is the [[lie-groups/stabilizer-lie-group|stabilizer]], then \(\mathcal O_\lambda\) carries the canonical immersed-manifold structure for which \(G/G_\lambda\to\mathcal O_\lambda\) is a \(G\)-equivariant [[fiber-bundles/diffeomorphism|diffeomorphism]]. Its dimension is \(\dim G-\dim G_\lambda\).

## Tangent space and homogeneous structure

At \(\mu\in\mathcal O_\lambda\), the [[differential-geometry/tangent-space|tangent space]] is
\[
T_\mu\mathcal O_\lambda
=\{\operatorname{ad}_X^*\mu:X\in\mathfrak g\}.
\]
Its kernel presentation identifies this tangent space with \(\mathfrak g/\mathfrak g_\mu\), where \(\mathfrak g_\mu\) is the Lie algebra of the stabilizer. Thus each coadjoint orbit is a [[lie-groups/homogeneous-space|homogeneous space]].

## Kirillov–Kostant–Souriau form

Every coadjoint orbit has a canonical invariant symplectic form. With \(X^\#_\mu=\frac{d}{dt}|_{0}\operatorname{Ad}_{\exp(tX)}^*\mu\), one common convention is
\[
\omega_\mu(X^\#_\mu,Y^\#_\mu)=\langle\mu,[X,Y]\rangle.
\]
This is well defined, closed, and nondegenerate, so \(\mathcal O_\lambda\) is a [[differential-geometry/symplectic-manifold|symplectic manifold]].

## Examples and sign conventions

For an [[lie-groups/abelian-lie-group|abelian Lie group]] every coadjoint orbit is a single point. After identifying \(\mathfrak{so}(3)^*\cong\mathbb R^3\), the nonzero coadjoint orbits of \(\mathrm{SO}(3)\) are spheres. Authors who define [[differential-geometry/infinitesimal-generator-lie-action|fundamental vector fields]] or [[fiber-bundles/moment-map|moment maps]] with the opposite sign write the negative of the displayed symplectic form; the underlying orbit is unchanged.

## References

1. A. A. Kirillov, *Elements of the Theory of Representations*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-3-642-66243-0). Relevant: “The Method of Orbits.”
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Springer, 2008. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Hamiltonian group actions and coadjoint orbits.
