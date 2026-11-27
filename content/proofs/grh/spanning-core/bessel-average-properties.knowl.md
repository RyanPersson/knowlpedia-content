+++
id = "proofs/grh/spanning-core/bessel-average-properties"
title = "The Bessel average is a Bessel function reproduced by the discrete series kernel"
kind = "theorem"
summary = "For a parameter of large gap the Bessel average converges absolutely, is a bounded Bessel function, is integrable on the quotient, is fixed by the kernel of the discrete series, and its L2 norm is a period."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DiscreteSeries.integrable_besselIntegrand", "New.DiscreteSeries.isBesselFunction_besselAverage", "New.DiscreteSeries.besselAverage_mul", "New.DiscreteSeries.convolve_besselAverage", "New.DiscreteSeries.integrable_besselAverage", "New.DiscreteSeries.formalDegree_mul_integral_norm_sq_besselAverage", "New.DiscreteSeries.besselBallVolume_le_of_period", "New.DiscreteSeries.besselBallVolume", "New.DiscreteSeries.lintegral_decay_le_besselBallVolume", "New.DiscreteSeries.lintegral_enorm_besselIntegrand_le", "New.DiscreteSeries.norm_dsCoeffInFrame_le", "New.DiscreteSeries.lintegral_unfold_besselGraphMeasure", "New.DiscreteSeries.measurePreserving_unfold_besselGraphMeasure", "New.DiscreteSeries.enorm_besselAverage_le"]
lean_files = ["src/New/Spanning/Bessel/LargeFunction.lean"]
proof_status = "outline"
+++

**Theorem.** Fix a unitary sign frame for signs \(\varepsilon\), a doubled parameter \(l\) with [[?lean:New.HCParam.HasLargeGap|large gap]] (gap \(500r^3+\mathrm{exc}\)), coefficient \(c_\lambda\) and formal degree \(\deg_\lambda\); a continuous \(\mathrm{rep}\colon U(\kappa)\to U(I)\); a unit vector \(v\in\mathbb{C}^I\); and \(x\in G_1\). Let \(W=\mathcal W_{x,v}\) be the [[proofs/grh/spanning-core/bessel-period-group-and-average|Bessel average]] and \(\pi(g,h)=\psi(g)\,\mathrm{rep}(h)\) on \(R\). Let \(\mathrm{vol}_x\) be the measure of \(\{s=(g,h)\in R:\lVert x^{-1}gx-1\rVert\le1\}\) (norm in the frame), which is finite and nonzero.

1. \(\int_R\lVert c_\lambda(x^{-1}gy)\,\pi(s)^{-1}v\rVert\,ds\le16^{9r^2}\mathrm{vol}_x\) for every \(y\); in particular the average converges absolutely and \(\lVert W\rVert\le16^{9r^2}\mathrm{vol}_x\).
2. \(W(gy)=\pi(s)W(y)\) for \(s=(g,h)\in R\); hence \(W\) is a [[?lean:New.IsBesselFunction|Bessel function of type \(\mathrm{rep}\)]].
3. \(\int_{G_1}\deg_\lambda c_\lambda(a^{-1})\,W(ya)\,da=W(y)\).
4. \(W\) is integrable for the measure \(\mu\) of \(\mathsf U\backslash G_1\), and \(\deg_\lambda\int\lVert W\rVert^2d\mu=\langle v,W(x)\rangle\).
5. If moreover \(\langle v,\mathrm{rep}(k)v\rangle=c_u(k)\) for a parameter \(u\) of \(U(\kappa)\), and \(\mathrm{vol}_x\le P\cdot\lvert\text{period}\rvert\) with the period of the [[proofs/grh/spanning-core/stationary-point-with-large-period|stationary point theorem]] and \(P\ge0\), then \(\mathrm{vol}_x\le P\deg_\lambda\int\lVert W\rVert^2d\mu\).

## Proof

*Outline.* Library inputs, used as named and not reproved (their statements were read at the call sites): the decay \(\lvert c_\lambda(g)\rvert\le(2/\lVert g\rVert)^{j+9r^2}\) for \(j\le\mathrm{exc}\) (`New.norm_dsCoeff_le_pow`); the covering bound for a proper homomorphism \(j\) into \(U(\varepsilon)\): \(\int(2/\lVert j(s)g_0\rVert)^{N}ds\le16^{N}\operatorname{vol}\{\lVert j(s)-1\rVert\le1\}\), \(N=9r^2\) (`New.lintegral_decay_le`); that \(\deg_\lambda c_\lambda\) is an integrable idempotent kernel with the product formula \(\int\deg_\lambda c_\lambda(a^{-1})c_\lambda(ga)\,da=c_\lambda(g)\) (`New.isIdempotentKernel_dsCoeffInFrame`).

(1) \(\pi\) is unitary and \(\lVert v\rVert=1\), so the norm of the integrand is \(\lvert c_\lambda(x^{-1}gy)\rvert\le(2/\lVert x^{-1}gy\rVert)^{9r^2}\); apply the covering bound to \(s\mapsto x^{-1}gx\) (proper) at the point \(x^{-1}y\).

(2) Substitute \(t\mapsto ts^{-1}\) in the integral (the measure on \(R\) is right invariant, \(\sigma\) is additive on \(S\), so \(\psi\) is a character); the unitary operator \(\pi(s)\) comes out of the absolutely convergent integral. Boundedness is (1); measurability follows from joint continuity of the integrand.

(3) Exchange the integral over \(a\in G_1\) with that over \(R\) (Fubini; the double integral converges by (1) and integrability of the kernel) and apply the product formula under the integral.

(4) \(\int\lVert W\rVert d\mu\le\int\!\!\int_R\lvert c_\lambda(x^{-1}gy)\rvert\,ds\,d\mu(y)=\int_{G_1}\lvert c_\lambda\rvert<\infty\), by the unfolding \(\int_{G_1}f=\int\!\int_Rf(x\,g\,y)\,ds\,d\mu(y)\) (from the unfolding along \(\mathsf U\) and the total mass \(1\) of \(U(\kappa)\)). For the norm: with \(\Phi(g)=\overline{\deg_\lambda c_\lambda(x^{-1}g)}\langle v,W(g)\rangle\), (2) and unitarity give \(\int_R\Phi(gy)\,ds=\deg_\lambda\lVert W(y)\rVert^2\); integrate over \(\mu\), unfold to \(\int_{G_1}\Phi\), substitute \(g=xa\), use \(\overline{c_\lambda(a)}=c_\lambda(a^{-1})\) and (3) at \(y=x\).

(5) The hypothesis on \(v\) gives \(\overline{c_u(h)}=\langle v,\mathrm{rep}(h)^{-1}v\rangle\), so the period equals \(\langle v,W(x)\rangle=\deg_\lambda\int\lVert W\rVert^2d\mu\ge0\) by (4). \(\blacksquare\)

## References

1. Lean: `New.DiscreteSeries.isBesselFunction_besselAverage`, `New.DiscreteSeries.convolve_besselAverage`, `New.DiscreteSeries.integrable_besselAverage`, `New.DiscreteSeries.formalDegree_mul_integral_norm_sq_besselAverage`, `New.DiscreteSeries.besselBallVolume_le_of_period` in `src/New/Spanning/Bessel/LargeFunction.lean`.
