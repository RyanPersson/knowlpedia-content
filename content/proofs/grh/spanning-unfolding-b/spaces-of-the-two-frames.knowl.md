+++
id = "proofs/grh/spanning-unfolding-b/spaces-of-the-two-frames"
title = "Spaces attached to the two frames of a term"
kind = "definition"
summary = "The sum of the spans of the frame and of its image, its orthogonal complement, the flags of the two frames, and the subspace of X0 that the link isometry maps into X0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.frameSum", "New.Filling.framePerp", "New.Filling.inclPositive", "New.Filling.linkedX₀", "New.Filling.flagSpan", "New.Filling.mem_linkedX₀", "New.Filling.mem_range_inclPositive", "New.Filling.mem_framePerp", "New.Filling.mem_framePerp_iff_orthogonal", "New.Filling.colSpan_framePair", "New.Filling.mem_flagSpan", "New.Filling.mem_isotropicSpan", "New.Filling.mem_commonIsotropic_iff", "New.Filling.commonIsotropic_le_isotropicSpan_one", "New.Filling.commonIsotropic_le_isotropicSpan_coe", "New.Filling.orthogonal_frame_iff", "New.Filling.form_frameImage_one", "New.Filling.form_frameImage_coe", "New.Filling.flagSpan_zero", "New.Filling.finrank_flagSpan_coe", "New.mem_colSpan_submatrix", "New.Filling.isotropicSpan_le_colSpan_frameImage", "New.Filling.commonIsotropic_le_colSpan_frameImage_one", "New.Filling.commonIsotropic_le_colSpan_frameImage_coe", "New.Filling.finrank_colSpan_frameImage"]
lean_files = ["src/New/Spanning/Unfolding/TermStructure.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma\in G(E)\), \(f=(f_0,\dots,f_\varrho)=(e_0,\dots,e_{\varrho-1},z_N)\) the frame, \(A=\langle e_0,\dots,e_{\varrho-1}\rangle\) and \(A^+=A+Ez_N\) the span of the frame. Let \(\Upsilon_\gamma\) be the [[proofs/grh/spanning-unfolding-b/link-isometry|link isometry]] of the positive space \(X_0\perp Ez^+\).

* The **frame sum** is \(A^+_\gamma=A^++\gamma A^+\), and the **frame complement** is \((A^+_\gamma)^\perp\), the orthogonal complement for the form \(h\) of \(V\).
* For \(0\le j\le\varrho+1\) and an invertible matrix \(M\), the **flag** \(MA_{\le j}\) is the span of \(Mf_0,\dots,Mf_{j-1}\); it has dimension \(j\). The cases used are \(M=1\) and \(M=\gamma\).
* The **linked subspace** is
\[
X_0^\gamma=X_0\cap\Upsilon_\gamma^{-1}X_0=\{v\in X_0:\ \text{the }z^+\text{-coordinate of }\Upsilon_\gamma(v)\text{ is }0\}.
\]

## Properties

A vector \(y\) lies in \((A^+_\gamma)^\perp\) if and only if \(y\in(A+\gamma A)^\perp\) and the \(z_N\)-coordinates of \(y\) and of \(\gamma^{-1}y\) vanish: orthogonality to \(A^+\) means vanishing of the \(e^*\)-coordinates and of the \(z_N\)-coordinate (as \(h(z_N,z_N)=-N\ne0\)), and \(h(\gamma w,y)=h(w,\gamma^{-1}y)\). The space \(I_\gamma=A\cap\gamma A\) is contained in \(A^+\) and in \(\gamma A^+\).

## References

1. Lean: `New.Filling.frameSum`, `New.Filling.framePerp`, `New.Filling.linkedX₀`, `New.Filling.flagSpan`, `New.Filling.mem_framePerp` in `src/New/Spanning/Unfolding/TermStructure.lean`.
