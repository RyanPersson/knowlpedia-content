+++
id = "proofs/grh/spanning-unfolding-b/trace-against-a-small-central-idempotent"
title = "Trace of the twisted translations against a small central idempotent"
kind = "lemma"
summary = "For a central idempotent x of one factor with real part of x(1) at most b^(-8)/2, the real part of the trace of r_psi(x) is at most b^(-4) times the source dimension."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.re_sum_coeff_mul_trace_besselTranslate_le", "New.Filling.sum_norm_sq_coeff_of_isCentralProj"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over a CM field with Weil data, \(i\in\{0,1\}\), and \(x\) a [[?lean:New.IsCentralProj|central idempotent]] of \(\mathbb{C}[G_i]\), where \(G_i\) is the factor of \(\bar G\) above \(p_i\), embedded by \(\phi_i\). Then \(\sum_{t\in G_i}\lvert x(t)\rvert^2=\operatorname{Re}x(1)\), and if \(\operatorname{Re}x(1)\le b^{-8}/2\), then
\[
\operatorname{Re}\sum_{t\in G_i}x(t)\operatorname{tr}r_\psi(\phi_i(t))\le b^{-4}\dim_S .
\]

## Proof

*The identity.* \(\lvert G_i\rvert x\) is a character of \(G_i\) ([[?lean:New.IsCentralProj.isChar_card_mul_coeff|central idempotents and characters]]), so \(x(t^{-1})=\overline{x(t)}\); comparing the coefficients of \(1\) in \(x\cdot x=x\) gives \(\sum_tx(t)x(t^{-1})=x(1)\), i.e. \(\sum_t\lvert x(t)\rvert^2=x(1)\).

*The bound.* \(\phi_i(t)\) is trivial above the other prime, so \(\operatorname{tr}r_\psi(\phi_i(t))=\dim_S\,\bar\psi_{\mathsf U}(\phi_i(t))\) by [[proofs/grh/spanning-unfolding-b/trace-of-the-twisted-translations|the trace of the twisted translations]]. Since \(x\) is a class function and \(g\phi_i(t)g^{-1}=\phi_i(g_itg_i^{-1})\), the sum \(\sum_tx(t)\bar\psi_{\mathsf U}(g\phi_i(t)g^{-1})\) does not depend on \(g\in\bar G\); averaging over \(g\) replaces \(\bar\psi_{\mathsf U}\) by its [[proofs/grh/spanning-unfolding-b/reduced-unipotent-character|conjugation mean]]. By the Cauchy–Schwarz inequality and [[proofs/grh/spanning-unfolding-b/square-sum-of-the-induced-character|the square sum of the induced character]] (restricted to the image of the injective map \(\phi_i\)),
\[
\Bigl\lvert\sum_tx(t)\bar\psi^\natural_{\mathsf U}(\phi_i(t))\Bigr\rvert^2\le\sum_t\lvert x(t)\rvert^2\cdot\sum_t\lvert\bar\psi^\natural_{\mathsf U}(\phi_i(t))\rvert^2\le\frac{b^{-8}}2\cdot2=b^{-8}.
\]
So the real part of the sum of traces is at most \(\dim_S\cdot b^{-4}\).

## References

1. Lean: `New.Filling.re_sum_coeff_mul_trace_besselTranslate_le`, `New.Filling.sum_norm_sq_coeff_of_isCentralProj` in `src/New/Spanning/Unfolding/Moments.lean`.
