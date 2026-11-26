+++
id = "grh-lean/regular-twists"
title = "Selecting twists with controlled denominators"
kind = "theorem"
summary = "One tame twist per comparison place meets simultaneous Selmer and special-value bounds."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["grh-lean/selmer-twisting", "grh-lean/projection-denominators", "arithmetic-geometry/padic-comparison-place"]
+++

For [[grh-lean/arithmetic-data|admissible data]] there is a family \(\xi_\iota\), one twist at each [[arithmetic-geometry/padic-comparison-place|comparison place]] \(\iota\) above \(\ell\). Its modulus is prime to \(\ell\). The first \(m\) powers satisfy the required inverse special-value bounds, and the weighted denominators of the projections to lifts fit a common budget.

## Proof

Describe the finitely many relevant systems of [[harmonic-analysis/hecke-eigensystem|Hecke eigenvalues]] by [[grh-lean/attached-representations|attached Galois summands]]. For each \(\iota\), use [[grh-lean/selmer-twisting|the simultaneous twisting theorem]] on these representations and on the systems controlling special values. Small Selmer lengths then give [[grh-lean/projection-denominators|a denominator bound for the projection to genuine lifts]]. The bounds can be summed over rational primes, and choosing one of the allowed twists at each \(\iota\) produces the family.

## References

- [New/Congruences/FitTwistsExist.lean, New.exists_isRegularFamily](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L517)
- [New/Determinant/Twist/FitTwists.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/FitTwists.lean)
