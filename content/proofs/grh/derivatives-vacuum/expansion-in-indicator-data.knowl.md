+++
id = "proofs/grh/derivatives-vacuum/expansion-in-indicator-data"
title = "A vector with integral values is bounded by indicator data"
kind = "lemma"
summary = "For a vector F of the twelve space with integral values whose theta function is a theta function for pi_M a0^12, and any linear form L, some indicator datum modulo pi_M has |L| at least that of M^(12f) L(F) times a value of the vacuum."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_norm_le_norm_indicatorDatum"]
lean_files = ["src/New/Derivatives/Sharpness/BoundAttained.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/derivatives-vacuum/twelve-space-and-indicator-data|the twelve space]]; \(f=\lvert\Phi\rvert\).

**Lemma.** Let \(F\in\mathcal{S}(V_{12})\) have \(\lvert\iota_pF(x_f)\rvert_p\le1\) for all finite adelic \(x\), and let \(\Theta_F\) be a theta function for \(\pi_M\mathfrak{a}_0^{12}\). Let \(\mathfrak{m}\) be a modulus of \(E\) with ideal \((\pi_M)\), \(L\colon\mathcal{S}(V_{12})\to\mathbb{C}\) a linear form and \(y\) a finite adelic vector. Then there is a class \(y_0\) modulo \(\mathfrak{m}\) with
\[ \bigl\lvert\iota_p\bigl(M^{12f}\,L(F)\,\mathrm{vac}(y_f)\bigr)\bigr\rvert_p\le\bigl\lvert\iota_p\,L(\mathbb{1}_{\mathfrak{m},y_0})\bigr\rvert_p . \]

## Proof

Finite Fourier inversion for \(\delta=\bar\pi_M\), \(N=M\) ([[?lean:New.Space.exists_fourier_coefficients|Fourier coefficients of a theta function]]; asserted) gives a finite set \(Y\), vectors \(u_i\in E^{12}\) with \(\bar\pi_Mu_i\in\mathfrak{a}_0^{12}\), and coefficients \(c_i\) such that
\[ M^{12f}F=\sum_{i\in Y}c_i\,\varrho((u_i)_f)\mathrm{vac},\qquad c_i\,\mathrm{vac}=\text{a sum of Heisenberg translates of }F. \]
From the second identity and the integrality of the values of \(F\), the values of \(c_i\mathrm{vac}\) are integral (Lean `New.Space.norm_mul_vacElem_le_one_of_eq_sum`); in particular \(\lvert\iota_p(c_i\mathrm{vac}(y_f))\rvert_p\le1\). Each translate \(\varrho((u_i)_f)\mathrm{vac}\) with \(\bar\pi_M\alpha^{-1}u_i\) integral is a sum over the classes \(y_0\) modulo \((\pi_M)\) of indicator data times values of the self-dual character, i.e. roots of unity (Lean `New.exists_rho_finVec_vacElem_eq_sum_modDatum`; asserted). Hence
\[ M^{12f}L(F)\,\mathrm{vac}(y_f)=\sum_{i,y_0}\psi_{i,y_0}\cdot\bigl(c_i\mathrm{vac}(y_f)\bigr)\cdot L(\mathbb{1}_{\mathfrak{m},y_0}), \]
and by the ultrametric inequality the left side is bounded by \(\max_{y_0}\lvert\iota_pL(\mathbb{1}_{\mathfrak{m},y_0})\rvert_p\), a maximum over a finite set.

## References

1. Lean: `New.Data.exists_norm_le_norm_indicatorDatum` in `src/New/Derivatives/Sharpness/BoundAttained.lean`.
