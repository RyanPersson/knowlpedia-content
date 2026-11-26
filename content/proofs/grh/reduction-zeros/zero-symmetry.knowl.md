+++
id = "proofs/grh/reduction-zeros/zero-symmetry"
title = "Symmetry of the zeros of Dirichlet L-functions"
kind = "theorem"
summary = "A zero s of L(., chi) off the imaginary axis and different from 1 is a pole of the Gamma factor or gives the zero 1 - s of L(., chi inverse); chi need not be primitive."
aliases = ["reflection of zeros"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.gammaFactor_eq_zero_or_LFunction_one_sub_eq_zero", "New.exists_isPrimitive_changeLevel_eq", "New.gammaFactor_changeLevel"]
lean_files = ["src/Lib/Analytic/ZeroSymmetry.lean"]
proof_status = "full"
+++

**Theorem.** Let \(N\ge1\), let \(\chi\) be a complex [[?c:Dirichlet character|Dirichlet character]] modulo \(N\) (primitive or not), and let \(s\in\mathbb{C}\) with \(\operatorname{Re}s\ne0\), \(s\ne1\) and \(L(s,\chi)=0\). Then at least one of the following holds:

* \(s\) is a pole of the [[?c:Archimedean Gamma factor of a Dirichlet character|Gamma factor]] \(\gamma_\chi\), where \(\gamma_\chi(s)=\Gamma_{\mathbb{R}}(s)\) if \(\chi(-1)=1\) and \(\gamma_\chi(s)=\Gamma_{\mathbb{R}}(s+1)\) if \(\chi(-1)=-1\), with \(\Gamma_{\mathbb{R}}(s)=\pi^{-s/2}\Gamma(s/2)\);
* \(L(1-s,\chi^{-1})=0\).

Multiplicities are not compared.

## Proof

*Reduction to a primitive character.* Let \(M\mid N\) be the [[?c:conductor of a Dirichlet character|conductor]] of \(\chi\) and \(\psi\) the [[?c:primitive Dirichlet character|primitive]] character modulo \(M\) that [[?c:induced Dirichlet character|induces]] \(\chi\). Then \(\psi(-1)=\chi(-1)\), so \(\gamma_\psi=\gamma_\chi\); also \(\chi^{-1}\) is induced by \(\psi^{-1}\), which is primitive modulo \(M\). For every \(w\) with \(\psi\) non-principal or \(w\neq1\),
\[
L(w,\chi)=L(w,\psi)\prod_{p\mid N}\bigl(1-\psi(p)p^{-w}\bigr), \tag{1}
\]
and likewise for \(\chi^{-1}\) and \(\psi^{-1}\).

*The zero passes to \(\psi\).* Apply (1) at \(w=s\ne1\). The product is nonzero by the [[proofs/grh/reduction-zeros/euler-factors-nonvanishing|lemma on Euler factors]], as \(\operatorname{Re}s\neq0\). Hence \(L(s,\psi)=0\).

*The functional equation.* Assume that \(s\) is not a pole of \(\gamma_\chi=\gamma_\psi\). Let \(\Lambda(w,\psi)=\gamma_\psi(w)L(w,\psi)\) be the [[?c:completed Dirichlet L-function|completed \(L\)-function]]; it is holomorphic except, when \(M=1\), for poles at \(0\) and \(1\). Since \(s\ne0\) (because \(\operatorname{Re}s\ne0\)), \(s\neq 1\) and \(\gamma_\psi\) is finite at \(s\), we get \(\Lambda(s,\psi)=\gamma_\psi(s)L(s,\psi)=0\). The [[?c:functional equation of Dirichlet L-functions|functional equation]] for the primitive character \(\psi^{-1}\) reads
\[
\Lambda(1-w,\psi^{-1})=M^{\,w-1/2}\,W(\psi^{-1})\,\Lambda(w,\psi)
\]
with a root number \(W(\psi^{-1})\); at \(w=s\) it gives \(\Lambda(1-s,\psi^{-1})=0\). The function \(1/\gamma_{\psi^{-1}}\) is entire and \(L(w,\psi^{-1})=\Lambda(w,\psi^{-1})/\gamma_{\psi^{-1}}(w)\) for \(w\notin\{0,1\}\). As \(1-s\notin\{0,1\}\), we get \(L(1-s,\psi^{-1})=0\).

*Back to \(\chi^{-1}\).* Apply (1) to \(\chi^{-1}\), \(\psi^{-1}\) at \(w=1-s\), which is \(\neq1\) since \(s\ne0\): \(L(1-s,\chi^{-1})=L(1-s,\psi^{-1})\cdot\prod_{p\mid N}(\cdots)=0\). \(\blacksquare\)

## Remarks

Only the reflection of zeros is kept from the functional equation; neither the identity for \(\chi\) itself nor the root number is used. In the source the Gamma factor takes the value \(0\) at its poles, and the first alternative is written \(\gamma_\chi(s)=0\).

## References

1. Lean: `New.gammaFactor_eq_zero_or_LFunction_one_sub_eq_zero` in `src/Lib/Analytic/ZeroSymmetry.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, Cambridge University Press, 2007, Corollaries 10.3 and 10.8 (as cited in the head of the Lean file).
