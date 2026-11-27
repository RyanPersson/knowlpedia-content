+++
id = "proofs/grh/spanning-unfolding-b/terms-of-cell-rank-zero-are-scalar-multiples-of-the-bessel-subgroup"
title = "Terms with norm-one pairs from index zero are scalar multiples of the Bessel subgroup"
kind = "theorem"
summary = "A rational isometry lies in the Bessel subgroup exactly when the pair (1,1) occurs at every index; a term for which a norm-one pair occurs from index zero is an integral scalar of norm one times an element of the Bessel subgroup, and its residue lies in the corresponding scalar coset."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_scalar_mul_besselS", "New.mem_besselS_of_pairOccursAt", "New.PairOccursAt.apply_besselFrame_zero", "New.scalarIsometry_inv_mul_mem_besselS", "New.Filling.normOnePairOccursFrom_zero_of_mem_besselS", "New.Filling.translateByClassReps_mem_besselS", "New.Filling.apply_besselFrame_zero_mem_Ô", "New.Filling.val_reduction_of_eq_smul_one", "New.mulVec_apply_eq_of_eq_zero_of_lt"]
lean_files = ["src/New/Spanning/Unfolding/SquareExpansion.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma\in G(E)\), and \(\mathsf{S}\) the [[?lean:New.Shape.Form.besselS|Bessel subgroup]].

1. If the [[proofs/grh/spanning-unfolding-b/cell-rank-of-a-term|pair \((1,1)\) occurs]] at every index \(0\le a\le\varrho\) for \(\gamma\), then \(\gamma\in\mathsf{S}\). Conversely, if \(\gamma\in\mathsf{S}\), then a norm-one pair (with \(c=1\)) occurs from \(0\).
2. If \(\zeta\bar\zeta=1\) and the pair \((\zeta,1)\) occurs at every index for \(\gamma\), then \(\gamma_{f_0f_0}=\zeta\) and \(\zeta^{-1}\gamma\in\mathsf{S}\).
3. Let \(\gamma\) be a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|term over]] \((c,s,c')\) for which a norm-one pair occurs from \(0\). Then there is \(\zeta\in E\), integral at all finite places, with \(\zeta\bar\zeta=1\), such that \(\gamma=\zeta\gamma_0\) with \(\gamma_0\in\mathsf{S}(E)\), and \(s\) lies in the [[proofs/grh/spanning-unfolding-b/avoiding-scalar-cosets|scalar coset]] \(\zeta\bar R_0\).
4. If \(\gamma\in\mathsf{S}(E)\), then \(h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}\in\mathsf{S}\) for all classes \(c,c'\).

## Proof

Recall that \(\mathsf{S}\) is the set of isometries whose frame columns agree with those of the identity in all rows \(j\) with \(\operatorname{level}(j)\ge b\), for each frame index \(b\) ([[?lean:New.Filling.mem_besselS_iff_frameImage|characterisation by frame columns]]); the level of \(f_b\) is \(b\).

(1) By induction on \(b\) we show \((\gamma f_b)_j=(f_b)_j\) for all rows \(j\) of level \(\ge b\). Take \(x,y\) with \(f\cdot x=\gamma f\cdot y\), \(x_b=y_b=1\), vanishing above \(b\). In a row \(j\) of level \(\ge b\), the frame vectors \(f_a\), \(a<b\), have entry \(0\), and by induction so do the \(\gamma f_a\), \(a<b\). So row \(j\) of the relation reads \((f_b)_j=(\gamma f_b)_j\). Conversely, for \(\gamma\in\mathsf{S}\) and an index \(a\), the vector \(\gamma f_a\) agrees with \(f_a\) in all rows of level \(\ge a\); in particular it has no \(X_0\)-part, no \(e^*\)-part, and its coordinates at \(f_b\), \(b\ge a\), are \(\delta_{ab}\). So \(\gamma f_a=f\cdot x\) with \(x_a=1\), \(x_b=0\) for \(b>a\): the pair \((1,1)\) occurs at \(a\).

(2) Row \(f_0\) of the relation at index \(0\), \(x_0f_0=y_0\gamma f_0\) with \(x_0=\zeta\), \(y_0=1\), gives \(\gamma_{f_0f_0}=\zeta\). Multiplying each relation \(f\cdot x=\gamma f\cdot y\) by \(\bar\zeta\) gives \(f\cdot(\bar\zeta x)=(\zeta^{-1}\gamma)f\cdot y\) with leading coefficients \(\bar\zeta\zeta=1\) and \(1\); apply (1) to \(\zeta^{-1}\gamma=\bar\zeta\gamma\).

(4) Write \(\gamma=u\tilde\eta\) with \(u\in\mathsf{U}(E)\), \(\eta\in U(X_0)(E)\) ([[?lean:New.exists_besselU_mul_toBesselH|decomposition of the Bessel subgroup]]). Then \(h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}=h_c^{-1}\,u_{\mathrm{fin}}\,\iota_H(\eta)\,h_{c'}\), a product of elements of \(H\) and \(\mathsf{U}\), all in \(\mathsf{S}\) ([[proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis|Bessel groups in the lattice basis]]).

(3) Let \(k=h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}\in K\) with \(\bar k=s\), and \(\zeta\) as in the hypothesis. By (2), \(\zeta=\gamma_{f_0f_0}\). The frame columns of \(k\) are the [[proofs/grh/spanning-unfolding-b/class-coordinates|class coordinates]] \(C_c\) applied to those of \(\gamma\) ([[proofs/grh/spanning-unfolding-b/frame-products-of-terms-are-integral|frame image in class coordinates]]), and the row of \(C_c\) at \(e_0\) is that of the identity; so \(k_{f_0f_0}=\gamma_{f_0f_0}=\zeta\), which is therefore integral. Put \(\gamma_0=\zeta^{-1}\gamma\in\mathsf{S}(E)\) by (2). The scalar \(\zeta\) defines an element \(z\in K\) (its inverse \(\bar\zeta\) is integral too), and \(k_0=z^{-1}k=h_c^{-1}(\gamma_0)_{\mathrm{fin}}h_{c'}\), because scalars commute with all matrices. By (4), \(k_0\in K\cap\mathsf{S}\), so \(t=\bar k_0\in\bar R_0\). Finally \(s=\bar z\,\bar k_0\), and the reduction of the scalar matrix \(z\) at a chosen place \(w\) is the scalar \(\zeta\bmod w\); so \(s_w=(\zeta\bmod w)\,t_w\).

## References

1. Lean: `New.Filling.exists_scalar_mul_besselS`, `New.mem_besselS_of_pairOccursAt`, `New.scalarIsometry_inv_mul_mem_besselS`, `New.Filling.normOnePairOccursFrom_zero_of_mem_besselS` in `src/New/Spanning/Unfolding/SquareExpansion.lean`.
