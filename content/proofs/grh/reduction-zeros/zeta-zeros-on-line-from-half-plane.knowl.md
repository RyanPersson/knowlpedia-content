+++
id = "proofs/grh/reduction-zeros/zeta-zeros-on-line-from-half-plane"
title = "From the half-plane to the critical line for the zeta function"
kind = "theorem"
summary = "If no Dirichlet L-function vanishes to the right of the line Re s = 1/2, then the Riemann hypothesis holds."
aliases = ["Riemann hypothesis from non-vanishing"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.zeta_zeros_on_line"]
lean_files = ["src/New/Main.lean"]
proof_status = "full"
+++

**Theorem.** Assume the [[proofs/grh/reduction-zeros/dirichlet-l-nonvanishing-right-of-half|half-plane form of the generalized Riemann hypothesis]]. Then the [[proofs/grh/reduction-zeros/riemann-zeta-zeros-on-line|Riemann hypothesis]] holds: if \(\zeta(s)=0\), \(s\notin\{-2,-4,-6,\dots\}\) and \(s\ne1\), then \(\operatorname{Re}s=\tfrac12\).

## Proof

Let \(s\) be such a zero of the [[?c:Riemann zeta function|Riemann zeta function]].

*Step 1: \(s\neq0\).* Indeed \(\zeta(0)=-\tfrac12\ne0\).

*Step 2: \(s\) is a zero of the completed zeta function.* Let \(\Gamma_{\mathbb{R}}(w)=\pi^{-w/2}\Gamma(w/2)\) and let \(\Lambda(w)=\Gamma_{\mathbb{R}}(w)\zeta(w)\) be the [[?c:completed Riemann zeta function|completed zeta function]], which is holomorphic on \(\mathbb{C}\setminus\{0,1\}\). The function \(1/\Gamma_{\mathbb{R}}\) is entire, its zeros are the poles \(0,-2,-4,\dots\) of \(\Gamma_{\mathbb{R}}\), and for \(w\ne0\), \(w\neq 1\),
\[
\zeta(w)=\Lambda(w)\cdot\frac{1}{\Gamma_{\mathbb{R}}(w)} .
\]
Our \(s\) is not \(0\) and not one of \(-2,-4,\dots\), so \(1/\Gamma_{\mathbb{R}}(s)\ne0\), and \(\zeta(s)=0\) gives \(\Lambda(s)=0\).

*Step 3: reflection.* By the [[?c:functional equation of the Riemann zeta function|functional equation]] \(\Lambda(1-w)=\Lambda(w)\) we get \(\Lambda(1-s)=0\). Since \(s\ne1\) and \(s\ne0\), the point \(1-s\) is neither \(0\) nor \(1\), so the displayed formula applies at \(w=1-s\) and gives \(\zeta(1-s)=0\).

*Step 4: two inequalities.* The zeta function is the [[?c:Dirichlet L-function|\(L\)-function]] of the unique [[?c:Dirichlet character|Dirichlet character]] modulo \(1\). So for every \(z\neq1\) with \(\zeta(z)=0\) the hypothesis (applied with \(N=1\) and the clause \(z\ne1\)) shows that \(\operatorname{Re}z>\tfrac12\) is impossible, that is, \(\operatorname{Re}z\le\tfrac12\). Apply this to \(z=s\) (allowed since \(s\ne1\)) and to \(z=1-s\) (allowed since \(s\neq0\)): \(\operatorname{Re}s\le\tfrac12\) and \(1-\operatorname{Re}s\le\tfrac12\). Hence \(\operatorname{Re}s=\tfrac12\). \(\blacksquare\)

## Remarks

In the source the Gamma factor is a function on all of \(\mathbb{C}\) that takes the value \(0\) at its poles; "\(\Gamma_{\mathbb{R}}(s)\neq0\)" there means that \(s\) is not a pole. The proof above uses the entire function \(1/\Gamma_{\mathbb{R}}\) instead.

## References

1. Lean: `New.zeta_zeros_on_line` in `src/New/Main.lean`.
