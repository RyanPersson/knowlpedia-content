+++
id = "grh-lean/prime-identity"
title = "Recovering the prime remainder from the place sum"
kind = "theorem"
summary = "Two weights isolate one residue class and cancel the common main terms."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/prime-remainder-in-progression", "grh-lean/arithmetic-data"]
+++

For [[grh-lean/arithmetic-data|admissible data]], write \(R_q(y)=R_{d,q}(y)\) for the [[analytic-number-theory/prime-remainder-in-progression|prime remainder]]. The total remainder of the place sums is exactly
\[
 R=a\bigl(|\Phi_b|(R_{q_0}(x)-R_{q_0}(x_1))+|\Phi_a|R_1(x_1)\bigr).
\]

## Proof

Fix an integer \(n\) in the prime-power sum. Multiplication by its place class shows that as \(\tau\) ranges over \(\Phi_a\), exactly \(|\Phi_b|\) of the translated places \(-n\tau\) lie in \(\Phi_b\) if \(n\equiv1\bmod q_0\), and none otherwise. Subtract the common cutoff \(x_1\) from the new cutoff \(x\) at precisely those places. The positive-part weight becomes \(a(1/n-1/y)\) on \(n\le y\).

Sum over \(n\) and subtract the expected main term. The logarithms and the constant for modulus \(1\) cancel against it. The two copies of the constant for \(q_0\) cancel between cutoffs. Finally \(f=\varphi(q_0)|\Phi_a|\) and \(|\Phi_a|/|\Phi_b|\le\log b\). Dividing by \(a|\Phi_b|\) converts a one-sided bound for \(R\) into one for \(R_{q_0}(x)\).

## References

- [New/Reduction/PrimeSums.lean, totalRemainder_eq](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L177)
