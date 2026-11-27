+++
id = "proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one"
title = "The class cutoffs: translates sum to one, support in boxes"
kind = "proposition"
summary = "The translates of the cutoff of a class under the unipotent congruence subgroup add up to one; the cutoff is measurable and vanishes outside frame boxes; every point of the cut can be moved to a boxed point."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.tsum_classCutoff_eq_one", "New.Filling.measurable_classCutoff", "New.Filling.isBoxPartitionOfUnity_reducedIndicator", "New.Filling.IsBoxPartitionOfUnity.mem_frameBox", "New.Filling.mem_frameBox_of_classCutoff_ne_zero", "New.Filling.mem_boxedPoints_of_classCutoff_ne_zero", "New.Filling.exists_classUnipotent_mul_mem_boxedPoints", "New.Filling.exists_gramSchmidtMatrix_le"]
lean_files = ["src/New/Spanning/Unfolding/Packing.lean"]
proof_status = "full"
+++

**Proposition.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity and \(S\) [[?lean:New.Filling|filling data]] over \(E\) satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], with parameter \(b\) and \(n=\varrho+1\). For a [[?lean:New.Filling.Classes|class]] \(c\) let \(\beta_c:G_\infty\to[0,\infty]\) be the [[?lean:New.Filling.classCutoff|class cutoff]]: \(\beta_c=\beta\cdot\omega\), where \(\beta\) is a chosen measurable function with \(\sum_{u\in\mathsf U^0_c(M)}\beta(uy)=1\) for all \(y\), and \(\omega\) is the indicator of the points [[?lean:New.Filling.reducedPoints|reduced]] for a chosen [[?lean:New.Filling.IsResidueDomain|residue domain]] ([[?lean:New.Filling.reducedIndicator|reduced indicator]]). Then:

1. \(\beta_c\) is measurable.
2. For every \(y\in G_\infty\), \(\displaystyle\sum_{u\in\mathsf U_c(M)}\beta_c(u\,y)=1\).
3. If \(\beta_c(y)\ne0\), \(R\ge0\), and at a place \(v\) the [[?lean:New.besselLength|Bessel length]] of \(y_v\) is at most \(b^{6n+2}R\), then all frame vectors \(y_v^{-1}f_a\) have norm at most \(b^{37n}R\) (the [[?lean:New.Filling.frameBoxRadius|frame box radius]] times \(R\)).
4. If \(\beta_c(y)\ne0\) and every \(y_v\) is [[?lean:New.InCut|in the cut]] (Bessel length at most \(b^{6n+2}\)), then \(y\) is a [[?lean:New.Filling.boxedPoints|boxed point]].
5. If every \(y_v\) is in the cut, there is \(u\in\mathsf U_c(M)\) with \(u\,y\) a boxed point.
6. For every \(y\) there is \(u\in\mathsf U_c(M)\) such that all entries of the [[?lean:New.gramSchmidtMatrix|Gram–Schmidt matrices]] of the components of \(u\,y\) have absolute value at most \(b^{26}\).

## Proof

A residue domain exists under the standing hypotheses ([[?lean:New.Filling.exists_isResidueDomain|existence of a residue domain]]), so \(\omega\) is the indicator of the reduced points of an actual residue domain, and by the theorem on [[proofs/grh/spanning-unfolding-a/reduced-points-give-box-partition-of-unity|reduced points]] it is a partition of unity in boxes for every class.

1. \(\beta\) and \(\omega\) are measurable.

2. Apply the partition property (item 4 of that theorem) to the weight \(a(u)=\beta(u\,y)\): for every \(\gamma\), \(\sum_{u\in\mathsf U^0_c(M)}a(u\gamma)=\sum_u\beta(u\,(\gamma y))=1\). Hence \(\sum_{\gamma}\beta(\gamma y)\omega(\gamma y)=1\).

3. \(\beta_c(y)\ne0\) gives \(\omega(y)\ne0\), so the frame vectors of \(y_v\) have norm at most \(b^{27}\) times the Bessel length, hence at most \(b^{27+6n+2}R\le b^{37n}R\), because \(b\ge1\) and \(29+6n\le37n\).

4. \(\omega(y)\ne0\) means \(y\) is reduced; together with the cut condition this is the definition of a boxed point ([[?lean:New.Filling.mem_boxedPoints_of_reducedIndicator_ne_zero|boxed points from the reduced indicator]]).

5. By 2 some \(u\) has \(\beta_c(uy)\ne0\). Left translation by the image of a rational unipotent element, which lies in the Bessel subgroup at each place, does not change the Bessel length ([[?lean:New.besselLength_besselS_mul|invariance of the Bessel length]]), so \(uy\) is still in the cut, and 4 applies.

6. Take a residue domain \(D\) and, by the [[proofs/grh/spanning-unfolding-a/unique-coset-moving-a-point-to-a-reduced-point|unique coset theorem]], an element \(u_0\) with \(u_0y\) reduced for \(D\); the entries of the Gram–Schmidt matrices of reduced points are bounded by \(b^{26}\) ([[?lean:New.Filling.IsResidueDomain.norm_gramSchmidtMatrix_le|bound for reduced points]]).

## References

1. Lean: `New.Filling.tsum_classCutoff_eq_one` in `src/New/Spanning/Unfolding/Packing.lean`.
2. Lean: `New.Filling.measurable_classCutoff` in `src/New/Spanning/Unfolding/Packing.lean`.
3. Lean: `New.Filling.isBoxPartitionOfUnity_reducedIndicator` in `src/New/Spanning/Unfolding/Packing.lean`.
4. Lean: `New.Filling.IsBoxPartitionOfUnity.mem_frameBox` in `src/New/Spanning/Unfolding/Packing.lean`.
5. Lean: `New.Filling.mem_frameBox_of_classCutoff_ne_zero` in `src/New/Spanning/Unfolding/Packing.lean`.
6. Lean: `New.Filling.mem_boxedPoints_of_classCutoff_ne_zero` in `src/New/Spanning/Unfolding/Packing.lean`.
7. Lean: `New.Filling.exists_classUnipotent_mul_mem_boxedPoints` in `src/New/Spanning/Unfolding/Packing.lean`.
8. Lean: `New.Filling.exists_gramSchmidtMatrix_le` in `src/New/Spanning/Unfolding/Packing.lean`.
