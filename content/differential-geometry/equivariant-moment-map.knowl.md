+++
id = "differential-geometry/equivariant-moment-map"
title = "Equivariant moment map"
kind = "definition"
summary = "A moment map that intertwines a Lie group action with the coadjoint action on the dual Lie algebra."
aliases = ["coadjoint-equivariant moment map"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/lie-group", "fiber-bundles/moment-map", "fiber-bundles/coadjoint-action-of-a-lie-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let a [[fiber-bundles/lie-group|Lie group]] \(G\) act symplectically on \((M,\omega)\), and let \(\mu:M\to\mathfrak g^*\) be a [[fiber-bundles/moment-map|moment map]]. It is an **equivariant moment map** if
\[
\mu(g\cdot x)=\operatorname{Ad}_g^*\mu(x)
\]
for every \(g\in G\) and \(x\in M\), where \(\operatorname{Ad}^*\) is the [[fiber-bundles/coadjoint-action-of-a-lie-group|coadjoint action]]. Thus \(\mu\) satisfies both the differential moment-map identity for every \(\xi\in\mathfrak g\) and the global compatibility condition intertwining the two \(G\)-actions.

## Infinitesimal criterion

Differentiating equivariance at the identity gives
\[
d\mu_x\bigl(\xi_M(x)\bigr)=\operatorname{ad}_\xi^*\mu(x).
\]
With the coadjoint convention \(\operatorname{Ad}_g^*\lambda=\lambda\circ\operatorname{Ad}_{g^{-1}}\), this formula uses the corresponding infinitesimal coadjoint action. If \(G\) is connected, the infinitesimal identity for every \(\xi\) implies the global equivariance condition.

## Equivariance defect

For a nonequivariant moment map, the difference
\[
\sigma(g)=\mu(g\cdot x)-\operatorname{Ad}_g^*\mu(x)
\]
is independent of \(x\) when \(M\) is connected and defines a group cocycle with values in \(\mathfrak g^*\). Changing \(\mu\) by a constant changes this cocycle by a coboundary. Consequently, the obstruction to choosing an equivariant moment map is a cohomology class rather than merely a poor normalization.

## Consequences and conventions

Equivariance makes inverse images of coadjoint-invariant subsets \(G\)-invariant and is the hypothesis normally used in Hamiltonian reduction. Sign conventions for the [[differential-geometry/infinitesimal-generator-lie-action|fundamental vector field]], the moment-map equation, and the infinitesimal coadjoint action vary together in the literature; the global equation in the core is convention-independent once the cited coadjoint action has been fixed.

## References

1. J.-P. Ortega and T. S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [Springer DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: §4.2.
2. V. Guillemin and S. Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1990. [Cambridge DOI record](https://doi.org/10.1017/CBO9780511624110). Relevant: Chapter 3.
