+++
id = "proofs/grh/derivatives-vacuum/sharpness-of-the-valuation-bound"
title = "Sharpness of the valuation bound"
kind = "theorem"
summary = "For every degree l between the weights and the weights plus x^42 there is one nonzero number t with all conjugates at most exp(f m b / k) such that at every prime some Taylor coefficient of degree l of an indicator datum modulo pi_M, times l! and the twelfth power of the vacuum scale and divided by t, has valuation at most the predicted valuation S_p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_rpow_neg_localPrimeSumTotal_le_norm_coeff", "New.Data.norm_natCast_prod_eq_rpow_neg_sum"]
lean_files = ["src/New/Derivatives/Sharpness/BoundAttained.lean"]
proof_status = "full"
+++

Let \(D\) be [[?lean:New.Data|admissible data]] over parameters \(P\), with field \(E\), places \(\Phi\) (\(f=\lvert\Phi\rvert\)), weights \(\kappa\), scales \(x,b\), ranks \(m,r\), \(k=r+1-m\), level \(M\) and \(\pi_M\). Notation as in [[proofs/grh/derivatives-vacuum/twelve-space-and-indicator-data|the twelve space]].

**Theorem.** Let \(l\colon\Phi\to\mathbb{N}\) with \(\kappa(\tau)\le l_\tau\le\kappa(\tau)+x^{42}\) for all \(\tau\). Then there is \(t\in\mathbb{C}\), \(t\ne0\), such that

1. \(\lvert\sigma(t)\rvert\le\exp(fmb/k)\) for every field automorphism \(\sigma\) of \(\mathbb{C}\);
2. for every modulus \(\mathfrak{m}\) of \(E\) with ideal \((\pi_M)\), every prime \(p\) and every \(p\)-adic place \(\iota_p\) of \(\mathbb{C}\), there are an exponent \(\gamma\) on \(\Phi\times\{1,\dots,12\}\) with \(\sum_b\gamma_{\tau,b}=l_\tau\) for all \(\tau\), and a class \(y_0\) modulo \(\mathfrak{m}\), such that
\[ \Bigl\lvert\iota_p\Bigl(\frac{c_{\mathrm{vac}}^{12}}{t}\prod_{\tau}l_\tau!\cdot[z^\gamma]\mathcal{T}(\mathbb{1}_{\mathfrak{m},y_0})\Bigr)\Bigr\rvert_p\ge p^{-S_p}, \]
where \(S_p\) is the [[?lean:New.Data.localPrimeSumTotal|predicted valuation]] at \(p\), evaluated at the weights and therefore independent of \(l\):
\[ S_p=\sum_{\tau\in\Phi}s_p(\kappa(\tau),\tau),\qquad s_p(y,\sigma)=v(\pi_p)\sum_{e\in I_p}\Bigl(\frac{y}{p^e}-\kappa([-p^e]\sigma)\Bigr)^{+}, \]
with \(s_p\) the [[?lean:New.Data.localPrimeSum|local prime sum]], \(I_p\) the set of positive partner exponents and \([\nu]\) the place named by \(\nu\).

## Proof

*The constant.* By [[proofs/grh/derivatives-vacuum/integral-vacuum-values|the values of the integral vacuum]] choose \(y\) with \(c_0=\theta^\circ(y_f)\ne0\), and put
\[ t=M^{12f}\prod_\tau B(l_\tau)^2\cdot c_0\ne0 . \]
Property 1 is [[proofs/grh/derivatives-vacuum/size-of-the-sharpness-constant|the lemma on its conjugates]].

*The frame.* By [[proofs/grh/derivatives-vacuum/tight-frame-of-length-m|the tight frame of length \(M\)]] there is a tight frame \((w,c)\) of length \(M\) with \(c_i\ge6fb\) and, for the given \(\iota_p\), a member \(w_{i_0}\) with a unit linear form. Since \(l_\tau\le2b\), \(3\lvert l\rvert\le6fb\le c_i\).

*The bound on the curve.* \(l\) is [[proofs/grh/derivatives-vacuum/degree-near-the-weights|near the weights]], so by [[proofs/grh/derivatives-vacuum/valuation-bound-on-twelve-copies|the valuation bound on twelve copies]]
\[ \operatorname{val}_{12}(l)\le r:=S_p+2\sum_\tau v_p(B(l_\tau))-\sum_\tau v_p(l_\tau!). \]

*Reduction.* By [[proofs/grh/derivatives-vacuum/reduction-to-the-curve|the reduction to the curve]] there are \(\gamma\), \(y_0\) with \(p^{-r}\lvert\iota_p(M^{12f}c_0)\rvert_p\le\lvert\iota_p(c_{\mathrm{vac}}^{12}[z^\gamma]\mathcal{T}(\mathbb{1}_{\mathfrak{m},y_0}))\rvert_p\). Recall that the \(p\)-adic absolute value of a product of nonzero natural numbers is \(p\) to minus the sum of their valuations. Multiply by \(\lvert\prod_\tau l_\tau!\rvert_p=p^{-\sum v_p(l_\tau!)}\) and divide by \(\lvert\iota_pt\rvert_p=\lvert\iota_p(M^{12f}c_0)\rvert_p\,p^{-2\sum v_p(B(l_\tau))}\) (nonzero as \(c_0\ne0\)): the left side becomes \(p^{-r-\sum v(l!)+2\sum v(B)}=p^{-S_p}\).

## References

1. Lean: `New.Data.exists_rpow_neg_localPrimeSumTotal_le_norm_coeff`, `New.Data.norm_natCast_prod_eq_rpow_neg_sum` in `src/New/Derivatives/Sharpness/BoundAttained.lean`.
2. The Lean file head names as related work (sharpness for one curve): K. Bannai and S. Kobayashi, Algebraic theta functions and the p-adic interpolation of Eisenstein-Kronecker numbers, 2006 (arXiv v1); K. Bannai, S. Kobayashi and S. Yasuda, Radius of convergence of the p-adic sigma function, 2017; P. Schneider and J. Teitelbaum, p-adic Fourier theory, 2001; K. Bannai and S. Kobayashi, Integral structures on p-adic Fourier theory, 2016 (no locators are given there).
