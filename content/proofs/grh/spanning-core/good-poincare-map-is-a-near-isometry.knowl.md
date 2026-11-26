+++
id = "proofs/grh/spanning-core/good-poincare-map-is-a-near-isometry"
title = "The projected Poincaré map is a near isometry"
kind = "theorem"
summary = "The scaled Poincaré map followed by the projector onto good forms is a near isometry with error 5 b^-4."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.isNearIsometry_e₀_comp_scaledPoincare", "New.Data.finrank_targetForms_ne_zero"]
lean_files = ["src/New/Spanning/SecondMoment/SpanningTheorem.lean"]
proof_status = "outline"
+++

**Theorem (good forms).** Let \(D\) be admissible data, \(P\) the [[proofs/grh/spanning-core/scaled-poincare-map|scaled Poincaré map]], \(e_0\) the [[?lean:New.Data.e₀|good idempotent]] acting on the forms of principal level on \(Y_0\) through \(\rho\), and \(b\) the scale of the data. Then \(\rho(e_0)P\) is a [[proofs/grh/spanning-core/near-isometry-in-mean-square|near isometry]] with error \(5b^{-4}\): for every subspace \(U\) of the source,
\[
\lVert\rho(e_0)\,P\,\mathrm{pr}_U\rVert_{\mathrm{HS}}^2\ \ge\ \dim U-5b^{-4}D_X .
\]
**Corollary.** The space of [[?lean:New.Data.targetForms|target forms]] is not zero.

## Proof

*Outline.* By [[proofs/grh/spanning-core/bad-types-are-rare|bad types are rare]], \(\rho(e_0)\) is the action of \(e_{p_0}\otimes e_{p_1}\) under the level representation, the \(e_{p_i}\) are central idempotents, and \(\operatorname{Re}(1-e_{p_i})(1)\le\frac12b^{-8}\). By [[proofs/grh/spanning-core/unfolding-of-the-scaled-poincare-map|unfolding]], \(P\) has amplitude blocks, and the level representation is unitary. These are exactly the hypotheses of [[?lean:New.Filling.HasAmplitudeBlocks.isNearIsometry_piTensorElem_comp|`New.Filling.HasAmplitudeBlocks.isNearIsometry_piTensorElem_comp`]] (area of `New/Spanning/Unfolding/Moments`), whose conclusion is the claim. (That theorem shows \(\lVert P^*P-1\rVert^2_{\mathrm{HS}}\le b^{-12}D_X\) and uses [[proofs/grh/spanning-core/near-isometry-from-small-defect|the defect criterion]] and [[proofs/grh/spanning-core/near-isometry-after-projection|the projection lemma]].)

For the corollary: the source is not zero and \(5b^{-4}<1\) (size inequality), so by Property 2 of [[proofs/grh/spanning-core/near-isometry-in-mean-square|near isometries]] the image of \(\rho(e_0)\), which is the space of target forms, is not zero. \(\blacksquare\)

## References

1. Lean: `New.Data.isNearIsometry_e₀_comp_scaledPoincare`, `New.Data.finrank_targetForms_ne_zero` in `src/New/Spanning/SecondMoment/SpanningTheorem.lean`.
