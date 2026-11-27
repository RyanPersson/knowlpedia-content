+++
id = "proofs/grh/spanning-unfolding-a/fundamental-box-for-arithmetic-unipotent-group"
title = "A fundamental box for the arithmetic unipotent group in row coordinates"
kind = "proposition"
summary = "Each coset u Gamma of the image of the unipotent congruence subgroup has exactly one point whose row coordinates lie in a box of fundamental domains, of total volume the unipotent covolume."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_box_existsUnique_rowCoords_mem", "New.Filling.unipotentCovolume_eq_prod"]
lean_files = ["src/New/Spanning/Unfolding/CutoffIntegral.lean"]
proof_status = "full"
+++

**Proposition.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity with \(f\) [[?c:Infinite place of a number field|infinite places]], \(S\) [[?lean:New.Filling|filling data]] satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], \(c\) a class and \(\Gamma_c\subseteq\mathsf U_\infty\) the image of \(\mathsf U_c(M)\). There are measurable sets \(F_a\subseteq\mathbb C^{\mathcal F_a\times\{v\}}\) and \(F'_a\subseteq\mathbb R^{\{v\}}\) (\(a=1,\dots,\varrho\)) such that:

1. for every \(u\in\mathsf U_\infty\) there is exactly one \(\gamma\in\Gamma_c\) such that the [[proofs/grh/spanning-unfolding-a/row-coordinates-of-real-unipotent-group|row coordinates]] of \(u\gamma\) lie in \(\prod_aF_a\times\prod_aF'_a\);
2. \(\prod_a\operatorname{vol}(F_a)\cdot\prod_a\operatorname{vol}(F'_a)\) equals the [[?lean:New.Filling.unipotentCovolume|unipotent covolume]]
\[
\operatorname{cov}_{\mathsf U}=\Bigl(\frac{M^{2d+\varrho}}{N^{k}}\Bigr)^{f}\frac{\lvert\operatorname{disc}E\rvert^{\varrho/4}}{\operatorname{vol}(\widehat{\mathcal O})^{d}\,\Lambda},\qquad d=\sum_{a=0}^{\varrho-1}(2a+k+1),
\]
where \(\Lambda=\prod_v\prod_{a=0}^{\varrho}\lambda_v(a)^{k+2(\varrho-a)}\) and \(\lambda_v(a)=\kappa_v^{2(\varrho-a)}/N\) ([[?lean:New.Filling.frameScaleProd|product of frame scales]]). In particular it does not depend on \(c\).

## Proof

Take for \(F_a\) and \(F'_a\) the fundamental domains of the free lattice \(L_a\) and of the imaginary lattice \(L'_a\) from the proposition on the [[proofs/grh/spanning-unfolding-a/lattices-of-unipotent-row-coordinates|lattices of row coordinates]].

*1.* Regard the row coordinates as a family of \(2\varrho\) injective coordinates on the group \(\mathsf U_\infty\) (vanishing at \(1\)), the free block of the row \(e_a\) with degree \(2(\varrho-1-a)\) and the imaginary block of the row \(e_a\) with degree \(2(\varrho-1-a)+1\) (rows counted from \(0\)): the last rows come first, and within a row the free entries come before the imaginary part. We verify the hypotheses of the general statement on a [[?lean:New.Filling.existsUnique_mul_mem_box|unique translate into a box]] (see also its special case, [[proofs/grh/spanning-unfolding-a/reduction-of-unitriangular-matrices|reduction of unitriangular matrices]]) for the subgroup \(\Gamma_c\), the lattices \(L_a,L'_a\) and the domains \(F_a,F'_a\).

- *Triangular translation.* If the coordinates of \(\gamma\) of degree below that of the free block of the row \(e_a\) vanish, i.e. all coordinates in rows \(d>a\), then the free entries of the row \(e_a\) of \(x\gamma\) are those of \(\gamma\) plus those of \(x\). If moreover the free entries of the row \(e_a\) of \(\gamma\) vanish, then the \((e_a,e_a^{*})\) entry of \(x\gamma\) is the sum of those of \(\gamma\) and \(x\), in particular for imaginary parts. Both are the lemma on [[proofs/grh/spanning-unfolding-a/additivity-of-unipotent-row-entries|additivity of row entries]].
- *Values in the lattices.* The free entries of the row \(e_a\) of any \(\gamma\in\Gamma_c\) lie in \(L_a\); and if the coordinates of lower degree vanish, the additivity just proved (at one place) shows that the imaginary coordinates of the row \(e_a\) lie in \(L'_a\).
- *Attainment.* Every \(l\in L_a\) (respectively \(L'_a\)) is the corresponding coordinate of some \(\gamma\in\Gamma_c\) whose other coordinates of degree at most that of the block vanish.

All three are parts (ii), (iii) of the proposition on lattices. The general statement then gives 1.

*2.* By that proposition \(\operatorname{vol}(F_a)=\bigl((\prod_vM^2/\lambda_v(a))/\operatorname{vol}(\widehat{\mathcal O})\bigr)^{n_a}\) with \(n_a=2(\varrho-1-a)+k+1\), and \(\operatorname{vol}(F'_a)=\prod_v\lvert M/\lambda_v(a)\rvert\cdot\lvert\operatorname{disc}E\rvert^{1/4}\). Multiply over \(a=0,\dots,\varrho-1\): \(\sum_an_a=d\), so the powers of \(M\) give \(M^{f(2d+\varrho)}\), the volume factor gives \(\operatorname{vol}(\widehat{\mathcal O})^{-d}\), the discriminant gives \(\lvert\operatorname{disc}E\rvert^{\varrho/4}\), and \(\lambda_v(a)\) occurs to the power \(-(n_a+1)=-(k+2(\varrho-a))\). In \(\Lambda\) the remaining factor \(a=\varrho\) is \(\lambda_v(\varrho)^{k}=N^{-k}\) at each place, which accounts for \(N^{-kf}\) in the formula. Hence the product is \(\operatorname{cov}_{\mathsf U}\).

## References

1. Lean: `New.Filling.exists_box_existsUnique_rowCoords_mem` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
2. Lean: `New.Filling.unipotentCovolume_eq_prod` in `src/New/Spanning/Unfolding/CutoffIntegral.lean`.
