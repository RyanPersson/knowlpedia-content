+++
id = "proofs/grh/reduction-zeros/newman-circle-bound"
title = "The bound on the circle in Newman's method"
kind = "lemma"
summary = "On |z| = 1/X the function F(z) - zP(z) is at most 3U times the modulus of exp(2 - Uz - X(1+Xz)^2/4), when the coefficients are dominated in the window by a series convergent at 3/4."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_sub_mul_sum_term_le", "New.norm_le_of_term_le_majorant", "New.exists_shift_le_re_exponent", "New.norm_term_le_exp_mul"]
lean_files = ["src/Lib/Analytic/Primes.lean"]
proof_status = "full"
+++

**Lemma.** Let \(a\colon\mathbb{N}\to[0,\infty)\), \(b\colon\mathbb{N}\to\mathbb{C}\), \(F\colon\mathbb{C}\to\mathbb{C}\), and reals \(X\ge200\), \(U\ge X^{2}\), \(C\le X\) be such that

* \(\sum_{n\ge1}a(n)n^{-1-z}=F(z)/z\) for \(\operatorname{Re}z>0\);
* \(\lvert F(z)\rvert\le2\) for \(\lvert z\rvert\le1/X\);
* \(\sum_{n\ge1}\lvert b(n)\rvert n^{-3/4}=C\);
* \(a(n)\le\lvert b(n)\rvert\) whenever \(U\le\log n\le U+X^{2}\).

Let \(P(z)=\sum_{n<e^{U}}a(n)n^{-1-z}\). Then for all \(z\) with \(\lvert z\rvert=1/X\),
\[
\lvert F(z)-zP(z)\rvert\le3U\,e^{E(z)},\qquad E(z)=\operatorname{Re}\bigl(2-Uz-\tfrac X4(1+Xz)^{2}\bigr).
\]

## Proof

Write \(x=\operatorname{Re}z\).

*The exponent.* On \(\lvert z\rvert=1/X\) one has \(X^{2}(\operatorname{Im}z)^{2}=1-X^{2}x^{2}\), so \(\operatorname{Re}(1+Xz)^{2}=2Xx(1+Xx)\) and
\[
E(z)=2-(U+t)\,x,\qquad t=\tfrac{X^{2}}2(1+Xx)\in[0,X^{2}].
\]

*Moving a term.* \(\lvert n^{-1-z}\rvert=n^{\sigma-x}\,n^{-1-\sigma}\) for real \(\sigma\). So if \(\log n\,(\sigma-x)\le E\), the \(n\)-th term at \(1+z\) is at most \(e^{E}\) times the \(n\)-th term at \(1+\sigma\). We use \(\sigma=1/U\) for \(a\), where \(\sum a(n)n^{-1-1/U}=U\,F(1/U)\le2U\) (as \(1/U\le1/X\)), and \(\sigma=-\tfrac14\) for \(b\), with total \(C\le X\le U\). So any part of the series of \(a\) at \(1+z\) whose terms are dominated in this way is at most \(e^{E}(2U+C)\le3Ue^{E}\).

*Case \(x\le1/U\).* For \(n<e^{U}\): \(\log n(1/U-x)\le U(1/U-x)=1-Ux\le E\), because \(tx\le t/U\le1\). Hence \(\lvert P(z)\rvert\le3Ue^{E}\). Also \(E\ge0\) (as \(Ux\le1\), \(tx\le1\)). So \(\lvert F(z)-zP(z)\rvert\le2+\tfrac1{200}3Ue^{E}\le3Ue^{E}\).

*Case \(x\ge1/U\).* Then \(F(z)/z-P(z)=\sum_{n\ge e^{U}}a(n)n^{-1-z}\). For \(U\le\log n\le U+X^{2}\) we have \(a(n)\le\lvert b(n)\rvert\) and \(\log n(-\tfrac14-x)\le U(-\tfrac14-x)\le E\), because \(tx\le X^{2}/X\le U/200\). For \(\log n>U+X^{2}\ge U+t\): \(\log n(1/U-x)\le(U+t)(1/U-x)\le2-(U+t)x=E\). So the tail is at most \(3Ue^{E}\), and \(\lvert F(z)-zP(z)\rvert=\lvert z\rvert\cdot\lvert F(z)/z-P(z)\rvert\le3Ue^{E}\). \(\blacksquare\)

## References

1. Lean: `New.exists_shift_le_re_exponent`, `New.norm_term_le_exp_mul`, `New.norm_le_of_term_le_majorant`, `New.norm_sub_mul_sum_term_le` in `src/Lib/Analytic/Primes.lean`.
