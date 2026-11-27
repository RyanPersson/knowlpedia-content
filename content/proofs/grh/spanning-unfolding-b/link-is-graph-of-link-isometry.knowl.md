+++
id = "proofs/grh/spanning-unfolding-b/link-is-graph-of-link-isometry"
title = "The link is the graph of the link isometry"
kind = "theorem"
summary = "The link isometry preserves the form of the positive space, the link is its graph, two isometries have the same link isometry exactly when they have the same link, and it is invariant under the Bessel unipotent group."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.dotProduct_positiveGram_mulVec_linkIsometry", "New.Filling.mem_link_iff_linkIsometry", "New.Filling.linkIsometry_eq_iff", "New.Filling.linkIsometry_inv_mul_mul_of_mem_besselU"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma,\gamma'\in G(E)\), and \(\Upsilon_\gamma\) the [[proofs/grh/spanning-unfolding-b/link-isometry|link isometry]] of the [[proofs/grh/spanning-unfolding-b/positive-space-and-link-maps|positive space]] \((P,h^+)\).

1. \(h^+(\Upsilon_\gamma a,\Upsilon_\gamma b)=h^+(a,b)\) for all \(a,b\in P\).
2. A pair \(p\) of middle vectors lies in the link \(L_\gamma\) if and only if \(\Upsilon_\gamma(\operatorname{src}p)=\operatorname{tgt}p\).
3. \(\Upsilon_\gamma=\Upsilon_{\gamma'}\) if and only if \(L_\gamma=L_{\gamma'}\).
4. If \(u,u'\) lie in the Bessel unipotent group, then \(\Upsilon_{u^{-1}\gamma u'}=\Upsilon_\gamma\).

## Proof

(1) Write \(a=\operatorname{src}p\), \(b=\operatorname{src}q\) with \(p,q\in L_\gamma\). Then \(\Upsilon_\gamma a=\operatorname{tgt}p\), \(\Upsilon_\gamma b=\operatorname{tgt}q\), and the claim is part 1 of [[proofs/grh/spanning-unfolding-b/rank-of-the-link|the lemma on the link]].

(2) If \(p\in L_\gamma\) the identity holds by construction. Conversely suppose \(\Upsilon_\gamma(\operatorname{src}p)=\operatorname{tgt}p\). Choose \(q\in L_\gamma\) with \(\operatorname{src}q=\operatorname{src}p\); then \(\operatorname{tgt}q=\Upsilon_\gamma(\operatorname{src}q)=\operatorname{tgt}p\). A pair is determined by its source and target, so \(p=q\in L_\gamma\).

(3) By (2) the link is determined by \(\Upsilon_\gamma\). Conversely, if \(L_\gamma=L_{\gamma'}\) and \(a=\operatorname{src}p\) with \(p\) in this link, then \(\Upsilon_\gamma a=\operatorname{tgt}p=\Upsilon_{\gamma'}a\).

(4) By (3) and [[proofs/grh/spanning-unfolding-b/link-and-cells-are-invariant-under-the-unipotent-group|the invariance of the link]].

## References

1. Lean: `New.Filling.dotProduct_positiveGram_mulVec_linkIsometry`, `New.Filling.mem_link_iff_linkIsometry`, `New.Filling.linkIsometry_eq_iff`, `New.Filling.linkIsometry_inv_mul_mul_of_mem_besselU` in `src/New/Spanning/Unfolding/Link.lean`.
