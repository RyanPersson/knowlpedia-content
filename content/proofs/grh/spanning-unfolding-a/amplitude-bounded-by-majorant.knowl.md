+++
id = "proofs/grh/spanning-unfolding-a/amplitude-bounded-by-majorant"
title = "The Bessel kernel is continuous and the amplitude is bounded by its majorant"
kind = "lemma"
summary = "The kernel W(y) tensor W(gamma^-1 y)* is continuous, its norm is the product of the local norms, and the norm of an amplitude is at most the integral of the norm of its integrand."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.enorm_amplitude_le", "New.Filling.enorm_besselKernel", "New.Filling.continuous_besselKernel", "New.Filling.continuous_besselFn"]
lean_files = ["src/New/Spanning/Unfolding/CutoffIntegral.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a [[?c:CM field|CM field]], \(S\) [[?lean:New.Filling|filling data]] over \(E\), \(\gamma\) a rational [[?c:Isometry of a hermitian space|isometry]] of \(V\), and fix a side (full or cut). For \(y\in G_\infty=\prod_vG_1\) let \(W(y)=\bigotimes_vW_v(y_v)\) be the product of the local Bessel functions of that side, with coordinates \(W_i(y)=\prod_vW_{v,i_v}(y_v)\) indexed by tuples \(i=(i_v)_v\) ([[?lean:New.Filling.besselFn|Bessel function at the infinite places]]), and let
\[
\mathcal K_\gamma(y)=W(y)\otimes W(\gamma^{-1}y)^{*},\qquad \mathcal K_\gamma(y)_{(i,j)}=W_i(y)\,\overline{W_j(\gamma^{-1}y)},
\]
be the [[?lean:New.Filling.besselKernel|Bessel kernel]], a vector of the Euclidean space \(\mathbb C^{I\times I}\). Then:

1. \(y\mapsto W_i(y)\) and \(y\mapsto\mathcal K_\gamma(y)\) are continuous on \(G_\infty\).
2. \(\lVert\mathcal K_\gamma(y)\rVert=\prod_v\lVert W_v(y_v)\rVert\cdot\prod_v\lVert W_v((\gamma^{-1}y)_v)\rVert\) (Euclidean norms).
3. For classes \(c,c'\), the [[?lean:New.Filling.amplitude|amplitude]] \(\mathcal A(c,c';\gamma)=\int_{G_\infty}\beta_c(y)\beta_{c'}(\gamma^{-1}y)\,\mathcal K_\gamma(y)\,dy\) satisfies
\[
\lVert\mathcal A(c,c';\gamma)\rVert\le\int_{G_\infty}\beta_c(y)\beta_{c'}(\gamma^{-1}y)\,\lVert\mathcal K_\gamma(y)\rVert\,dy ,
\]
the right side being the [[?lean:New.Filling.amplitudeMajorant|amplitude majorant]] (a value in \([0,\infty]\)). Here \(\beta_c\) is the [[?lean:New.Filling.classCutoff|class cutoff]]; in the amplitude the product of cutoffs enters through its real value, with \(\infty\) read as \(0\), and the integral is the [[?c:Bochner integral|Bochner integral]], which is \(0\) when the integrand is not integrable.

## Proof

1. The local Bessel functions are continuous (part of the definition of a [[?lean:New.BesselSystem|Bessel system]]), and left translation by \(\gamma^{-1}\), finite products and complex conjugation are continuous.

2. The squared norm of \(\mathcal K_\gamma(y)\) is \(\sum_{i,j}\lvert W_i(y)\rvert^2\lvert W_j(\gamma^{-1}y)\rvert^2=\bigl(\sum_i\prod_v\lvert W_{v,i_v}(y_v)\rvert^2\bigr)\bigl(\sum_j\prod_v\lvert W_{v,j_v}((\gamma^{-1}y)_v)\rvert^2\bigr)\), and a sum over tuples of a product over places is the product over places of the sums.

3. The norm of a Bochner integral is at most the integral of the norm, and the real value of an extended nonnegative number is at most that number.

## References

1. Lean: `New.Filling.enorm_amplitude_le` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
2. Lean: `New.Filling.enorm_besselKernel` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
3. Lean: `New.Filling.continuous_besselKernel` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
4. Lean: `New.Filling.continuous_besselFn` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
