+++
id = "proofs/grh/reduction-zeros/theta-series-of-coefficients"
title = "Theta series with a Gaussian weight"
kind = "definition"
summary = "For a parity j and coefficients c(n), the series sqrt(u) times the sum of c(n) w(nu) with w(z) = z^j exp(-pi z^2), and the Mellin transform of the weight."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.gaussianMonomial", "New.gaussianTheta", "New.thetaSeries", "New.gaussianMellin", "New.gaussianMellin_eq", "New.norm_gaussianMonomial_le", "New.summable_and_norm_gaussianTheta_le", "New.norm_thetaSeries_le", "New.integrableOn_norm_thetaSeries_div", "New.gaussianMellin_differentiableOn_and_bdd", "New.exists_pos_le_norm_gaussianMellin"]
lean_files = ["src/Lib/Analytic/DirichletTheta.lean"]
+++

Let \(j\in\{0,1\}\) and let \(c\colon\mathbb{N}\to\mathbb{C}\) be a sequence. The **weight of parity \(j\)** is \(w_j(z)=z^{j}e^{-\pi z^{2}}\) for real \(z\). For real \(u\) put
\[
\vartheta_c(u)=\sum_{n\ge1}c(n)\,w_j(nu),\qquad\theta_c(u)=\sqrt u\;\vartheta_c(u),
\]
the **theta series** of \(c\) (of parity \(j\)), and
\[
\Gamma_j(s)=\int_0^\infty w_j(z)\,z^{s}\,\frac{dz}{z}\qquad(\operatorname{Re}s>0),
\]
the [[?c:Mellin transform|Mellin transform]] of the weight.

## Properties

Assume \(\lvert c(n)\rvert\le1\) for all \(n\), and \(t>0\).

* \(\lvert w_j(t)\rvert\le3e^{-2t}\) for \(t\ge0\). (Indeed \(t^{j}\le e^{t}\) and \(t-\pi t^{2}\le1-2t\).)
* The series converges absolutely, \(\lvert\vartheta_c(t)\rvert\le3e^{-t}/t\) and \(\lvert\theta_c(t)\rvert\le3e^{-t}/\sqrt t\). (Compare with \(\sum_{n\ge1}3e^{-2nt}=3e^{-2t}/(1-e^{-2t})\) and use \(te^{-t}\le1-e^{-2t}\).)
* For \(r>0\) the integral \(\int_r^\infty\lvert\theta_c(u)\rvert\,du/u\) converges.
* \(\Gamma_j(s)=\tfrac12\,\Gamma_{\mathbb{R}}(s+j)=\tfrac12\pi^{-(s+j)/2}\Gamma\bigl(\tfrac{s+j}2\bigr)\) for \(\operatorname{Re}s>0\). It is holomorphic on \(\operatorname{Re}s>0\), bounded on \(\tfrac12\le\operatorname{Re}s\le2\), has no zero, and is bounded away from \(0\) on every compact subset of \(\operatorname{Re}s>0\).

## References

1. Lean: `New.gaussianMonomial`, `New.gaussianTheta`, `New.thetaSeries`, `New.gaussianMellin` and the lemmas named in the front matter, in `src/Lib/Analytic/DirichletTheta.lean`.
