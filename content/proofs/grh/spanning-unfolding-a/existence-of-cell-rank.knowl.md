+++
id = "proofs/grh/spanning-unfolding-a/existence-of-cell-rank"
title = "A term with agreeing characters and vanishing discriminant has a cell rank"
kind = "theorem"
summary = "If the characters of gamma agree and the term discriminant of gamma vanishes, then gamma has a cell rank j <= rho."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.CharsAgree.exists_hasCellRank", "New.Filling.CharsAgree.leadingMinor_ne_zero", "New.Filling.CharsAgree.exists_coords_ne_zero_of_common_vector"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), \(f=(f_0,\dots,f_\varrho)\) the frame and \(\gamma\) a rational [[?c:Isometry of a hermitian space|isometry]] whose characters [[?lean:New.Filling.CharsAgree|agree]]. Let \(Z(\gamma)=(h(f_a,\gamma f_b))\) be the [[?lean:New.Filling.frameProducts|matrix of frame products]], \(D_l\) its [[?lean:New.leadingMinor|leading minor]] of order \(l\), and \(\operatorname{disc}(\gamma)=D_{\varrho+1}\overline{D_{\varrho+1}}-N^2D_\varrho\overline{D_\varrho}\) the [[?lean:New.Filling.termDisc|term discriminant]]. Assume \(\operatorname{disc}(\gamma)=0\). Then \(\gamma\) has a [[?lean:New.Filling.HasCellRank|cell rank]] \(j\in\{0,\dots,\varrho+1\}\), that is:

- *(norm-one pair from \(j\) on; [[?lean:New.NormOnePairOccursFrom|definition]])* there is \(\zeta\in E\) with \(\zeta\bar\zeta=1\) such that for every index \(a\ge j\) the pair \((\zeta,1)\) [[?lean:New.PairOccursAt|occurs at \(a\)]] for \(f\) and \(\gamma f\);
- \(D_j\ne0\);
- \(j=\varrho+1\) if and only if \(\operatorname{disc}(\gamma)\ne0\); so here \(j\le\varrho\).

## Proof

For \(j=\varrho+1\) the norm-one pair condition is empty, so the set of \(j\) for which it holds is nonempty; let \(j\) be its least element.

**(a) A common vector has nonzero coordinates in both frames at some index \(\ge j\).** Let \(f\cdot x=\gamma f\cdot y\) with \(x\ne0\), and let \(l\) be the top index of \((x,y)\). By the theorem on [[proofs/grh/spanning-unfolding-a/climbing-common-vectors-over-the-field|climbing over the field]], \(x_l\bar x_l=y_l\bar y_l\ne0\), so \(x_l,y_l\ne0\). Dividing by \(y_l\), the pair \((\zeta,1)\), \(\zeta=x_l/y_l\), occurs at \(l\), hence at all higher indices, and \(\zeta\bar\zeta=1\). So the norm-one pair condition holds from \(l\) on, and \(j\le l\) by minimality.

**(b) \(j\le\varrho\).** The vanishing of the discriminant means that there are \(x\) and \(y\ne0\) with \(f\cdot x=\gamma f\cdot y\) ([[?lean:New.Filling.termDisc_eq_zero_iff_exists|vanishing of the term discriminant]]); then \(x\ne0\) because the vectors \(\gamma f_b\) are linearly independent. By (a) some index \(l\le\varrho\) has \(j\le l\).

**(c) \(D_j\ne0\).** Suppose \(D_j=0\). Then there is \(y\ne0\) with \(y_a=0\) for \(a\ge j\) and \((Z(\gamma)y)_a=0\) for \(a<j\) (the matrix consisting of the first \(j\) rows of \(Z(\gamma)\) completed by rows of the identity has determinant \(D_j\); [[?lean:New.Filling.det_paddedLeading|determinant of the padded leading block]]). We claim \(Z(\gamma)y=0\).

The norm-one pair condition from \(j\) on also holds for \(\gamma^{-1}\): if \(f\cdot x=\gamma f\cdot y'\) with coefficients \((\zeta,1)\) at \(a\), then \(f\cdot(\bar\zeta y')=\gamma^{-1}f\cdot(\bar\zeta x)\) has coefficients \((\bar\zeta,1)\) at \(a\). This condition implies that the upper coordinates of common vectors may be prescribed ([[?lean:New.Filling.exists_frameImage_eq_of_normOnePairOccursFrom|common vectors with prescribed upper coordinates]]): for every \(w\in E^{\varrho+1}\) there are \(X,Y\) with
\[
f\cdot Y=\gamma^{-1}f\cdot X,\quad\text{i.e.}\quad\gamma f\cdot Y=f\cdot X,\qquad X_a=\overline{w_a}\ \text{ for } a\ge j .
\]
Then, \(\gamma\) being an isometry and the only nonzero product among frame vectors being \(h(z,z)=-N\),
\[
\sum_a\overline{X_a}\,(Z(\gamma)y)_a=h(f\cdot X,\gamma f\cdot y)=h(\gamma f\cdot Y,\gamma f\cdot y)=h(f\cdot Y,f\cdot y)=-N\,\overline{Y_\varrho}\,y_\varrho=0,
\]
because \(y_\varrho=0\) (as \(j\le\varrho\)); this is [[?lean:New.Filling.frameProducts_mulVec_of_frameImage_eq|frame products of a common vector]]. On the left the terms with \(a<j\) vanish and for \(a\ge j\) the coefficient is \(w_a\). As \(w\) is arbitrary, \((Z(\gamma)y)_a=0\) for \(a\ge j\) as well, so \(Z(\gamma)y=0\).

So \(\gamma f\cdot y\) is orthogonal to the whole frame, and therefore lies in the span of the frame ([[?lean:New.Filling.exists_frameImage_eq_of_frameProducts_mulVec_eq_zero|vectors orthogonal to the frame]]): \(f\cdot x=\gamma f\cdot y\) for some \(x\), and \(x\ne0\) since \(y\ne0\). By (a) there is \(l\ge j\) with \(y_l\ne0\), contradicting \(y_a=0\) for \(a\ge j\).

**(d)** With (b), \(j\le\varrho\) and \(\operatorname{disc}(\gamma)=0\), so the third condition holds.

## References

1. Lean: `New.Filling.CharsAgree.exists_hasCellRank` in `src/New/Spanning/Unfolding/Climbing.lean`.
2. Lean: `New.Filling.CharsAgree.leadingMinor_ne_zero` in `src/New/Spanning/Unfolding/Climbing.lean`.
3. Lean: `New.Filling.CharsAgree.exists_coords_ne_zero_of_common_vector` in `src/New/Spanning/Unfolding/Climbing.lean`.
