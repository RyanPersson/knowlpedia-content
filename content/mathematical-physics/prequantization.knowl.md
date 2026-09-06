+++
id = "mathematical-physics/prequantization"
title = "Prequantization"
kind = "definition"
summary = "The geometric construction that represents all classical observables on sections of a line bundle before imposing a polarization."
aliases = ["Kostant-Souriau prequantization", "geometric prequantization", "prequantum line bundle construction"]
domains = ["mathematical-physics", "differential-geometry", "fiber-bundles"]
prerequisites = ["differential-geometry/symplectic-manifold", "fiber-bundles/line-bundle", "fiber-bundles/connection-on-a-vector-bundle", "mathematical-physics/quantization-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]] and \(\hbar>0\). A **prequantization** consists of a Hermitian [[fiber-bundles/line-bundle|line bundle]] \(L\to M\) with a compatible [[fiber-bundles/connection-on-a-vector-bundle|connection]] whose curvature is the prescribed scalar multiple of \(\omega\), together with the induced [[mathematical-physics/quantization-map|quantization map]] on smooth sections of \(L\). With the conventions
\[
\iota_{X_f}\omega=-df,
\qquad F_\nabla=\frac{i}{\hbar}\omega,
\]
the Kostant–Souriau operator is
\[
Q_{\mathrm{pre}}(f)=i\hbar\nabla_{X_f}+f,
\]
and satisfies \([Q_{\mathrm{pre}}(f),Q_{\mathrm{pre}}(g)]=i\hbar Q_{\mathrm{pre}}(\{f,g\})\) on a common invariant domain.

## Integrality condition

Such a line bundle with connection exists precisely when the de Rham class \([\omega/(2\pi\hbar)]\) is integral, meaning that it lies in the image of \(H^2(M;\mathbb Z)\to H^2_{\mathrm{dR}}(M;\mathbb R)\). This is the prequantization condition on the symplectic form. Different prequantum bundles can remain when this condition holds; their ambiguity is governed by flat Hermitian line bundles.

## Why prequantization is not yet quantization

The prequantum Hilbert space is generally too large and the representation of observables is typically reducible. [[mathematical-physics/geometric-quantization|Geometric quantization]] therefore adds a polarization and, in many treatments, a half-form correction to select the physical state space. “Prequantization” names the line-bundle and operator stage before that reduction.

## Equivariant lifts

A [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian group action]] need not lift to the prequantum line bundle as an action preserving its Hermitian structure and connection. When a lift exists, it differentiates to the Kostant–Souriau operators associated with the [[differential-geometry/comoment-map|comoment map]]. Failure to lift can leave only a [[lie-groups/projective-unitary-representation|projective unitary representation]] of the original group or require passage to a [[algebra-groups/central-extension|central extension]].

## References

1. B. Kostant, “Quantization and Unitary Representations,” in C. T. Taam, ed., *Lectures in Modern Analysis and Applications III*, Lecture Notes in Mathematics 170, Springer, 1970, 87–208. [DOI record](https://doi.org/10.1007/BFb0079068). Relevant: prequantum line bundles and infinitesimal symmetry operators.
2. N. M. J. Woodhouse, *Geometric Quantization*, 2nd ed., Oxford University Press, 1992. [Publisher record](https://global.oup.com/academic/product/geometric-quantization-9780198502708). Relevant: Chapters 5–6, prequantization and polarized sections.
