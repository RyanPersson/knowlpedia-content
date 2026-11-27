+++
id = "proofs/grh/spanning-unfolding-a/groups-of-a-graded-fitting-space"
title = "The Bessel groups and the embedding of U(X_0) for a fitting space"
kind = "proposition"
summary = "Under the identifications of a fitting space, the unipotent and Bessel groups of the grading correspond to those of S, and the embeddings of U(X_0) agree at the finite and infinite places."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.mem_unipotent_iff_mem_besselU", "New.Filling.Fits.mem_besselGroup_iff_mem_besselS", "New.Filling.Fits.finiteEquiv_inclX", "New.Filling.Fits.finiteEquiv_inclXFin", "New.Filling.Fits.adelicToFin_adelicEquiv_inclX", "New.Filling.Fits.adelicToInf_inclX", "New.Filling.Fits.inclXFin_mem_stdLevel_iff", "New.Filling.Fits.inclXFin_mem_stdPrincipalLevel_iff", "New.Filling.Fits.gradeOf_eq_two_mul_sub_level", "New.Filling.Fits.coe_adelicEquiv_inclX"]
lean_files = ["src/New/Spanning/Unfolding/PoincareSeries.lean"]
proof_status = "outline"
+++

**Proposition.** Let \(V\) with grading \(Y\) [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fit]] the [[?lean:New.Filling|filling data]] \(S\) over a [[?c:CM field|CM field]] \(E\), with identifications \(\alpha:G\to G_S(\mathbb A)\) and \(\psi:G_f\to G_{S,f}\). Then:

1. The grade of a basis index \(i\) in \(Y\) is \(2(\varrho-\operatorname{level}(i))\), with the levels \(a\) on \(e_a\), \(\varrho\) on the middle block and \(2\varrho-a\) on \(e_a^{*}\).
2. \(g\in G\) lies in the [[?lean:New.Grading.unipotent|unipotent group of the grading]] iff \(\alpha(g)\) lies in the Bessel unipotent group \(\mathsf U\); and \(g\) lies in the [[?lean:New.Grading.besselGroup|Bessel group of the grading]] iff \(\alpha(g)\) lies in the [[?lean:New.Shape.Form.besselS|Bessel subgroup]].
3. For an adelic point \(a\) of \(U(X_0)\) and the embedding \(j_Y\) given by the grading ([[?lean:New.Grading.inclX|inclusion of \(U(X_0)\)]]): \(\alpha(j_Y(a))\) is the block matrix acting by \(a\) on \(X_0\) and trivially elsewhere; its finite part in the lattice basis is \(\iota(a_f)\) ([[?lean:New.Filling.inclHFin|inclusion of \(U(X_0)\)]]); \(\psi(j_Y(a)_f)=\iota(a_f)\); and its rescaled infinite part is, at each place, the block embedding of \(a_v\) into \(G_1\).
4. For a finite adelic point \(a\) of \(U(X_0)\): \(j_Y(a)\) is integral iff \(\iota(a)\in K\), and \(j_Y(a)\in J_M\) iff \(\iota(a)\in K(M)\).

## Proof

1. Direct from the standard labelling of the grading (three blocks of indices).
2. Both groups are defined by prescribing certain entries \((i,j)\) of the same matrix to be those of the identity. For the unipotent groups the prescribed positions are those with \(\operatorname{grade}(i)\le\operatorname{grade}(j)\), resp. \(\operatorname{level}(j)\le\operatorname{level}(i)\), which agree by 1. For the Bessel groups the same comparison of prescribed positions is made block by block; this case check is only asserted here (it is the proof of the declaration named in the last reference).
3. The first statement is the block form of the embedding in the standard labelling. Taking finite parts and conjugating into the lattice basis gives \(\iota(a_f)\). Then \(\psi(j_Y(a)_f)=\iota(\eta)^{-1}\iota(a_f)\iota(\eta)=\iota(a_f)\) because \(\eta\) is central in the finite adelic points of \(U(X_0)\). At the [[?c:Infinite place of a number field|infinite places]] the diagonal rescaling is \(1\) on \(X_0\), so conjugating by it fixes the block matrix.
4. From 3 and property 2 of fitting spaces (\(\psi\) preserves integrality and reductions at the chosen places).

## References

1. Lean: `New.Filling.Fits.mem_unipotent_iff_mem_besselU` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
2. Lean: `New.Filling.Fits.mem_besselGroup_iff_mem_besselS` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
3. Lean: `New.Filling.Fits.finiteEquiv_inclX` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
4. Lean: `New.Filling.Fits.finiteEquiv_inclXFin` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
5. Lean: `New.Filling.Fits.adelicToFin_adelicEquiv_inclX` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
6. Lean: `New.Filling.Fits.adelicToInf_inclX` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
7. Lean: `New.Filling.Fits.inclXFin_mem_stdLevel_iff` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
8. Lean: `New.Filling.Fits.inclXFin_mem_stdPrincipalLevel_iff` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
9. Lean: `New.Filling.Fits.gradeOf_eq_two_mul_sub_level` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
10. Lean: `New.Filling.Fits.coe_adelicEquiv_inclX` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
11. The step asserted without proof above is proved in Lean by `New.Filling.Fits.mem_besselGroup_iff_mem_besselS`.
