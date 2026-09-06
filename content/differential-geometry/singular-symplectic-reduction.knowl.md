+++
id = "differential-geometry/singular-symplectic-reduction"
title = "Singular symplectic reduction"
kind = "definition"
summary = "Symplectic reduction without regularity or freeness, producing a stratified quotient rather than generally a manifold."
aliases = ["stratified symplectic quotient"]
domains = ["differential-geometry"]
prerequisites = ["lie-groups/compact-lie-group", "differential-geometry/hamiltonian-lie-group-action", "differential-geometry/symplectic-manifold", "fiber-bundles/moment-map", "lie-groups/orbit-space", "fiber-bundles/regular-value", "topology/connected-component", "differential-geometry/shifting-trick"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let a [[lie-groups/compact-lie-group|compact Lie group]] \(G\) have a [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian action]] on a [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\) with equivariant [[fiber-bundles/moment-map|moment map]] \(\mu:M\to\mathfrak g^*\). The **singular symplectic reduction at zero** is the [[lie-groups/orbit-space|orbit space]]
\[
M/\!/G=\mu^{-1}(0)/G
\]
when \(0\) need not be a [[fiber-bundles/regular-value|regular value]] and the action on \(\mu^{-1}(0)\) need not be free. It is generally not a manifold. Its decomposition by [[topology/connected-component|connected components]] of orbit-type sets gives it the structure of a stratified space whose strata are smooth symplectic manifolds. Reduction at a nonzero value is handled similarly using its coadjoint stabilizer, or by the [[differential-geometry/shifting-trick|shifting trick]].

## Orbit-type strata

For a closed subgroup \(H\subseteq G\), let \(M_{(H)}\) denote the points whose stabilizers are conjugate to \(H\). The pieces
\[
\bigl(\mu^{-1}(0)\cap M_{(H)}\bigr)/G
\]
need not be connected; their connected components are the symplectic strata. On each component, the restricted form descends by the same kernel-removal mechanism as regular reduction. Different strata can have different dimensions and fit together according to stabilizer type.

In this compact-group setting, the orbit-type pieces are symplectic and their decomposition is a stratification; the natural smooth functions carry a compatible Poisson bracket.

## Relation to regular reduction

If \(0\) is regular and the action on \(\mu^{-1}(0)\) is free, there is only the principal orbit type on the level set, and the singular construction reduces to the [[differential-geometry/marsden-weinstein-meyer-reduction-theorem|Marsden–Weinstein–Meyer reduced manifold]]. With locally free rather than [[algebra-groups/free-action|free action]], the quotient is typically a symplectic orbifold. Stabilizers of different dimensions are what force genuinely stratified behavior.

As a basic model, a circle acting on a [[differential-geometry/symplectic-vector-space|symplectic vector space]] with weights of both signs can have a zero level containing the fixed origin and free or locally free points away from it. Their images lie in strata of different dimensions, so no single manifold chart can describe the quotient near the image of the origin.

## Conventions and scope

**Warning.** “Singular” refers to the quotient's failure to be a [[fiber-bundles/smooth-manifold|smooth manifold]], not to a degenerate two-form on each stratum: every stratum carries a nondegenerate symplectic form.

For noncompact groups, proper Hamiltonian actions admit broader singular-reduction theorems, but the precise hypotheses and stratification category require care. The core uses the classical compact-group setting. “Singular reduction” is also used for Poisson, presymplectic, and infinite-dimensional quotients; those are not included automatically here.

## References

1. Reyer Sjamaar and Eugene Lerman, “Stratified Symplectic Spaces and Reduction,” *Annals of Mathematics* 134 (1991), 375–422. [DOI record](https://doi.org/10.2307/2001809). Relevant: Theorem 2.1 on symplectic pieces, §3 on the reduced Poisson algebra, and Theorem 6.11 on stratification.
2. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: Chapter 8, singular reduction and symplectic strata.
