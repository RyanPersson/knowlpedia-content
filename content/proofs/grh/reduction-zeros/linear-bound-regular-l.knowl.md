+++
id = "proofs/grh/reduction-zeros/linear-bound-regular-l"
title = "A linear bound for the regularised L-function"
kind = "lemma"
summary = "Partial summation gives |f_chi(s)| <= 1 + 4N|s| for Re s >= 1/2."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_regularL_le_linear", "New.norm_sum_char_sub_le", "New.sum_range_char_add", "New.norm_integral_mul_cpow_le", "New.differentiableAt_integral_mul_cpow", "New.integrableOn_mul_cpow_of_bounded", "New.norm_sub_ite_le"]
lean_files = ["src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\chi\) be a Dirichlet character modulo \(N\ge1\), with [[proofs/grh/reduction-zeros/regularised-l-function|regularised \(L\)-function]] \(\mathfrak{f}_\chi\) and mean value \(\kappa=\kappa_\chi\).

1. For real \(x\ge0\): \(\bigl\lvert\sum_{1\le n\le x}\chi(n)-\kappa x\bigr\rvert\le2N\).
2. For \(\operatorname{Re}s\ge\tfrac12\): \(\lvert\mathfrak{f}_\chi(s)\rvert\le1+4N\lvert s\rvert\).

## Proof

1. The sum of \(\chi\) over any \(N\) consecutive integers is \(N\kappa\). So \(S(M)=\sum_{n\le M}(\chi(n)-\kappa)\) has period \(N\) in \(M\), and \(\lvert S(M)\rvert\le2M\). With \(M=\lfloor x\rfloor\) and \(M'=M\bmod N\le N-1\): \(\lvert\sum_{n\le x}\chi(n)-\kappa x\rvert=\lvert S(M')-\kappa(x-M)\rvert\le2(N-1)+1\le2N\).

2. Let \(r(t)=\sum_{n\le t}\chi(n)-\kappa t\), so \(\lvert r\rvert\le2N\), and \(\Phi(z)=\int_1^\infty r(t)t^{-z-1}dt\). This integral converges for \(\operatorname{Re}z>0\), is holomorphic there, and \(\lvert\Phi(z)\rvert\le2N/\operatorname{Re}z\). For \(\operatorname{Re}z>1\), [[?c:Abel summation formula|Abel summation]] gives
\[
L(z,\chi)=z\int_1^\infty\Bigl(\sum_{n\le t}\chi(n)\Bigr)t^{-z-1}dt=z\Bigl(\Phi(z)+\frac{\kappa}{z-1}\Bigr),
\]
hence \(\mathfrak{f}_\chi(z)=(z-\delta_\chi)\bigl(\Phi(z)+\kappa/(z-1)\bigr)=\kappa+(z-\delta_\chi)\Phi(z)\): for principal \(\chi\), \(\delta_\chi=1\); otherwise \(\kappa=0\) and \(\delta_\chi=0\). Both sides are holomorphic on \(\operatorname{Re}z>0\), so by the [[complex-analysis/identity-theorem|identity theorem]] the identity holds there. For \(\operatorname{Re}s\ge\tfrac12\) we have \(\lvert s-\delta_\chi\rvert\le\lvert s\rvert\) (for \(\delta_\chi=1\): \((\operatorname{Re}s-1)^2\le(\operatorname{Re}s)^2\)) and \(\lvert\Phi(s)\rvert\le4N\). So \(\lvert\mathfrak{f}_\chi(s)\rvert\le1+4N\lvert s\rvert\). \(\blacksquare\)

## References

1. Lean: `New.norm_sum_char_sub_le`, `New.norm_regularL_le_linear` in `src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean`.
