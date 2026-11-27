+++
id = "proofs/grh/reduction-zeros/cauchy-estimate-for-slope"
title = "Cauchy's estimate for the Taylor coefficients of a slope"
kind = "lemma"
summary = "If F is holomorphic and bounded by M on a disc about 1 + H reaching to 1 - eta, the normalised Taylor coefficients of (F(s) - F(1))/(s - 1) at 1 + H decay like exp(-(k+1) eta/(2H))."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_iteratedDeriv_dslope_le", "New.norm_taylorCoeff_dslope_le", "New.one_sub_le_re_and_norm_le_of_mem_closedBall"]
lean_files = ["src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean"]
proof_status = "full"
+++

**Lemma.** Let \(0<\eta\le H\), and let \(F\) be complex differentiable at every point of the closed disc \(D\) of radius \(H+\eta\) about \(1+H\) (so \(F\) is holomorphic on the open disc and continuous on \(D\); no neighbourhood of the boundary is needed), with \(\lvert F\rvert\le M\) on \(D\). Let \(g(s)=\dfrac{F(s)-F(1)}{s-1}\) for \(s\ne1\) and \(g(1)=F'(1)\). Then for every integer \(k\ge0\),
\[
\Bigl\lvert\frac{(-H)^{k}H}{k!}\,g^{(k)}(1+H)\Bigr\rvert\le\frac{4MH}{\eta}\,\exp\Bigl(-\frac{(k+1)\,\eta}{2H}\Bigr).
\]
Every point \(s\) of \(D\) has \(\operatorname{Re}s\ge1-\eta\) and \(\lvert s\rvert\le2H+\eta+1\).

## Proof

The point \(1\) lies in the interior of \(D\) (its distance to the centre is \(H<H+\eta\)), so \(g\) is holomorphic on the open disc and continuous on \(D\). On the boundary circle, \(\lvert s-1\rvert\ge(H+\eta)-H=\eta\), so \(\lvert g(s)\rvert\le(\lvert F(s)\rvert+\lvert F(1)\rvert)/\eta\le2M/\eta\). The [[complex-analysis/cauchy-derivative-estimate|Cauchy estimate]], in the form for functions holomorphic in an open disc and continuous on its closure (apply it on concentric circles of radius \(\varrho<H+\eta\) and let \(\varrho\to H+\eta\), using the continuity of \(g\)), gives \(\lvert g^{(k)}(1+H)\rvert\le k!\,(2M/\eta)/(H+\eta)^{k}\). Hence the left side is at most
\[
\frac{2M}{\eta}\,(H+\eta)\Bigl(\frac{H}{H+\eta}\Bigr)^{k+1}\le\frac{2M}{\eta}\cdot2H\cdot e^{-(k+1)\eta/(2H)},
\]
because \(\dfrac{H}{H+\eta}=1-\dfrac{\eta}{H+\eta}\le1-\dfrac{\eta}{2H}\le e^{-\eta/(2H)}\). The last assertion is the triangle inequality. \(\blacksquare\)

## References

1. Lean: `New.norm_iteratedDeriv_dslope_le`, `New.norm_taylorCoeff_dslope_le`, `New.one_sub_le_re_and_norm_le_of_mem_closedBall` in `src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean`.
