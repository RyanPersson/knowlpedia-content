+++
id = "proofs/grh/spanning-unfolding-a/reduced-points-give-box-partition-of-unity"
title = "The indicator of the reduced points is a partition of unity in boxes"
kind = "theorem"
summary = "Under the standing hypotheses the indicator of the reduced points for a residue domain is measurable, invariant under the fixer of the frame, supported in boxes, and its translates under the unipotent congruence subgroup sum to one."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.IsResidueDomain.isBoxPartitionOfUnity"]
lean_files = ["src/New/Spanning/Unfolding/ReducedPoints.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, let \(S\) be [[?lean:New.Filling|filling data]] over \(E\) satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], let \(D\) be a [[?lean:New.Filling.IsResidueDomain|residue domain]] and \(c\) a [[?lean:New.Filling.Classes|class]]. Let \(\omega:G_\infty\to\{0,1\}\) be the indicator function of the set of points [[?lean:New.Filling.reducedPoints|reduced]] for \(D\). Then \(\omega\) is a [[?lean:New.Filling.IsBoxPartitionOfUnity|partition of unity in boxes]] for \(c\), that is:

1. \(\omega\) is measurable and \(\omega\le1\);
2. if \(\omega(y)\ne0\) then for every [[?c:Infinite place of a number field|infinite place]] \(v\) the frame vectors of \(y_v\) have norm at most \(b^{27}\) times the [[?lean:New.besselLength|Bessel length]] of \(y_v\) (that is, \(y_v\) lies in the [[?lean:New.frameBox|frame box]] of that radius);
3. \(\omega(s\,y)=\omega(y)\) whenever every component \(s_v\) lies in the [[?lean:New.Shape.Form.besselFixer|fixer of the frame]];
4. for every \(y\in G_\infty\) and every weight \(a:\mathsf U_c(M)\to[0,\infty]\) such that \(\sum_{u\in\mathsf U^0_c(M)}a(u\gamma)=1\) for all \(\gamma\in\mathsf U_c(M)\),
\[
\sum_{\gamma\in\mathsf U_c(M)}a(\gamma)\,\omega(\gamma\,y)=1 .
\]

## Proof

1. The set of reduced points is measurable ([[?lean:New.Filling.IsResidueDomain.measurableSet_reducedPoints|measurability of the reduced points]]), and an indicator is at most one.

2. This is the bound for reduced points, [[?lean:New.Filling.IsResidueDomain.mem_frameBox|reduced points lie in frame boxes]], which uses the standing hypotheses and the bound \(b^{26}\) on \(D\).

3. The set of reduced points is invariant under left multiplication by tuples in the fixer of the frame ([[?lean:New.Filling.mul_mem_reducedPoints_iff|invariance of the reduced points]]).

4. By the theorem on the [[proofs/grh/spanning-unfolding-a/unique-coset-moving-a-point-to-a-reduced-point|unique coset]], there is \(\gamma_0\) such that \(\gamma y\) is reduced exactly for \(\gamma\in\mathsf U^0_c(M)\gamma_0\). The map \(u\mapsto u\gamma_0\) is injective on \(\mathsf U^0_c(M)\), and the summand \(a(\gamma)\omega(\gamma y)\) vanishes off its image, on which \(\omega(\gamma y)=1\). Hence the sum equals \(\sum_{u\in\mathsf U^0_c(M)}a(u\gamma_0)=1\).

## References

1. Lean: `New.Filling.IsResidueDomain.isBoxPartitionOfUnity` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
