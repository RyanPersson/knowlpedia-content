+++
id = "grh-lean/projection-denominators"
title = "Clearing the denominators of the lift projector"
kind = "theorem"
summary = "First-order congruences translate bounds on extensions into bounds on a projection."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/selmer-group", "harmonic-analysis/hecke-eigensystem"]
+++

In the lift setting, upper bounds for the twisted [[arithmetic-geometry/selmer-group|Selmer lengths]] of the main summands bound the denominators of projection onto the genuine lifted [[harmonic-analysis/hecke-eigensystem|Hecke eigenspaces]] on forms orthogonal to the [[harmonic-analysis/false-lift-subspace|false lifts]].

## Proof

A [[linear-algebra/projector-denominator|denominator of the projection]] measures a congruence between the wanted eigensystems and the other eigensystems. Use [[grh-lean/auxiliary-primes|auxiliary primes in triangular order]] to bound the even classes of the [[arithmetic-geometry/tate-twist|Tate twists]]. Separate the local lift types by their Hecke polynomials. From the first-order congruence one extracts extension classes with the specified local conditions. The Selmer-length estimate bounds the possible congruence. Construct an operator that preserves the eigenspaces, carries the projected integral forms to integral forms and has bounded eigenvalue [[algebra-fields-galois/valuation-on-a-field|valuations]]. Taking its [[linear-algebra/determinant|determinant]] and accounting for the finite group order gives the clearing bound.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.Congruences.FirstOrder.DenominatorBound:1321).

## References

- [New/Congruences/FirstOrder/DenominatorBound.lean, denominatorLe_clearingBound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/DenominatorBound.lean#L1321)
- [New/Congruences/FirstOrder/DenominatorBound.lean, exists_operator_ellVal_le_liftValuationBound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/DenominatorBound.lean#L1156)
