+++
id = "grh-lean/jet-sharpness"
title = "A coefficient attains the local jet bound"
kind = "theorem"
summary = "Fourier inversion exhibits an indicator datum whose coefficient survives to the required precision."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/theta-jet", "linear-algebra/tight-frame", "analytic-number-theory/finite-fourier-inversion"]
+++

At each prime, among the admissible nearby degrees and indicator data, there is a theta coefficient whose valuation, after factorial and fixed scalar normalizations, is at most the predicted local prime sum plus the valuation of one common scalar of controlled conjugate size.

## Proof

Use the functions attached to a [[linear-algebra/tight-frame|tight frame]] on the CM lattice to express a theta product times monomials as the Taylor expansion of a vector with integral values. Its restriction to a curve supplies a coefficient at the required precision. [[analytic-number-theory/finite-fourier-inversion|Finite Fourier inversion]] writes the vector in translates of the vacuum. Those translates are combinations of indicator data with roots of unity as coefficients. If every contributing coefficient had larger valuation, the recovered coefficient would also have larger valuation. One therefore attains the required upper bound.

## References

- [New/Derivatives/Sharpness/BoundAttained.lean, exists_rpow_neg_localPrimeSumTotal_le_norm_coeff](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L381)
