+++
id = "proofs/grh/reduction-zeros/residue-of-log-deriv-entire-l"
title = "Residues of the logarithmic derivative of an L-function"
kind = "lemma"
summary = "The logarithmic derivative of the L-function with the pole removed has at most simple poles, and the residue at a point is the order of vanishing there."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.tendsto_sub_mul_logDeriv_entireL_analyticOrderNatAt", "New.tendsto_sub_mul_of_continuousAt"]
lean_files = ["src/Lib/Analytic/EntireLFunction.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\chi\) be a complex [[?c:Dirichlet character|Dirichlet character]] modulo \(N\ge1\) and \(E_\chi\) [[?lean:New.entireL|its \(L\)-function with the pole removed]]. For every \(s\in\mathbb{C}\),
\[
\lim_{z\to s,\ z\neq s}(z-s)\,\frac{E_\chi'(z)}{E_\chi(z)}=\operatorname{ord}_sE_\chi ,
\]
the [[complex-analysis/order-of-zero-or-pole|order of vanishing]] of \(E_\chi\) at \(s\).

## Proof

Let \(n=\operatorname{ord}_sE_\chi\), finite by the [[proofs/grh/reduction-zeros/entire-l-basic-properties|basic properties]]. Near \(s\) we have \(E_\chi(z)=(z-s)^n g(z)\) with \(g\) holomorphic at \(s\) and \(g(s)\ne0\). For \(z\ne s\) near \(s\), \(g(z)\ne0\) and the [[complex-analysis/logarithmic-derivative|logarithmic derivative]] is
\[
\frac{E_\chi'(z)}{E_\chi(z)}=\frac{n}{z-s}+\frac{g'(z)}{g(z)} ,
\]
so \((z-s)E_\chi'(z)/E_\chi(z)=n+(z-s)g'(z)/g(z)\). The function \(g'/g\) is continuous at \(s\), so the last term tends to \(0\). \(\blacksquare\)

## References

1. Lean: `New.tendsto_sub_mul_logDeriv_entireL_analyticOrderNatAt` in `src/Lib/Analytic/EntireLFunction.lean`.
