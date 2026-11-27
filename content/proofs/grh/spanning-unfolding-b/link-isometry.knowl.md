+++
id = "proofs/grh/spanning-unfolding-b/link-isometry"
title = "Link isometry"
kind = "construction"
summary = "The linear automorphism of the positive space whose graph, after exchanging z-coordinates, is the link of a rational isometry."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.linkIsometry", "New.Filling.linkSourceEquiv", "New.Filling.linkTargetEquiv", "New.Filling.linkSourceEquiv_apply", "New.Filling.linkTargetEquiv_apply", "New.Filling.linkIsometry_linkSource", "New.Filling.exists_mem_link_linkSource_eq"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) and \(\gamma\in G(E)\) with [[?lean:New.link|link]] \(L_\gamma\). By [[proofs/grh/spanning-unfolding-b/rank-of-the-link|the rank of the link]], the [[proofs/grh/spanning-unfolding-b/positive-space-and-link-maps|source and target maps]] restrict to linear bijections \(\operatorname{src},\operatorname{tgt}\colon L_\gamma\to P\) onto the positive space \(P=X_0\perp Ez^+\). The **link isometry** of \(\gamma\) is the linear automorphism
\[
\Upsilon_\gamma=\operatorname{tgt}\circ\operatorname{src}^{-1}\colon P\to P .
\]
Thus for every pair \(p=(y_0+\lambda'z_N,\ y_0'+\lambda z_N)\in L_\gamma\),
\[
\Upsilon_\gamma(y_0+\lambda z^+)=y_0'+\lambda'z^+ ,
\]
and every element of \(P\) is \(\operatorname{src}(p)\) for a unique \(p\in L_\gamma\).

## Remarks

That \(\Upsilon_\gamma\) preserves the form of \(P\), and that \(L_\gamma\) is its graph, is [[proofs/grh/spanning-unfolding-b/link-is-graph-of-link-isometry|the theorem on the link isometry]].

## References

1. Lean: `New.Filling.linkIsometry`, `New.Filling.linkSourceEquiv`, `New.Filling.linkTargetEquiv`, `New.Filling.linkIsometry_linkSource` in `src/New/Spanning/Unfolding/Link.lean`.
