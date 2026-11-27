+++
id = "proofs/grh/derivatives-vacuum/theta-product-times-monomials-as-a-vector"
title = "Theta products times monomials in y are Taylor series of integral vectors"
kind = "lemma"
summary = "For a tight frame of length M and exponents e with 3 e_(b,i) <= c_i, the product over twelve copies of the series prod y(mu_i z)^(e_(b,i)) Theta is the p-adic Taylor series of a vector of the twelve space with p-integral values whose theta function is a theta function for pi_M a0^12."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_integral_isThetaFunction_twelveTaylor_eq", "New.Data.map_subst_linearSeries_copy"]
lean_files = ["src/New/Derivatives/Sharpness/BoundAttained.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/twelve-space-and-indicator-data|the twelve space]] and [[proofs/grh/derivatives-vacuum/resolution-forms-of-a-frame|resolution forms]]. Let \(p\) be a prime with a \(p\)-adic place \(\iota_p\); \(\theta\), \(y\) are the series of the [[proofs/grh/derivatives-vacuum/cm-curve-and-period|CM curve]] \(\mathcal{E}\).

**Lemma.** Let \((w_i)_{i\in J}\) with multiplicities \((c_i)\) be a tight frame of length \(M\), \(\mu\) its resolution forms, \(\Theta=\prod_i\theta(\mu_iz)^{c_i}\), and \(e_{b,i}\in\mathbb{N}\) (\(1\le b\le12\), \(i\in J\)) with \(3e_{b,i}\le c_i\). Then there is \(F\in\mathcal{S}(V_{12})\) with

1. \(\iota_p\mathcal{T}(F)=\prod_{b=1}^{12}\Bigl(\prod_iy(\mu_iz_b)^{e_{b,i}}\,\Theta(z_b)\Bigr)\), \(z_b\) the \(b\)-th copy of the variables;
2. \(\lvert\iota_pF(x_f)\rvert_p\le1\) for all finite adelic vectors \(x\);
3. \(\Theta_F\) is a [[?lean:New.IsThetaFunction|theta function]] for \(\pi_M\mathfrak{a}_0^{12}\).

## Proof

Apply [[proofs/grh/derivatives-vacuum/existence-of-resolution-product-along-tight-frame|the existence of resolution products]] to \(V_{12}\) (index set \(n=\{1,\dots,12\}\)), \(\delta=\bar\pi_M\), \(N=M\), the frame \((w,c)\), \(C=\mathcal{E}\), \(a=\Omega_0\) (area \(\lvert\Omega_0\rvert^2\sqrt d/2=\frac{\lvert a\rvert^2}{N}\frac{M\sqrt d}2\)), and the exponent triples \(x_{(i,b)}=(c_i-3e_{b,i},\,0,\,e_{b,i})\), of degree \(c_i\). The monomial section is \(\theta^{c_i-3e}G^{e}=y^{e}\theta^{c_i}\) near \(0\), as \(G=y\theta^3\). This gives \(F\) with 2 and 3 (\(\bar\delta=\pi_M\)).

For 1, use the jet series of the translate by \(\gamma=0\) ([[proofs/grh/derivatives-vacuum/resolution-product-theta-values-and-jets|jets of resolution products]]): the shifts vanish, and at the scale \(c=\pi_M\lambda\) the linear form of the factor \((i,b)\) has coefficients
\[ \frac{\Omega_0}{\pi_M}\cdot\frac{1}{c_A}\cdot\pi_M\frac{\varpi c_A}{\Omega_0}\,\overline{\Phi_\tau(w_i)}=\varpi\,\overline{\Phi_\tau(w_i)} \]
in the variables \(z_{\tau,b}\). Write \(\tilde\mu_i\) for this complex linear form, \(\tilde\mu_i(z)=\varpi\sum_\tau\overline{\Phi_\tau(w_i)}z_\tau\); the resolution form is its image, \(\mu_i=\iota_p(\tilde\mu_i)\). So, over \(\mathbb{C}\), \(\mathcal{T}(F)=\prod_{i,b}T(y^{e_{b,i}}\theta^{c_i})(\tilde\mu_iz_b)\), with \(T\) the complex Taylor series at \(0\) of the functions \(y\), \(\theta\) of \(\mathcal{E}\). Applying \(\iota_p\) to all coefficients commutes with products and with substitution of linear forms; it turns \(T(y)\), \(T(\theta)\) into the \(p\)-adic series \(y\), \(\theta\) and \(\tilde\mu_i\) into \(\mu_i\). Grouping the factors by \(b\) gives 1.

## References

1. Lean: `New.Data.exists_integral_isThetaFunction_twelveTaylor_eq`, `New.Data.map_subst_linearSeries_copy` in `src/New/Derivatives/Sharpness/BoundAttained.lean`.
