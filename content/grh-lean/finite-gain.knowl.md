+++
id = "grh-lean/finite-gain"
title = "Finite-place divisibility of the composite lift"
kind = "theorem"
summary = "Jet coefficients supply gains while collisions and exceptional levels incur a summable index loss."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/theta-jet", "grh-lean/jet-count", "arithmetic-geometry/twisted-lattice-index"]
+++

At a prime \(p\), after a source-lattice change of controlled [[arithmetic-geometry/colength-of-lattices|colength]], the composite lift has [[algebra-fields-galois/valuation-on-a-field|valuation]] at least \(g_p-e_p\). Here \(g_p\) is the prescribed gain, \(e_p\ge0\), and \(\sum_{p\in U} e_p\log p\le fa(\log b)^3\) for every [[shared-foundations/finite-set|finite set]] \(U\) of primes.

## Proof

Expand the chain into products of [[harmonic-analysis/theta-jet|theta jets]]. At a nonsplit prime the [[grh-lean/jet-count|local jet count]] gives the gain unless several places impose the same condition. Sparsity bounds the cost of collisions. At exceptional primes one marks the colliding places and changes the source using normalized [[harmonic-analysis/hecke-operator|Hecke operators]]. Their [[algebra-modules/elementary-divisor-theorem|elementary divisors]] control the resulting [[arithmetic-geometry/twisted-lattice-index|index loss]]. Handle the level prime separately, and add the errors with weights \(\log p\). This produces the single budget valid for all finite sets of primes.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#module=New.UpperBound.Divisibility.LocalDivisibility).

## References

- [New/UpperBound/Divisibility/LocalDivisibility.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/LocalDivisibility.lean)
- [New/Reduction/ShortAndEnough.lean, exists_colengthDvd_gaugeLe_divisibilityError](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L74)
- [New/Reduction/ShortAndEnough.lean, sum_divisibilityError_mul_log_le](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L56)
