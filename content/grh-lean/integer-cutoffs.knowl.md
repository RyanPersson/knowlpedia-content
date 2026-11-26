+++
id = "grh-lean/integer-cutoffs"
title = "The prime bound at every large integer"
kind = "theorem"
summary = "The chain length saves a square root and the larger cutoff absorbs the analytic error."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["grh-lean/admissibility", "grh-lean/prime-identity", "grh-lean/main-inequality", "analytic-number-theory/prime-number-theorem-progressions"]
+++

Fix the modulus and prime of the [[grh-lean/arithmetic-data|arithmetic data]], and \(0<\delta<1/100\). For all sufficiently large integers \(x\), \(R_{d,q_0}(x)\le(64\varphi(q_0)+3)x^{-1/2+6\delta}\).

## Proof

Use [[grh-lean/admissibility|existence of admissible data]] with \(m\ge\sqrt x,\ \log b\le2x^\delta,\ \log x_1\ge x^{\delta/12}\). The [[grh-lean/main-inequality|covolume comparison]] and [[grh-lean/prime-identity|prime-sum identity]] give
\[
 R_{d,q_0}(x)\le\frac{\varphi(q_0)(\log b)^6}{m}
             +|R_{d,q_0}(x_1)|+\log b\,|R_{d,1}(x_1)|.
\]
The first term has size at most \(64\varphi(q_0)x^{-1/2+6\delta}\). For fixed \(d,q_0\), [[grh-lean/tail-bound|the prime number theorem at the larger cutoff]] makes both errors smaller than the remaining allowance. All three estimates apply at the same \(x\).

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.Reduction.OneSidedBound:125).

## References

- [New/Reduction/OneSidedBound.lean, eventually_primeRemainder_natCast_le](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L125)
- [New/Reduction/OneSidedBound.lean, Data.primeRemainder_le](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L33)
