+++
id = "proofs/grh/spanning-unfolding-a/unitary-group-of-x0-in-lattice-basis"
title = "Integrality and reduction of U(X_0) in the lattice basis"
kind = "proposition"
summary = "The image of k in U(X_0)(A_f) in the big group is integral iff k is integral with row k_0 congruent to that of 1 modulo pi; its reduction at a chosen place is trivial iff that of k is."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.inclHFin_mem_latticeStabilizer_iff", "New.Filling.mem_congruenceGL_iff_isIntMatrix_scaleAt", "New.Filling.reduction_inclHFin_eq_one_iff", "New.Filling.mem_latticeStabilizer_iff_isIntMatrix_sub_one", "New.Filling.inclHFin_sub_one_eq", "New.Filling.isIntMatrix_middleInclusionMatrix_mul_iff", "New.Filling.classSum_sourceLevel_eq_sum", "New.Filling.card_resField_eq_levelPrime"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
proof_status = "full"
+++

**Proposition.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), with the integral [[?c:Idele group|finite idele]] \(\pi\) (\(\pi\bar\pi=N\); at each finite place \(\pi\) or \(\bar\pi\) is a unit), and let \(k\) be a finite adelic point of \(U(X_0)\), a unitary matrix for the standard form with rows and columns indexed by \(\kappa\); \(k_0\in\kappa\) is the distinguished index. Let \(\iota(k)\) be its image in the finite adelic unitary group of \(V\), written in the lattice basis ([[?lean:New.Filling.inclHFin|inclusion of \(U(X_0)\)]]), and \(K\) the [[?lean:New.Filling.latticeStabilizer|lattice stabiliser]].

1. **(General criterion.)** Let \(p\) be an integral finite idele such that at each finite place \(p\) or \(\bar p\) is a unit, and \(o\) an index. A finite adelic unitary matrix \(k\) is integral with row \(o\) congruent to that of \(1\) modulo \(p\) if and only if the matrix obtained from \(k-1\) by dividing its row \(o\) by \(p\) and its column \(o\) by \(\bar p\) is integral.
2. An [[?c:Isometry of a hermitian space|isometry]] \(x\) of \(V\) (finite adelic, lattice basis) lies in \(K\) if and only if \(x-1\) has entries in \(\widehat{\mathcal O}\).
3. \(\iota(k)\in K\) if and only if \(k\) is integral and its row \(k_0\) is congruent to that of \(1\) modulo \(\pi\) ([[?lean:New.congruenceGL|congruence subgroup]] for the row \(k_0\)).
4. If \(\iota(k)\in K\), then for every chosen place \(w\) (above \(p_0\) or \(p_1\)), the reduction of \(\iota(k)\) modulo \(w\) is \(1\) if and only if the reduction of \(k\) modulo \(w\) is \(1\).
5. The [[algebra-commutative/residue-field|residue field]] at a chosen place above \(p_i\) has \(p_i\) elements; and for the [[?lean:New.Filling.sourceLevel|source level]], whose stabilisers are trivial, the class sum of a function is its plain sum over the [[?lean:New.Filling.Classes|classes]].

## Proof

*1.* Let \(A=k-1\). If \(k\) is integral with row \(o\) of \(A\) divisible by \(p\), then, as \(k^{-1}=k^{*}\) lies in the same group, row \(o\) of \(A^{*}\) is divisible by \(p\), i.e. column \(o\) of \(A\) is divisible by \(\bar p\). All entries of \(A\) are integral. The corner entry \((o,o)\) is divided by \(p\bar p\); at each place one of the two is a unit, so integrality follows from the row statement or the column statement at that place. Conversely, multiplying the scaled matrix by the integral diagonal matrices with \(\bar p\), resp. \(p\), at \(o\) shows that \(p^{-1}\cdot\)(row \(o\) of \(A\)) and \(A\) are integral.

*2.* If \(x\in K\), \(x-1\) is integral. Conversely the form in the lattice basis is unimodular ([[?lean:New.Filling.isUnimodular_latticeMiddle|unimodularity of the lattice form]]), so an isometry with \(x-1\) integral has integral inverse \(J^{-1}x^{*}J\) ([[?lean:New.IsUnimodular.mem_unitaryLevel|membership in the unitary level]] with level \(1\)).

*3.* In the lattice basis, \(\iota(k)-1\) vanishes outside the block with rows \(\kappa\cup\{z\}\) and columns \(\kappa\), where it equals \(B\cdot\bigl((k-1)D\bigr)\): here \(D\) is the diagonal matrix dividing column \(k_0\) by \(\bar\pi\), and \(B\) ([[?lean:New.middleInclusionMatrix|middle inclusion matrix]]) expresses the orthonormal basis of \(X_0\) in the lattice basis of \(X_0\oplus Ez\); \(B\,l\) has the rows of \(l\) outside \(k_0\), the row \(k_0\) times \(\bar\pi\), and the row \(k_0\) times \(-\pi^{-1}\). Since \(\pi,\bar\pi\) are integral, \(B\,l\) is integral if and only if \(l\) is integral and its row \(k_0\) is divisible by \(\pi\), i.e. if and only if \(l\) stays integral after dividing its row \(k_0\) by \(\pi\). With \(l=(k-1)D\), 2 and 1 (for \(p=\pi\), \(o=k_0\)) give the claim.

*4.* Each side says that all entries of the matrix minus \(1\) are non-units at \(w\). A chosen place has norm \(p_i\ne N\), so \(\pi\) and \(\bar\pi\) are units at \(w\) and the scalings in the formula of 3 do not change valuations at \(w\); the additional row of \(B\) repeats the condition on the row \(k_0\).

*5.* The first claim is the definition of the norm of the chosen places; the second holds because the weights of a class sum are the inverse orders of the stabilisers ([[?lean:New.classSum|class sum]]), which are \(1\) here.

## References

1. Lean: `New.Filling.inclHFin_mem_latticeStabilizer_iff` in `src/New/Spanning/Unfolding/Climbing.lean`.
2. Lean: `New.Filling.mem_congruenceGL_iff_isIntMatrix_scaleAt` in `src/New/Spanning/Unfolding/Climbing.lean`.
3. Lean: `New.Filling.reduction_inclHFin_eq_one_iff` in `src/New/Spanning/Unfolding/Climbing.lean`.
4. Lean: `New.Filling.mem_latticeStabilizer_iff_isIntMatrix_sub_one` in `src/New/Spanning/Unfolding/Climbing.lean`.
5. Lean: `New.Filling.inclHFin_sub_one_eq` in `src/New/Spanning/Unfolding/Climbing.lean`.
6. Lean: `New.Filling.isIntMatrix_middleInclusionMatrix_mul_iff` in `src/New/Spanning/Unfolding/Climbing.lean`.
7. Lean: `New.Filling.classSum_sourceLevel_eq_sum` in `src/New/Spanning/Unfolding/Climbing.lean`.
8. Lean: `New.Filling.card_resField_eq_levelPrime` in `src/New/Spanning/Unfolding/Climbing.lean`.
