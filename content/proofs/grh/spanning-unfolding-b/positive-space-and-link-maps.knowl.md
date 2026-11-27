+++
id = "proofs/grh/spanning-unfolding-b/positive-space-and-link-maps"
title = "The positive space and the source and target maps of a link"
kind = "definition"
summary = "The positive definite companion of the middle space, the two maps from pairs of middle vectors that exchange the z-coordinates, and the isotropic spaces attached to an isometry."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.positiveGram", "New.Filling.linkSource", "New.Filling.linkTarget", "New.Filling.isotropicSpan", "New.Filling.commonIsotropic", "New.Filling.isotropicPerp", "New.Filling.eq_of_linkSource_eq_of_linkTarget_eq", "New.Filling.dotProduct_positiveGram_mulVec_eq_sum_add", "New.Filling.dotProduct_ratMiddle_mulVec_eq_sum_sub", "New.Filling.eq_zero_of_positiveGram_form_eq_zero", "New.Filling.mem_isotropicPerp", "New.Filling.link_eq_map", "New.Filling.mem_link_iff_exists_mem_isotropicPerp", "New.Filling.linkMatrix_mulVec_mem_link", "New.Filling.linkSource_linkMatrix_mulVec", "New.Filling.linkTarget_linkMatrix_mulVec"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\). The middle space is \(X_0\perp Ez_N\), with coordinates indexed by \(\kappa\sqcup\{z\}\), orthonormal on \(X_0\) and \(h(z_N,z_N)=-N\).

* The **positive space** is \(P=X_0\perp Ez^+\), the same coordinate space with the form \(h^+\) that is orthonormal on \(X_0\) and has \(h^+(z^+,z^+)=N\):
\[
h^+(a,b)=\sum_{i\in\kappa}\bar a_ib_i+N\,\bar a_zb_z .
\]
* For a pair \(p=(p_1,p_2)\) of middle vectors, \(p_1=y_0+\lambda'z_N\), \(p_2=y_0'+\lambda z_N\) with \(y_0,y_0'\in X_0\), the **source** and **target** are
\[
\operatorname{src}(p)=y_0+\lambda z^+,\qquad \operatorname{tgt}(p)=y_0'+\lambda'z^+ .
\]
Both are linear maps to \(P\), and \(p\) is determined by \((\operatorname{src}(p),\operatorname{tgt}(p))\).
* For \(\gamma\in G(E)\) and \(A=\langle e_0,\dots,e_{\varrho-1}\rangle\): the **common isotropic space** is \(I_\gamma=A\cap\gamma A\), and the **isotropic complement** is \((A+\gamma A)^\perp\), the orthogonal complement for the form of \(V\).

## Properties

The form \(h^+\) is anisotropic: at an infinite place \(v\), \(\Phi_v(h^+(a,a))=\sum_i\lvert\Phi_v(a_i)\rvert^2+N\lvert\Phi_v(a_z)\rvert^2\), which vanishes only for \(a=0\). For \(y\in(A+\gamma A)^\perp\), the pair \(p=(y_{\mathrm{mid}},(\gamma^{-1}y)_{\mathrm{mid}})\) of the [[?lean:New.link|link]] has \(\operatorname{src}(p)=y_{X_0}+(\gamma^{-1}y)_z\,z^+\) and \(\operatorname{tgt}(p)=(\gamma^{-1}y)_{X_0}+y_z\,z^+\).

## References

1. Lean: `New.Filling.positiveGram`, `New.Filling.linkSource`, `New.Filling.linkTarget`, `New.Filling.commonIsotropic`, `New.Filling.isotropicPerp` in `src/New/Spanning/Unfolding/Link.lean`.
