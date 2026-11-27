+++
id = "proofs/grh/reduction-zeros/prime-remainder-is-polar"
title = "The remainder is polar, with residues counting zeros"
kind = "theorem"
summary = "The function v -> R_q(e^v) is polar: its transform has at most simple poles in Re s > 0, none at 1, with residue (n(s) - n'(s))/(phi(q) s (1-s)) counting zeros of the L-functions modulo q and of their twists."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.isPolar_primeRemainder"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
proof_status = "full"
+++

**Theorem (poles).** Let \(d\) be a prime with \(d\equiv7\pmod8\) and let \(q\ge1\) be prime to \(d\). Then the function \(v\mapsto R_q(e^{v})\), with \(R_q\) the [[proofs/grh/reduction-zeros/prime-remainder|remainder]], is [[proofs/grh/reduction-zeros/polar-function|polar]] with residues
\[
r(s)=\begin{cases}\dfrac{1}{\varphi(q)\,s(1-s)}\displaystyle\sum_{\psi\bmod q}\bigl(\operatorname{ord}_sE_\psi-\operatorname{ord}_sE_{\psi\chi_K}\bigr)&s\notin\{0,1\},\\[8pt]0&s\in\{0,1\},\end{cases}
\]
where \(\psi\) runs over the [[?c:Dirichlet character|Dirichlet characters]] modulo \(q\), \(E_\chi\) is [[?lean:New.entireL|the \(L\)-function of \(\chi\) with the pole removed]], and \(\psi\chi_K\) is the [[?lean:New.quadTwist|twist]] by \((\cdot/d)\).

Explicitly: \(v\mapsto R_q(e^v)\) is measurable; \(\lvert R_q(e^{v})\rvert\le(\lvert c_q\rvert+5)e^{v}\) for \(v\ge0\); and \(\int_0^\infty R_q(e^v)e^{(1-s)v}dv\) continues from \(\operatorname{Re}s>2\) to a meromorphic function on \(\mathbb{C}\) which, in \(\operatorname{Re}s>0\), is holomorphic at \(1\) and has at most simple poles with residues \(r(s)\).

## Proof

Only \(d\ne2\) and \(\gcd(q,d)=1\) are used. Let \(F(s)=G_q(s)/s-c_q\) and \(\Phi(s)=F(s)/(s-1)\), a meromorphic function on \(\mathbb{C}\) (see [[proofs/grh/reduction-zeros/log-deriv-mean|\(G_q\)]]).

*Measurability and growth.* \(R_q(e^{v})\) is built from step functions of \(v\), from \(e^{-v}\) and from \(v\), so it is measurable; the growth bound is the [[proofs/grh/reduction-zeros/growth-of-prime-remainder|growth lemma]].

*Transform.* For \(\operatorname{Re}s>2\), \(\Phi(s)=\int_0^\infty R_q(e^{v})e^{(1-s)v}dv\) by the [[proofs/grh/reduction-zeros/laplace-transform-of-prime-remainder|computation of the transform]].

*The point \(1\).* \(F\) is holomorphic at \(1\) and \(F(1)=G_q(1)-c_q=0\) because [[proofs/grh/reduction-zeros/g-q-at-one-is-real|\(G_q(1)\) is real]]. So \((z-1)\Phi(z)=F(z)\to0=r(1)\) as \(z\to1\).

*Other points.* For \(\operatorname{Re}\rho>0\), \(\rho\ne1\), we have \(\rho\neq0\), and the [[proofs/grh/reduction-zeros/residues-of-log-deriv-mean|residue lemma]] with \(\kappa=c_q\) gives \((z-\rho)\Phi(z)\to r(\rho)\). \(\blacksquare\)

## Remarks

In the source the residue is written by the single formula with \(s(1-s)\) in the denominator; at \(s=0\) and \(s=1\) this is a division by zero, which has the value \(0\) there. Only the values of \(r\) on \(\operatorname{Re}s>0\) enter the definition of a polar function.

## References

1. Lean: `New.isPolar_primeRemainder` in `src/New/Reduction/Zeros/PrimeError.lean`.
