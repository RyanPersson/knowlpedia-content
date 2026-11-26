+++
id = "grh-lean/selmer-twisting"
title = "Controlling Selmer groups by a simultaneous tame twist"
kind = "theorem"
summary = "Auxiliary local conditions suppress the surviving global classes across several representations."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/selmer-group", "arithmetic-geometry/anticyclotomic-character", "arithmetic-geometry/galois-cohomology"]
+++

For the finite collection of main summands and special-value data in the twist construction, a tame character can be chosen so that each of its first \(m\) powers has the imposed ramification bounds, short twisted [[arithmetic-geometry/selmer-group|Selmer groups]] and bounded [[algebra-fields-galois/valuation-on-a-field|valuations]] of the required special-value ratios.

## Proof

A [[arithmetic-geometry/selmer-group|Selmer condition]] selects global [[arithmetic-geometry/galois-cohomology|cohomology classes]] by their restrictions at the places of the field. Present the main summands as lattices with local conditions, and add the systems encoding the special values. The [[grh-lean/twist-polynomials|polynomial specialization argument]] chooses auxiliary ramification and a single character for this finite list. Its restriction estimates give bounds for the lengths with divisible coefficients. Read the resulting Galois character as the local realization of the tame character used by the lifts. The same choice works for the required powers.

## References

- [New/Congruences/Selmer/TwistingTheorem.lean, exists_mFoldTwist_hasDivisibleSelmerLengthLe](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/TwistingTheorem.lean#L370)
- [New/Congruences/Selmer/GeneralTheorem.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean)
