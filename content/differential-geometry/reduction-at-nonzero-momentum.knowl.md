+++
id = "differential-geometry/reduction-at-nonzero-momentum"
title = "Symplectic reduction at nonzero momentum"
kind = "theorem"
summary = "Regular reduction at a nonzero moment-map value uses the coadjoint stabilizer of that value."
aliases = ["nonzero-level reduction", "reduction at a coadjoint value"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let a [[fiber-bundles/lie-group|Lie group]] \(G\) act on \((M,\omega)\), and suppose the action is [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian]] with equivariant [[fiber-bundles/moment-map|moment map]] \(\mu:M\to\mathfrak g^*\). Fix \(\alpha\in\mathfrak g^*\). If \(\alpha\) is a [[fiber-bundles/regular-value|regular value]] and its coadjoint stabilizer \(G_\alpha\) acts freely and properly on \(\mu^{-1}(\alpha)\), then the [[differential-geometry/symplectic-quotient|quotient]]
\[
M/\!/\!_\alpha G=\mu^{-1}(\alpha)/G_\alpha
\]
is a [[fiber-bundles/smooth-manifold|smooth manifold]]. It carries a unique symplectic form \(\omega_\alpha\) characterized by
\[
\pi^*\omega_\alpha=i^*\omega,
\]
where \(i\) is inclusion and \(\pi\) is the orbit projection. Its dimension is \(\dim M-\dim G-\dim G_\alpha\).

## Why the stabilizer acts

Equivariance gives \(\mu(g\cdot m)=\operatorname{Ad}_g^*\mu(m)\). Therefore \(g\) preserves the individual level \(\mu^{-1}(\alpha)\) exactly when \(g\in G_\alpha\); the full group usually moves this level through the family \(\mu^{-1}(\operatorname{Ad}_g^*\alpha)\). This is why quotienting \(\mu^{-1}(\alpha)\) by all of \(G\) is generally undefined.

For \(m\in\mu^{-1}(\alpha)\), the kernel of \(i^*\omega\) equals the [[differential-geometry/tangent-space|tangent space]] to the \(G_\alpha\)-orbit. Thus the restricted form is basic for the free [[lie-groups/proper-action-lie|proper action]] and descends to a nondegenerate two-form. Closedness descends from \(d\omega=0\) [Ortega and Ratiu, §4.3](https://doi.org/10.1007/978-1-4757-3811-7).

## Dimension and special cases

Regularity makes \(\mu^{-1}(\alpha)\) have codimension \(\dim G\). Quotienting by the free \(G_\alpha\)-action removes another \(\dim G_\alpha\) dimensions, giving the formula in the core. If \(\alpha\) is fixed by the coadjoint action, then \(G_\alpha=G\) and
\[
\dim(M/\!/\!_\alpha G)=\dim M-2\dim G,
\]
the familiar zero-level count.

For an [[algebra-groups/abelian-group|abelian group]] every coadjoint value is fixed, so nonzero levels are reduced by the full group. For a nonabelian group, \(G_\alpha\) can be strictly smaller, and the dimension formula reflects that difference.

## Relation to zero-level reduction

The [[differential-geometry/shifting-trick|shifting trick]] converts reduction at \(\alpha\) into zero-level reduction of \(M\) times the [[differential-geometry/coadjoint-orbit|coadjoint orbit]] through \(\alpha\) equipped with the opposite [[differential-geometry/kirillov-kostant-souriau-form|Kirillov–Kostant–Souriau form]]. This also identifies \(\mu^{-1}(\alpha)/G_\alpha\) with \(\mu^{-1}(\mathcal O_\alpha)/G\) under the corresponding regularity hypotheses.

**Warning.** If regularity, freeness, or properness fails, the [[lie-groups/orbit-space|orbit space]] still exists set-theoretically but need not be a manifold; that setting belongs to [[differential-geometry/singular-symplectic-reduction|singular symplectic reduction]].

## References

1. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: §4.3, point reduction at a coadjoint value.
2. Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry*, 2nd ed., Springer, 1999. [DOI record](https://doi.org/10.1007/978-0-387-21792-5). Relevant: §10.3, regular point and orbit reduction.
