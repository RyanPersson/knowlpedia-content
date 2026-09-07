+++
id = "mathematical-physics/fock-cook-quantization"
title = "Fock–Cook Quantization"
kind = "knowl"
summary = "The bosonic canonical-commutation-relation representation defined by field operators on symmetric Fock space."
aliases = ["fock-cook-quantization", "Fock–Cook Quantization"]
domains = ["mathematical-physics"]
legacy_source_path = "shale-paper/fock-cook-quantization.md"
prerequisites = ["mathematical-physics/symmetric-fock-space", "mathematical-physics/creation-annihilation-operators"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(H\) be a complex [[linear-algebra/hilbert-space|Hilbert space]], let \(S(H)\) be its [[mathematical-physics/symmetric-fock-space|symmetric Fock space]], and let \(C(z)\) and \(C^*(z)\) be the [[mathematical-physics/creation-annihilation-operators|creation and annihilation operators]] associated with \(z\in H\). The **Fock–Cook field operator** is the closure
\[
R(z)=\frac1{\sqrt2}\,(C(z)+C^*(z))^{\sim},
\]
initially defined on the finite-particle subspace. The corresponding Weyl operators are
\[
V(z)=e^{iR(z)}.
\]

## Remarks

The unitaries \(V(z)\) satisfy the [[mathematical-physics/weyl-ccr-quantization|Weyl canonical commutation relations]]. In the setting of Shale's theorem, a symplectic transformation \(T\in Sp(K)\) is unitarily implementable in this representation exactly when \(T\in rSp(K)\).

## Examples

- For finite-dimensional \(H\), this is the standard bosonic Fock representation of the canonical commutation relations.
