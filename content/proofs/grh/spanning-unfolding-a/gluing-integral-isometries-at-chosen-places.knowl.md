+++
id = "proofs/grh/spanning-unfolding-a/gluing-integral-isometries-at-chosen-places"
title = "Gluing integral isometries at the chosen places"
kind = "lemma"
summary = "From integral matrices u, u' with u* J u' = J and a set P of chosen places, one gets an integral isometry reducing to u at the places of P and to 1 at the other chosen places."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_reduction_eq_of_invAdjoint", "New.Filling.exists_idempotent_reduceAt_eq_ite", "New.conjTranspose_one_add_smul_sub_one_mul_mul_eq", "New.Filling.reduction_apply_eq_one_apply"]
lean_files = ["src/New/Spanning/Unfolding/ReducedGroups.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), \(J\) the [[?c:Gram matrix|Gram matrix]] of \(V\) in the lattice basis over the integral [[catalog/arithmetic/adeles-number-field-finite|finite adeles]] \(\widehat{\mathcal O}\), and \(u,u'\) square matrices over \(\widehat{\mathcal O}\) with \(u^{*}Ju'=J\) (\(u'\) is an *inverse adjoint* of \(u\)). Let \(P\) be a set of chosen places. Then there is \(k\) in the [[?lean:New.Filling.latticeStabilizer|lattice stabiliser]] \(K\) such that

1. \(k_{ab}=\delta_{ab}\) at every position \((a,b)\) where both \(u_{ab}=\delta_{ab}\) and \(u'_{ab}=\delta_{ab}\);
2. the reduction of \(k\) at a chosen place \(w\) is \(u\bmod w\) if \(w\in P\), and \(1\) otherwise.

Moreover, if \(k\in K\) has \(k_{ab}=\delta_{ab}\), then every reduction of \(k\) has the same entry at \((a,b)\).

## Proof

*An [[?c:Idempotent element|idempotent]].* Let \(e\in\widehat{\mathcal O}\) be the idempotent that is \(1\) at the places of \(P\) and \(0\) at all other finite places. Its conjugate \(\bar e\) is the idempotent of the conjugate places; no conjugate of a chosen place is chosen, so \(e\bar e=0\), \(e\) reduces to \(1\) at the places of \(P\) and to \(0\) at the other chosen places, and \(\bar e\) reduces to \(0\) at all chosen places.

*Gluing.* Put \(m=1+e(u-1)+\bar e(u'-1)\): it is \(u\) on the factor \(e\widehat{\mathcal O}\), \(u'\) on \(\bar e\widehat{\mathcal O}\) and \(1\) on the rest. Taking [[?c:Conjugate transpose|conjugate transposes]] in \(u^{*}Ju'=J\) gives \(u'^{*}Ju=J\). Expanding, and using \(e^2=e\), \(\bar e^2=\bar e\), \(e\bar e=0\),
\[
m^{*}Jm=J+e\,(u'^{*}Ju-J)+\bar e\,(u^{*}Ju'-J)=J .
\]
So \(m\) is an integral [[?c:Isometry of a hermitian space|isometry]] (the form is unimodular, so \(m\) is invertible over \(\widehat{\mathcal O}\)); let \(k\) be its image in the finite adelic group. Property 1 is clear from the formula for \(m\), and 2 follows by reducing \(e\) and \(\bar e\).

The last statement holds because reduction is entrywise.

## References

1. Lean: `New.Filling.exists_reduction_eq_of_invAdjoint` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
2. Lean: `New.Filling.exists_idempotent_reduceAt_eq_ite` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
3. Lean: `New.conjTranspose_one_add_smul_sub_one_mul_mul_eq` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
4. Lean: `New.Filling.reduction_apply_eq_one_apply` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
