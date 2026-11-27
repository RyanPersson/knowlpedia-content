+++
id = "proofs/grh/spanning-unfolding-a/moving-a-block-by-the-bessel-subgroup"
title = "Moving a block by elements of the Bessel subgroup"
kind = "proposition"
summary = "If sigma, sigma' in the Bessel subgroup are terms over (c, t, c_1) and (c', t', c_1'), a linear map carrying the kernel at (gamma, y) to the kernel at (sigma gamma sigma'^-1, sigma y) carries the block over (c_1, s, c_1') to the block over (c, t s t'^-1, c')."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.amplitudeSum_mul_mul_inv", "New.Filling.tsum_classCutoff_ratToInf_mul_eq_one", "New.Filling.mem_termsOver_iff_mul_mul_inv_mem"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Proposition.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], \(T\) a [[?lean:New.Filling.IsStable|stable]] set and \(\tau\) a side. Let \(\sigma,\sigma'\) be rational points of the [[?lean:New.Shape.Form.besselS|Bessel subgroup]] such that \(\sigma\) is a [[?lean:New.Filling.termsOver|term]] over \((c,t,c_1)\) and \(\sigma'\) a term over \((c',t',c_1')\), and such that \(\gamma\in T\iff\sigma\gamma\sigma'^{-1}\in T\) for all \(\gamma\). Let \(L\) be a continuous linear endomorphism of \(\mathbb C^{I\times I}\) with
\[
\mathcal K^{\tau}_{\sigma\gamma\sigma'^{-1}}(\sigma y)=L\bigl(\mathcal K^{\tau}_\gamma(y)\bigr)\qquad\text{for all }\gamma,\ y .
\]
Then for every \(s\) in the residue group
\[
A^{\tau}_T(c,\;t\,s\,t'^{-1},\;c')=L\bigl(A^{\tau}_T(c_1,s,c_1')\bigr).
\]

## Proof

*Terms.* Since terms are closed under inverses and composable products, \(\gamma\) is a term over \((c_1,s,c_1')\) if and only if \(\sigma\gamma\sigma'^{-1}\) is a term over \((c,tst'^{-1},c')\). Together with the hypothesis on \(T\), \(\gamma\mapsto\sigma\gamma\sigma'^{-1}\) is a bijection \(T\cap\mathcal T(c_1,s,c_1')\to T\cap\mathcal T(c,tst'^{-1},c')\).

*Translated cutoffs.* For every \(y\), \(\sum_{u\in\mathsf U_{c_1}(M)}\beta_c(\sigma u y)=1\). Indeed the Bessel subgroup normalises \(\mathsf U\), and by the statement on terms (with \(s=1\), \(\sigma'=\sigma\)) conjugation by \(\sigma\) maps \(\mathsf U_{c_1}(M)\) bijectively onto \(\mathsf U_c(M)\); so the sum is \(\sum_{u\in\mathsf U_c(M)}\beta_c(u\sigma y)=1\) by the proposition on [[proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one|class cutoffs]]. The same holds for \(\sigma'\).

*Change of weight.* Let \(\varphi(\gamma,y)=\beta_c(\sigma y)\,\beta_{c'}(\sigma'\gamma^{-1}y)\). Its sum over the orbit of \((\gamma,y)\) under \(\mathsf U_{c_1}(M)\times\mathsf U_{c_1'}(M)\) is the product of the two sums above (note \((u\gamma u'^{-1})^{-1}uy=u'\gamma^{-1}y\)), hence \(1\). By the theorem on [[proofs/grh/spanning-unfolding-a/change-of-weight-in-block-sums|change of weight]], \(A^{\tau}_T(c_1,s,c_1')=\sum_\gamma\int\varphi(\gamma,y)\mathcal K^{\tau}_\gamma(y)\,dy\) with integrable integrands. Apply \(L\), which commutes with the integral and the sum, and use the hypothesis on \(L\):
\[
L\int\varphi(\gamma,y)\mathcal K^{\tau}_\gamma(y)\,dy=\int\beta_c(\sigma y)\beta_{c'}\bigl((\sigma\gamma\sigma'^{-1})^{-1}\sigma y\bigr)\mathcal K^{\tau}_{\sigma\gamma\sigma'^{-1}}(\sigma y)\,dy=\mathcal A^{\tau}(c,c';\sigma\gamma\sigma'^{-1}),
\]
by the invariance of [[harmonic-analysis/haar-measure|Haar measure]] under \(y\mapsto\sigma y\). Summing over \(\gamma\) through the bijection gives the claim.

## References

1. Lean: `New.Filling.amplitudeSum_mul_mul_inv` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
2. Lean: `New.Filling.tsum_classCutoff_ratToInf_mul_eq_one` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
3. Lean: `New.Filling.mem_termsOver_iff_mul_mul_inv_mem` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
