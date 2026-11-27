+++
id = "proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier"
title = "The tail integral J and the mollifier"
kind = "definition"
summary = "For coefficients c and T > 0: the integral over u > 1/T of (|theta_c| + |theta_{mu c}|) du/u, and the truncated Mellin transform of theta_{mu c}."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.thetaTailIntegral", "New.mollifier", "New.thetaTailIntegral_eq_add", "New.mollifier_differentiableOn_and_bounded", "New.norm_mollifier_le", "New.norm_integral_cpow_smul_thetaSeries_le", "New.norm_cpow_smul_thetaSeries_le", "New.integral_norm_thetaSeries_div_nonneg"]
lean_files = ["src/Lib/Analytic/QuadraticTwist.lean"]
+++

Let \(j\in\{0,1\}\), let \(c\colon\mathbb{N}\to\mathbb{C}\) satisfy \(\lvert c(n)\rvert\le1\) for all \(n\), let \(T>0\), and let \(\theta_c\) be the [[proofs/grh/reduction-zeros/theta-series-of-coefficients|theta series]] of parity \(j\); write \(\mu c\) for the sequence \(n\mapsto c(n)\mu(n)\), with \(\mu\) the [[?c:Möbius function|Möbius function]]. The **tail integral** is
\[
J(c,T)=\int_{1/T}^\infty\bigl(\lvert\theta_c(u)\rvert+\lvert\theta_{\mu c}(u)\rvert\bigr)\frac{du}u ,
\]
and the **mollifier** is, for \(s\in\mathbb{C}\),
\[
\mathcal{M}(s)=\mathcal{M}_{c,T}(s)=\int_{1/T}^\infty\theta_{\mu c}(u)\,u^{s-1/2}\,\frac{du}u .
\]
Both integrals converge absolutely, by the bound \(\lvert\theta_c(u)\rvert\le3e^{-u}/\sqrt u\) (and the same for \(\mu c\), as \(\lvert\mu(n)c(n)\rvert\le1\)).

## Properties

* \(J(c,T)\) is finite and is the sum of the two tail integrals of \(\lvert\theta_c\rvert\) and \(\lvert\theta_{\mu c}\rvert\), each \(\ge0\).
* \(\mathcal{M}\) is holomorphic on \(\operatorname{Re}s>0\) and bounded on \(\tfrac12\le\operatorname{Re}s\le2\): it is the Mellin transform of \(\vartheta_{\mu c}\) cut to \(u>1/T\), which is at most \(3Te^{-u}\) in absolute value.
* On \(\operatorname{Re}s=\tfrac12\): \(\lvert\mathcal{M}(s)\rvert\le J(c,T)\), because \(\lvert u^{s-1/2}\rvert=1\).
* On \(\operatorname{Re}s=2\) and for \(u>0\): \(\lvert\theta_c(u)u^{s-1/2}/u\rvert\le3e^{-u}\), by the trivial bound \(\lvert\theta_c(u)\rvert\le3e^{-u}/\sqrt u\).

For a character \(c=\chi\), and for \(\operatorname{Re}s>1\), \(\mathcal{M}(s)\) is the truncation at \(1/T\) of the integral over \((0,\infty)\) that equals \(\Gamma_j(s)/L(s,\chi)\) by [[proofs/grh/reduction-zeros/mellin-of-theta-series|the Mellin transform of a theta series]].

## Remarks

In the source \(J\) and \(\mathcal{M}\) are defined for arbitrary \(c\) and \(T\) by integrals that take the value \(0\) when they do not converge; for unbounded coefficients they can diverge. Convergence is proved, and the objects are used, only for \(\lvert c(n)\rvert\le1\) and \(T>0\).

## References

1. Lean: `New.thetaTailIntegral`, `New.mollifier` and the lemmas named in the front matter, in `src/Lib/Analytic/QuadraticTwist.lean`.
