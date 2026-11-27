+++
id = "proofs/grh/spanning-unfolding-b/terms-with-the-same-frame-image"
title = "Terms with the same image of the frame"
kind = "lemma"
summary = "For an admissible filling datum, two terms from the same class with the same image of the frame have residues in one coset of the reduced Bessel group, and if the residues are equal they differ by an integral unipotent element fixing the frame."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.termsOver.inv_mul_mem_reducedImage", "New.Filling.termsOver.eq_and_mem_classUnipotent₀", "New.Filling.mem_besselS_of_frameImage_eq_one"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]]. Let \(\gamma\) be a [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|term over]] \((c,r,c')\) and \(u\) a term over \((c,r',d)\) such that \(\gamma f_a=uf_a\) for every frame vector \(f_a\).

1. \(r^{-1}r'\) lies in the reduced image \(\bar R_0\) of the Bessel subgroup.
2. If \(r=r'\), then \(c'=d\) and \(\gamma^{-1}u\in\mathsf{U}^0_{c'}(M)\).

## Proof

An isometry that fixes every frame vector lies in the Bessel subgroup \(\mathsf{S}\) ([[?lean:New.Filling.mem_besselS_iff_frameImage|characterisation of \(\mathsf{S}\) by the frame columns]]); and \(s^{-1}s'\) fixes the frame if and only if \(s\) and \(s'\) have the same frame columns.

(1) Let \(m=h_c^{-1}\gamma_{\mathrm{fin}}h_{c'}\) and \(m'=h_c^{-1}u_{\mathrm{fin}}h_d\), elements of \(K\) with reductions \(r,r'\). By [[proofs/grh/spanning-unfolding-b/frame-products-of-terms-are-integral|the frame image in class coordinates]], the frame columns of \(m\) and \(m'\) are \(C_c\) times those of \(\gamma\) and \(u\), hence equal. So \(m^{-1}m'\in K\cap\mathsf{S}\), and its reduction \(r^{-1}r'\) lies in \(\bar R_0\).

(2) By [[proofs/grh/spanning-unfolding-b/terms-compose-like-a-groupoid|the groupoid law]], \(\gamma^{-1}u\) is a term over \((c',1,d)\), so \(h_{c'}^{-1}(\gamma^{-1}u)_{\mathrm{fin}}h_d\in K(M)\); and \(\gamma^{-1}u\) fixes the frame, so it lies in \(\mathsf{S}(E)\). By [[proofs/grh/spanning-unfolding-b/bessel-subgroup-terms-in-principal-level|the lemma on the Bessel subgroup and the principal level]], \(c'=d\) and \(\gamma^{-1}u\in\mathsf{U}_{c'}(M)\). Since it also fixes each frame vector, it lies in \(\mathsf{U}^0_{c'}(M)\).

## References

1. Lean: `New.Filling.termsOver.inv_mul_mem_reducedImage`, `New.Filling.termsOver.eq_and_mem_classUnipotent₀` in `src/New/Spanning/Unfolding/Terms.lean`.
