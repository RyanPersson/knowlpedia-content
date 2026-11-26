+++
id = "grh-lean/zero-criterion"
title = "A one-sided prime-sum criterion for nonvanishing"
kind = "theorem"
summary = "Avoid twisted zeros, compute a residue, and apply positivity to the transform."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/prime-remainder-in-progression", "grh-lean/twist-avoidance", "grh-lean/remainder-transform", "grh-lean/landau"]
+++

Let \(8\mid q\), \(q>0\), \(\gcd(d_0,q)=1\), \(d_0\equiv7\bmod8\), and \(\beta>1/2\). Suppose that for every prime \(d\equiv d_0\bmod q\) the [[analytic-number-theory/prime-remainder-in-progression|remainder]] satisfies \(R_{d,q}(x)\le x^{\beta-1}\) for all sufficiently large \(x\). Then for every \(\psi\bmod q\), \(L(\rho,\psi)\ne0\) when \(\Re\rho>\beta\) and \(\rho\ne1\).

## Proof

Fix \(\rho\). Choose [[grh-lean/twist-avoidance|one twist avoiding zeros]] for all the characters at once, with height bound \(|\Im\rho|\). In this region the [[grh-lean/remainder-transform|residue formula]] reduces to
\[
 r(s)=\frac{\sum_{\psi\bmod q}\operatorname{ord}_s F_\psi}{\varphi(q)s(1-s)}
\]
away from \(0,1\), where \(F_\psi\) is the [[analytic-number-theory/entire-dirichlet-l-function|pole-removed function]]. At real points between \(\beta\) and \(1\) the [[complex-analysis/residue|residue]] is nonnegative. From \(1\) onward the pole-removed functions are nonzero and the residue vanishes.

The hypothesis supplies the one-sided exponential bound needed by [[grh-lean/landau|Landau’s argument]]. It gives \(r(\rho)=0\). The numerator is a sum of nonnegative [[complex-analysis/analytic-zero-order|orders of vanishing]], so each order is zero. Since \(\rho\ne1\), this gives the assertion for the original \(L\)-function.

## References

- [New/Reduction/Zeros/Criterion.lean, New.LFunction_ne_zero_of_primeRemainder_le](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/Criterion.lean#L37)
