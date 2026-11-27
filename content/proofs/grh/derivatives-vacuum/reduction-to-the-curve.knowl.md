+++
id = "proofs/grh/derivatives-vacuum/reduction-to-the-curve"
title = "Reduction of the sharpness bound to the curve"
kind = "theorem"
summary = "If val_12(l) <= r for a tight frame of length M with multiplicities at least 3|l|, then some Taylor coefficient of degree l of an indicator datum modulo pi_M, times the twelfth power of the vacuum scale, has valuation at most r plus that of M^(12f) times a value of the integral vacuum."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_le_norm_coeff_indicatorDatum"]
lean_files = ["src/New/Derivatives/Sharpness/BoundAttained.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/theta-product-times-monomials-as-a-vector|the previous lemmas]]; \(\theta^\circ\) is the [[proofs/grh/derivatives-vacuum/integral-vacuum|integral vacuum]] of \(V_{12}\) and \(c_{\mathrm{vac}}\) the vacuum scale.

**Theorem.** Let \((w,c)\) be a tight frame of length \(M\), \(l\) a degree on \(\Phi\) with \(3\lvert l\rvert\le c_i\) for all \(i\), and suppose \(\operatorname{val}_{12}(l)\le r\) ([[proofs/grh/derivatives-vacuum/least-valuation-relation|least valuation]] for \(\mathcal{E}\), the resolution forms of \(w\), and \(c\)). Let \(\mathfrak{m}\) be a modulus with ideal \((\pi_M)\) and \(y\) a finite adelic vector. Then there are an exponent \(\gamma\) on \(\Phi\times\{1,\dots,12\}\) with \(\sum_b\gamma_{\tau,b}=l_\tau\) for all \(\tau\), and a class \(y_0\) modulo \(\mathfrak{m}\), with
\[ p^{-r}\,\bigl\lvert\iota_p\bigl(M^{12f}\theta^\circ(y_f)\bigr)\bigr\rvert_p\le\bigl\lvert\iota_p\bigl(c_{\mathrm{vac}}^{12}\,[z^\gamma]\mathcal{T}(\mathbb{1}_{\mathfrak{m},y_0})\bigr)\bigr\rvert_p . \]

## Proof

By rule 4 of [[proofs/grh/derivatives-vacuum/least-valuation-rules|the rules]] there are exponents \(\alpha_b\) with \(\sum_b\alpha_b=l\) and monomials \(\prod_iy(\mu_iz)^{e_{b,i}}\), \(\lvert e_b\rvert\le\lvert l\rvert\), with \(\prod_b\lvert[z^{\alpha_b}](\prod_iy(\mu_iz)^{e_{b,i}}\Theta)\rvert_p\ge p^{-r}\). Then \(3e_{b,i}\le3\lvert l\rvert\le c_i\), so [[proofs/grh/derivatives-vacuum/theta-product-times-monomials-as-a-vector|the lemma on vectors]] gives \(F\); let \(\gamma\) be the copy exponent of \((\alpha_b)\) and \(a=[z^\gamma]\mathcal{T}(F)\). By the product property of copy exponents, \(\lvert\iota_pa\rvert_p\ge p^{-r}\).

Apply [[proofs/grh/derivatives-vacuum/expansion-in-indicator-data|the expansion in indicator data]] to the linear form \(L=c_{\mathrm{vac}}^{12}\,[z^\gamma]\mathcal{T}(\cdot)\): there is \(y_0\) with \(\lvert\iota_p(M^{12f}c_{\mathrm{vac}}^{12}a\,\mathrm{vac}(y_f))\rvert_p\le\lvert\iota_pL(\mathbb{1}_{\mathfrak{m},y_0})\rvert_p\). Since \(V_{12}\) has rank \(12\), \(\theta^\circ=c_{\mathrm{vac}}^{12}\mathrm{vac}\), so the left side is \(\lvert\iota_pa\rvert_p\,\lvert\iota_p(M^{12f}\theta^\circ(y_f))\rvert_p\ge p^{-r}\lvert\iota_p(M^{12f}\theta^\circ(y_f))\rvert_p\).

## References

1. Lean: `New.Data.exists_le_norm_coeff_indicatorDatum` in `src/New/Derivatives/Sharpness/BoundAttained.lean`.
