+++
id = "proofs/grh/spanning-unfolding-a/integral-of-class-cutoff-is-unipotent-covolume"
title = "The integral of a class cutoff over the real unipotent group"
kind = "theorem"
summary = "For every class c and point y, the integral of u -> beta_c(u y) over the real unipotent group is the unipotent covolume."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.lintegral_classCutoff_eq_unipotentCovolume"]
lean_files = ["src/New/Spanning/Unfolding/CutoffIntegral.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, and \(S\) [[?lean:New.Filling|filling data]] over \(E\) satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]]. For every [[?lean:New.Filling.Classes|class]] \(c\) and every \(y\in G_\infty\),
\[
\int_{\mathsf U_\infty}\beta_c(u\,y)\,d\mu(u)=\operatorname{cov}_{\mathsf U},
\]
where \(\beta_c\) is the [[?lean:New.Filling.classCutoff|class cutoff]], \(\mathsf U_\infty=\prod_v\mathsf U\) is the real unipotent group with the product \(\mu\) of the [[harmonic-analysis/haar-measure|Haar measures]] [[?lean:New.Shape.besselHaar|\(\mu_{\mathsf U}\)]], and \(\operatorname{cov}_{\mathsf U}\) is the [[?lean:New.Filling.unipotentCovolume|unipotent covolume]], a positive real number depending neither on \(c\) nor on \(y\). In other words, \(\operatorname{cov}_{\mathsf U}\) is the covolume of the arithmetic group \(\mathsf U_c(M)\) in \(\mathsf U_\infty\).

## Proof

Let \(F_a,F'_a\) be the sets of the proposition on the [[proofs/grh/spanning-unfolding-a/fundamental-box-for-arithmetic-unipotent-group|fundamental box]], and let \(B\subseteq\mathsf U_\infty\) be the preimage of the box \(\prod_aF_a\times\prod_aF'_a\) under the [[proofs/grh/spanning-unfolding-a/row-coordinates-of-real-unipotent-group|row coordinates]]. It is measurable, and each coset \(u\Gamma_c\) meets it exactly once. By the lemma on [[proofs/grh/spanning-unfolding-a/integral-of-class-cutoff-over-fundamental-set|integration over a set of representatives]], the integral equals \(\mu(B)\). Since the row coordinates carry \(\mu\) to [[?c:Lebesgue measure|Lebesgue measure]], \(\mu(B)\) is the Lebesgue volume of the box, which is the product of the volumes of the \(F_a\) and \(F'_a\), namely \(\operatorname{cov}_{\mathsf U}\). (The product of the real volumes is the positive number \(\operatorname{cov}_{\mathsf U}\), so none of the volumes is infinite.)

## Remarks

The source describes this as a case of the covolume computation for Heisenberg radicals, with a fixed product Haar measure in place of Tate's self-dual measures.

## References

1. Lean: `New.Filling.lintegral_classCutoff_eq_unipotentCovolume` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
