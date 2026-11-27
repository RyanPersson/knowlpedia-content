+++
id = "proofs/grh/spanning-unfolding-a/packing-of-weights"
title = "Packing of weights bounded by class cutoffs"
kind = "lemma"
summary = "Weights bounded by x times class cutoffs at translates gamma^-1 y of a point, for terms gamma over a fixed (c, s), add up to at most (b^(6 n^2) R^2)^(dim V) x."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.tsum_le_of_le_classCutoff_mul"]
lean_files = ["src/New/Spanning/Unfolding/Packing.lean"]
proof_status = "full"
+++

**Lemma (packing of weights).** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity and \(S\) [[?lean:New.Filling|filling data]] over \(E\) satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]]; \(b\) its parameter, \(n=\varrho+1\). Fix a class \(c\), an element \(s\) of the [[?lean:New.Filling.ResidueGL|residue group]], a point \(y\in G_\infty\), \(R\ge1\) and \(x\in[0,\infty]\). Let \(\alpha\) be an index set with maps \(p\mapsto k_p\) (a class), \(p\mapsto\gamma_p\) (a rational [[?c:Isometry of a hermitian space|isometry]]), \(p\mapsto w_p\in[0,\infty]\), such that \(p\mapsto(k_p,\gamma_p)\) is injective and, for every \(p\) with \(w_p\ne0\):

1. \(\gamma_p\) is a [[?lean:New.Filling.termsOver|term]] over \((c,s,k_p)\);
2. at every [[?c:Infinite place of a number field|infinite place]] the [[?lean:New.besselLength|Bessel length]] of \((\gamma_p^{-1}y)_v\) is at most \(b^{6n+2}R\);
3. \(w_p\le\beta_{k_p}(\gamma_p^{-1}y)\cdot x\), with \(\beta\) the [[?lean:New.Filling.classCutoff|class cutoff]].

Let \(\mathcal V\) be a real subspace containing the differences of the families of frame vectors of \(\gamma_p^{-1}y\) and \(\gamma_q^{-1}y\) for all \(p,q\) with \(w_p,w_q\ne0\). Then
\[
\sum_{p\in\alpha}w_p\le\bigl(b^{6n^2}R^2\bigr)^{\dim_{\mathbb R}\mathcal V}\cdot x .
\]

## Proof

Restrict to the support \(A\) of \(w\). For \(p\in A\), hypothesis 3 gives \(\beta_{k_p}(\gamma_p^{-1}y)\ne0\), so by item 3 of the proposition on [[proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one|class cutoffs]] the frame vectors of \(\gamma_p^{-1}y\) have norm at most \(b^{37n}R\).

Colour \(p\in A\) by the frame image \(\gamma_pf\). By the theorem on [[proofs/grh/spanning-unfolding-a/packing-of-frames|packing of frames]] there are at most \((b^{6n^2}R^2)^{\dim\mathcal V}\) colours. If \(p,q\) have the same colour then, both being terms over \((c,s,\cdot)\) with the same frame image, \(k_p=k_q\) and \(\gamma_p^{-1}\gamma_q\in\mathsf U^0_{k_p}(M)\) ([[?lean:New.Filling.termsOver.eq_and_mem_classUnipotent₀|terms with the same frame]]). By the [[proofs/grh/spanning-unfolding-a/colouring-bound-for-weighted-sums|colouring bound]] it suffices to show that a nonempty set \(B\subseteq A\) of pairwise so related indices has total weight at most \(x\).

Fix \(p\in B\). For \(q\in B\), \(k_q=k_p\) and \(u_q=\gamma_q^{-1}\gamma_p\in\mathsf U_{k_p}(M)\); the map \(q\mapsto u_q\) is injective by injectivity of \(q\mapsto(k_q,\gamma_q)\). Since \(\gamma_q^{-1}y=u_q\,(\gamma_p^{-1}y)\), hypothesis 3 and item 2 of the proposition on class cutoffs give
\[
\sum_{q\in B}w_q\le x\sum_{q\in B}\beta_{k_p}\bigl(u_q\,\gamma_p^{-1}y\bigr)\le x\sum_{u\in\mathsf U_{k_p}(M)}\beta_{k_p}\bigl(u\,\gamma_p^{-1}y\bigr)=x .
\]

## References

1. Lean: `New.Filling.tsum_le_of_le_classCutoff_mul` in `src/New/Spanning/Unfolding/Packing.lean`.
