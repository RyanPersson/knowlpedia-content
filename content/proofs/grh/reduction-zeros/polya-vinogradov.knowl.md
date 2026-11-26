+++
id = "proofs/grh/reduction-zeros/polya-vinogradov"
title = "The Pólya–Vinogradov inequality for initial intervals"
kind = "theorem"
summary = "For a non-principal character modulo q every sum of chi(v) over 1 <= v <= X is at most 2 sqrt(q)(1 + log q) in absolute value; sqrt(q)(1 + log q) for primitive characters."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.polya_vinogradov", "New.norm_sum_le_of_isPrimitive", "New.norm_sum_stdAddChar_pow_le", "New.four_mul_le_norm_stdAddChar_sub_one", "New.card_divisors_le_two_mul_sqrt", "New.apply_eq_sum_moebius_smul_of_changeLevel_eq", "New.sum_eq_sum_divisors_of_changeLevel_eq", "New.filter_dvd_Ioc_eq_image_mul"]
lean_files = ["src/Lib/Analytic/PolyaVinogradov.lean"]
proof_status = "full"
+++

**Theorem (Pólya–Vinogradov).** Let \(\chi\) be a complex [[?c:Dirichlet character|Dirichlet character]] modulo \(q\ge1\) and \(X\ge0\) an integer.

1. If \(\chi\) is [[?c:primitive Dirichlet character|primitive]] and \(q\ne1\), then \(\bigl\lvert\sum_{1\le v\le X}\chi(v)\bigr\rvert\le\sqrt q\,(1+\log q)\).
2. If \(\chi\) is not principal, then \(\bigl\lvert\sum_{1\le v\le X}\chi(v)\bigr\rvert\le2\sqrt q\,(1+\log q)\).

## Proof

*Geometric sums.* Let \(1\le k\le q-1\), \(x=k/q\in(0,1)\) and \(e_k=e^{2\pi ik/q}\). The chord \(\lvert e_k-1\rvert=2\sin(\pi x)=4\sin(\tfrac{\pi x}2)\cos(\tfrac{\pi x}2)\ge4x(1-x)\), since by concavity \(\sin(\tfrac\pi2x)\ge x\) and \(\cos(\tfrac\pi2x)\ge1-x\) on \([0,1]\). Therefore
\[
\Bigl\lvert\sum_{v=1}^{X}e_k^{\,v}\Bigr\rvert=\frac{\lvert e_k^{X+1}-e_k\rvert}{\lvert e_k-1\rvert}\le\frac{2}{4x(1-x)}=\frac q2\Bigl(\frac1k+\frac1{q-k}\Bigr).
\]

*Part 1.* By Fourier inversion on \(\mathbb{Z}/q\) and the formula \(\widehat\chi(k)=\chi^{-1}(-k)\tau(\chi)\) for primitive \(\chi\),
\[
\sum_{v=1}^{X}\chi(v)=\frac1q\sum_{k\bmod q}\Bigl(\sum_{v=1}^{X}e_k^{\,v}\Bigr)\chi^{-1}(-k)\,\tau(\chi).
\]
The term \(k=0\) vanishes because \(\chi^{-1}(0)=0\) for \(q\ne1\). With \(\lvert\tau(\chi)\rvert=\sqrt q\) ([[proofs/grh/reduction-zeros/gauss-sum-modulus|modulus of the Gauss sum]]) and the bound for geometric sums,
\[
\Bigl\lvert\sum_{v=1}^{X}\chi(v)\Bigr\rvert\le\frac1q\sum_{k=1}^{q-1}\frac{\sqrt q\,q}{2}\Bigl(\frac1k+\frac1{q-k}\Bigr)\le\sqrt q\sum_{k=1}^{q}\frac1k\le\sqrt q\,(1+\log q).
\]

*Part 2.* Let \(\psi\) be the primitive character modulo \(M\mid q\) inducing \(\chi\), and \(q=Mr\). Since \(\chi\) is not principal, \(M\neq1\). For every \(v\), \(\chi(v)=\psi(v)\) if \(\gcd(v,r)=1\) and \(\chi(v)=0\) otherwise (note \(\gcd(v,q)=1\) iff \(\gcd(v,M)=1\) and \(\gcd(v,r)=1\)); so with the [[?c:Möbius function|Möbius function]] \(\mu\), \(\chi(v)=\sum_{e\mid\gcd(v,r)}\mu(e)\psi(v)\). Summing over \(v=ev'\):
\[
\sum_{v\le X}\chi(v)=\sum_{e\mid r}\mu(e)\psi(e)\sum_{v'\le X/e}\psi(v').
\]
By part 1 each inner sum is at most \(\sqrt M(1+\log M)\le\sqrt M(1+\log q)\). The number of divisors of \(r\) is at most \(2\sqrt r\) (of two complementary divisors one is \(\le\sqrt r\)). Hence the total is at most \(2\sqrt r\sqrt M(1+\log q)=2\sqrt q(1+\log q)\). \(\blacksquare\)

## References

1. Lean: `New.norm_sum_le_of_isPrimitive`, `New.polya_vinogradov` in `src/Lib/Analytic/PolyaVinogradov.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, 2007, Theorem 9.18 (as cited in the head of the Lean file).
