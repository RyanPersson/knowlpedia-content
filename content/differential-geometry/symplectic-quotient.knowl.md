+++
id = "differential-geometry/symplectic-quotient"
title = "Symplectic quotient"
kind = "definition"
summary = "The orbit space of a moment-map level set by the stabilizer of its value."
aliases = ["reduced phase space", "Marsden–Weinstein quotient"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,\omega,\mu)\) be a [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian \(G\)-space]] with equivariant [[fiber-bundles/moment-map|moment map]] \(\mu:M\to\mathfrak g^*\), and let \(\alpha\in\mathfrak g^*\). Write \(G_\alpha\) for the [[algebra-groups/stabilizer|stabilizer]] of \(\alpha\) under the [[fiber-bundles/coadjoint-action-of-a-lie-group|coadjoint action]]. Equivariance makes \(\mu^{-1}(\alpha)\) invariant under \(G_\alpha\). The **symplectic quotient of \(M\) at \(\alpha\)** is the [[lie-groups/orbit-space|orbit space]]
\[
M/\!/\!_\alpha G:=\mu^{-1}(\alpha)/G_\alpha.
\]
This definition specifies the underlying quotient even when it is singular. Calling it a [[differential-geometry/symplectic-manifold|symplectic manifold]], and constructing its reduced symplectic form, requires additional regularity hypotheses. If \(\alpha\) is coadjoint-fixed, then \(G_\alpha=G\).

## Regular reduction

If \(\alpha\) is a [[fiber-bundles/regular-value|regular value]] and the \(G_\alpha\)-action on \(\mu^{-1}(\alpha)\) is free and proper, the orbit space is a [[fiber-bundles/quotient-manifold|quotient manifold]]. There is then a unique symplectic form \(\omega_\alpha\) satisfying
\[
\pi^*\omega_\alpha=i^*\omega,
\]
where \(i:\mu^{-1}(\alpha)\hookrightarrow M\) is inclusion and \(\pi:\mu^{-1}(\alpha)\to M/\!/\!_\alpha G\) is the quotient map. This is the regular Marsden–Weinstein reduction theorem [Ortega and Ratiu, Chapter 6](https://doi.org/10.1007/978-1-4757-3811-7).

## Examples and singular behavior

Let \(S^1\) act on \(\mathbb C^n\) by scalar multiplication, with its standard symplectic form. Under the convention \(d\langle\mu,\xi\rangle=\iota_{\xi_M}\omega\) used here, a moment map is \(\mu(z)=-\tfrac12\lVert z\rVert^2\). For \(\alpha<0\), the level set is a sphere and its quotient is \(\mathbb{CP}^{n-1}\), carrying a scaled Fubini–Study form.

Regularity is not merely cosmetic. For a nonfree action or a [[differential-geometry/critical-value-of-a-smooth-map|critical value]], orbit dimensions can jump, so the quotient need not be a manifold; [[differential-geometry/singular-symplectic-reduction|singular symplectic reduction]] instead organizes it into symplectic strata [Ortega and Ratiu, Chapters 8–9](https://doi.org/10.1007/978-1-4757-3811-7).

## Conventions and scope

Some authors reserve “symplectic quotient” for a regular reduced manifold and use “reduced space” for the possibly singular orbit space. Reduction at the [[differential-geometry/coadjoint-orbit|coadjoint orbit]] through \(\alpha\) is also written \(\mu^{-1}(\mathcal O_\alpha)/G\); under the standard hypotheses it corresponds to the level-set formulation above. The notation \(M/\!/G\) usually means reduction at \(0\), but the chosen value should always be stated.

## References

1. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [Springer DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: Chapter 6 on regular reduction and Chapters 8–9 on singular reduction.
2. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [Cambridge DOI record](https://doi.org/10.1017/CBO9780511624110). Relevant: Chapter 5 on symplectic reduction.
