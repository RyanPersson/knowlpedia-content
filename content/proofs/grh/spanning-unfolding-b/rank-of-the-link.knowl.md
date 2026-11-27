+++
id = "proofs/grh/spanning-unfolding-b/rank-of-the-link"
title = "The link has rank k + 1"
kind = "lemma"
summary = "The link of a rational isometry has dimension k + 1; source and target preserve the positive form on it and are bijections from the link onto the positive space."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.finrank_link", "New.Filling.form_linkSource_eq_form_linkTarget", "New.Filling.eq_zero_of_linkSource_or_linkTarget_eq_zero", "New.Filling.bijective_domRestrict_link", "New.Filling.finrank_link_add_finrank_commonIsotropic", "New.Filling.rank_add_finrank_isotropicPerp", "New.Filling.rank_isotropicFramePair_add_finrank_commonIsotropic", "New.Filling.colSpan_isotropicFramePair", "New.Filling.finrank_isotropicSpan_coe", "New.Filling.mem_commonIsotropic", "New.Filling.mem_isotropicSpan_coe", "New.Filling.isotropicSpan_eq_map", "New.Filling.mem_isotropicSpan_one", "New.Filling.ratGram_form_of_eStar_eq_zero", "New.rank_conjTranspose_eq", "New.colSpan_fromCols"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma\in G(E)\), \(L_\gamma\) the [[?lean:New.link|link]] of \(\gamma\), and \(\operatorname{src},\operatorname{tgt}\colon L_\gamma\to P\) the [[proofs/grh/spanning-unfolding-b/positive-space-and-link-maps|source and target maps to the positive space]].

1. For \(p,q\in L_\gamma\): \(h^+(\operatorname{src}p,\operatorname{src}q)=h^+(\operatorname{tgt}p,\operatorname{tgt}q)\).
2. If \(p\in L_\gamma\) and \(\operatorname{src}p=0\) or \(\operatorname{tgt}p=0\), then \(p=0\).
3. \(\dim_EL_\gamma=k+1\).
4. Every linear map from pairs of middle vectors to middle vectors that is injective on \(L_\gamma\) restricts to a bijection \(L_\gamma\to E^{\kappa\sqcup\{z\}}\). In particular \(\operatorname{src}\) and \(\operatorname{tgt}\) are bijections \(L_\gamma\to P\).

## Proof

(1) Let \(p,q\) come from \(y,y'\in(A+\gamma A)^\perp\). The vectors \(y,y',\gamma^{-1}y,\gamma^{-1}y'\) have vanishing \(e^*\)-blocks ([[proofs/grh/spanning-unfolding-b/link-in-coordinates|the link in coordinates]]), so their products for \(h\) are the products of their middle blocks for the middle form: \(h(y,y')=\langle y_{X_0},y'_{X_0}\rangle-N\bar y_zy'_z\), and likewise for \(\gamma^{-1}y,\gamma^{-1}y'\). Since \(\gamma\) is an isometry, \(h(\gamma^{-1}y,\gamma^{-1}y')=h(y,y')\), that is
\[
\langle(\gamma^{-1}y)_{X_0},(\gamma^{-1}y')_{X_0}\rangle-N\overline{(\gamma^{-1}y)_z}(\gamma^{-1}y')_z=\langle y_{X_0},y'_{X_0}\rangle-N\bar y_zy'_z .
\]
Moving the two \(z\)-terms to the opposite sides gives \(h^+(\operatorname{tgt}p,\operatorname{tgt}q)=h^+(\operatorname{src}p,\operatorname{src}q)\).

(2) By (1) with \(q=p\), \(\operatorname{src}p\) and \(\operatorname{tgt}p\) have the same \(h^+\)-norm; \(h^+\) is anisotropic, so both vanish if one does, and then \(p=0\).

(3) \(A\) and \(\gamma A\) have dimension \(\varrho\) (the first \(\varrho\) columns of \(\gamma\) are independent, having the first \(\varrho\) rows of \(\gamma^{-1}\) as a left inverse), so \(\dim(A+\gamma A)+\dim I_\gamma=2\varrho\). Since the form is nondegenerate, \(\dim(A+\gamma A)+\dim(A+\gamma A)^\perp=r\) (the matrix whose kernel is \((A+\gamma A)^\perp\) has the rank of \(A+\gamma A\), as conjugate transposition and multiplication by an invertible matrix preserve rank). The map \(y\mapsto(y_{\mathrm{mid}},(\gamma^{-1}y)_{\mathrm{mid}})\) from \((A+\gamma A)^\perp\) onto \(L_\gamma\) has kernel the \(y\) with \(y\in A\) and \(\gamma^{-1}y\in A\), i.e. \(I_\gamma\); so \(\dim L_\gamma+\dim I_\gamma=\dim(A+\gamma A)^\perp\). Combining, \(\dim L_\gamma=r-2\varrho=k+1\).

(4) An injective linear map between spaces of the same finite dimension \(k+1\) is bijective; (2) gives injectivity of \(\operatorname{src}\) and \(\operatorname{tgt}\).

## References

1. Lean: `New.Filling.finrank_link`, `New.Filling.form_linkSource_eq_form_linkTarget`, `New.Filling.eq_zero_of_linkSource_or_linkTarget_eq_zero`, `New.Filling.bijective_domRestrict_link` in `src/New/Spanning/Unfolding/Link.lean`.
