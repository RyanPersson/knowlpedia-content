+++
id = "proofs/grh/spanning-unfolding-b/class-coordinates"
title = "Coordinates of the lattice of a class"
kind = "definition"
summary = "The matrices that take rational coordinates to coordinates in the basis of the lattice of a class, on the whole space and on X0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.classCoord", "New.Filling.classCoordX₀", "New.Filling.ratGram", "New.Filling.classCoord_conj_splitGram"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] and \(c\) a class with [[proofs/grh/spanning-unfolding-b/class-basis|class basis]] \(B_c\) and representative \(g_c\in U(X_0)(\mathbb{A}_f)\).

* The **class coordinates** of \(c\) are the matrix \(C_c=B_c^{-1}\) over \(\mathbb{A}_f\); it takes rational coordinates to coordinates in the basis of the lattice \(\tilde g_c\Lambda_0\).
* The **class coordinates on \(X_0\)** are the \((\kappa\sqcup\{z\})\times\kappa\) matrix \(C_c^{X_0}=I_\pi\,g_c^{-1}\), where \(I_\pi\) is the [[?lean:New.middleInclusionMatrix|middle inclusion matrix]], whose columns are the standard basis vectors \(x_i\) of \(X_0\) written in the lattice basis of the middle space.

Both depend on the choice of the representative \(g_c\).

## Properties

Let \(J\) be the Gram matrix in the standard basis and \(J^{\mathrm{lat}}\) the one in the lattice basis, over \(\mathbb{A}_f\). Then \(C_c^{*}J^{\mathrm{lat}}C_c=J\). Indeed \(B_c=\tilde g_cB\) with \(\tilde g_c\) an isometry of \(J\) and \(B^*JB=J^{\mathrm{lat}}\) ([[?lean:New.gram_besselLatticeBasis|Gram matrix of the lattice basis]]), so \(B_c^*JB_c=J^{\mathrm{lat}}\); now multiply by \(C_c^*\) on the left and \(C_c\) on the right.

## References

1. Lean: `New.Filling.classCoord`, `New.Filling.classCoordX₀`, `New.Filling.classCoord_conj_splitGram` in `src/New/Spanning/Unfolding/Terms.lean`.
