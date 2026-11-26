+++
id = "proofs/grh/reduction-zeros/zero-free-region"
title = "A zero-free region for Dirichlet L-functions"
kind = "theorem"
summary = "For large l the L-function with the pole removed has no zero on Re s >= 1 - l^(-25), |s| <= e^l, and its logarithmic derivative is at most 2 l^25 there."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.eventually_norm_logDeriv_entireL_le", "New.norm_logDeriv_entireL_le", "New.norm_logDeriv_regularL_le"]
lean_files = ["src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean"]
proof_status = "full"
+++

**Theorem.** Let \(\chi\) be a complex [[?c:Dirichlet character|Dirichlet character]] modulo \(N\ge1\), \(E_\chi\) [[?lean:New.entireL|its \(L\)-function with the pole removed]] and \(\mathfrak{f}_\chi\) the [[proofs/grh/reduction-zeros/regularised-l-function|regularised \(L\)-function]].

1. (Uniform form.) Let \(l\ge10^{10}\) with \(N\le e^{l}\), and suppose that, if \(\chi^{2}\) is principal, \(\lvert\mathfrak{f}_\chi(z)\rvert\ge1/l\) whenever \(\lvert z-1\rvert\le1/l\). Then for all \(s\) with \(\operatorname{Re}s\ge1-l^{-25}\) and \(\lvert s\rvert\le e^{l}\):
\[
E_\chi(s)\ne0\qquad\text{and}\qquad\Bigl\lvert\frac{E_\chi'(s)}{E_\chi(s)}\Bigr\rvert\le2\,l^{25}.
\]
2. (Fixed character.) There is \(l_0=l_0(\chi)\) such that the conclusion of 1 holds for all \(l\ge l_0\).

## Proof

1. Let \(\eta=l^{-25}\) and \(v=s+2\eta\). Every \(z\) with \(\lvert z-s\rvert\le2\eta\) has \(\operatorname{Re}z\ge1-3\eta\ge1-1/(2l)\) and \(\lvert z\rvert\le e^{l}+2\eta\le2e^{l}\), so \(\lvert\mathfrak{f}_\chi'(z)\rvert\le2l^{3}\) by the [[proofs/grh/reduction-zeros/bound-regular-l-near-one-line|derivative bound]]. Hence \(\lvert\mathfrak{f}_\chi(v)-\mathfrak{f}_\chi(s)\rvert\le2l^{3}\cdot2\eta=4/l^{22}\). Since \(\operatorname{Re}v\ge1+\eta\) and \(\lvert v\rvert\le\tfrac32e^{l}\), the [[proofs/grh/reduction-zeros/lower-bound-right-of-one|lower bound]] gives \(\lvert\mathfrak{f}_\chi(v)\rvert\ge12/l^{22}\). So \(\lvert\mathfrak{f}_\chi(s)\rvert\ge8/l^{22}>0\) and
\[
\Bigl\lvert\frac{\mathfrak{f}_\chi'(s)}{\mathfrak{f}_\chi(s)}\Bigr\rvert\le\frac{2l^{3}\,l^{22}}{8}=\frac{l^{25}}4 .
\]
Now \(E_\chi=u\,\mathfrak{f}_\chi\) with \(u(s)=s\) or \(u=1\). As \(\operatorname{Re}s\ge\tfrac12\), \(u(s)\ne0\), so \(E_\chi(s)\ne0\), and \(E_\chi'/E_\chi=\mathfrak{f}_\chi'/\mathfrak{f}_\chi+u'/u\) with \(\lvert u'(s)/u(s)\rvert\le1/\lvert s\rvert\le2\). Since \(2\le l^{25}\), the sum is at most \(2l^{25}\).

2. Take \(l\ge10^{10}\), \(l\ge N\) (so \(N\le l\le e^{l}\)) and \(1/l\le r_0\), where \(r_0\) is from part 3 of the lower bound; then the hypothesis of 1 holds. \(\blacksquare\)

## Remarks

This is the classical zero-free region in the crude form that the 3-4-1 inequality gives directly, with a power of \(\log\lvert s\rvert\). For characters with \(\chi^2\) principal the points near \(1\) are handled by \(\mathfrak f_\chi(1)\ne0\) and continuity, so \(l_0\) depends on \(\chi\) (no uniformity in the modulus is claimed in part 2).

## References

1. Lean: `New.norm_logDeriv_regularL_le`, `New.norm_logDeriv_entireL_le`, `New.eventually_norm_logDeriv_entireL_le` in `src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, 2007, Chapter 11 (as cited in the head of the Lean file).
