+++
id = "proofs/grh/reduction-zeros/riemann-formula-for-character"
title = "The L-function of a character as a Mellin transform, and the symmetry of its theta series"
kind = "theorem"
summary = "For non-principal chi of parity j and Re s > 0 the Mellin transform of the theta series at s - 1/2 is Gamma_j(s)L(s, chi); for primitive chi the absolute value of the theta series is invariant under u -> 1/(qu)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.hasMellin_thetaSeries_char", "New.mellin_gaussianTheta_char", "New.norm_thetaSeries_inv", "New.integral_norm_thetaSeries_div", "New.image_inv_const_mul_Ioo", "New.norm_thetaSeries"]
lean_files = ["src/Lib/Analytic/DirichletTheta.lean"]
proof_status = "full"
+++

**Theorem.** Let \(\chi\neq1\) be a complex Dirichlet character modulo \(q\ge1\) and \(j\in\{0,1\}\) with \(\chi(-1)=(-1)^{j}\). Let \(\theta_\chi(u)=\sqrt u\sum_{n\ge1}\chi(n)w_j(nu)\) be its [[proofs/grh/reduction-zeros/theta-series-of-coefficients|theta series]].

1. (Riemann's formula.) For \(\operatorname{Re}s>0\) the integral below converges absolutely and
\[
\int_0^\infty\theta_\chi(u)\,u^{s-1/2}\,\frac{du}u=\Gamma_j(s)\,L(s,\chi).
\]
2. (Symmetry.) If \(\chi\) is [[?c:primitive Dirichlet character|primitive]], then \(\lvert\theta_\chi(1/(qt))\rvert=\lvert\theta_\chi(t)\rvert\) for \(t>0\).
3. (Fold.) If \(\chi\) is primitive, \(\displaystyle\int_0^\infty\lvert\theta_\chi(u)\rvert\frac{du}u=2\int_{q^{-1/2}}^\infty\lvert\theta_\chi(u)\rvert\frac{du}u\).

## Proof

1. By the bound \(\lvert\vartheta_\chi(t)\rvert\le3eqe^{-t}\) of [[proofs/grh/reduction-zeros/poisson-summation-for-character-theta|Poisson summation]], the Mellin transform of \(\vartheta_\chi\) converges absolutely and is holomorphic on \(\operatorname{Re}s>0\) ([[proofs/grh/reduction-zeros/mellin-of-theta-series|part 3 there]]). So is \(\Gamma_jL(\cdot,\chi)\). The two agree for \(\operatorname{Re}s>1\) by the [[proofs/grh/reduction-zeros/mellin-of-theta-series|Mellin transform of a theta series]], hence on \(\operatorname{Re}s>0\) by the [[complex-analysis/identity-theorem|identity theorem]].

2. For primitive \(\chi\), \(\check\chi(n)=q^{-1}\tau(\chi)\overline{\chi(n)}\), so, \(w_j\) being real, \(\vartheta_{\check\chi}(u)=q^{-1}\tau(\chi)\overline{\vartheta_\chi(u)}\) and \(\lvert\vartheta_{\check\chi}(u)\rvert=q^{-1/2}\lvert\vartheta_\chi(u)\rvert\) by the [[proofs/grh/reduction-zeros/gauss-sum-modulus|modulus of the Gauss sum]]. By Poisson summation,
\[
\lvert\theta_\chi(1/(qt))\rvert=(qt)^{-1/2}\lvert\vartheta_\chi(1/(qt))\rvert=(qt)^{-1/2}q^{1/2}\lvert\vartheta_{\check\chi}(1/(qt))\rvert=t^{-1/2}\,t\,\lvert\vartheta_\chi(t)\rvert=\lvert\theta_\chi(t)\rvert .
\]

3. The integral converges by part 1 at \(s=\tfrac12\). The map \(u\mapsto1/(qu)\) is a bijection from \((0,q^{-1/2})\) onto \((q^{-1/2},\infty)\), preserves \(du/u\), and preserves \(\lvert\theta_\chi\rvert\) by part 2. So the integrals over the two intervals are equal. \(\blacksquare\)

## Remarks

The transformation formula is proved in absolute value only, so no root number appears.

## References

1. Lean: `New.hasMellin_thetaSeries_char`, `New.norm_thetaSeries_inv`, `New.integral_norm_thetaSeries_div` in `src/Lib/Analytic/DirichletTheta.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, 2007, Chapter 10 (as cited in the head of the Lean file).
