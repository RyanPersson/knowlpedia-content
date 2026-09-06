+++
id = "differential-geometry/marsden-weinstein-meyer-reduction-theorem"
title = "Marsden–Weinstein–Meyer reduction theorem"
kind = "theorem"
summary = "A free proper Hamiltonian action reduces a regular zero level to a symplectic manifold of dimension lowered by twice the group dimension."
aliases = ["symplectic reduction theorem", "regular reduction theorem"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group", "differential-geometry/symplectic-manifold", "differential-geometry/hamiltonian-lie-group-action", "fiber-bundles/moment-map", "fiber-bundles/regular-value", "fiber-bundles/smooth-manifold"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let a \(k\)-dimensional [[fiber-bundles/lie-group|Lie group]] \(G\) act freely and properly on a \(2n\)-dimensional [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\) by a [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian action]] with equivariant [[fiber-bundles/moment-map|moment map]] \(\mu:M\to\mathfrak g^*\). If \(0\) is a [[fiber-bundles/regular-value|regular value]], then
\[
M_{\mathrm{red}}=\mu^{-1}(0)/G
\]
is a [[fiber-bundles/smooth-manifold|smooth manifold]] of dimension \(2n-2k\). Writing \(i:\mu^{-1}(0)\hookrightarrow M\) and \(\pi:\mu^{-1}(0)\to M_{\mathrm{red}}\), there is a unique symplectic form \(\omega_{\mathrm{red}}\) such that
\[
\pi^*\omega_{\mathrm{red}}=i^*\omega.
\]
This symplectic manifold is the regular zero-level reduction, or Marsden–Weinstein–Meyer quotient, of \(M\) by \(G\).

## Roles of the hypotheses

Regularity makes \(\mu^{-1}(0)\) an [[differential-geometry/embedded-submanifold|embedded submanifold]] of codimension \(k\). Properness and freeness make its [[lie-groups/orbit-space|orbit space]] a smooth manifold and \(\pi\) a principal \(G\)-bundle. Equivariance ensures that the zero level is \(G\)-invariant.

At each \(m\in\mu^{-1}(0)\), the [[differential-geometry/tangent-space|tangent space]] to the \(G\)-orbit equals the kernel of \(i^*\omega_m\). Hence \(i^*\omega\) is horizontal; its \(G\)-invariance makes it basic. It therefore descends uniquely through \(\pi\), and quotienting precisely by its kernel makes the descended form nondegenerate. Closedness follows from
\[
\pi^*(d\omega_{\mathrm{red}})=d(i^*\omega)=0
\]
and injectivity of pullback by a surjective submersion.

## Dimension count and examples

The regular level has dimension \(2n-k\), and every free orbit has dimension \(k\); the quotient therefore has dimension \(2n-2k\). The evenness is also forced by the existence of \(\omega_{\mathrm{red}}\).

For the scalar \(S^1\)-action on \(\mathbb C^n\), choosing a positive regular level of a shifted moment map gives a sphere. Dividing by \(S^1\) yields complex [[algebraic-geometry-foundations/projective-space|projective space]] with a multiple of the Fubini–Study form. This illustrates both stages of the dimension loss: one equation cuts out the level and one orbit direction is removed.

## Variants and failure modes

At a nonzero coadjoint value \(\alpha\), the appropriate quotient is by \(G_\alpha\), as stated in [[differential-geometry/reduction-at-nonzero-momentum|reduction at nonzero momentum]]. If the action is only locally free, the quotient is naturally a symplectic orbifold. If regularity or local freeness fails, orbit types and dimensions may jump, and [[differential-geometry/singular-symplectic-reduction|singular symplectic reduction]] replaces the single reduced manifold by symplectic strata.

**Warning.** Some formulations omit “\(0\) is regular” because freeness of the action on the level set implies the needed infinitesimal surjectivity. Listing regularity separately makes the geometric roles of the assumptions explicit and covers the standard theorem statement.

## References

1. Jerrold E. Marsden and Alan Weinstein, “Reduction of Symplectic Manifolds with Symmetry,” *Reports on Mathematical Physics* 5 (1974), 121–130. [DOI record](https://doi.org/10.1016/0034-4877%2874%2990021-4). Relevant: the symplectic reduction theorem and pullback characterization of the reduced form.
2. Kenneth R. Meyer, “Symmetries and Integrals in Mechanics,” in *Dynamical Systems*, Academic Press, 1973, 259–272. [DOI record](https://doi.org/10.1016/B978-0-12-550350-1.50025-4). Relevant: independent formulation of reduction by symmetries.
3. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: Chapter 6, regular symplectic reduction.
