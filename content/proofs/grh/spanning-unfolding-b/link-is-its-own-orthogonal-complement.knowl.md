+++
id = "proofs/grh/spanning-unfolding-b/link-is-its-own-orthogonal-complement"
title = "The link is its own orthogonal complement"
kind = "lemma"
summary = "For the form T minus T on pairs of middle vectors, a pair lies in the link of a rational isometry if and only if it is orthogonal to the link."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.mem_link_iff_orthogonal", "New.Filling.dotProduct_linkForm_mulVec_eq_sub"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma\in G(E)\) with link \(L_\gamma\), and let \(\ell\) be the [[proofs/grh/spanning-unfolding-b/common-link|link form]] \(\ell(p,q)=h_{\mathrm{mid}}(p_1,q_1)-h_{\mathrm{mid}}(p_2,q_2)\) on pairs of middle vectors, where \(h_{\mathrm{mid}}\) is the form \(\operatorname{diag}(1,\dots,1,-N)\).

1. \(\ell(p,q)=h^+(\operatorname{src}p,\operatorname{src}q)-h^+(\operatorname{tgt}p,\operatorname{tgt}q)\) for all pairs \(p,q\).
2. \(p\in L_\gamma\) if and only if \(\ell(q,p)=0\) for all \(q\in L_\gamma\).

## Proof

(1) With \(p=(y_0+\lambda'z_N,y_0'+\lambda z_N)\) and \(q=(w_0+\mu'z_N,w_0'+\mu z_N)\): \(\ell(p,q)=\langle y_0,w_0\rangle-N\bar\lambda'\mu'-\langle y_0',w_0'\rangle+N\bar\lambda\mu=\bigl(\langle y_0,w_0\rangle+N\bar\lambda\mu\bigr)-\bigl(\langle y_0',w_0'\rangle+N\bar\lambda'\mu'\bigr)\).

(2) If \(p\in L_\gamma\), then \(\ell(q,p)=0\) for \(q\in L_\gamma\) by (1) and [[proofs/grh/spanning-unfolding-b/rank-of-the-link|the lemma on the link]]. Conversely assume \(\ell(q,p)=0\) for all \(q\in L_\gamma\), and put \(d=\Upsilon_\gamma(\operatorname{src}p)-\operatorname{tgt}p\) with the [[proofs/grh/spanning-unfolding-b/link-isometry|link isometry]] \(\Upsilon_\gamma\). Choose \(q\in L_\gamma\) with \(\operatorname{src}q=\Upsilon_\gamma^{-1}d\), so \(\operatorname{tgt}q=d\). Then, using that [[proofs/grh/spanning-unfolding-b/link-is-graph-of-link-isometry|\(\Upsilon_\gamma\) preserves \(h^+\)]] and (1),
\[
h^+(d,d)=h^+(\operatorname{tgt}q,\Upsilon_\gamma\operatorname{src}p)-h^+(\operatorname{tgt}q,\operatorname{tgt}p)=h^+(\operatorname{src}q,\operatorname{src}p)-h^+(\operatorname{tgt}q,\operatorname{tgt}p)=\ell(q,p)=0 .
\]
As \(h^+\) is anisotropic, \(d=0\), and \(p\in L_\gamma\) because the link is the graph of \(\Upsilon_\gamma\).

## References

1. Lean: `New.mem_link_iff_orthogonal`, `New.Filling.dotProduct_linkForm_mulVec_eq_sub` in `src/New/Spanning/Unfolding/Link.lean`.
