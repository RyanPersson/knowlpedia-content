+++
id = "proofs/grh/reduction-zeros/g-one-and-chowla-selberg-constant"
title = "The constant c_1 for the modulus 1"
kind = "lemma"
summary = "For q = 1 the real part of G_1(1) is -1 minus the constant gamma - Re L'/L(1, chi_K)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.re_logDerivMean_one", "New.re_logDerivMean_one_eq_add_re_logDeriv"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
proof_status = "full"
+++

**Lemma.** Let \(d\) be a prime and let \(E=E_{\chi_K}\) be [[?lean:New.entireL|the \(L\)-function with the pole removed]] of the Legendre symbol \(\chi_K=(\cdot/d)\), regarded as the twist of the character modulo \(1\) (so \(E=L(\cdot,\chi_K)\) for odd \(d\)). Let \(\gamma\) be the [[?c:Euler–Mascheroni constant|Euler–Mascheroni constant]]. For the [[proofs/grh/reduction-zeros/log-deriv-mean|function \(G_1\)]] of modulus \(q=1\),
\[
\operatorname{Re}G_1(1)=-1-\gamma+\operatorname{Re}\frac{E'(1)}{E(1)}=-1-\Bigl(\gamma-\operatorname{Re}\frac{E'(1)}{E(1)}\Bigr).
\]
The number in brackets is the constant called [[?lean:New.chowlaSelbergConst|`chowlaSelbergConst`]] in the source.

## Proof

There is one character modulo \(1\), and its \(L\)-function with the pole removed is \(Z(s)=(s-1)\zeta(s)\). So \(G_1=E'/E-Z'/Z-1\). The logarithmic derivative of \(Z\) at \(1\) is \(\gamma\), because \(\zeta(s)=1/(s-1)+\gamma+O(s-1)\) gives \(Z(1)=1\), \(Z'(1)=\gamma\). \(\blacksquare\)

## References

1. Lean: `New.re_logDerivMean_one_eq_add_re_logDeriv`, `New.re_logDerivMean_one` in `src/New/Reduction/Zeros/PrimeError.lean`.
