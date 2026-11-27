+++
id = "proofs/grh/spanning-core/cut-pair-from-the-bessel-average"
title = "The normalised Bessel average and its cut form a cut pair"
kind = "theorem"
summary = "If the Bessel average at a point of bounded length has L2 norm not much smaller than a ball volume, a multiple of it is reproduced by the discrete series kernel and forms a cut pair with its cut."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_isCutPair_besselAverage", "New.exists_isDecayMajorant_besselAverage", "New.scaledBesselLength_pow_mul_enorm_besselAverage_le", "New.besselLength_div_le_half_norm", "New.lintegral_formalDegree_mul_decay_le", "New.formalDegree_mul_lintegral_decay_le", "New.formalDegree_mul_volume_ball_le", "New.norm_frameEquiv", "New.lintegral_besselGraph_mul_eq", "New.exists_enorm_sq_mul_eq"]
lean_files = ["src/New/Spanning/Bessel/CutTailBound.lean"]
proof_status = "outline"
+++

**Theorem.** Fix a unitary sign frame for signs \(\varepsilon\) on \(G_1\) (rank \(r\), \(n=\varrho+1\)), a doubled parameter \(l\) of [[?lean:New.HCParam.HasLargeGap|large gap with excess \(A\)]] and entries of modulus \(\le L\), with coefficient \(c_\lambda\) and formal degree \(\deg_\lambda\); a continuous \(\mathrm{rep}\colon U(\kappa)\to U(I)\), a unit vector \(v\), a point \(x\) with \(\ell(x)\le b^{5n}\), and \(W=\mathcal W_{x,v}\) the [[proofs/grh/spanning-core/bessel-period-group-and-average|Bessel average]]. Let \(f\ge1\), \(m\ge0\) and assume
\[
\mathrm{vol}_x\le b^m\deg_\lambda\int\lVert W\rVert^2d\mu,\qquad b\ge2000,\quad r\ge100,\quad m\le301r^2,\quad r+L+1\le b^4,\quad3r^3f\le A,
\]
with \(\mathrm{vol}_x\) as in [[proofs/grh/spanning-core/bessel-average-properties|the properties of the Bessel average]]. Then there are \(c\in\mathbb{R}\) and \(F=cW\), continuous, such that \(F*(\deg_\lambda c_\lambda)=F\) and \((F,F^\flat)\) is a [[proofs/grh/spanning-core/cut-pair-of-bessel-functions|cut pair]] for \((b,f,\mathrm{rep})\), where \(F^\flat\) is the [[proofs/grh/spanning-core/cut-of-a-bessel-function|cut]] of \(F\).

## Proof

*Outline.* By the [[proofs/grh/spanning-core/bessel-average-properties|properties of the Bessel average]], \(W\) is a Bessel function, reproduced by \(e=\deg_\lambda c_\lambda\) (hence continuous, as a convolution with an integrable kernel), and \(\mu\)-integrable; \(\int\lVert W\rVert^2d\mu\) is finite and nonzero (else \(\mathrm{vol}_x=0\)). Choose \(c\) with \(c^2\int\lVert W\rVert^2d\mu=\lvert I\rvert\) and put \(F=cW\). Properties 1–4 and 6 of a cut pair follow from the properties of the cut; property 5 from Property 4 of the cut once a decay majorant exists.

*Decay majorant.* Let \(N=9r^2\), \(\varphi(g)=(2/\lVert g\rVert)^N\), \(\Phi(y)=\int_R\varphi(x^{-1}gy)\,ds\), \(w=\lvert c\rvert\Phi\), \(a=\lvert c\rvert16^N\mathrm{vol}_x\).
* \(w\) is left \(S\)-invariant (right invariance of the measure on \(R\)) and \(\Phi\le16^N\mathrm{vol}_x\) (covering bound), so \(w\le a<\infty\).
* *Decay.* For \(s=(g,h)\in R\) and \(g'=x^{-1}gy\): \(\ell(y)=\ell(gy)\le\lVert g'\rVert\,\ell(x)\le\lVert g'\rVert b^{5n}\), so \(\ell(y)/b^{6n}\le\lVert g'\rVert/2\) (as \(b\ge2\)). With \(\lvert c_\lambda(g')\rvert\le(2/\lVert g'\rVert)^{i+N}\) for \(i=3r^3f\le A\) (library decay of the coefficient), \(\ell_b(y)^i\lvert c_\lambda(g')\rvert\le\varphi(g')\) (if \(\ell_b(y)=1\) use \(i=0\) and \(\lVert g'\rVert\ge1\)). Integrating over \(R\): \(\ell_b(y)^{3r^3f}\lVert F(y)\rVert\le w(y)\); the same for \(F^\flat\).
* *Mass.* By unfolding, \(\int\Phi\,d\mu=\int_{G_1}\varphi\). The library tail bound `New.integral_tail_le` gives \(\deg_\lambda\int_{G_1}(2/\lVert g\rVert)^M\le b^{50r^2+1}2^M\) for \(M>8r^2\) (after transport by the frame, which preserves norms, and using \(r+L+1\le b^4\), \(b\ge2000\)); hence \(\deg_\lambda\int\varphi\cdot16^N\le b^{99r^2}\). Therefore
\[
a\int w\,d\mu=c^2\,16^N\mathrm{vol}_x\int\varphi\le b^m\Bigl(\deg_\lambda\int\varphi\cdot16^N\Bigr)\Bigl(c^2\int\lVert W\rVert^2d\mu\Bigr)\le b^{m+99r^2}\lvert I\rvert\le b^{400r^2}\lvert I\rvert .
\]

Quoted from the library and not reproved: the tail bound `integral_tail_le` (its exact form \(b\,(b\cdot(b^4)^6)^{2r^2}2^M\) is read at the call site), the decay of the coefficient and the covering bound. \(\blacksquare\)

## Remarks

The Lean file head names as related work Muić (2015), Miličić (1977) and Wallach, *Real Reductive Groups II* (1992).

## References

1. Lean: `New.exists_isCutPair_besselAverage`, `New.exists_isDecayMajorant_besselAverage`, `New.scaledBesselLength_pow_mul_enorm_besselAverage_le` in `src/New/Spanning/Bessel/CutTailBound.lean`.
