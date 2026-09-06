+++
id = "mathematical-physics/geometric-quantization"
title = "Geometric quantization"
kind = "definition"
summary = "A method that constructs a quantum state space from prequantum line-bundle data and a polarization of a symplectic manifold."
aliases = ["Kostant-Souriau geometric quantization", "polarized geometric quantization"]
domains = ["mathematical-physics", "differential-geometry", "fiber-bundles"]
section_mode = "progressive"
prerequisites = ["differential-geometry/symplectic-manifold", "mathematical-physics/prequantization"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Geometric quantization** is a procedure that starts from a [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\), chooses [[mathematical-physics/prequantization|prequantum]] line-bundle data, and then chooses a polarization \(P\) to reduce the prequantum sections to quantum states. Schematically, its Hilbert space is obtained by completing a suitable space of sections \(s\) satisfying
\[
\nabla_Xs=0\qquad (X\in P),
\]
with modifications when polarized sections are distributional or when a half-form correction is used. Only observables whose Hamiltonian flows preserve the polarization act directly by the prequantum operator on this polarized state space.

## Polarizations

A real polarization is, roughly, an integrable Lagrangian distribution in the tangent bundle, while a complex polarization is an integrable Lagrangian subbundle of the complexified tangent bundle satisfying additional reality conditions. Kähler polarizations are the best-behaved complex examples: polarized sections become holomorphic sections of the prequantum line bundle.

The choice is essential rather than cosmetic. Different polarizations can give different concrete realizations of the same quantum theory, and comparison between them requires additional transforms or pairing constructions.

## Half-form correction

When an appropriate square root of the canonical bundle along the polarization exists, tensoring by this half-form bundle corrects the measure and operator formulas. The correction is responsible for familiar shifts in spectra and improves the behavior of quantization under changes of polarization.

## Relation to representations

If a [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian Lie group action]] lifts to the prequantum bundle and preserves the polarization, it acts on the polarized state space. The result may be a genuine [[lie-groups/strongly-continuous-unitary-representation|unitary representation]] of a lifted group and only a [[lie-groups/projective-unitary-representation|projective representation]] of the original symmetry group. The [[lie-groups/metaplectic-representation|metaplectic representation]] is the basic linear example involving the half-form phenomenon.

## References

1. B. Kostant, “Quantization and Unitary Representations,” in C. T. Taam, ed., *Lectures in Modern Analysis and Applications III*, Lecture Notes in Mathematics 170, Springer, 1970, 87–208. [DOI record](https://doi.org/10.1007/BFb0079068). Relevant: polarizations and induced unitary representations.
2. N. M. J. Woodhouse, *Geometric Quantization*, 2nd ed., Oxford University Press, 1992. [Publisher record](https://global.oup.com/academic/product/geometric-quantization-9780198502708). Relevant: Chapters 4–10, prequantization, polarizations, and half-forms.
