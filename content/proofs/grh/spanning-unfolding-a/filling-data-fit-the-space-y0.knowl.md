+++
id = "proofs/grh/spanning-unfolding-a/filling-data-fit-the-space-y0"
title = "The filling data of admissible data fit the space Y_0"
kind = "theorem"
summary = "For admissible data D, the hermitian space Y_0 with its grading fits the filling data of D, with central element the inverse of the lattice scale."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.filling_fits", "New.Data.inclXFin_zero_mem_stdLevel_iff", "New.Data.comap_inclXFin_zero_chosenLevel"]
lean_files = ["src/New/Spanning/Unfolding/FillingAdmissible.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]] and \(S_D\) its [[?lean:New.Data.filling|filling data]]. The [[?c:Hermitian form|hermitian space]] \(Y_0\) ([[?lean:New.Data.spaceY|space \(Y_j\)]] for \(j=0\)) with its grading ([[?lean:New.Data.gradingY|grading of \(Y_j\)]]) [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fits]] \(S_D\), with the [[?c:Harish-Chandra parameter|Harish-Chandra parameters]] \(l_v\) given by [[?lean:New.Data.paramW|the parameters of \(W\)]], the weights \(kw_v\) given by the [[?lean:New.Data.columnCount|column counts]], and the central element \(\eta=u^{-1}\), where \(u\) is the [[?lean:New.Data.latticeScale|lattice scale]] of \(Y_0\), a finite adele of norm one acting as a scalar on \(X_0\).

Consequences:

1. a finite adelic point \(a\) of \(U(X_0)\) preserves the lattice of \(Y_0\) if and only if \(a\) is integral and its last row is congruent to that of \(1\) modulo \(\pi\);
2. the finite adelic points of \(U(X_0)\) lying in the principal level of \(Y_0\) at the chosen places form the level \(K_{X_0}\) of \(X_0\) ([[?lean:New.Data.levelX|level of \(X_j\)]] for \(j=0\)).

## Proof

The five conditions of fitting are checked as follows.

- *Types.* The Bessel system at each real place has the required type by construction ([[?lean:New.Data.isDiscreteSeriesBessel_filling_besselSystem|type of the Bessel systems of the data]]).
- *Labelling.* The grading of \(Y_0\) is standardly indexed by definition.
- *[[?c:Idempotent element|Idempotent]] kernel.* The type kernel of the parameters is a cusp kernel, in particular idempotent ([[?lean:New.Data.isCuspKernel_typeKernel_paramW|the type kernel of the data is a cusp kernel]]).
- *The point.* By the choice of \(Y_0\), its finite frame is the graded lattice basis (with the lattice scale \(u\)) times an integral matrix \(\gamma\) that reduces to \(1\) at the chosen places ([[?lean:New.Data.exists_spaceY_xFin_eq|finite frame of \(Y_j\)]]). The graded lattice basis scales only the string by \(u\); hence it equals \(u\cdot\iota_0(u^{-1})\cdot B\), where \(B\) is the lattice basis of \(S_D\) and \(\iota_0(u^{-1})\) scales \(X_0\) by \(u^{-1}=\bar u\). **This matrix identity is only asserted here**; in the source it is a comparison of block matrices entry by entry (inside the declaration named in the last reference), which I did not re-derive because it depends on the definition of the graded lattice basis in another area.
- *Centrality.* Scalars commute with \(U(X_0)\) ([[?lean:New.Seesaw.commute_scalarFin|scalars are central]]).

Consequence 1 combines item 4 of the proposition on [[proofs/grh/spanning-unfolding-a/groups-of-a-graded-fitting-space|groups of a graded fitting space]] with item 3 of the proposition on [[proofs/grh/spanning-unfolding-a/unitary-group-of-x0-in-lattice-basis|\(U(X_0)\) in the lattice basis]]. Consequence 2 combines the same item 4 with the identification of \(K_{X_0}\) as the preimage of \(K(M)\) ([[?lean:New.Data.levelX_zero_eq_comap|the level of \(X_0\) as a preimage]]).

## References

1. Lean: `New.Data.filling_fits` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
2. Lean: `New.Data.inclXFin_zero_mem_stdLevel_iff` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
3. Lean: `New.Data.comap_inclXFin_zero_chosenLevel` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
4. The step asserted without proof above is proved in Lean by `New.Data.filling_fits`.
