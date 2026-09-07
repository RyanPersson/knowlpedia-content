+++
id = "lie-groups/restricted-symplectic-group-rspk"
title = "Restricted Symplectic Group rSp(K)"
kind = "knowl"
summary = "The implementable symplectic transformations in Shale's Fock representation"
aliases = ["restricted-symplectic-group-rspk", "Restricted Symplectic Group rSp(K)"]
domains = ["lie-groups"]
legacy_source_path = "shale-paper/restricted-symplectic-group-rspk.md"
prerequisites = ["lie-groups/restricted-general-linear-group-rgl", "lie-groups/symplectic-group", "shale-paper/hilbert-schmidt-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **restricted [[lie-groups/symplectic-group|symplectic group]]** is
\[
\mathrm{rSp}(K)=\mathrm{Sp}(K)\cap \mathrm{rGL}(K),
\]
where \(\mathrm{rGL}(K)\) is the [[lie-groups/restricted-general-linear-group-rgl|restricted general linear group]].

In Shale's Theorem 4.1 ([[mathematical-physics/fock-cook-quantization|Fock–Cook quantization]]), \(T\) is unitarily implementable iff \(T\in rSp(K)\),
equivalently \((T^*T)^{1/2}-I\) is [[shale-paper/hilbert-schmidt-operator|Hilbert–Schmidt]].

## Remarks

**Key properties:**
- Closed under [[functional-analysis/polar-decomposition|polar decomposition]].
- Carries a continuous [[lie-groups/projective-unitary-representation|projective unitary representation]] \(\overline{Y}\).

## Examples

- Finite-dimensional case: \(rSp(K)=Sp(K)\).
