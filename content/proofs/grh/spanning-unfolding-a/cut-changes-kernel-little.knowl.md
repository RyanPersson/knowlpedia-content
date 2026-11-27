+++
id = "proofs/grh/spanning-unfolding-a/cut-changes-kernel-little"
title = "Pointwise bounds for the Bessel kernel and for the effect of the cut"
kind = "lemma"
summary = "Via decay majorants, the kernel is bounded by the majorant at y times an inverse power of the length at gamma^-1 y, and replacing W by its cut changes it by at most 2 b^(-2 r^3 f) times that bound."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.enorm_besselKernel_sub_cut_le", "New.Filling.le_scaledBesselLengthProd_mul", "New.Filling.pow_mul_pow_mul_prod_enorm_le", "New.Filling.pow_mul_prod_enorm_le_majorant", "New.Filling.pow_mul_prod_enorm_le_bound"]
lean_files = ["src/New/Spanning/Unfolding/AmplitudeSums.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\) with \(f\) [[?c:Infinite place of a number field|infinite places]], \(b\) its parameter, \(r\) the rank, and put \(i_0=r^{3}f\). At each infinite place \(v\) let \((w_v,a_v)\) be a [[?lean:New.IsDecayMajorant|decay majorant]] of the pair \((W_v,W_v^{\flat})\) of the full and the cut Bessel function: \(w_v:G_1\to[0,\infty]\) is measurable, left invariant under the Bessel subgroup, bounded by the finite constant \(a_v\), and for both sides \(\tau\) and all \(x\in G_1\)
\[
\max\bigl(1,\ell(x)/b^{6n}\bigr)^{3i_0}\,\lVert W_v^{\tau}(x)\rVert\le w_v(x).
\]
Let \(P\) be the [[proofs/grh/spanning-unfolding-a/scaled-bessel-length-product|product of the scaled lengths]], \(\gamma\) a rational [[?c:Isometry of a hermitian space|isometry]], \(y\in G_\infty\), \(z=\gamma^{-1}y\), and \(\mathcal K^{\tau}_\gamma\) the [[?lean:New.Filling.besselKernel|Bessel kernel]] of side \(\tau\). Then:

1. \(P(y)^{3i_0}\prod_v\lVert W^{\tau}_v(y_v)\rVert\le\prod_vw_v(y_v)\le\prod_va_v\); in particular \(P(y)^{2i_0}\prod_v\lVert W_v^{\tau}(y_v)\rVert\) is at most \(\prod_vw_v(y_v)\) and at most \(\bigl(\prod_va_v\bigr)P(y)^{-i_0}\).
2. If \(\mathcal K^{\tau}_\gamma(y)\ne\mathcal K^{\flat}_\gamma(y)\) then \(b\le P(y)\,P(z)\).
3. \(\displaystyle\lVert\mathcal K^{\tau}_\gamma(y)-\mathcal K^{\flat}_\gamma(y)\rVert\le2\,b^{-2i_0}\,\prod_vw_v(y_v)\cdot\prod_va_v\cdot P(z)^{-i_0}.\)

## Proof

1. Multiply the defining inequalities of the majorants over the places; the rest follows from \(P\ge1\) and \(w_v\le a_v\).

2. The full and the cut function at a place can differ at \(x\) only if \(\ell(x)>\tfrac12b^{6n+2}\) ([[?lean:New.IsCutPair.lt_besselLength_of_ne|support of the cut]]), in which case the scaled length of \(x\) is at least \(b^2/2\ge b\) (as \(b\ge1000\)). If \(P(y)P(z)<b\) then, both factors being \(\ge1\), \(P(y)<b\) and \(P(z)<b\), so every scaled length of \(y_v\) and \(z_v\) is \(<b\); hence \(W_v=W_v^{\flat}\) at all \(y_v\) and \(z_v\), and the two kernels agree.

3. If the kernels agree there is nothing to prove. Otherwise, by 2, \(b^{2i_0}\le P(y)^{2i_0}P(z)^{2i_0}\). For either side \(\sigma\), by the [[proofs/grh/spanning-unfolding-a/amplitude-bounded-by-majorant|factorisation of the norm of the kernel]] and 1,
\[
b^{2i_0}\lVert\mathcal K^{\sigma}_\gamma(y)\rVert\le P(y)^{2i_0}\prod_v\lVert W^{\sigma}_v(y_v)\rVert\cdot P(z)^{2i_0}\prod_v\lVert W^{\sigma}_v(z_v)\rVert\le\prod_vw_v(y_v)\cdot\prod_va_v\,P(z)^{-i_0}.
\]
The triangle inequality for \(\sigma=\tau\) and \(\sigma=\flat\) gives 3.

## References

1. Lean: `New.Filling.enorm_besselKernel_sub_cut_le` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
2. Lean: `New.Filling.le_scaledBesselLengthProd_mul` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
3. Lean: `New.Filling.pow_mul_pow_mul_prod_enorm_le` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
4. Lean: `New.Filling.pow_mul_prod_enorm_le_majorant` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
5. Lean: `New.Filling.pow_mul_prod_enorm_le_bound` in `src/New/Spanning/Unfolding/AmplitudeSums.lean`.
