+++
id = "proofs/grh/spanning-unfolding-b/common-link-by-link-isometries"
title = "The common link in terms of link isometries"
kind = "theorem"
summary = "A vector of X0 is in the common link of two rational isometries exactly when it is in the linked subspace of the first and the two link isometries agree on it; a rank inequality follows."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.mem_commonLink", "New.Filling.commonLink_self", "New.Filling.commonLink_le_linkedX₀_inf", "New.Filling.finrank_commonLink", "New.Filling.finrank_linkedX₀_add_finrank_inf_le", "New.Filling.mem_ker_zRowBlockDiagonal"]
lean_files = ["src/New/Spanning/Unfolding/TermStructure.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma,\gamma'\in G(E)\) with links \(L_\gamma,L_{\gamma'}\), [[proofs/grh/spanning-unfolding-b/link-isometry|link isometries]] \(\Upsilon_\gamma,\Upsilon_{\gamma'}\), [[proofs/grh/spanning-unfolding-b/spaces-of-the-two-frames|linked subspaces]] and [[proofs/grh/spanning-unfolding-b/common-link|common link]] \(C(\gamma,\gamma')\subset X_0\).

1. For \(v\in X_0\): \(v\in C(\gamma,\gamma')\) if and only if \(v\in X_0^\gamma\) and \(\Upsilon_\gamma(v)=\Upsilon_{\gamma'}(v)\).
2. \(C(\gamma,\gamma)=X_0^\gamma\), and \(C(\gamma,\gamma')\subset X_0^\gamma\cap X_0^{\gamma'}\).
3. \(\dim C(\gamma,\gamma')=\dim(L_\gamma\cap L_{\gamma'}\cap K)\), where \(K\) is the space of pairs both of whose members have \(z_N\)-coordinate \(0\).
4. \(\dim X_0^\gamma+\dim(L_\gamma\cap L_{\gamma'})\le\dim C(\gamma,\gamma')+(k+1)\).

## Proof

Since the middle form is \(\operatorname{diag}(1,\dots,1,-N)\) with \(N\ne0\), a middle vector is orthogonal to \(z_N\) exactly when its \(z_N\)-coordinate is \(0\); so \(C(\gamma,\gamma')\) is the set of \(X_0\)-parts of first members of pairs in \(L_\gamma\cap L_{\gamma'}\cap K\).

(1) Let \(p=(y_0+\lambda'z_N,y_0'+\lambda z_N)\in L_\gamma\cap L_{\gamma'}\cap K\), so \(\lambda=\lambda'=0\) and \(v=y_0\). Then \(\operatorname{src}p=v\) and \(\Upsilon_\gamma(v)=\operatorname{tgt}p=y_0'=\Upsilon_{\gamma'}(v)\), which lies in \(X_0\). Conversely, let \(v\in X_0^\gamma\) with \(\Upsilon_\gamma v=\Upsilon_{\gamma'}v\). Choose \(p\in L_\gamma\) with \(\operatorname{src}p=v\); then \(\operatorname{tgt}p=\Upsilon_\gamma v=\Upsilon_{\gamma'}(\operatorname{src}p)\), so \(p\in L_{\gamma'}\) because [[proofs/grh/spanning-unfolding-b/link-is-graph-of-link-isometry|the link is the graph of the link isometry]]. The \(z^+\)-coordinate of \(\operatorname{src}p=v\) is \(\lambda=0\), and that of \(\operatorname{tgt}p=\Upsilon_\gamma v\) is \(\lambda'=0\) as \(v\in X_0^\gamma\). So \(p\in K\) and \(v\in C(\gamma,\gamma')\).

(2) follows from (1) (for the second claim, \(\Upsilon_{\gamma'}v=\Upsilon_\gamma v\in X_0\)).

(3) The map \(p\mapsto y_0\) from \(L_\gamma\cap L_{\gamma'}\cap K\) onto \(C(\gamma,\gamma')\) is injective: if \(y_0=0\) and \(\lambda=0\) then \(\operatorname{src}p=0\), hence \(p=0\) by [[proofs/grh/spanning-unfolding-b/rank-of-the-link|the lemma on the link]].

(4) By (2) and (3), \(\dim X_0^\gamma=\dim(L_\gamma\cap K)\) and \(\dim C(\gamma,\gamma')=\dim(L_\gamma\cap L_{\gamma'}\cap K)\). The subspaces \(L_\gamma\cap K\) and \(L_\gamma\cap L_{\gamma'}\) of \(L_\gamma\) have sum of dimension at most \(\dim L_\gamma=k+1\) and intersection \(L_\gamma\cap L_{\gamma'}\cap K\); the dimension formula for sum and intersection gives the inequality.

## References

1. Lean: `New.Filling.mem_commonLink`, `New.Filling.commonLink_self`, `New.Filling.commonLink_le_linkedX₀_inf`, `New.Filling.finrank_commonLink`, `New.Filling.finrank_linkedX₀_add_finrank_inf_le` in `src/New/Spanning/Unfolding/TermStructure.lean`.
