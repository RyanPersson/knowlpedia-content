+++
id = "proofs/grh/spanning-unfolding-b/term-discriminant-norm-and-pair-count-scale"
title = "Norm of the discriminant of a term and the pair count scale"
kind = "notation"
summary = "The product over the infinite places of the absolute values of the discriminant of a term, and the number against which pairs of terms are counted."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.termDiscNorm", "New.Filling.pairCountScale", "New.Filling.pairCountScale_pos"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) with \(f\) infinite places.

* For \(\gamma\in G(E)\) with [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|discriminant]] \(\operatorname{disc}(\gamma)\in E\), the **discriminant norm** is
\[
\mathcal{N}(\gamma)=\prod_v\bigl\lvert\Phi_v(\operatorname{disc}(\gamma))\bigr\rvert .
\]
* The **pair count scale** is
\[
n_p=\frac{\lvert\bar R_0\rvert\cdot\lvert\mathcal{C}\rvert}{N^{kf}},
\]
with \(\bar R_0\) the [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|reduced image]] of the Bessel subgroup and \(\mathcal{C}\) the set of classes. It is positive.

## References

1. Lean: `New.Filling.termDiscNorm`, `New.Filling.pairCountScale`, `New.Filling.pairCountScale_pos` in `src/New/Spanning/Unfolding/Terms.lean`.
