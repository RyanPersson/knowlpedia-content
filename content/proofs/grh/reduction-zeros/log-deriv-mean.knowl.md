+++
id = "proofs/grh/reduction-zeros/log-deriv-mean"
title = "The mean of logarithmic derivatives G_q"
kind = "definition"
summary = "The mean over the characters modulo q of the difference of the logarithmic derivatives of the twisted and untwisted L-functions, less 1/phi(q)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.logDerivMean", "New.analyticAt_logDerivMean_of_one_le_re", "New.analyticAt_logDerivMean"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
+++

Let \(d\) be a prime and \(q\ge1\). For a complex [[?c:Dirichlet character|Dirichlet character]] \(\psi\) modulo \(q\) let \(E_\psi\) be [[?lean:New.entireL|its \(L\)-function with the pole removed]] and \(\psi\chi_K\) its [[?lean:New.quadTwist|quadratic twist]] by the Legendre symbol \((\cdot/d)\), a character modulo \(qd\). The function \(G_q=G_{d,q}\) is the [[complex-analysis/meromorphic-function|meromorphic function]]
\[
G_q(s)=\frac{1}{\varphi(q)}\Bigl(\sum_{\psi \bmod q}\Bigl(\frac{E_{\psi\chi_K}'(s)}{E_{\psi\chi_K}(s)}-\frac{E_\psi'(s)}{E_\psi(s)}\Bigr)-1\Bigr),
\]
where \(\varphi\) is the [[?c:Euler totient function|Euler totient function]] and the sum is over all \(\varphi(q)\) characters modulo \(q\).

## Properties

* \(G_q\) is holomorphic at every point where no \(E_\psi\) and no \(E_{\psi\chi_K}\) vanishes; in particular on \(\operatorname{Re}s\ge1\), by the [[proofs/grh/reduction-zeros/entire-l-basic-properties|non-vanishing there]].
* For odd \(d\) prime to \(q\) and \(\operatorname{Re}s>1\), \(G_q(s)=\sum_n\lambda(n)n^{-s}-\dfrac{s}{\varphi(q)(s-1)}\); see [[proofs/grh/reduction-zeros/dirichlet-series-of-weight|the Dirichlet series of the weight]].
* Its poles are described in [[proofs/grh/reduction-zeros/residues-of-log-deriv-mean|the residue lemma]].

## Remarks

In the source every [[complex-analysis/logarithmic-derivative|logarithmic derivative]] \(f'/f\) has the value \(0\) at the zeros of \(f\), so \(G_q\) is a function on all of \(\mathbb{C}\); its values at its poles are never used.

## References

1. Lean: `New.logDerivMean` in `src/New/Reduction/Zeros/PrimeError.lean`; `New.analyticAt_logDerivMean` in `src/New/Reduction/Zeros/PrimeNumberTheorem.lean`.
