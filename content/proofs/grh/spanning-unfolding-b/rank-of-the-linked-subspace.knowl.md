+++
id = "proofs/grh/spanning-unfolding-b/rank-of-the-linked-subspace"
title = "Rank of the linked subspace"
kind = "theorem"
summary = "The linked subspace of X0 is a hyperplane when the discriminant is nonzero, and all of X0 when the discriminant vanishes and the term has a cell rank."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.finrank_linkedX₀_add_one", "New.Filling.HasCellRank.linkedX₀_eq_top", "New.Filling.CharsAgree.linkedX₀_eq_top", "New.Filling.HasCellRank.finrank_linkedX₀_add_sub", "New.Filling.disjoint_colSpan_frameImage", "New.Filling.commonIsotropic_eq_bot", "New.Filling.finrank_frameSum_of_termDisc_ne_zero", "New.Filling.inv_mulVec_z_eq_of_pairOccursAt", "New.Filling.HasCellRank.le_of_termDisc_eq_zero"]
lean_files = ["src/New/Spanning/Unfolding/TermStructure.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) and \(\gamma\in G(E)\), with [[proofs/grh/spanning-unfolding-b/spaces-of-the-two-frames|linked subspace]] \(X_0^\gamma\subset X_0\).

1. If \(\operatorname{disc}(\gamma)\ne0\), then \(A^+\cap\gamma A^+=0\), \(A\cap\gamma A=0\), and \(\dim X_0^\gamma=k-1\).
2. If \(\gamma\) has [[proofs/grh/spanning-unfolding-b/cell-rank-of-a-term|cell rank]] \(j\) and \(\operatorname{disc}(\gamma)=0\), then \(j\le\varrho\) and \(X_0^\gamma=X_0\).
3. If \(\gamma\) has cell rank \(j\), then \(\dim X_0^\gamma+\max(j-\varrho,0)=k\).
4. If \(E\) contains a primitive \(5040\)-th root of unity, the [[proofs/grh/spanning-unfolding-b/characters-agree|characters agree]] at \(\gamma\) and \(\operatorname{disc}(\gamma)=0\), then \(X_0^\gamma=X_0\).

## Proof

(1) \(A^+\cap\gamma A^+=0\) is [[proofs/grh/spanning-unfolding-b/vanishing-of-the-term-discriminant|the criterion for the vanishing of the discriminant]]; \(A\cap\gamma A\) is contained in it. Both \(A^+\) and \(\gamma A^+\) have dimension \(n=\varrho+1\), so \(\dim A^+_\gamma=2n\) and, by [[proofs/grh/spanning-unfolding-b/frame-complement-and-linked-subspace|the theorem on the frame complement]], \(\dim X_0^\gamma=\dim(A^+_\gamma)^\perp-0=r-2n=k-1\).

(2) By the third condition of the cell rank, \(j=\varrho+1\) would force \(\operatorname{disc}(\gamma)\ne0\); so \(j\le\varrho\), and a pair \((\zeta,1)\) with \(\zeta\bar\zeta=1\) occurs at the top index \(\varrho\): there are \(x,x'\) with \(f\cdot x=\gamma f\cdot x'\), \(x_\varrho=\zeta\), \(x'_\varrho=1\). For every \(y\in(A+\gamma A)^\perp\), pairing \(y\) with this vector in two ways gives
\[
-N\bar\zeta\,y_z=h(f\cdot x,y)=h(\gamma f\cdot x',y)=h(f\cdot x',\gamma^{-1}y)=-N(\gamma^{-1}y)_z ,
\]
because the \(e^*\)-coordinates of \(y\) and \(\gamma^{-1}y\) vanish. So \((\gamma^{-1}y)_z=\bar\zeta\,y_z\). Now let \(v\in X_0\) and choose \(y\in(A+\gamma A)^\perp\) with \(y_0=v\), \((\gamma^{-1}y)_z=0\), so that the \(z^+\)-coordinate of \(\Upsilon_\gamma v\) is \(y_z\) (as in the proof of the theorem on the frame complement). Then \(\bar\zeta y_z=0\) and \(\bar\zeta\ne0\), so \(y_z=0\) and \(v\in X_0^\gamma\).

(3) If \(\operatorname{disc}(\gamma)=0\), use (2). Otherwise \(j=\varrho+1\) and (1) applies.

(4) Under these hypotheses \(\gamma\) has a cell rank ([[?lean:New.Filling.CharsAgree.exists_hasCellRank|existence of the cell rank]]); apply (2).

## References

1. Lean: `New.Filling.finrank_linkedX₀_add_one`, `New.Filling.HasCellRank.linkedX₀_eq_top`, `New.Filling.CharsAgree.linkedX₀_eq_top`, `New.Filling.HasCellRank.finrank_linkedX₀_add_sub`, `New.Filling.disjoint_colSpan_frameImage` in `src/New/Spanning/Unfolding/TermStructure.lean`.
