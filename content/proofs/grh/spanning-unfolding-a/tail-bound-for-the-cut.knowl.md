+++
id = "proofs/grh/spanning-unfolding-a/tail-bound-for-the-cut"
title = "Cutting the Bessel function changes the block sums little"
kind = "theorem"
summary = "The sum over terms of the integrals of beta_c(y) beta_d(gamma^-1 y) times the norm of the difference between the kernel and the cut kernel is at most cov_U b^(-k^3 f) / 2."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.tsum_lintegral_enorm_besselKernel_sub_cut_le", "New.Filling.inv_pow_mul_unipotentCovolume_mul_card_le", "New.Filling.cut_exponent_le"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity with \(f\) [[?c:Infinite place of a number field|infinite places]], \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], with parameter \(b\), \(k=\dim X_0\), \(n=\varrho+1\), rank \(r\). Let \(T\) be a set of rational [[?c:Isometry of a hermitian space|isometries]], \(c\) a class, \(s\) in the residue group, \(\tau\) a side. Then
\[
\sum_d\sum_{\gamma\in T\cap\mathcal T(c,s,d)}\int_{G_\infty}\beta_c(y)\,\beta_d(\gamma^{-1}y)\,\bigl\lVert\mathcal K^{\tau}_\gamma(y)-\mathcal K^{\flat}_\gamma(y)\bigr\rVert\,dy\ \le\ \tfrac12\operatorname{cov}_{\mathsf U}\,b^{-k^{3}f},
\]
where \(\mathcal K^{\flat}\) is the [[?lean:New.Filling.besselKernel|Bessel kernel]] built from the cut function, \(\beta\) the [[?lean:New.Filling.classCutoff|class cutoffs]], \(\mathcal T\) the [[?lean:New.Filling.termsOver|terms]] and \(\operatorname{cov}_{\mathsf U}\) the [[?lean:New.Filling.unipotentCovolume|unipotent covolume]].

## Proof

Fix decay majorants \((w_v,a_v)\) and put \(i_0=r^3f\). By item 3 of the [[proofs/grh/spanning-unfolding-a/cut-changes-kernel-little|pointwise bounds]], the integrand is at most \(2b^{-2i_0}\beta_c(y)\beta_d(\gamma^{-1}y)\prod_vw_v(y_v)\prod_va_vP(\gamma^{-1}y)^{-i_0}\). By item 2 of the theorem on [[proofs/grh/spanning-unfolding-a/convergence-of-block-sums|convergence of block sums]], the left side is at most
\[
2b^{-2r^3f}\cdot\operatorname{cov}_{\mathsf U}\cdot2b^{12n^3rf}\cdot b^{400r^2f}\cdot\lvert I\rvert .
\]
It remains to see that \(8\,b^{12n^3rf}b^{400r^2f}\lvert I\rvert\,b^{k^3f}\le b^{2r^3f}\). By the standing hypotheses \(\lvert I\rvert\le b^{2kf}\) and \(8\le b\), so it suffices that
\[
1+12n^3rf+400r^2f+2kf+k^3f\le2r^3f .
\]
The data satisfy \(1000(2\varrho+2)^9\le k\), hence \(12n^3+500\le k\), and \(k+1\le r\), \(f\ge1\). Then \(12n^3r\le r^2\), \(2k+1\le r^2\), so the left side is at most \((402r^2+k^3)f\le(r^3+r^3)f\), using \(402\le r\) and \(k\le r\).

## References

1. Lean: `New.Filling.tsum_lintegral_enorm_besselKernel_sub_cut_le` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
2. Lean: `New.Filling.inv_pow_mul_unipotentCovolume_mul_card_le` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
3. Lean: `New.Filling.cut_exponent_le` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
