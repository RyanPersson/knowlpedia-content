+++
id = "differential-geometry/moment-map-ambiguity"
title = "Uniqueness and ambiguity of moment maps"
kind = "proposition"
summary = "Two moment maps for the same action differ by a locally constant dual-Lie-algebra-valued function, constrained by equivariance."
aliases = ["moment-map normalization"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let a [[fiber-bundles/lie-group|Lie group]] \(G\) act symplectically on \(M\), and let \(\mu,\nu:M\to\mathfrak g^*\) be [[fiber-bundles/moment-map|moment maps]] for the same action and sign convention. Their difference \(\delta=\nu-\mu\) is locally constant: on each [[topology/connected-component|connected component]] \(C\subseteq M\), there is a covector \(c_C\in\mathfrak g^*\) with \(\delta|_C=c_C\). If both maps are [[differential-geometry/equivariant-moment-map|equivariant]], then
\[
c_{gC}=\operatorname{Ad}_g^*c_C.
\]
In particular, when \(M\) is connected, the ambiguity is addition of a single coadjoint-invariant covector \(c\in(\mathfrak g^*)^G\). These shifts describe every possible choice: once one moment-map value is fixed on each component, no further freedom remains.

## Proof

For every \(\xi\in\mathfrak g\), the two moment-map identities give
\[
d\langle\nu-\mu,\xi\rangle
=\iota_{\xi_M}\omega-\iota_{\xi_M}\omega=0.
\]
Each scalar component \(\langle\delta,\xi\rangle\) is therefore locally constant, so \(\delta\) is locally constant as a map to the finite-dimensional [[linear-algebra/vector-space|vector space]] \(\mathfrak g^*\). Equivariance of both maps gives
\[
\delta(gx)=\operatorname{Ad}_g^*\delta(x),
\]
which is exactly the stated relation among componentwise constants.

## Structure and consequences

For connected \(G\), a coadjoint-invariant covector annihilates the commutator algebra \([\mathfrak g,\mathfrak g]\). Hence a connected semisimple group admits no nonzero ambiguity of this kind. For an [[algebra-groups/abelian-group|abelian group]] the coadjoint action is trivial, so every constant covector gives another equivariant moment map.

Normalization conditions remove some or all of the ambiguity. For example, prescribing \(\mu(x_0)\) at one point of each connected component determines the moment map uniquely when those prescribed values are compatible with stabilizers and equivariance.

## Conventions and scope

**Warning.** Without equivariance, any locally constant \(\mathfrak g^*\)-valued shift preserves the differential moment-map identity; it need not be coadjoint invariant. If \(M\) is disconnected, equivariance may permute its components, so a separate arbitrary constant cannot generally be chosen on every component.

## References

1. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: §4.2, momentum-map equivariance and ambiguity.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Chapter 5, moment maps and Hamiltonian actions.
