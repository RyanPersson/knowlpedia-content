+++
id = "proofs/grh/reduction-zeros/mellin-of-theta-series"
title = "The Mellin transform of a theta series"
kind = "proposition"
summary = "For bounded coefficients and Re s > 1 the Mellin transform of the theta series at s - 1/2 is Gamma_j(s) times the Dirichlet series; with coefficients chi mu it is Gamma_j(s)/L(s, chi)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.mellin_thetaSeries", "New.mellin_gaussianTheta", "New.mellin_thetaSeries_sub_half", "New.cpow_smul_thetaSeries", "New.mellin_pow_mul_comp_sq", "New.mellin_thetaSeries_moebius", "New.norm_mul_moebius_le_one", "New.mellinConvergent_and_differentiableAt", "New.mellin_differentiableOn_and_bounded"]
lean_files = ["src/Lib/Analytic/DirichletTheta.lean"]
proof_status = "full"
+++

**Proposition.** Let \(j\in\{0,1\}\), \(\lvert c(n)\rvert\le1\) for all \(n\), and \(\theta_c\), \(\Gamma_j\) as in [[proofs/grh/reduction-zeros/theta-series-of-coefficients|the definition of theta series]].

1. For \(\operatorname{Re}s>1\):
\[
\int_0^\infty\theta_c(u)\,u^{s-1/2}\,\frac{du}u=\Gamma_j(s)\sum_{n\ge1}c(n)n^{-s}.
\]
2. For a Dirichlet character \(\chi\) and the [[?c:Möbius function|Möbius function]] \(\mu\), the coefficients \(c=\chi\mu\) give, for \(\operatorname{Re}s>1\): \(\displaystyle\int_0^\infty\theta_{\chi\mu}(u)u^{s-1/2}\frac{du}u=\frac{\Gamma_j(s)}{L(s,\chi)}\).
3. If \(f\colon(0,\infty)\to\mathbb{C}\) is measurable with \(\lvert f(t)\rvert\le De^{-t}\), its Mellin transform converges absolutely and is holomorphic on \(\operatorname{Re}s>0\), and is bounded on \(\tfrac12\le\operatorname{Re}s\le2\).

## Proof

1. \(\theta_c(u)u^{s-1/2}=\vartheta_c(u)u^{s}\). For each \(n\), the substitution \(z=nu\) gives \(\int_0^\infty c(n)w_j(nu)u^{s}du/u=c(n)n^{-s}\Gamma_j(s)\). The sum over \(n\) may be taken outside the integral because \(\sum_n\lvert c(n)\rvert n^{-\operatorname{Re}s}\int_0^\infty\lvert w_j(z)\rvert z^{\operatorname{Re}s}dz/z<\infty\) for \(\operatorname{Re}s>1\).

2. \(\lvert\chi(n)\mu(n)\rvert\le1\) and \(\sum\chi(n)\mu(n)n^{-s}=1/L(s,\chi)\) for \(\operatorname{Re}s>1\).

3. The integrand \(f(t)t^{s-1}\) is dominated near \(0\) by \(Dt^{\operatorname{Re}s-1}\) and at infinity by \(De^{-t}t^{\operatorname{Re}s-1}\). On the strip, \(t^{\operatorname{Re}s-1}\le t^{-1/2}+t\), which gives a bound independent of \(s\). \(\blacksquare\)

## References

1. Lean: `New.mellin_thetaSeries`, `New.mellin_thetaSeries_moebius`, `New.mellin_differentiableOn_and_bounded` in `src/Lib/Analytic/DirichletTheta.lean`.
