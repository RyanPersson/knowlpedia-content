+++
id = "proofs/grh/reduction-zeros/prime-in-log-window"
title = "A prime congruent to 1 modulo M^k with logarithm in a window"
kind = "theorem"
summary = "For 4 | M and fixed A, for large W there is a prime p = 1 mod M^k with U <= log p <= U + W whenever k > 1, M^k <= W^A and W <= U <= W^A."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_prime_modEq_one_log_mem", "New.hasSum_residueClass_one", "New.summable_vonMangoldt_not_prime", "New.norm_one_sub_mul_sum_div_totient_le", "New.analyticOnNhd_sub_mul_sum_term"]
lean_files = ["src/Lib/Analytic/Primes.lean"]
proof_status = "full"
+++

**Theorem.** Let \(M\ge1\) with \(4\mid M\) and let \(A\ge0\) be an integer. There is \(W_0\) such that for all real \(W\ge W_0\), all integers \(k>1\) with \(M^{k}\le W^{A}\) and all real \(U\) with \(W\le U\le W^{A}\), there is a prime \(p\) with
\[
p\equiv1\pmod{M^{k}}\qquad\text{and}\qquad U\le\log p\le U+W .
\]

## Proof

Write \(W=X^{2}\), \(q=M^{k}\le X^{2A}\), and let \(X\) be large. Let \(a(n)=\Lambda(n)\) if \(n\equiv1\pmod q\) and \(a(n)=0\) otherwise ([[?c:von Mangoldt function|von Mangoldt function]]), and
\[
F(z)=\frac1{\varphi(q)}\Bigl(1-z\sum_{\chi\bmod q}\frac{E_\chi'(1+z)}{E_\chi(1+z)}\Bigr).
\]

*The series.* For \(\operatorname{Re}z>0\), by [[?c:orthogonality of Dirichlet characters|orthogonality]] and the [[proofs/grh/reduction-zeros/dirichlet-series-of-chi-lambda|series of \(\chi\Lambda\)]]: \(\sum a(n)n^{-1-z}=\frac1{\varphi(q)}\sum_\chi\bigl(\delta_\chi/z-E_\chi'/E_\chi(1+z)\bigr)=F(z)/z\).

*The disc.* By the [[proofs/grh/reduction-zeros/zero-free-disc-uniform|uniform zero-free disc]] (with \(2A\) in place of \(A\)), for \(\lvert z\rvert\le1/X\) no \(E_\chi(1+z)\) vanishes and \(\lvert zE_\chi'/E_\chi(1+z)\rvert\le1\). So \(F\) is holomorphic on \(\lvert z\rvert\le1/X\), and \(\lvert F\rvert\le(1+\varphi(q))/\varphi(q)\le2\) there.

*The comparison series.* Let \(b(n)=\Lambda(n)\) if \(n\) is not prime and \(b(n)=0\) if \(n\) is prime. Since \(\sum_{n\le x}b(n)=\psi(x)-\theta(x)=O(\sqrt x)\) ([[?c:Chebyshev bound for the psi function|Chebyshev]]), \(C=\sum b(n)n^{-3/4}<\infty\). Take \(X\ge\max(200,C)\).

*Contradiction.* Suppose no prime \(p\equiv1\pmod q\) has \(\log p\in[U,U+X^{2}]\). Then \(a(n)\le b(n)\) for \(\log n\) in this window. With \(P(z)=\sum_{n<e^{U}}a(n)n^{-1-z}\) and
\[
G(z)=\bigl(F(z)-zP(z)\bigr)\exp\bigl(-(2-Uz-\tfrac X4(1+Xz)^{2})\bigr),
\]
the [[proofs/grh/reduction-zeros/newman-circle-bound|bound on the circle]] gives \(\lvert G(z)\rvert\le3U\) for \(\lvert z\rvert=1/X\). \(G\) is holomorphic on the closed disc, so \(\lvert G(0)\rvert\le3U\) by the [[complex-analysis/maximum-modulus-principle|maximum modulus principle]]. But \(G(0)=F(0)e^{X/4-2}=e^{X/4-2}/\varphi(q)\). Hence
\[
e^{X/4}\le3U\varphi(q)e^{2}\le3e^{2}X^{2A}X^{2A}=3e^{2}X^{4A},
\]
which is false for large \(X\). \(\blacksquare\)

## Remarks

This is a consequence of the [[?c:Siegel–Walfisz theorem|Siegel–Walfisz theorem]]; here only one prime is found, in a long window, for moduli that are powers of a fixed multiple of \(4\), by Newman's contour method.

## References

1. Lean: `New.exists_prime_modEq_one_log_mem` and the auxiliary declarations in the front matter, in `src/Lib/Analytic/Primes.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, 2007, Corollary 11.19 (as cited in the head of the Lean file).
