+++
id = "differential-geometry/moment-map-component"
title = "Moment-map component"
kind = "definition"
summary = "The scalar Hamiltonian obtained by pairing a moment map with one Lie algebra element."
aliases = ["component function of a moment map", "Hamiltonian for an infinitesimal generator"]
domains = ["differential-geometry", "lie-groups"]
section_mode = "progressive"
prerequisites = ["differential-geometry/symplectic-manifold", "fiber-bundles/moment-map", "differential-geometry/hamiltonian-function", "differential-geometry/infinitesimal-generator-lie-action"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) act on a [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\), let \(\mu:M\to\mathfrak g^*\) be a [[fiber-bundles/moment-map|moment map]], and fix \(\xi\in\mathfrak g\). The **moment-map component in the direction \(\xi\)** is the smooth function
\[
\mu^\xi:M\to\mathbb R,\qquad
\mu^\xi(p)=\langle\mu(p),\xi\rangle.
\]
With the conventions
\[
\xi_M(p)=\left.\frac{d}{dt}\right|_0\exp(t\xi)\mathbin{\cdot}p,
\qquad d\mu^\xi=\iota_{\xi_M}\omega,
\]
the function \(\mu^\xi\) is a [[differential-geometry/hamiltonian-function|Hamiltonian function]] for the [[differential-geometry/infinitesimal-generator-lie-action|infinitesimal generator]] \(\xi_M\).
It records the Hamiltonian associated with one infinitesimal symmetry.

## Linearity and reconstruction

The assignment \(\xi\mapsto\mu^\xi\) is linear from \(\mathfrak g\) to \(C^\infty(M)\). Conversely, a linear family of functions \(H_\xi\) determines a map \(\mu:M\to\mathfrak g^*\) by \(\langle\mu(p),\xi\rangle=H_\xi(p)\). Thus the component equations for all \(\xi\) are equivalent to the single \(\mathfrak g^*\)-valued moment-map equation.

## Equivariance and constants

If \(\mu\) is equivariant for the [[fiber-bundles/coadjoint-action-of-a-lie-group|coadjoint action]], then
\[
\mu^\xi(g\mathbin{\cdot}p)=\mu^{\operatorname{Ad}_{g^{-1}}\xi}(p).
\]
Adding a constant \(c\in\mathfrak g^*\) shifts each component by \(\langle c,\xi\rangle\) without changing its differential. Equivariance is preserved precisely when \(c\) is fixed by the coadjoint action.

## Examples and conventions

For the [[differential-geometry/cotangent-lift|cotangent-lifted action]] on \(T^*Q\), the standard component is \(\mu^\xi(q,\alpha)=\alpha(\xi_Q(q))\). On a [[differential-geometry/coadjoint-orbit|coadjoint orbit]] with its [[differential-geometry/kirillov-kostant-souriau-form|KKS form]], the inclusion moment map has \(\mu^\xi(\lambda)=\langle\lambda,\xi\rangle\). Authors using \(d\mu^\xi=-\iota_{\xi_M}\omega\) obtain the negative components relative to the present convention.

## References

1. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Progress in Mathematics 222, Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: Chapter 4, the standard momentum map and its component functions.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Chapter 5, Hamiltonian actions and moment maps.
