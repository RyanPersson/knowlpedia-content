+++
id = "proofs/grh/reduction-zeros/zeros-on-line-from-half-plane"
title = "From the half-plane to the critical line for Dirichlet L-functions"
kind = "theorem"
summary = "If no Dirichlet L-function vanishes to the right of the line Re s = 1/2, then all zeros in the open critical strip lie on that line."
aliases = ["zeros on the line from non-vanishing"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.zeros_on_line"]
lean_files = ["src/New/Main.lean"]
proof_status = "full"
+++

**Theorem.** Assume the [[proofs/grh/reduction-zeros/dirichlet-l-nonvanishing-right-of-half|half-plane form of the generalized Riemann hypothesis]]. Then the [[proofs/grh/reduction-zeros/dirichlet-l-zeros-on-line|critical-line form]] holds: for every \(N\ge1\), every [[?c:Dirichlet character|Dirichlet character]] \(\chi\) modulo \(N\) and every \(s\) with \(0<\operatorname{Re}s<1\) and \(L(s,\chi)=0\), one has \(\operatorname{Re}s=\tfrac12\).

## Proof

Let \(N,\chi,s\) be as in the statement. Since \(0<\operatorname{Re}s<1\), we have \(s\ne1\), \(s\neq0\) and \(1-s\ne1\).

*Reflection.* Let \(\gamma_\chi(s)\) be the [[?c:Archimedean Gamma factor of a Dirichlet character|Gamma factor]] of \(\chi\): \(\Gamma_{\mathbb{R}}(s)=\pi^{-s/2}\Gamma(s/2)\) if \(\chi(-1)=1\) and \(\Gamma_{\mathbb{R}}(s+1)\) if \(\chi(-1)=-1\). Its poles are at \(s=-2n\), respectively \(s=-1-2n\), with \(n\ge0\), so it has no pole in \(\operatorname{Re}s>0\). By the [[proofs/grh/reduction-zeros/zero-symmetry|symmetry of the zeros]], applied to the zero \(s\) (which has \(\operatorname{Re}s\ne0\) and \(s\ne1\)), either \(s\) is a pole of \(\gamma_\chi\) or \(L(1-s,\chi^{-1})=0\). The first case is excluded, hence
\[
L(1-s,\chi^{-1})=0 .
\]

*Two inequalities.* If \(\operatorname{Re}s>\tfrac12\), the hypothesis applied to \((N,\chi,s)\), with \(s\ne1\), gives \(L(s,\chi)\ne0\), a contradiction. So \(\operatorname{Re}s\le\tfrac12\). If \(\operatorname{Re}(1-s)>\tfrac12\), the hypothesis applied to \((N,\chi^{-1},1-s)\), with \(1-s\neq1\), gives \(L(1-s,\chi^{-1})\ne0\), a contradiction. So \(1-\operatorname{Re}s\le\tfrac12\). Together, \(\operatorname{Re}s=\tfrac12\). \(\blacksquare\)

## References

1. Lean: `New.zeros_on_line` in `src/New/Main.lean`.
