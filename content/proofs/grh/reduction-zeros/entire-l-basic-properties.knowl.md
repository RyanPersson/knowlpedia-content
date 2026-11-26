+++
id = "proofs/grh/reduction-zeros/entire-l-basic-properties"
title = "Basic properties of the L-function with the pole removed"
kind = "proposition"
summary = "The function equal to L(s, chi), times s - 1 for principal chi, is entire, has no zero in Re s >= 1, and has finite order of vanishing everywhere."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.analyticAt_entireL", "New.entireL_ne_zero", "New.analyticOrderAt_entireL_ne_top", "New.analyticOrderNatAt_entireL_eq_zero_iff"]
lean_files = ["src/Lib/Analytic/EntireLFunction.lean"]
proof_status = "outline"
+++

**Proposition.** Let \(\chi\) be a complex [[?c:Dirichlet character|Dirichlet character]] modulo \(N\ge1\) and let \(E_\chi\) be [[?lean:New.entireL|the \(L\)-function with the pole removed]]: \(E_\chi(s)=L(s,\chi)\) if \(\chi\) is not principal, and \(E_\chi\) is the continuation of \((s-1)L(s,\chi)\) if \(\chi\) is principal.

1. \(E_\chi\) is an [[complex-analysis/entire-function|entire function]].
2. \(E_\chi(s)\ne0\) for all \(s\) with \(\operatorname{Re}s\ge1\).
3. \(E_\chi\) is not identically zero; hence its [[complex-analysis/order-of-zero-or-pole|order of vanishing]] \(\operatorname{ord}_sE_\chi\) is a finite integer \(\ge0\) at every \(s\), and \(\operatorname{ord}_sE_\chi=0\) if and only if \(E_\chi(s)\ne0\).

## Proof

1. This is the analytic continuation of [[?c:Dirichlet L-function|Dirichlet \(L\)-functions]]: \(L(s,\chi)\) is entire for non-principal \(\chi\), and for principal \(\chi\) it has only a simple pole at \(1\), removed by the factor \(s-1\). (Cited from the library.)

2. By the [[?c:non-vanishing of Dirichlet L-functions on the line Re s = 1|non-vanishing on \(\operatorname{Re}s\ge1\)]], \(L(s,\chi)\neq0\) for \(\operatorname{Re}s\ge1\) if \(\chi\) is non-principal or \(s\ne1\). For non-principal \(\chi\) this is the claim. For principal \(\chi\) and \(s\ne1\), \(E_\chi(s)=(s-1)L(s,\chi)\ne0\); and \(E_\chi(1)\) is the residue of \(L(s,\chi)\) at \(1\), which is \(\prod_{p\mid N}(1-p^{-1})\ne0\). (Both facts are cited from the library.)

3. By 2, \(E_\chi(1)\ne0\). An entire function with infinite order of vanishing at one point vanishes identically, by the [[complex-analysis/identity-theorem|identity theorem]]. \(\blacksquare\)

## References

1. Lean: `New.analyticAt_entireL`, `New.entireL_ne_zero`, `New.analyticOrderAt_entireL_ne_top`, `New.analyticOrderNatAt_entireL_eq_zero_iff` in `src/Lib/Analytic/EntireLFunction.lean`; the cited facts are Mathlib's `differentiable_LFunction`, `differentiable_LFunctionTrivChar₁`, `LFunction_ne_zero_of_one_le_re`, `LFunctionTrivChar₁_apply_one_ne_zero`.
