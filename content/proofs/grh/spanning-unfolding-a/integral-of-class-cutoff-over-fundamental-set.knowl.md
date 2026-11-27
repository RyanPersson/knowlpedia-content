+++
id = "proofs/grh/spanning-unfolding-a/integral-of-class-cutoff-over-fundamental-set"
title = "The integral of a class cutoff is the measure of a set of coset representatives"
kind = "lemma"
summary = "If a measurable set B meets each coset u Gamma of the arithmetic unipotent group exactly once, the integral of the class cutoff over the real unipotent group is the Haar measure of B."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.lintegral_classCutoff_eq_measure"]
lean_files = ["src/New/Spanning/Unfolding/CutoffIntegral.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], \(c\) a class, \(y\in G_\infty\), and \(\Gamma_c\subseteq\mathsf U_\infty\) the image of \(\mathsf U_c(M)\) in the [[proofs/grh/spanning-unfolding-a/row-coordinates-of-real-unipotent-group|real unipotent group]]. Let \(\mu\) be the product over the [[?c:Infinite place of a number field|infinite places]] of the [[harmonic-analysis/haar-measure|Haar measures]] [[?lean:New.Shape.besselHaar|\(\mu_{\mathsf U}\)]], and let \(B\subseteq\mathsf U_\infty\) be a measurable set such that for every \(u\in\mathsf U_\infty\) there is exactly one \(\gamma\in\Gamma_c\) with \(u\gamma\in B\). Then
\[
\int_{\mathsf U_\infty}\beta_c(u\,y)\,d\mu(u)=\mu(B),
\]
where \(\beta_c\) is the [[?lean:New.Filling.classCutoff|class cutoff]].

## Proof

The hypothesis on \(B\), applied to \(u^{-1}\), says that for every \(u\) exactly one \(\gamma\in\Gamma_c\) has \(\gamma u\in B^{-1}\); so \(B^{-1}\) is a [[?c:Fundamental domain for a group action|fundamental domain]] for the left translation action of the countable group \(\Gamma_c\), which preserves \(\mu\). Hence for the measurable function \(\phi(u)=\beta_c(uy)\ge0\),
\[
\int_{\mathsf U_\infty}\phi\,d\mu=\int_{B^{-1}}\sum_{\gamma\in\Gamma_c}\phi(\gamma u)\,d\mu(u).
\]
By the proposition on [[proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one|class cutoffs]] (item 2, applied to the point \(uy\)), the inner sum is \(1\). So the integral equals \(\mu(B^{-1})=\mu(B)\), as \(\mu\) is invariant under inversion (the group is unimodular).

## References

1. Lean: `New.Filling.lintegral_classCutoff_eq_measure` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
