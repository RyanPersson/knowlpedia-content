+++
id = "proofs/grh/spanning-unfolding-a/unfolding-class-cutoff-against-invariant-weights"
title = "Unfolding a class cutoff against unipotent-invariant weights"
kind = "lemma"
summary = "The integral over G_infinity of a class cutoff times a product of left U-invariant local weights is the unipotent covolume times the product of the integrals of the weights over U backslash G_1."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.lintegral_classCutoff_mul_prod", "New.Filling.measurePreserving_pi_orbitMeasure", "New.Filling.integral_classCutoff_eq_unipotentCovolume"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity and \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]]. For each [[?c:Infinite place of a number field|infinite place]] \(v\) let \(w_v:G_1\to[0,\infty]\) be measurable and left invariant under the real unipotent group: \(w_v(ux)=w_v(x)\) for \(u\in\mathsf U\). Then for every class \(c\)
\[
\int_{G_\infty}\beta_c(y)\prod_vw_v(y_v)\,dy=\operatorname{cov}_{\mathsf U}\cdot\prod_v\int_{\mathsf U\backslash G_1}w_v\,d\dot x ,
\]
where \(\beta_c\) is the [[?lean:New.Filling.classCutoff|class cutoff]], \(dy\) is the product of the [[harmonic-analysis/haar-measure|Haar measures]] of \(G_1\), \(\operatorname{cov}_{\mathsf U}\) is the [[?lean:New.Filling.unipotentCovolume|unipotent covolume]], and \(d\dot x\) is the [[?lean:New.besselQuotMeasure|quotient measure on \(\mathsf U\backslash G_1\)]] for the Haar measure [[?lean:New.Shape.besselHaar|\(\mu_{\mathsf U}\)]] (in the source: Haar measure of \(G_1\) weighted by a chosen cutoff for \(\mathsf U\), so that integrals of invariant functions are integrals over the quotient).

## Proof

*Unfolding.* For a unimodular Haar measure \(\nu\) on a closed subgroup \(A\subseteq G_1\) with [[?c:Quotient measure on a homogeneous space|quotient measure]] \(\dot\mu\), the map \((x,u)\mapsto ux\) carries \(\dot\mu\otimes\nu\) to the Haar measure of \(G_1\) ([[?lean:New.measurePreserving_orbitMeasure|unfolding over a subgroup]]); taking products over the finitely many places, \((x,u)\mapsto(u_vx_v)_v\) carries \(\prod_v\dot\mu\otimes\prod_v\nu\) to the Haar measure of \(G_\infty\). Apply this with \(A=\mathsf U\), \(\nu=\mu_{\mathsf U}\), and use [[?c:Tonelli's theorem|Tonelli's theorem]]:
\[
\int_{G_\infty}\beta_c(y)\prod_vw_v(y_v)\,dy=\int\Bigl(\int_{\mathsf U_\infty}\beta_c(u\,x)\,d\mu(u)\Bigr)\prod_vw_v(x_v)\,d\dot x ,
\]
because \(w_v(u_vx_v)=w_v(x_v)\).

*The inner integral* equals \(\operatorname{cov}_{\mathsf U}\) for every \(x\), by the theorem on [[proofs/grh/spanning-unfolding-a/integral-of-class-cutoff-is-unipotent-covolume|the integral of a class cutoff]]. The remaining integral of a product of functions of the separate variables over a product measure is the product of the integrals.

## Remarks

The same theorem gives, for the complex-valued version, \(\int_{\mathsf U_\infty}\beta_c(ux)\,d\mu(u)=\operatorname{cov}_{\mathsf U}\) as a [[?c:Bochner integral|Bochner integral]] (the integrand is finite almost everywhere since its integral is finite).

## References

1. Lean: `New.Filling.lintegral_classCutoff_mul_prod` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
2. Lean: `New.Filling.measurePreserving_pi_orbitMeasure` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
3. Lean: `New.Filling.integral_classCutoff_eq_unipotentCovolume` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
