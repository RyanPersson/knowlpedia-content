+++
id = "proofs/grh/spanning-unfolding-a/meet-norm-bounded-by-index-of-determinant"
title = "The meet norm is bounded by the index of a two-by-two determinant"
kind = "theorem"
summary = "For an integral k whose reduction agrees, the norm of the product of the places above M where the frame meets its image is at most the index of the determinant of the products of two integral vectors with the last vectors of the two frames."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.meetNorm_le_genIndex_det", "New.Filling.meetNorm_le_genIndex_star", "New.Filling.reduceAboveM_det_eq_zero_of_meetsAt", "New.Filling.le_genIndex_det_of_le_meetNorm", "New.Filling.lastIndices"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] over \(E\), and \(k\in K\) ([[?lean:New.Filling.latticeStabilizer|lattice stabiliser]]) with reduction \(\bar k\) that [[?lean:New.Filling.Agrees|agrees]]. Let \(t_1,t_2\) be two vectors of the finite adelic space with integral coordinates in the lattice basis, and let \(P\) be the \(2(\varrho+1)\times2\) matrix of the products \(h\)-adjoint pairing of the frame vectors \(f_a\) and of their images \(kf_a\) with \(t_1,t_2\); precisely \(P=(f\mid kf)^{*}\,t\), where \((f\mid kf)\) is the [[?lean:New.framePair|pair of frames]] and \(t=(t_1\mid t_2)\). Assume

- all rows of \(P\) vanish except the two belonging to the last vectors \(f_\varrho=z\) and \(kf_\varrho\);
- the determinant \(\Delta\) of these two rows is a unit of the [[catalog/arithmetic/adeles-number-field-finite|finite adeles]].

Then the [[proofs/grh/spanning-unfolding-a/meeting-places-and-meet-norm|meet norm]] of \(\bar k\) satisfies
\[
\operatorname{mn}(\bar k)\le\bigl[\widehat{\mathcal O}:\Delta\widehat{\mathcal O}\bigr],
\]
where the right side is the [[?lean:New.genIndex|index]] of \(\Delta\) (the inverse of its Haar modulus). Consequently any natural number \(x\le\operatorname{mn}(\bar k)\) is at most that index.

## Proof

Let \(Q=t^{*}(f\mid kf)\), an integral \(2\times2(\varrho+1)\) matrix with \(P=Q^{*}\); all its columns vanish except those of \(f_\varrho\) and \(kf_\varrho\), and with \(\delta\in\widehat{\mathcal O}\) the determinant of these two columns, \(\Delta=\bar\delta\).

*Vanishing at meeting places.* Let \(\bar k\) meet at a place \(p\) above \(M\). By the theorem on [[proofs/grh/spanning-unfolding-a/climbing-common-vectors-modulo-a-place|climbing modulo a place]], there are coordinates \(x,y\) over the [[algebra-commutative/residue-field|residue field]] with \(f\cdot x=\bar k[p]f\cdot y\) and \((x_\varrho,y_\varrho)\ne(0,0)\); and \(\bar k[p]\) is the matrix of \(k\) reduced at \(p\). Hence the reduction of \(Q\) at \(p\) kills the vector \((x,-y)\): \(\bar Q(x,-y)=\bar t^{*}(f\cdot x-\bar kf\cdot y)=0\). Only the two last columns of \(\bar Q\) are nonzero, so the reduced \(2\times2\) matrix kills \((x_\varrho,-y_\varrho)\ne0\), and \(\operatorname{red}_p(\delta)=0\).

*Counting.* Let \(A\) be the set of places above \(M\) where \(\bar k\) meets. By the lemma on [[proofs/grh/spanning-unfolding-a/prescribing-residues-above-the-level|prescribing residues]], the product of the reductions \(\widehat{\mathcal O}\to\prod_{p\in A}k_p\) is surjective, and by the previous paragraph its kernel contains \(\delta\widehat{\mathcal O}\). So \(\prod_{p\in A}\lvert k_p\rvert=\operatorname{mn}(\bar k)\) is at most \(\lvert\widehat{\mathcal O}/\delta\widehat{\mathcal O}\rvert\) (residue fields at places above \(p_i\) have \(p_i\) elements). Finally \(\lvert\widehat{\mathcal O}/\delta\widehat{\mathcal O}\rvert\) is the index of \(\bar\delta=\Delta\) ([[?lean:New.genIndex_eq_card|index as the order of a quotient]], applied to the integral element \(\delta\) whose conjugate is a unit of the finite adeles).

## References

1. Lean: `New.Filling.meetNorm_le_genIndex_det` in `src/New/Spanning/Unfolding/Climbing.lean`.
2. Lean: `New.Filling.meetNorm_le_genIndex_star` in `src/New/Spanning/Unfolding/Climbing.lean`.
3. Lean: `New.Filling.reduceAboveM_det_eq_zero_of_meetsAt` in `src/New/Spanning/Unfolding/Climbing.lean`.
4. Lean: `New.Filling.le_genIndex_det_of_le_meetNorm` in `src/New/Spanning/Unfolding/Climbing.lean`.
5. Lean: `New.Filling.lastIndices` in `src/New/Spanning/Unfolding/Climbing.lean`.
