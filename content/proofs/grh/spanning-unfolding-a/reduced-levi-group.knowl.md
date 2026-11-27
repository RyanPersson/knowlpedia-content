+++
id = "proofs/grh/spanning-unfolding-a/reduced-levi-group"
title = "The reduction of U(X_0) and the index of the source level"
kind = "theorem"
summary = "The reduction of the integral points of U(X_0) at the chosen places is the product of the groups GL_k over the residue fields, and its order is the index of the source level in the stabiliser of the lattice."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_mulEquiv_reducedImage_besselH", "New.Filling.reducedImageBesselHEquiv", "New.Filling.relIndex_comap_principalLevel", "New.Filling.relIndex_sourceLevel", "New.Filling.inclHFin_mem_latticeStabilizer_of_supportedOn", "New.Filling.latticeStabilizerH", "New.Filling.toReducedImageBesselH", "New.Filling.reduceLatticeStabilizerH", "New.Filling.ker_toReducedImageBesselH", "New.mulEquivOfKerEq", "New.Filling.isConjApart_chosenPlaces", "New.Filling.coe_mem_principalLevel_iff_reduction_eq_one"]
lean_files = ["src/New/Spanning/Unfolding/ReducedGroups.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), \(\iota\) the [[?lean:New.Filling.inclHFin|inclusion]] of the finite adelic points of \(H=U(X_0)\) into the finite adelic group of \(V\) (lattice basis), \(K\) the [[?lean:New.Filling.latticeStabilizer|lattice stabiliser]], \(K(M)\) the [[?lean:New.Filling.principalLevel|principal level]], and \(\bar H\) the [[?lean:New.Filling.reducedImage|reduced image]] of the image of \(H\) ([[?lean:New.Shape.Form.besselH|the fixer of the basis vectors outside \(X_0\)]]).

1. There is a group isomorphism \(\phi:\bar H\xrightarrow{\ \sim\ }\prod_wGL_\kappa(k_w)\) (product over the chosen places) such that for every integral \(k\in H(\mathbb A_f)\) with \(\iota(k)\in K\), \(\phi\) maps the reduction of \(\iota(k)\) to the family of the reductions of \(k\).
2. \(\bigl[\iota^{-1}(K):\iota^{-1}(K(M))\bigr]=\lvert\bar H\rvert\).
3. If \(S\) satisfies the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], the [[?lean:New.Filling.sourceLevel|source level]] has index \(\lvert\bar H\rvert\) in \(\iota^{-1}(K)\).

## Proof

**1.** Let \(K_H\) be the group of integral \(k\) with \(\iota(k)\in K\). Two homomorphisms start from \(K_H\): \(\alpha(k)=\) reduction of \(\iota(k)\), with values in \(\bar H\), and \(\beta(k)=\) family of reductions of \(k\), with values in \(\prod_wGL_\kappa(k_w)\).

- \(\alpha\) is onto: an element of \(\bar H\) is the reduction of some \(x\in K\) in the image of \(H\), \(x=\iota(k)\), and then \(k\) is integral by the proposition on [[proofs/grh/spanning-unfolding-a/unitary-group-of-x0-in-lattice-basis|\(U(X_0)\) in the lattice basis]].
- \(\beta\) is onto: the chosen places are distinct and none is conjugate to a chosen place, so any family of invertible matrices over the [[algebra-commutative/residue-field|residue fields]] lifts to an integral unitary \(k\) that is \(1\) away from the chosen places and their conjugates ([[?lean:New.exists_reduceFamily_eq|lifting reductions at conjugate-apart places]]). Such a \(k\) lies in \(K_H\): the row \(k_0\) of \(k-1\) must be divisible by \(\pi\) at every finite place \(w\); if \(\pi\) is a unit at \(w\) this is integrality, and otherwise \(w\) has norm \(N\ne p_i\), so neither \(w\) nor \(\bar w\) is chosen and \(k=1\) at \(w\).
- \(\ker\alpha=\ker\beta\): for \(\iota(k)\in K\), the reduction of \(\iota(k)\) at \(w\) is \(1\) iff that of \(k\) is (same proposition, item 4).

Two surjective homomorphisms with the same kernel have isomorphic targets, compatibly with the maps; this gives \(\phi\) with \(\phi\circ\alpha=\beta\).

**2.** The reduction \(\iota^{-1}(K)\to\) residue group, \(k\mapsto\overline{\iota(k)}\), has image \(\bar H\) (as in the first bullet) and kernel \(\iota^{-1}(K(M))\), because an element of \(K\) lies in \(K(M)\) iff its reduction is \(1\).

**3.** By the standing hypotheses the source level is \(\iota^{-1}(K(M))\).

## References

1. Lean: `New.Filling.exists_mulEquiv_reducedImage_besselH` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
2. Lean: `New.Filling.reducedImageBesselHEquiv` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
3. Lean: `New.Filling.relIndex_comap_principalLevel` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
4. Lean: `New.Filling.relIndex_sourceLevel` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
5. Lean: `New.Filling.inclHFin_mem_latticeStabilizer_of_supportedOn` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
6. Lean: `New.Filling.latticeStabilizerH` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
7. Lean: `New.Filling.toReducedImageBesselH` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
8. Lean: `New.Filling.reduceLatticeStabilizerH` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
9. Lean: `New.Filling.ker_toReducedImageBesselH` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
10. Lean: `New.mulEquivOfKerEq` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
11. Lean: `New.Filling.isConjApart_chosenPlaces` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
12. Lean: `New.Filling.coe_mem_principalLevel_iff_reduction_eq_one` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
