+++
id = "proofs/grh/reduction-zeros/one-sided-criterion"
title = "The one-sided criterion for a zero-free half-plane"
kind = "theorem"
summary = "An eventual upper bound x^(beta-1) for the remainders R_q0, for all primes d of one residue class, excludes zeros of the L-functions modulo q0 in Re s > beta."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.LFunction_ne_zero_of_primeRemainder_le"]
lean_files = ["src/New/Reduction/Zeros/Criterion.lean"]
proof_status = "full"
+++

**Theorem (one-sided criterion).** Let \(q_0\ge1\) be an integer with \(8\mid q_0\), let \(d_0\) be a natural number with \(d_0\equiv7\pmod 8\) and \(\gcd(d_0,q_0)=1\), and let \(\beta>\tfrac12\). Suppose that for every prime \(d\equiv d_0\pmod{q_0}\) there is \(x_0\) such that the [[proofs/grh/reduction-zeros/prime-remainder|remainder]] \(R_{q_0}=R_{d,q_0}\) satisfies
\[
R_{q_0}(x)\le x^{\beta-1}\qquad\text{for all real }x\ge x_0 .
\]
Then \(L(\rho,\psi)\ne0\) for every [[?c:Dirichlet character|Dirichlet character]] \(\psi\) modulo \(q_0\) and every \(\rho\in\mathbb{C}\) with \(\rho\ne1\) and \(\operatorname{Re}\rho>\beta\).

Only an upper bound is assumed, and nothing is assumed about real zeros.

## Proof

Fix \(\psi\) and \(\rho\). Write \(E_\chi\) for [[?lean:New.entireL|the \(L\)-function of \(\chi\) with the pole removed]].

*Step 1: the class.* If \(d\) is a prime with \(d\equiv d_0\pmod{q_0}\), then \(d\equiv d_0\equiv7\pmod8\) because \(8\mid q_0\), and \(\gcd(d,q_0)=\gcd(d_0,q_0)=1\). The class of \(d_0\) is a unit modulo \(q_0\).

*Step 2: choice of \(d\).* By the [[proofs/grh/reduction-zeros/choice-of-prime|choice of the prime]], applied with the modulus \(q_0\), the class of \(d_0\), the number \(\beta>\tfrac12\) and the height \(H=\lvert\operatorname{Im}\rho\rvert\), there is a prime \(d\equiv d_0\pmod{q_0}\) such that
\[
E_{\chi\chi_K}(s)\ne0\quad\text{for all }\chi\bmod q_0\text{ and all }s\text{ with }\operatorname{Re}s\ge\beta,\ \lvert\operatorname{Im}s\rvert\le\lvert\operatorname{Im}\rho\rvert, \tag{1}
\]
where \(\chi\chi_K\) is the twist by \((\cdot/d)\). Fix this \(d\).

*Step 3: the residues.* By the [[proofs/grh/reduction-zeros/prime-remainder-is-polar|theorem on poles]], \(E(v)=R_{q_0}(e^{v})\) is [[proofs/grh/reduction-zeros/polar-function|polar]] with residues \(r\) given there. Let \(n(s)=\sum_{\chi\bmod q_0}\operatorname{ord}_sE_\chi\ge0\). By (1) and the [[proofs/grh/reduction-zeros/entire-l-basic-properties|basic properties]], \(\operatorname{ord}_sE_{\chi\chi_K}=0\) in the region of (1), hence
\[
r(s)=\frac{n(s)}{\varphi(q_0)\,s(1-s)}\qquad\text{for }\operatorname{Re}s>\beta,\ \lvert\operatorname{Im}s\rvert\le\lvert\operatorname{Im}\rho\rvert,\ s\neq1, \tag{2}
\]
and \(r(1)=0\).

*Step 4: sign at real points.* Let \(x>\beta\) be real. If \(x=1\), \(r(x)=0\). If \(\beta<x<1\), then \(x(1-x)>0\) and (2) gives \(r(x)\ge0\). If \(x>1\), then \(n(x)=0\) because no \(E_\chi\) vanishes on \(\operatorname{Re}s\ge1\), so \(r(x)=0\). In all cases \(\operatorname{Re}r(x)\ge0\).

*Step 5: the one-sided bound.* By hypothesis, for all large \(v\), \(R_{q_0}(e^{v})\le(e^{v})^{\beta-1}=e^{(\beta-1)v}\).

*Step 6: Landau.* By [[proofs/grh/reduction-zeros/no-pole-right-of-beta|the theorem on poles to the right of \(\beta\)]] (note \(\beta>0\)), \(r(\rho)=0\). As \(\operatorname{Re}\rho>\beta>0\) we have \(\rho\ne0\), and \(\rho\ne1\); so (2) gives \(n(\rho)=0\). All terms of \(n(\rho)\) are \(\ge0\), hence \(\operatorname{ord}_\rho E_\psi=0\), that is \(E_\psi(\rho)\ne0\).

*Step 7.* Since \(\rho\ne1\), \(E_\psi(\rho)\) is \(L(\rho,\psi)\) or \((\rho-1)L(\rho,\psi)\). Therefore \(L(\rho,\psi)\ne0\). \(\blacksquare\)

## Remarks

* The twisted \(L\)-functions enter the residue with a minus sign, so their zeros could cancel zeros of the \(L(s,\chi)\) or spoil the sign at real points. Step 2 removes them from the relevant box for one well-chosen \(d\); this is why the hypothesis is asked for all primes \(d\) of a class.
* A real zero \(x\in(\beta,1)\) of some \(E_\chi\) gives a residue \(\ge0\), which is the sign that Landau's lemma tolerates. So no hypothesis on real zeros is needed.
* In [[?lean:New.grh|the half-plane theorem]], for a character modulo \(q\), the criterion is applied with \(q_0=18480\,q\), \(d_0=q_0/2-1\), and the real-variable bound \(R_{q_0}(x)\le x^{-1/2+\varepsilon}\) for all large real \(x\), with \(\varepsilon=\beta-\tfrac12\), which is [[?lean:New.eventually_primeRemainder_le_rpow|the one-sided bound in the real variable]]. (That theorem is derived in the other chapter from a bound at integers, `New.eventually_primeRemainder_natCast_le`.) The \(L\)-function modulo \(q\) differs from the one of the induced character modulo \(q_0\) by Euler factors.

## References

1. Lean: `New.LFunction_ne_zero_of_primeRemainder_le` in `src/New/Reduction/Zeros/Criterion.lean`.
2. Related work named in the head of the Lean file: M. Suzuki, *On variants of Chebyshev's conjecture*, arXiv:2411.07436, 2024; H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, 2007, §15.1–15.2; E. Landau, *Über einen Satz von Tschebyschef*, 1905.
