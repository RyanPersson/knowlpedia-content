+++
id = "shale-paper/automorphism-thetaT"
title = "Field Automorphism θ(T) from a Symplectic Map"
kind = "knowl"
summary = "The *-automorphism induced by sending Weyl operators V(z) to V(Tz)"
aliases = ["automorphism-thetaT", "Field Automorphism θ(T) from a Symplectic Map"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/automorphism-thetaT.md"
prerequisites = ["lie-groups/symplectic-group-spk", "mathematical-physics/weyl-ccr-quantization", "operator-algebras/star-automorphism"]
dependency_heuristic = "component-dependency-review-v1"
dependency_review_count = 2
+++

For [[lie-groups/symplectic-group-spk|\(T\in Sp(K)\)]], \(\theta(T)\) is the unique [[operator-algebras/star-automorphism|*-automorphism]] of the CCR \(C^*\)-algebra \(\mathfrak A\) such that
\[
\theta(T)\,e^{iR(z)} = e^{iR(Tz)}.
\]

## Remarks

It induces an action on states by pullback:
\(\theta^*(T)E(X)=E(\theta(T)^{-1}X)\).

**Key property (paper use):**
- \(E\sim \theta^*(T)E\) holds exactly when \(T\) is unitarily implementable in the chosen quantization.

## Examples

- In finite dimensions, metaplectic operators implement \(\theta(T)\) projectively.
