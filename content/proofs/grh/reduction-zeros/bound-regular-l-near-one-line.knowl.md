+++
id = "proofs/grh/reduction-zeros/bound-regular-l-near-one-line"
title = "Growth of the regularised L-function near the line Re s = 1"
kind = "proposition"
summary = "For l >= 10^10 and N <= e^l: |f_chi(s)| <= l^2 on Re s >= 1 - 1/l, |s| <= 3e^l, and |f_chi'(s)| <= 2l^3 on Re s >= 1 - 1/(2l), |s| <= 2e^l."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_regularL_le_sq", "New.norm_deriv_regularL_le", "New.norm_LSeries_char_le", "New.norm_LSeries_le_mul_norm_regularL"]
lean_files = ["src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean"]
proof_status = "full"
+++

**Proposition.** Let \(\chi\) be a Dirichlet character modulo \(N\ge1\) with [[proofs/grh/reduction-zeros/regularised-l-function|regularised \(L\)-function]] \(\mathfrak{f}_\chi\). Let \(l\ge10^{10}\) be real with \(N\le e^{l}\).

1. If \(A>0\) and \(\operatorname{Re}s\ge1+1/A\), then \(\lvert L(s,\chi)\rvert\le1+A\).
2. If \(\operatorname{Re}s>1\) and, in case \(\chi\) is principal, \(\lvert s-1\rvert\ge1/l\), then \(\lvert L(s,\chi)\rvert\le2l\,\lvert\mathfrak{f}_\chi(s)\rvert\).
3. If \(\operatorname{Re}s\ge1-1/l\) and \(\lvert s\rvert\le3e^{l}\), then \(\lvert\mathfrak{f}_\chi(s)\rvert\le l^{2}\).
4. If \(\operatorname{Re}s\ge1-1/(2l)\) and \(\lvert s\rvert\le2e^{l}\), then \(\lvert\mathfrak{f}_\chi'(s)\rvert\le2l^{3}\).

(Parts 1 and 2 need only \(l\ge1\) and no bound on \(N\).)

## Proof

1. \(\lvert L(s,\chi)\rvert\le\zeta(\sigma)\le1+1/(\sigma-1)\) with \(\sigma=\operatorname{Re}s\), and \(1/(\sigma-1)\le A\).

2. \(L(s,\chi)=\mathfrak{f}_\chi(s)\,s/(s-\delta_\chi)\), so it suffices that \(\lvert s\rvert\le2l\lvert s-\delta_\chi\rvert\). For non-principal \(\chi\) this is clear. For principal \(\chi\): \(\lvert s\rvert\le\lvert s-1\rvert+1\le\lvert s-1\rvert(1+l)\le2l\lvert s-1\rvert\).

3. Let \(a=\operatorname{Re}s+2/l-\tfrac13\) and \(g(z)=\mathfrak{f}_\chi(z)/(z-s+2)\) on the strip \(a\le\operatorname{Re}z\le a+\tfrac13\). There \(\operatorname{Re}z\ge a\ge\tfrac23-\tfrac1l>\tfrac12\) and \(\operatorname{Re}(z-s+2)\ge\tfrac53+\tfrac2l\ge1\), so \(g\) is holomorphic and \(\lvert z-s+2\rvert\ge1\).

 *On the whole strip.* \(\lvert z\rvert\le\lvert z-s+2\rvert+3e^{l}+2\le4e^{l}\lvert z-s+2\rvert\), so by the [[proofs/grh/reduction-zeros/linear-bound-regular-l|linear bound]], \(\lvert\mathfrak{f}_\chi(z)\rvert\le1+4e^{l}\lvert z\rvert\le(1+16e^{2l})\lvert z-s+2\rvert\le e^{3l}\lvert z-s+2\rvert\). Thus \(\lvert g\rvert\le e^{3l}\).

 *On the right edge* \(\operatorname{Re}z=\operatorname{Re}s+2/l\ge1+1/l\): \(\lvert g(z)\rvert\le\lvert\mathfrak{f}_\chi(z)\rvert\le\lvert L(z,\chi)\rvert\le1+l\), by part 1 and \(\lvert z-\delta_\chi\rvert\le\lvert z\rvert\).

 The point \(s\) lies at the fraction \((\operatorname{Re}s-a)/(1/3)=1-6/l\) of the way from the left to the right edge. By the [[?c:Hadamard three-lines theorem|three-lines theorem]],
\[
\lvert g(s)\rvert\le(e^{3l})^{6/l}(1+l)^{1-6/l}\le e^{18}(1+l)\le3^{18}(1+l).
\]
Since \(g(s)=\mathfrak{f}_\chi(s)/2\), we get \(\lvert\mathfrak{f}_\chi(s)\rvert\le2\cdot3^{18}(1+l)\le l^{2}\) for \(l\ge10^{10}\).

4. Every \(z\) in the closed disc of radius \(1/(2l)\) about \(s\) has \(\operatorname{Re}z\ge1-1/l\) and \(\lvert z\rvert\le2e^{l}+1\le3e^{l}\). By part 3, \(\lvert\mathfrak{f}_\chi\rvert\le l^{2}\) on the circle, and the [[complex-analysis/cauchy-derivative-estimate|Cauchy estimate]] gives \(\lvert\mathfrak{f}_\chi'(s)\rvert\le l^{2}/(1/(2l))=2l^{3}\). \(\blacksquare\)

## References

1. Lean: `New.norm_LSeries_char_le`, `New.norm_LSeries_le_mul_norm_regularL`, `New.norm_regularL_le_sq`, `New.norm_deriv_regularL_le` in `src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, 2007, Lemma 10.15 (cited in the head of the Lean file; here with a square in place of the first power of the logarithm).
