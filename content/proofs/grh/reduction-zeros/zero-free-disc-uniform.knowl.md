+++
id = "proofs/grh/reduction-zeros/zero-free-disc-uniform"
title = "A zero-free disc about 1, uniform in powers of a fixed modulus"
kind = "proposition"
summary = "For 4 | M and fixed A, for large X all L-functions modulo M^k <= X^A (k > 1) are zero-free on |s - 1| <= 1/X with logarithmic derivative at most X."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.eventually_norm_logDeriv_entireL_le_near_one", "New.factorsThrough_sq_of_sq_eq_one", "New.exists_regularL_eq_of_sq_eq_one"]
lean_files = ["src/Lib/Analytic/Primes.lean"]
proof_status = "full"
+++

**Proposition.** Let \(M\ge1\) with \(4\mid M\), and let \(A\ge0\) be an integer.

1. If \(k\ge2\) and \(\chi\) is a Dirichlet character modulo \(M^{k}\) with \(\chi^{2}\) principal, then \(\chi\) is induced by a character \(\chi_0\) modulo \(M^{2}\), and the [[proofs/grh/reduction-zeros/regularised-l-function|regularised \(L\)-functions]] agree: \(\mathfrak{f}_\chi=\mathfrak{f}_{\chi_0}\).
2. There is \(X_0\) such that for all real \(X\ge X_0\), all integers \(k>1\) with \(M^{k}\le X^{A}\), all Dirichlet characters \(\chi\) modulo \(M^{k}\) and all \(s\) with \(\lvert s-1\rvert\le1/X\):
\[
E_\chi(s)\ne0\qquad\text{and}\qquad\lvert E_\chi'(s)/E_\chi(s)\rvert\le X ,
\]
with \(E_\chi\) [[?lean:New.entireL|the \(L\)-function with the pole removed]].

## Proof

1. It suffices that every unit \(u\) of \(\mathbb{Z}/M^{k}\) with \(u\equiv1\pmod{M^{2}}\) is a square, since then \(\chi(u)=\chi(w)^{2}=1\) and \(\chi\) factors through \((\mathbb{Z}/M^2)^\times\). Write \(M=4m\) and \(1-u=M^{2}t\). The element \(Mmt\) is nilpotent in \(\mathbb{Z}/M^{k}\), and the polynomial \(c^{2}+c+Mmt\) has derivative \(2c+1\), a unit at \(c=0\); by Hensel's lemma (Newton iteration from \(0\)) it has a root \(c\). Then \((1+2c)^{2}=1+4(c^{2}+c)=1-4Mmt=1-M^{2}t=u\). The moduli \(M^{k}\) and \(M^{2}\) have the same prime factors, so no Euler factors are added on induction: \(L(s,\chi)=L(s,\chi_0)\), \(\chi\) is principal iff \(\chi_0\) is, and \(\mathfrak{f}_\chi=\mathfrak{f}_{\chi_0}\).

2. Apply the uniform form of the [[proofs/grh/reduction-zeros/zero-free-region|zero-free region]] with \(l=(A+1)\log X\), so \(e^{l}=X^{A+1}\ge M^{k}\). For large \(X\): \(l\ge10^{10}\), \(2l^{25}\le X\), and \(1/l\le r_0(\chi_0)\) for each of the finitely many characters \(\chi_0\) modulo \(M^{2}\) ([[proofs/grh/reduction-zeros/lower-bound-right-of-one|lower bound near \(1\)]]). By part 1 the hypothesis near \(1\) then holds for every \(\chi\) modulo \(M^{k}\) with \(\chi^{2}\) principal, uniformly in \(k\). If \(\lvert s-1\rvert\le1/X\) then \(\operatorname{Re}s\ge1-1/X\ge1-l^{-25}\) and \(\lvert s\rvert\le2\le e^{l}\); so \(E_\chi(s)\ne0\) and \(\lvert E_\chi'/E_\chi(s)\rvert\le2l^{25}\le X\). \(\blacksquare\)

## Remarks

No exceptional zero can occur, because the real characters come from the fixed modulus \(M^{2}\).

## References

1. Lean: `New.factorsThrough_sq_of_sq_eq_one`, `New.exists_regularL_eq_of_sq_eq_one`, `New.eventually_norm_logDeriv_entireL_le_near_one` in `src/Lib/Analytic/Primes.lean`.
