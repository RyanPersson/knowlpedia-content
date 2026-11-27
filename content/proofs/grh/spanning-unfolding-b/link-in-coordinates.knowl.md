+++
id = "proofs/grh/spanning-unfolding-b/link-in-coordinates"
title = "The link of an isometry in coordinates"
kind = "lemma"
summary = "A vector is orthogonal to the isotropic span A and to its image exactly when its dual coordinates and those of its preimage vanish; this describes the link by an explicit condition on the isometry."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.mem_link", "New.orthogonal_isotropicFramePair_iff", "New.linkMatrix_mulVec", "New.splitGram_mulVec"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Lemma.** Let \(F\) be a commutative ring with involution, \(J\) the split Gram matrix of \(\varrho\) hyperbolic planes \((e_a,e_a^*)\) and a middle form \(T\), \(\gamma\) an isometry of \(J\), and \(A\) the span of \(e_0,\dots,e_{\varrho-1}\). Write a vector as a triple of blocks \((t_e,t_{\mathrm{mid}},t_{e^*})\).

1. A vector \(t\) satisfies \(h(e_a,t)=0\) and \(h(\gamma e_a,t)=0\) for all \(a\) if and only if \(t_{e^*}=0\) and \((\gamma^{-1}t)_{e^*}=0\).
2. The [[?lean:New.link|link]] of \(\gamma\), the module of the pairs \(\bigl(t_{\mathrm{mid}},(\gamma^{-1}t)_{\mathrm{mid}}\bigr)\) for \(t\) as in 1, consists exactly of the pairs \((p_1,p_2)\) of middle vectors for which there is \(a\in F^\varrho\) with
\[
\gamma\,(a,\,p_2,\,0)=(\ast,\,p_1,\,0).
\]

## Proof

(1) \(Jt=(t_{e^*},\,Tt_{\mathrm{mid}},\,t_e)\), so \(h(e_a,t)\) is the \(e_a^*\)-coordinate of \(t\). Since \(\gamma\) is an isometry, \(h(\gamma e_a,t)=h(e_a,\gamma^{-1}t)\), the \(e_a^*\)-coordinate of \(\gamma^{-1}t\).

(2) If \(t\) is as in 1, then \(\gamma^{-1}t=(a,p_2,0)\) with \(a=(\gamma^{-1}t)_e\) and \(p_2=(\gamma^{-1}t)_{\mathrm{mid}}\), and \(\gamma(a,p_2,0)=t=(\ast,p_1,0)\). Conversely, given \(a\) with \(\gamma(a,p_2,0)=(\ast,p_1,0)\), the vector \(t=\gamma(a,p_2,0)\) has \(t_{e^*}=0\) and \((\gamma^{-1}t)_{e^*}=0\), and its pair of middle blocks is \((p_1,p_2)\).

## References

1. Lean: `New.mem_link`, `New.orthogonal_isotropicFramePair_iff` in `src/New/Spanning/Unfolding/Link.lean`.
