+++
id = "proofs/grh/reduction-zeros/dirichlet-series-of-chi-lambda"
title = "The Dirichlet series of a character times the von Mangoldt function"
kind = "lemma"
summary = "For Re s > 1 the series of chi(n) Lambda(n) n^(-s) equals delta/(s-1) minus the logarithmic derivative of the L-function with the pole removed."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.LSeriesHasSum_mul_vonMangoldt"]
lean_files = ["src/Lib/Analytic/EntireLFunction.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\chi\) be a complex [[?c:Dirichlet character|Dirichlet character]] modulo \(N\ge1\), \(\Lambda\) the [[?c:von Mangoldt function|von Mangoldt function]] and \(E_\chi\) [[?lean:New.entireL|the \(L\)-function with the pole removed]]. Put \(\delta_\chi=1\) if \(\chi\) is principal and \(\delta_\chi=0\) otherwise. For \(\operatorname{Re}s>1\) the series below converges absolutely and
\[
\sum_{n\ge1}\chi(n)\Lambda(n)\,n^{-s}=\frac{\delta_\chi}{s-1}-\frac{E_\chi'(s)}{E_\chi(s)} .
\]

## Proof

For \(\operatorname{Re}s>1\) the series converges absolutely and equals \(-L'(s,\chi)/L(s,\chi)\); this is the [[?c:logarithmic derivative of a Dirichlet L-function as a Dirichlet series|standard formula]], and \(L(s,\chi)\ne0\) there. If \(\chi\) is not principal, \(E_\chi=L(\cdot,\chi)\) and \(\delta_\chi=0\). If \(\chi\) is principal, \(E_\chi(s)=(s-1)L(s,\chi)\) near \(s\) (as \(s\ne1\)), so \(E_\chi'/E_\chi=1/(s-1)+L'/L\), and the formula follows. \(\blacksquare\)

## References

1. Lean: `New.LSeriesHasSum_mul_vonMangoldt` in `src/Lib/Analytic/EntireLFunction.lean`.
