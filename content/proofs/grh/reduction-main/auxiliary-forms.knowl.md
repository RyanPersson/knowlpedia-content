+++
id = "proofs/grh/reduction-main/auxiliary-forms"
title = "Auxiliary forms span the target"
kind = "theorem"
summary = "There are nonzero scalars gamma(theta), of absolute value a power of Nm Q(theta) times m^2 ratios of Hecke values, such that the target is spanned by forms whose scaled lifts are integral away from the modulus and whose untwisted lift is short at every conjugate."
aliases = ["IsAuxiliaryForm", "auxiliary form", "exists_span_isAuxiliaryForm_eq_top"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsAuxiliaryForm", "New.Data.exists_span_isAuxiliaryForm_eq_top", "New.Data.HasSmallRatios.heightLe_inv_rpow_mul_prod_turnRatio", "New.Data.mul_completion_cost_le"]
lean_files = ["src/New/Determinant/Twist/LongForms.lean"]
proof_status = "outline"
+++

**Definition.** Let \(D\) be [[proofs/grh/reduction-main/data|data]] and \(\gamma\) a function from the [[proofs/grh/reduction-main/m-fold-twist|\(m\)-fold twists]] to \(\mathbb C\). A target form \(y\in\mathcal T\) is **auxiliary for \(\gamma\)** if

1. \(\gamma(\vartheta)\Theta_\vartheta y\) is integral at \(\iota\) for every finite place \(\iota\mid\ell\) and every \(m\)-fold twist \(\vartheta\) with \(\gcd(\ell,\mathrm{Nm}\,Q(\vartheta))=1\); and
2. \(\lVert\Theta_1y\rVert_\sigma^2\le\exp(2x_1^2b^2)\) for every \(\sigma\in\operatorname{Aut}(\mathbb C)\).

(Notation of the [[proofs/grh/reduction-main/target-lattice|target lattice]].)

**Theorem (auxiliary forms).** There are an integer \(e\) and numbers \(\gamma(\vartheta)\in\mathbb C^\times\) with \(\gamma(1)=1\) and
\[
\lvert\gamma(\vartheta)\rvert=\bigl(\mathrm{Nm}\,Q(\vartheta)\bigr)^{e/2}\prod_{0\le i,j<m}\operatorname{turn}_{i,j}(\vartheta)\qquad\text{for all }\vartheta ,
\]
where \(\operatorname{turn}_{i,j}\) are the [[?lean:New.Data.turnRatio|turn ratios]] (products of ratios of Hecke \(L\)-values), such that \(\mathcal T\) is spanned by the forms auxiliary for \(\gamma\).

**Lemma.** (a) If the family \(\theta\) [[proofs/grh/reduction-main/regular-family-of-twists|has small ratios]], then for every integer \(e\) the family \(\iota\mapsto\bigl(\mathrm{Nm}Q(\theta_\iota)^{e/2}\prod_{i,j<m}\operatorname{turn}_{i,j}(\theta_\iota)\bigr)^{-1}\) has height at most \(m^2\,t\,x_1\). (b) If \(n\ge(1-4/b^2)d_T\) and \(d_T=n+n'\), then \(n'(2x_1^2b^2+b)\le d_T\,b\).

## Proof

*Theorem (outline).* The file [[?lean:New.Data.exists_span_short_lifts_eq_top|spanning forms with short lifts]] provides scalars \(c(\vartheta)\in\mathbb C^\times\) whose absolute value is, up to a constant factor and a fixed power of \(\mathrm{Nm}Q(\vartheta)\), the product of the turn ratios, such that the forms of principal level on \(Y_0\) are spanned by forms \(\psi\) with \((c(\vartheta)/c(1))\,\iota_\vartheta\psi\) integral at every prime not dividing \(\mathrm{Nm}Q(\vartheta)\) and with all conjugate values of \(\iota_1\psi\) of squared norm \(\le\exp(x^{202}b^2)\). Put \(\gamma(\vartheta)=c(\vartheta)/c(1)\); the formula for \(\lvert\gamma\rvert\) follows since the turn ratios are \(1\) at the trivial twist and are nonnegative (`HasAbsUpToNormPower.exists_norm_div_eq`). Apply the surjection \(\psi\mapsto\#\bar G\,e_0\psi\) onto \(\mathcal T\): it maps a spanning set to a spanning set, keeps the lifts integral ([[?lean:New.Data.goodProjTranslate_mem_integralForms|integrality of the good part]]), and raises the logarithm of the squared norms by at most \(x^{99}\) ([[?lean:New.Data.normSqAt_goodProjTranslate_le|size of the good part]]); and \(x^{99}+x^{202}b^2\le2x_1^2b^2\). The quoted statements are asserted here.

*Lemma.* (a) is the general bound [[?lean:New.Data.HasSmallRatios.heightLe_inv_rpow_mul_prod|height of inverse ratio products]] (\(\#s\cdot t\,x_1\) for \(\#s\) ramified ratios; the power of \(\mathrm{Nm}Q\) costs nothing by the unit rule of [[proofs/grh/reduction-main/height-calculus|the calculus of heights]]) applied to the \(m^2\) turn ratios. (b) \(n'=d_T-n\le\frac4{b^2}d_T\), so \(n'(2x_1^2b^2+b)\le d_T\cdot4(2x_1^2+b^{-1})\le d_Tb\), as \(8x_1^2+4\le b\).

## References

1. Lean: `New.Data.IsAuxiliaryForm`, `New.Data.exists_span_isAuxiliaryForm_eq_top`, `New.Data.HasSmallRatios.heightLe_inv_rpow_mul_prod_turnRatio`, `New.Data.mul_completion_cost_le` in `src/New/Determinant/Twist/LongForms.lean`.
