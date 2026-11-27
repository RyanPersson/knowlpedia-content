+++
id = "proofs/grh/spanning-unfolding-b/expansion-of-the-squares"
title = "Expansion of the squares"
kind = "theorem"
summary = "Over a set of residues avoiding the scalar cosets, the square root of the second moment of the terms off the Bessel subgroup is bounded by the square root of the link-by-link bound plus a small multiple of the square root of the identity second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.sqrt_secondMoment_compl_besselS_le", "New.sqrt_add_le_sqrt_add_sqrt", "New.Filling.forty_le_k_mul_numInfPlaces"]
lean_files = ["src/New/Spanning/Unfolding/SquareExpansion.lean"]
proof_status = "full"
+++

**Theorem (expansion of the squares).** Let \(E\) contain a primitive \(5040\)-th root of unity and let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), with [[proofs/grh/spanning-unfolding-b/filling-constants|constants]] \(\nu=\operatorname{cov}_{\mathsf U}\), \(\mathcal{M}_{\mathrm{id}}\). For a family of blocks \(A(c,s,c')\) and \(\Omega\subset\bar G\) let
\[
\mathsf{E}(A,\Omega)=\nu^{-2}\sum_{c,c'\in\mathcal{C}}\ \sum_{s\in\Omega}\lVert A(c,s,c')\rVert^2
\]
be the [[?lean:New.Filling.secondMoment|second moment]], and let the [[?lean:New.Filling.linkSecondMoment|link second moment]] of a set \(T\) of terms be
\[
\mathsf{E}_{\mathrm{link}}(T,\Omega)=\sum_{c,c'}\sum_{s\in\Omega}\sum_{\Lambda}\bigl\lVert A^{\flat}_{T\cap\{\operatorname{link}=\Lambda\}}(c,s,c')\bigr\rVert^2\in[0,\infty],
\]
with \(A^\flat\) the [[proofs/grh/spanning-unfolding-b/filling-amplitude|amplitude sums]] of the cut side and \(\Lambda\) running over all subspaces. Let \(\Omega\) [[proofs/grh/spanning-unfolding-b/avoiding-scalar-cosets|avoid the scalar cosets]], let \(C\ge0\) and suppose
\[
\mathsf{E}_{\mathrm{link}}\bigl(\{\gamma:\operatorname{disc}(\gamma)\ne0\},\Omega\bigr)\le C\,\nu^2 .
\]
Then, with \(A\) the amplitude sums of the full side and \(\mathsf{S}\) the rational Bessel subgroup,
\[
\sqrt{\mathsf{E}\bigl(A_{G(E)\setminus\mathsf{S}},\Omega\bigr)}\le\sqrt C+b^{-15}\sqrt{\mathcal{M}_{\mathrm{id}}} .
\]

## Proof

By [[proofs/grh/spanning-unfolding-b/terms-off-the-bessel-subgroup-reduce-to-remaining-terms|the reduction to the remaining terms]], the blocks of \(G(E)\setminus\mathsf{S}\) at \(s\in\Omega\) are those of \(\Gamma^*\), so \(\mathsf{E}(A_{G(E)\setminus\mathsf{S}},\Omega)=\mathsf{E}(A_{\Gamma^*},\Omega)\). Write \(A_{\Gamma^*}=(A_{\Gamma^*}-A^\flat_{\Gamma^*})+A^\flat_{\Gamma^*}\). By [[?lean:New.Filling.sqrt_secondMoment_add_le|Minkowski's inequality for second moments]],
\[
\sqrt{\mathsf{E}(A_{\Gamma^*},\Omega)}\le\sqrt{\mathsf{E}(A_{\Gamma^*}-A^\flat_{\Gamma^*},\Omega)}+\sqrt{\mathsf{E}(A^\flat_{\Gamma^*},\Omega)} .
\]
Passing to the cut costs little: \(\mathsf{E}(A_U-A^\flat_U,\Omega)\le b^{-40}\mathcal{M}_{\mathrm{id}}\) for every set \(U\) ([[?lean:New.Filling.secondMoment_sub_cut_le|cost of the cut]]). For the cut side, the [[?lean:New.Filling.secondMoment_remainingTerms_le|reduction of the remaining terms to one link]] gives, from the hypothesis,
\[
\mathsf{E}(A^\flat_{\Gamma^*},\Omega)\le C+b^{-kf}\mathcal{M}_{\mathrm{id}}\le C+b^{-40}\mathcal{M}_{\mathrm{id}},
\]
since \(kf\ge40\) (as \(k\ge1000(2\varrho+2)\ge40\) and \(f\ge1\)) and \(b\ge1\). Using \(\sqrt{x+y}\le\sqrt x+\sqrt y\) and \(\sqrt{b^{-40}\mathcal{M}_{\mathrm{id}}}=b^{-20}\sqrt{\mathcal{M}_{\mathrm{id}}}\),
\[
\sqrt{\mathsf{E}(A_{\Gamma^*},\Omega)}\le\sqrt C+2b^{-20}\sqrt{\mathcal{M}_{\mathrm{id}}}=\sqrt C+2b^{-5}\cdot b^{-15}\sqrt{\mathcal{M}_{\mathrm{id}}},
\]
and \(2b^{-5}\le1\) because \(b\ge1000\).

## References

1. Lean: `New.Filling.sqrt_secondMoment_compl_besselS_le` in `src/New/Spanning/Unfolding/SquareExpansion.lean`.
