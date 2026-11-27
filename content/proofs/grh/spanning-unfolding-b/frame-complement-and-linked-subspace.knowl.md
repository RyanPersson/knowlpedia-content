+++
id = "proofs/grh/spanning-unfolding-b/frame-complement-and-linked-subspace"
title = "The frame complement modulo the common isotropic space is the linked subspace"
kind = "theorem"
summary = "Taking X0-parts maps the orthogonal complement of the two frames onto the linked subspace of X0, isometrically, with kernel the common isotropic space; this space is the radical of the frame sum."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.range_framePerpToX₀", "New.Filling.form_framePerpToX₀", "New.Filling.ker_framePerpToX₀", "New.Filling.frameSum_inf_framePerp", "New.Filling.framePerpToX₀", "New.Filling.framePerpToX₀_apply", "New.Filling.linkIsometry_comp_indexX₀", "New.Filling.exists_mem_isotropicPerp_comp_eq", "New.Filling.commonIsotropic_le_framePerp", "New.Filling.form_self_eq_zero_iff_mem_commonIsotropic", "New.Filling.finrank_linkedX₀_add_finrank_commonIsotropic", "New.Filling.finrank_frameSum_add_finrank_framePerp"]
lean_files = ["src/New/Spanning/Unfolding/TermStructure.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma\in G(E)\), and use the [[proofs/grh/spanning-unfolding-b/spaces-of-the-two-frames|spaces of the two frames]] \(A^+_\gamma\), \((A^+_\gamma)^\perp\), \(X_0^\gamma\) and \(I_\gamma=A\cap\gamma A\). Let \(\pi_\gamma\colon(A^+_\gamma)^\perp\to X_0\), \(y\mapsto y_0\), take the \(X_0\)-coordinates.

1. For \(y\in(A^+_\gamma)^\perp\): \(\Upsilon_\gamma(y_0)=(\gamma^{-1}y)_0\). The image of \(\pi_\gamma\) is \(X_0^\gamma\).
2. \(\langle\pi_\gamma y,\pi_\gamma y'\rangle=h(y,y')\) for \(y,y'\in(A^+_\gamma)^\perp\), with \(\langle\,,\rangle\) the standard hermitian product of \(X_0\).
3. \(I_\gamma\subset(A^+_\gamma)^\perp\) and \(\ker\pi_\gamma=I_\gamma\). Hence \(\dim X_0^\gamma+\dim I_\gamma=\dim(A^+_\gamma)^\perp\), and \(\dim A^+_\gamma+\dim(A^+_\gamma)^\perp=r\).
4. \(A^+_\gamma\cap(A^+_\gamma)^\perp=I_\gamma\): the common isotropic space is the radical of the frame sum.

## Proof

(1) Let \(y\in(A^+_\gamma)^\perp\). Its pair in the link has source \(y_0+(\gamma^{-1}y)_zz^+=y_0\) and target \((\gamma^{-1}y)_0+y_zz^+=(\gamma^{-1}y)_0\), since both \(z\)-coordinates vanish; so \(\Upsilon_\gamma(y_0)=(\gamma^{-1}y)_0\in X_0\) and \(y_0\in X_0^\gamma\). Conversely let \(v\in X_0^\gamma\). By [[proofs/grh/spanning-unfolding-b/isotropic-complement-maps-onto-positive-space|surjectivity of \(\Pi_\gamma\)]] there is \(y\in(A+\gamma A)^\perp\) with \(y_0=v\) and \((\gamma^{-1}y)_z=0\); then \(\Upsilon_\gamma(v)\) is the target of its pair, whose \(z^+\)-coordinate is \(y_z\). As \(v\in X_0^\gamma\), \(y_z=0\), so \(y\in(A^+_\gamma)^\perp\) and \(\pi_\gamma y=v\).

(2) \(y,y'\) have vanishing \(e^*\)-coordinates, so \(h(y,y')=\langle y_0,y_0'\rangle-N\bar y_zy'_z\), and \(y_z=0\).

(3) If \(y\in I_\gamma\), then \(y\) and \(\gamma^{-1}y\) lie in \(A\), so \(y\in(A+\gamma A)^\perp\) with all middle coordinates of \(y\) and \(\gamma^{-1}y\) zero; thus \(y\in(A^+_\gamma)^\perp\). For \(y\in(A^+_\gamma)^\perp\), \(\Pi_\gamma(y)=y_0+0\cdot z^+\), so \(\pi_\gamma y=0\) if and only if \(\Pi_\gamma y=0\), if and only if \(y\in I_\gamma\). The first dimension formula is rank–nullity for \(\pi_\gamma\) with (1). The second holds because \(h\) is nondegenerate: \((A^+_\gamma)^\perp\) is the kernel of the matrix \(P^*J\), where the columns of \(P\) span \(A^+_\gamma\), and \(P^*J\) has the rank of \(P\).

(4) By (3), \(I_\gamma\subset(A^+_\gamma)^\perp\), and \(I_\gamma\subset A\subset A^+_\gamma\). Conversely, if \(y\in A^+_\gamma\cap(A^+_\gamma)^\perp\), then \(h(y,y)=0\); by (2), \(\langle y_0,y_0\rangle=0\), and the form of \(X_0\) is anisotropic, so \(\pi_\gamma y=0\) and \(y\in I_\gamma\) by (3).

## References

1. Lean: `New.Filling.range_framePerpToX₀`, `New.Filling.form_framePerpToX₀`, `New.Filling.ker_framePerpToX₀`, `New.Filling.frameSum_inf_framePerp` in `src/New/Spanning/Unfolding/TermStructure.lean`.
