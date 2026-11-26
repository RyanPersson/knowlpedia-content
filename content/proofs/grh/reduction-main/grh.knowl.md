+++
id = "proofs/grh/reduction-main/grh"
title = "Main theorem in half-plane form: Dirichlet L-functions do not vanish to the right of the critical line"
kind = "theorem"
summary = "No Dirichlet L-function vanishes at a point with real part greater than 1/2, the pole of the principal characters excepted."
aliases = ["grh", "generalized Riemann hypothesis in half-plane form", "DirichletLNonvanishingRightOfHalf"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.grh", "DirichletLNonvanishingRightOfHalf"]
lean_files = ["src/New/Reduction/OneSidedBound.lean", "src/Statements.lean"]
proof_status = "full"
+++

**Theorem.** Let \(q\ge1\), let \(\chi\) be a [[?c:Dirichlet character|Dirichlet character]] modulo \(q\) with values in \(\mathbb C\), and let \(\rho\in\mathbb C\) with \(\operatorname{Re}\rho>\tfrac12\). Assume \(\chi\ne1\) or \(\rho\ne1\) (here \(1\) is the trivial character modulo \(q\)). Then
\[
L(\rho,\chi)\ne0 ,
\]
where \(L(s,\chi)\) is the [[?c:Dirichlet L-function|Dirichlet \(L\)-function]], continued to \(\mathbb C\) (to \(\mathbb C\setminus\{1\}\) if \(\chi=1\); in Lean the value of a function at its pole is a junk value, which is why the case \(\chi=1,\rho=1\) is excluded).

## Proof

Complete relative to the [[proofs/grh/reduction-main/one-sided-bound|one-sided bound]] and the [[?lean:New.LFunction_ne_zero_of_primeRemainder_le|one-sided criterion]] of the chapter on zeros: *let \(q_0\) be a positive multiple of \(8\), \(d_0\equiv7\pmod8\) prime to \(q_0\), and \(\beta>\tfrac12\); if for every prime \(d\equiv d_0\pmod{q_0}\) one has \(R_{d,q_0}(x)\le x^{\beta-1}\) for all large real \(x\), then \(L(\rho,\psi)\ne0\) for every character \(\psi\) modulo \(q_0\) and every \(\rho\ne1\) with \(\operatorname{Re}\rho>\beta\).*

If \(\rho=1\), then \(\chi\ne1\) and \(L(1,\chi)\ne0\) by [[?c:non-vanishing of Dirichlet L-functions on the line Re s = 1|Dirichlet's theorem]]. Let \(\rho\ne1\); choose \(\beta\) with \(\tfrac12<\beta<\operatorname{Re}\rho\). Put \(q_0=18480q\) and \(d_0=9240q-1=q_0/2-1\). Then \(8\mid q_0\), \(d_0\equiv7\pmod8\), and \(\gcd(d_0,q_0)=1\) because \(d_0\) is odd and \(q_0=2(d_0+1)\). For every prime \(d\equiv d_0=q_0/2-1\pmod{q_0}\) the one-sided bound with \(\varepsilon=\beta-\tfrac12\) gives \(R_{d,q_0}(x)\le x^{-1/2+\varepsilon}=x^{\beta-1}\) for all large real \(x\). By the criterion, \(L(\rho,\psi)\ne0\) for the character \(\psi\) modulo \(q_0\) induced by \(\chi\). Since
\[
L(s,\psi)=L(s,\chi)\prod_{p\mid q_0}\bigl(1-\chi(p)p^{-s}\bigr)
\]
(valid at \(\rho\) because \(\chi\ne1\) or \(\rho\ne1\)), \(L(\rho,\chi)\ne0\).

## Remarks

The remaining forms of the theorem (zeros in the critical strip on the line, the Riemann zeta function, primitive characters) are derived from this one in `Main.lean` with the lemmas of `New/Main`, outside this chapter.

## References

1. Lean: `New.grh` in `src/New/Reduction/OneSidedBound.lean`; the statement `DirichletLNonvanishingRightOfHalf` in `src/Statements.lean`.
