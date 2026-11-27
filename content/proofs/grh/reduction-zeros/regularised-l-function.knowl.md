+++
id = "proofs/grh/reduction-zeros/regularised-l-function"
title = "The regularised L-function"
kind = "definition"
summary = "L(s, chi), multiplied by (s-1)/s if chi is principal; holomorphic in Re s > 0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.regularL", "New.differentiableAt_regularL", "New.regularL_eq", "New.charMean", "New.norm_charMean_le_one", "New.charMean_eq_zero"]
lean_files = ["src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean"]
+++

Let \(\chi\) be a complex [[?c:Dirichlet character|Dirichlet character]] modulo \(N\ge1\) and \(E_\chi\) [[?lean:New.entireL|its \(L\)-function with the pole removed]]. The **regularised \(L\)-function** is
\[
\mathfrak{f}_\chi(s)=\begin{cases}E_\chi(s)/s&\text{if }\chi\text{ is principal and }s\ne0,\\ E_\chi(s)=L(s,\chi)&\text{if }\chi\text{ is not principal (all }s\in\mathbb{C}).\end{cases}
\]
(In the source the principal branch has the value \(0\) at \(s=0\), by the convention for division by zero; this value is not used.) The **mean value** of \(\chi\) is \(\kappa_\chi=\frac1N\sum_{a\bmod N}\chi(a)\).

## Properties

* \(\mathfrak{f}_\chi\) is holomorphic on \(\operatorname{Re}s>0\).
* For \(\operatorname{Re}s>1\): \(\mathfrak{f}_\chi(s)=L(s,\chi)\,\dfrac{s-\delta_\chi}{s}\), with \(\delta_\chi=1\) if \(\chi\) is principal and \(0\) otherwise.
* \(\lvert\kappa_\chi\rvert\le1\), and \(\kappa_\chi=0\) if \(\chi\) is not principal (by [[?c:orthogonality of Dirichlet characters|orthogonality]]).

Dividing by \(s\) keeps \(\mathfrak{f}_\chi\) of the size of \(L(s,\chi)\) for large \(\lvert s\rvert\).

## References

1. Lean: `New.regularL`, `New.charMean` in `src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean`.
