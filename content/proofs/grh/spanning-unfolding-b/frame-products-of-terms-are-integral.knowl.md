+++
id = "proofs/grh/spanning-unfolding-b/frame-products-of-terms-are-integral"
title = "Frame products of terms are algebraic integers"
kind = "lemma"
summary = "The frame image and frame products of the translate of a rational isometry by class representatives are those of the isometry in class coordinates; for a term over a block the frame products are algebraic integers."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.isIntegral_frameProducts", "New.Filling.frameGram_translateByClassReps", "New.Filling.frameImage_translateByClassReps", "New.Filling.termsOver.isIntMatrix_translateByClassReps"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]], \(c,c'\) classes, \(\gamma\in G(E)\) and \(\tau=h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}\in G_{\mathrm{fin}}\).

1. The frame columns of \(\tau\) are \(C_c\) times the frame columns of \(\gamma\), where \(C_c\) are the [[proofs/grh/spanning-unfolding-b/class-coordinates|class coordinates]].
2. The frame products of \(\tau\) for the Gram matrix \(J^{\mathrm{lat}}\) in the lattice basis equal the [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|frame products]] \(Z(\gamma)\), read in \(\mathbb{A}_f\).
3. If \(S\) is [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] and \(\gamma\) is a term over some block \((c,s,c')\), then every entry of \(Z(\gamma)\) is an [[?c:Algebraic integer|algebraic integer]].

## Proof

(1) By [[proofs/grh/spanning-unfolding-b/class-basis|the class basis]], the matrix of \(\tau\) is \(B_c^{-1}\gamma B_{c'}=C_c\gamma B_{c'}\). The matrix \(B_{c'}=\tilde g_{c'}B\) fixes the frame vectors \(e_a\) and \(z\): \(\tilde g_{c'}\) acts only on \(X_0\), and \(B\) changes only the basis vector \(x_{k_0}\). So the frame columns of \(\tau\) are \(C_c\) times those of \(\gamma\).

(2) Let \(F\) be the matrix of frame columns of the identity. The class basis \(B_c\) fixes the frame vectors, so \(C_cF=F\) and therefore \(F^{\mathsf T}C_c^{*}=(C_cF)^{*}=F^{\mathsf T}\). Using \(J=C_c^{*}J^{\mathrm{lat}}C_c\) ([[proofs/grh/spanning-unfolding-b/class-coordinates|class coordinates]]) and (1),
\[
Z(\gamma)=F^{\mathsf T}J\gamma F=F^{\mathsf T}C_c^{*}J^{\mathrm{lat}}C_c\gamma F=F^{\mathsf T}J^{\mathrm{lat}}\,(\tau F),
\]
which is the matrix of frame products of \(\tau\) for \(J^{\mathrm{lat}}\).

(3) For a term, \(\tau\) has entries in \(\widehat{\mathcal{O}}\). The matrix \(J^{\mathrm{lat}}\) is integral ([[proofs/grh/spanning-unfolding-b/lattice-middle-form-is-unimodular|unimodularity]]), so the entries of \(J^{\mathrm{lat}}\tau\), in particular the frame products of \(\tau\), lie in \(\widehat{\mathcal{O}}\). By (2) the entries of \(Z(\gamma)\in E\) are integral at every finite place, hence algebraic integers.

## References

1. Lean: `New.Filling.isIntegral_frameProducts`, `New.Filling.frameGram_translateByClassReps`, `New.Filling.frameImage_translateByClassReps` in `src/New/Spanning/Unfolding/Terms.lean`.
