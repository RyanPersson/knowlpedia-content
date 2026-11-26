+++
id = "proofs/grh/reduction-zeros/bad-primes-are-rare"
title = "Bad primes are rare"
kind = "theorem"
summary = "In a class modulo N whose primes are 7 mod 8 and prime to N, the primes d up to X for which some twisted L-function has a zero in the box Re s >= 1/2 + 9 delta, |Im s| <= H number O(X^(1 - delta/2))."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.zero_density_quadTwist", "New.exists_card_zero_quadTwist_le", "New.IsBadPrime", "New.IsPrimeWithTwistZero"]
lean_files = ["src/Lib/Analytic/QuadraticTwist.lean"]
proof_status = "full"
+++

**Definition.** Let \(N\ge1\), \(a\) a residue class modulo \(N\), and \(\beta,H\) real. A natural number \(d\) is a **bad prime** of the class \(a\) (for the box \(\beta,H\)) if \(d\) is prime, \(d\equiv a\pmod N\), and there are a Dirichlet character \(\xi\) modulo \(N\) and \(s\in\mathbb{C}\) with \(\operatorname{Re}s\ge\beta\), \(\lvert\operatorname{Im}s\rvert\le H\) and \(L(s,\xi\chi_K)=0\), where \(\xi\chi_K\) is the [[?lean:New.quadTwist|twist]] of \(\xi\) by \((\cdot/d)\).

**Theorem (zero density for quadratic twists).** Let \(N\ge1\), \(\delta>0\), \(H\in\mathbb{R}\), and let \(a\) be a class modulo \(N\) such that every prime \(d\equiv a\pmod N\) satisfies \(d\equiv7\pmod8\) and \(\gcd(N,d)=1\). Then there are \(C\) and \(X_0\) such that for all integers \(X\ge X_0\),
\[
\#\{d\le X:\ d\text{ is a bad prime of the class }a\text{ for }\beta=\tfrac12+9\delta,\ H\}\le C\,X^{1-\delta/2}.
\]

## Proof

*Step 1: a primitive character.* Let \(\psi\) be primitive modulo \(M\ge1\). We claim: there is \(C_\psi\) such that for all large \(T\) the number of primes \(d\equiv7\pmod 8\) with \(\gcd(M,d)=1\), \(Md\le T^{2}\) and with a zero of \(L(\cdot,\psi\chi_K)\) in the box is at most \(C_\psi T^{2-\delta}\).

Choose \(j\in\{0,1\}\) with \(\psi(-1)=-(-1)^{j}\). For such \(d\): \(\psi\chi_K\) is primitive modulo \(Md\le T^{2}\) ([[proofs/grh/reduction-zeros/twist-of-primitive-is-primitive|twist of a primitive character]]), not principal ([[proofs/grh/reduction-zeros/quad-twist-not-principal|twists are not principal]]), and \((\psi\chi_K)(-1)=\psi(-1)(-1/d)=-\psi(-1)=(-1)^{j}\) because \(d\equiv3\pmod4\). Its values at \(n\ge1\) are \(\psi(n)(n/d)=\psi(n)(-d/n^{\circ})\) by [[proofs/grh/reduction-zeros/legendre-as-jacobi-of-odd-part|reciprocity]]. So by [[proofs/grh/reduction-zeros/zero-forces-large-tail-integral|the three-lines theorem]], for large \(T\), \(J(c_d,T)>T^{2\delta}\) with \(c_v(n)=\psi(n)(-v/n^{\circ})\). All \(J(c_v,T)\ge0\), and \(d\le T^{2}\). By the [[proofs/grh/reduction-zeros/mean-value-theta-jacobi|mean value estimate]] with \(\alpha=\psi\),
\[
\#\{d\}\cdot T^{2\delta}\le\sum_{1\le v\le T^{2}}J(c_v,T)\le C\,T^{2+\delta},
\]
so the number is at most \(CT^{2-\delta}\).

*Step 2: all characters modulo \(N\).* For each \(\xi\) modulo \(N\) let \(\psi_\xi\) be the primitive character modulo \(M_\xi\mid N\) inducing it. Let \(d\le X\) be a bad prime, with \(\xi\) and a zero \(s\) of \(L(\cdot,\xi\chi_K)\) in the box. By hypothesis \(d\equiv7\pmod8\) and \(\gcd(N,d)=1\), so \(\gcd(M_\xi,d)=1\). The character \(\xi\chi_K\) modulo \(Nd\) is induced by \(\psi_\xi\chi_K\) modulo \(M_\xi d\), which is not principal, so
\[
L(s,\xi\chi_K)=L(s,\psi_\xi\chi_K)\prod_{p\mid Nd}\bigl(1-(\psi_\xi\chi_K)(p)p^{-s}\bigr),
\]
and the product is nonzero because \(\operatorname{Re}s>0\) ([[proofs/grh/reduction-zeros/euler-factors-nonvanishing|Euler factors]]). Hence \(L(s,\psi_\xi\chi_K)=0\). With \(T=\sqrt{NX}\): \(M_\xi d\le NX=T^{2}\). So \(d\) is counted in Step 1 for \(\psi_\xi\). Summing over the finitely many \(\xi\), for large \(X\),
\[
\#\{\text{bad }d\le X\}\le\sum_\xi C_{\psi_\xi}T^{2-\delta}=\Bigl(\sum_\xi C_{\psi_\xi}\Bigr)N^{1-\delta/2}X^{1-\delta/2}.\ \blacksquare
\]

## Remarks

Such a count also follows from the large sieve for real characters; the proof here needs only the Pólya–Vinogradov inequality, because theta series keep all sums short.

## References

1. Lean: `New.IsPrimeWithTwistZero`, `New.IsBadPrime`, `New.exists_card_zero_quadTwist_le`, `New.zero_density_quadTwist` in `src/Lib/Analytic/QuadraticTwist.lean`.
