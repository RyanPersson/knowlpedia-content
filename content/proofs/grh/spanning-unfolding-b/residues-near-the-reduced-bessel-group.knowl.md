+++
id = "proofs/grh/spanning-unfolding-b/residues-near-the-reduced-bessel-group"
title = "Residues that agree with the reduced Bessel group above one level prime"
kind = "lemma"
summary = "Residues in a scalar coset of the reduced Bessel group are not open; residues agreeing with the reduced Bessel group above one level prime meet at all those places and avoid the nontrivial scalar cosets."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.avoidsScalarCosets_setOf_exists_apply_eq", "New.Filling.InScalarCoset.not_isOpenElement", "New.Filling.meetsAt_of_eq_of_mem_reducedImage", "New.Filling.prod_levelPrime_le_meetNorm_of_eq", "New.Filling.eq_one_of_reduceAt_scalar_eq_one", "New.Filling.AvoidsScalarCosets.not_normOnePairOccursFrom_zero", "New.Filling.apply_besselFrame_zero_of_mem_besselS", "New.Filling.apply_besselFrame_zero_of_mem_reducedImage", "New.Filling.inScalarCoset_one", "New.leadingMinor_frameGram_eq_zero"]
lean_files = ["src/New/Spanning/Unfolding/SquareExpansion.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\bar R_0\subset\bar G\) the reduced image of the Bessel subgroup, and \(i\in\{0,1\}\).

1. Every \(t\in\bar R_0\) fixes the first frame vector modulo every chosen place: the column of \(t_w\) at \(f_0=e_0\) is that of the identity.
2. If \(s\) lies in a [[proofs/grh/spanning-unfolding-b/avoiding-scalar-cosets|scalar coset]] \(\zeta\bar R_0\), then \(s\) is not [[?lean:New.Filling.IsOpenElement|open]].
3. If \(s_w=t_w\) for all \(w\in C_i\), for some \(t\in\bar R_0\), then \(s\) [[?lean:New.Filling.MeetsAt|meets]] at every \(w\in C_i\) and at its conjugate; consequently \(p_i^{2f}\le\operatorname{meet}(s)\), the [[?lean:New.Filling.meetNorm|meet norm]] of \(s\).
4. Suppose \(E\) contains a primitive \(5040\)-th root of unity and \(S\) is [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]]. If \(\zeta\in E\) is integral, \(\zeta\bar\zeta=1\), and \(\zeta\equiv1\) modulo every \(w\in C_i\), then \(\zeta=1\). Hence the set
\[
\Omega_i=\{s\in\bar G:\ \exists\,t\in\bar R_0,\ s_w=t_w\ \text{for all }w\in C_i\}
\]
avoids the scalar cosets.
5. If \(\Omega\) avoids the scalar cosets, \(s\in\Omega\), and \(\gamma\notin\mathsf{S}(E)\) is a term over \((c,s,c')\), then no norm-one pair occurs from \(0\) for \(\gamma\).

## Proof

(1) An integral element \(k\) of the Bessel subgroup has the column of the identity at \(f_0\) (all rows have level \(\ge0\)); reduce modulo \(w\).

(2) By (1), in the column of \(s_w=(\zeta\bmod w)t_w\) at \(e_0\) all entries off the diagonal vanish. As \(\varrho>0\), \(e_0\) is orthogonal to every frame vector, so the first column of the matrix of frame products \(\bigl(h(f_a,s_wf_b)\bigr)\) is zero, and all its leading minors of positive order vanish. Openness requires the minor of order \(1\) to be nonzero at some \(w\in C_0\) (\(1<n\) as \(\varrho\ge10^5\)).

(3) At a place \(w\in C_i\) or its conjugate, the action of \(s\) is that of \(t=\bar k\) with \(k\in K\cap\mathsf{S}\), namely the reduction of \(k\) by \(r\mapsto r\bmod w\) or \(r\mapsto\bar r\bmod w\) ([[proofs/grh/spanning-unfolding-b/principal-level-is-congruence-subgroup|reduction at the conjugate]]). In both cases the column at \(f_0\) is that of the identity by (1), so \(f_0\) is a nonzero vector common to the span of the frame and its image. There are \(2f\) such pairs (place, conjugation), each contributing a factor \(p_i\) to the meet norm.

(4) Regard \(\zeta\) as a rational point of the unitary group of the standard form of rank one; it is integral and reduces to \(1\) at all \(w\in C_i\), so it is \(1\) by [[proofs/grh/spanning-unfolding-b/freeness-in-small-rank|freeness in small rank]] (\(1\le k\)). Now let \(s\in\Omega_i\), with \(s_w=t_w\), and suppose \(s_w=(\zeta\bmod w)t'_w\) with \(t'\in\bar R_0\). Comparing the \((f_0,f_0)\) entries with (1): \(1=\zeta\bmod w\) for all \(w\in C_i\), so \(\zeta=1\).

(5) By [[proofs/grh/spanning-unfolding-b/terms-of-cell-rank-zero-are-scalar-multiples-of-the-bessel-subgroup|the theorem on norm-one pairs from index zero]], \(\gamma=\zeta\gamma_0\) with \(\gamma_0\in\mathsf{S}(E)\) and \(s\in\zeta\bar R_0\); since \(\Omega\) avoids the scalar cosets, \(\zeta=1\), so \(\gamma\in\mathsf{S}(E)\), a contradiction.

## References

1. Lean: `New.Filling.avoidsScalarCosets_setOf_exists_apply_eq`, `New.Filling.InScalarCoset.not_isOpenElement`, `New.Filling.meetsAt_of_eq_of_mem_reducedImage`, `New.Filling.prod_levelPrime_le_meetNorm_of_eq`, `New.Filling.eq_one_of_reduceAt_scalar_eq_one`, `New.Filling.AvoidsScalarCosets.not_normOnePairOccursFrom_zero` in `src/New/Spanning/Unfolding/SquareExpansion.lean`.
