+++
id = "proofs/grh/spanning-unfolding-a/reduced-unipotent-group"
title = "The reduction of the Bessel unipotent group"
kind = "theorem"
summary = "The reduction of the integral points of U at the chosen places consists of all tuples of block unitriangular matrices, and has order M^(f rho (2k + 2 rho + 1))."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.mem_reducedImage_besselU", "New.Filling.card_reducedImage_besselU", "New.Filling.card_freeEntry_besselIndex", "New.card_freeEntry_level", "New.card_unitriangular", "New.unitriangularEquiv", "New.exists_unitriangular_map_eq", "New.exists_invAdjoint_unitriangular", "New.splitGram_apply_eq_zero"]
lean_files = ["src/New/Spanning/Unfolding/ReducedGroups.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\) with \(f\) [[?c:Infinite place of a number field|infinite places]], and let \(\bar{\mathsf U}\) be the [[?lean:New.Filling.reducedImage|reduced image]] of the finite adelic [[?lean:New.Shape.Form.besselU|Bessel unipotent group]]: the image of \(K\cap\mathsf U\) in the [[?lean:New.Filling.ResidueGL|residue group]] \(\prod_wGL_r(k_w)\).

1. An element \(s=(s_w)\) of the residue group lies in \(\bar{\mathsf U}\) if and only if every \(s_w\) is [[?c:Unitriangular matrix|block upper unitriangular]] for the levels (\(s_{w,ij}=\delta_{ij}\) whenever \(\operatorname{level}(j)\le\operatorname{level}(i)\); the levels are \(a\) on \(e_a\), \(\varrho\) on \(X_0\oplus Ez\), \(2\varrho-a\) on \(e_a^{*}\)).
2. \(\lvert\bar{\mathsf U}\rvert=M^{f\varrho(2k+2\varrho+1)}\) ([[?lean:New.Filling.unipotentOrder|unipotent order]]), where \(M=p_0p_1\) and \(k=\dim X_0\).

## Proof

**1.** If \(s\) is the reduction of \(k\in K\cap\mathsf U\), the entries of \(k\) at the prescribed positions are those of \(1\), and so are their reductions. Conversely let all \(s_w\) be block unitriangular. A block unitriangular matrix is the same as a choice of its *free entries*, at the positions \((i,j)\) with \(\operatorname{level}(i)<\operatorname{level}(j)\). Lift the free entries of all \(s_w\) simultaneously to \(\widehat{\mathcal O}\) (lemma on [[proofs/grh/spanning-unfolding-a/prescribing-residues-above-the-level|prescribing residues]]); this gives a block unitriangular matrix \(u\) over \(\widehat{\mathcal O}\) with \(u\equiv s_w\) at every chosen \(w\). It has a block unitriangular inverse adjoint: with \(J\) the [[?c:Gram matrix|Gram matrix]] in the lattice basis,
\[
u'=J^{-1}(u^{-1})^{*}J=1+J^{-1}(u^{-1}-1)^{*}J
\]
satisfies \(u^{*}Ju'=J\); and since \(J\) and \(J^{-1}\) (the split form of the inverse middle block) have nonzero entries only at positions whose levels add up to \(2\varrho\), conjugate transposition reverses the order of the levels and the two Gram matrices reverse it back, so \(J^{-1}Z^{*}J\) is strictly block upper triangular whenever \(Z\) is. By the lemma on [[proofs/grh/spanning-unfolding-a/gluing-integral-isometries-at-chosen-places|gluing]] (with \(P\) all chosen places) there is \(k\in K\) that agrees with \(1\) wherever \(u\) and \(u'\) do — so \(k\in\mathsf U\) — and reduces to \(s_w\) at every \(w\).

**2.** By 1, \(\bar{\mathsf U}\) is the product over the chosen places of the groups of block unitriangular matrices over \(k_w\), each of order \(\lvert k_w\rvert^{d}\) with \(d\) the number of free entries. The blocks have sizes \(1,\dots,1,k+1,1,\dots,1\) (\(\varrho\) ones on each side), so
\[
d=\binom{2\varrho}{2}+2\varrho(k+1)=\varrho(2\varrho-1)+2\varrho(k+1)=\varrho(2k+2\varrho+1).
\]
(Count by rows: the row \(e_a\) has its free entries at the \(e_b\), \(b>a\), at the \(k+1\) middle columns and at all \(\varrho\) columns \(e_b^{*}\); a middle row has \(\varrho\); the row \(e_a^{*}\) has those \(e_b^{*}\) with \(b<a\).) For each of the two primes \(p_i\) there are \(f\) chosen places, with [[algebra-commutative/residue-field|residue fields]] of \(p_i\) elements. Hence \(\lvert\bar{\mathsf U}\rvert=(p_0p_1)^{fd}\).

## References

1. Lean: `New.Filling.mem_reducedImage_besselU` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
2. Lean: `New.Filling.card_reducedImage_besselU` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
3. Lean: `New.Filling.card_freeEntry_besselIndex` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
4. Lean: `New.card_freeEntry_level` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
5. Lean: `New.card_unitriangular` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
6. Lean: `New.unitriangularEquiv` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
7. Lean: `New.exists_unitriangular_map_eq` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
8. Lean: `New.exists_invAdjoint_unitriangular` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
9. Lean: `New.splitGram_apply_eq_zero` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
