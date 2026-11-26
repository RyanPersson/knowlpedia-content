+++
id = "proofs/grh/reduction-zeros/lower-bound-right-of-one"
title = "A lower bound for L-functions to the right of the line Re s = 1"
kind = "proposition"
summary = "From the 3-4-1 inequality: eta^3 <= 256 l^7 |f_chi(s)|^4 for Re s >= 1 + eta, and |f_chi(s)| >= 12/l^22 for Re s >= 1 + l^(-25)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.pow_three_le_mul_norm_regularL_pow", "New.div_pow_le_norm_regularL", "New.eventually_le_norm_regularL"]
lean_files = ["src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean"]
proof_status = "full"
+++

**Proposition.** Let \(\chi\) be a Dirichlet character modulo \(N\ge1\), \(\mathfrak{f}_\chi\) its [[proofs/grh/reduction-zeros/regularised-l-function|regularised \(L\)-function]], and \(l\ge10^{10}\) with \(N\le e^{l}\).

1. Let \(0<\eta\le1\), \(\operatorname{Re}s\ge1+\eta\), \(\lvert s\rvert\le\tfrac32e^{l}\), and suppose that \(\chi^{2}\) is not principal or \(\lvert s-1\rvert\ge1/l\). Then \(\eta^{3}\le256\,l^{7}\,\lvert\mathfrak{f}_\chi(s)\rvert^{4}\).
2. Suppose that, if \(\chi^2\) is principal, \(\lvert\mathfrak{f}_\chi(z)\rvert\ge1/l\) for all \(z\) with \(\lvert z-1\rvert\le1/l\). Then \(\lvert\mathfrak{f}_\chi(s)\rvert\ge12/l^{22}\) for \(\operatorname{Re}s\ge1+l^{-25}\), \(\lvert s\rvert\le\tfrac32e^{l}\).
3. For every \(\chi\) there is \(r_0>0\) such that for \(0<r\le r_0\): \(\lvert\mathfrak{f}_\chi(z)\rvert\ge r\) whenever \(\lvert z-1\rvert\le r\).

## Proof

1. Write \(s=\sigma+it\) and \(s_2=\sigma+2it\). The [[?c:3-4-1 inequality for Dirichlet L-functions|3-4-1 inequality]] gives \(\lvert L(\sigma,\chi_0)\rvert^{3}\lvert L(s,\chi)\rvert^{4}\lvert L(s_2,\chi^{2})\rvert\ge1\), with \(\chi_0\) principal modulo \(N\). By the [[proofs/grh/reduction-zeros/bound-regular-l-near-one-line|growth bounds]]: \(\lvert L(\sigma,\chi_0)\rvert\le1+1/\eta\le2/\eta\); \(\lvert L(s,\chi)\rvert\le2l\lvert\mathfrak{f}_\chi(s)\rvert\) (if \(\chi\) is principal so is \(\chi^2\), hence \(\lvert s-1\rvert\ge1/l\)); and \(\lvert L(s_2,\chi^{2})\rvert\le2l\lvert\mathfrak{f}_{\chi^2}(s_2)\rvert\le2l\cdot l^{2}\), using \(\lvert s_2-1\rvert\ge\lvert s-1\rvert\), \(\lvert s_2\rvert\le2\lvert s\rvert\le3e^{l}\). Hence \(1\le(2/\eta)^{3}(2l)^{4}\lvert\mathfrak{f}_\chi(s)\rvert^{4}\cdot2l^{3}=256\,l^{7}\lvert\mathfrak{f}_\chi(s)\rvert^4/\eta^{3}\).

2. If \(\chi^{2}\) is principal and \(\lvert s-1\rvert<1/l\), the hypothesis gives \(\lvert\mathfrak{f}_\chi(s)\rvert\ge1/l\ge12/l^{22}\). Otherwise part 1 with \(\eta=l^{-25}\) gives \(\lvert\mathfrak{f}_\chi(s)\rvert^{4}\ge l^{-75}/(256l^{7})=l^{6}/(256\,l^{88})\ge12^{4}/l^{88}\), since \(256\cdot12^{4}\le l^{6}\).

3. \(\mathfrak{f}_\chi(1)=E_\chi(1)\ne0\) by the [[proofs/grh/reduction-zeros/entire-l-basic-properties|basic properties]], and \(\mathfrak{f}_\chi\) is continuous at \(1\): take \(r_0\le\lvert\mathfrak{f}_\chi(1)\rvert/2\) so small that \(\lvert\mathfrak{f}_\chi\rvert\ge\lvert\mathfrak{f}_\chi(1)\rvert/2\) on \(\lvert z-1\rvert\le r_0\). \(\blacksquare\)

## References

1. Lean: `New.pow_three_le_mul_norm_regularL_pow`, `New.div_pow_le_norm_regularL`, `New.eventually_le_norm_regularL` in `src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean`.
