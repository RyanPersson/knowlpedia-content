+++
id = "grh-lean/remainder-transform"
title = "Residues of the weighted prime remainder"
kind = "theorem"
summary = "An explicit transform recovers the difference between untwisted and twisted zero counts."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/prime-remainder-in-progression", "harmonic-analysis/laplace-transform", "complex-analysis/analytic-zero-order"]
+++

For the [[analytic-number-theory/prime-remainder-in-progression|quadratic prime remainder]] with \(d\equiv7\bmod8\) coprime to \(q\), put \(E(v)=R_{d,q}(e^v)\). The transform \(\int_0^\infty E(v)e^{(1-s)v}\,dv\) extends [[complex-analysis/meromorphic-function|meromorphically]] to \(\Re s>0\) with at most simple poles. For \(s\ne1\) there its [[complex-analysis/residue|residue]] is
\[
 \frac{\sum_{\chi\bmod q}(\operatorname{ord}_s F_\chi-\operatorname{ord}_s F_{\chi(\cdot/d)})}{\varphi(q)s(1-s)} .
\]

## Proof

In a right half-plane integrate the ramp weight \(1/n-1/x\) explicitly. The resulting [[analytic-number-theory/dirichlet-series|Dirichlet series]] is a difference of logarithmic derivatives because [[analytic-number-theory/von-mangoldt-function|von Mangoldt coefficients]] occur in \(-L'/L\). [[algebra-representation-theory/character-orthogonality|Character orthogonality]] restricts it to the identity class. The logarithmic and constant terms in the definition of \(R\) cancel the singular terms at \(1\). Now continue the expression from the right. A logarithmic derivative has a simple pole at a zero with [[complex-analysis/residue|residue]] its [[complex-analysis/analytic-zero-order|order]], which gives the numerator with the displayed sign.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.Reduction.Zeros.PrimeError:414).

## References

- [New/Reduction/Zeros/PrimeError.lean, isPolar_primeRemainder](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L414)
