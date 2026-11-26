+++
id = "grh-lean/real-cutoffs"
title = "The upper bound at every large real cutoff"
kind = "theorem"
summary = "Construct data at the integer part of the cutoff, estimate the tails, and pass to the real variable."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/prime-remainder-in-progression", "grh-lean/integer-cutoffs"]
+++

For a positive modulus \(q_0\) divisible by \(18480\), a prime \(d\equiv q_0/2-1\bmod q_0\), and every \(\epsilon>0\), the [[analytic-number-theory/prime-remainder-in-progression|prime remainder]] satisfies \(R_{d,q_0}(y)\le y^{-1/2+\epsilon}\) for every sufficiently large real \(y\).

## Proof

Choose \(0<\delta<1/100\) with \(7\delta\le\epsilon\). The [[grh-lean/integer-cutoffs|integer-cutoff estimate]] gives \(R_{d,q_0}(x)\le Cx^{-1/2+6\delta}\). For \(x=\lfloor y\rfloor\) the set of [[analytic-number-theory/prime-power|prime powers]] in the sum is unchanged. Estimating the change in the weight and the logarithm gives \(R(y)-R(\lfloor y\rfloor)\le26/y\). For \(y\ge2\), \(\lfloor y\rfloor\ge y/2\). Absorb the fixed constants using \(y^\delta\), which tends to infinity.

## References

- [New/Reduction/OneSidedBound.lean, eventually_primeRemainder_le_rpow](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L200)
