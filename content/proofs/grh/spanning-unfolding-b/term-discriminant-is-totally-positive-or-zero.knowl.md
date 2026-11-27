+++
id = "proofs/grh/spanning-unfolding-b/term-discriminant-is-totally-positive-or-zero"
title = "The discriminant of a term is totally positive or zero"
kind = "theorem"
summary = "At every infinite place the discriminant of a rational isometry is real and nonnegative; it is either totally positive, with invertible frame products, or zero."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.termDisc_pos_or_eq_zero", "New.Filling.map_termDisc_eq_norm", "New.Filling.hasCellRank_last"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] and \(\gamma\in G(E)\), with [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|frame products \(Z=Z(\gamma)\), leading minors \(D_l\)]] and discriminant \(\operatorname{disc}(\gamma)=D_{\varrho+1}\overline{D_{\varrho+1}}-N^2D_\varrho\overline{D_\varrho}\).

1. For every infinite place \(v\), \(\Phi_v(\operatorname{disc}(\gamma))=\lvert\Phi_v(\operatorname{disc}(\gamma))\rvert\): it is real and \(\ge0\).
2. Either \(\Phi_v(\operatorname{disc}(\gamma))>0\) for all \(v\) and \(\det Z(\gamma)\ne0\), or \(\operatorname{disc}(\gamma)=0\).
3. If \(\operatorname{disc}(\gamma)\ne0\), then \(\gamma\) has [[proofs/grh/spanning-unfolding-b/cell-rank-of-a-term|cell rank]] \(\varrho+1\).

## Proof

(1) By Cramer's rule ([[?lean:New.exists_mulVec_eq_single_det|last column of the adjugate]]) there is \(y\in E^{\varrho+1}\) with \(Zy=(0,\dots,0,\det Z)\) and \(y_\varrho=D_\varrho\). By [[proofs/grh/spanning-unfolding-b/norm-identity-for-combinations-of-the-moved-frame|the norm identity]] with \(D=\det Z=D_{\varrho+1}\) and \(t=\gamma f\cdot y\),
\[
\Phi_v(\operatorname{disc}(\gamma))=\lvert\Phi_v(D_{\varrho+1})\rvert^2-N^2\lvert\Phi_v(D_\varrho)\rvert^2=N\sum_{i\in\kappa}\lvert\Phi_v(t_{x_i})\rvert^2\ \ge0 .
\]

(3) Assume \(\operatorname{disc}(\gamma)\ne0\). The condition on norm-one pairs from \(\varrho+1\) is empty (take \(c=1\)). If \(\det Z=0\), then \(\Phi_v(\operatorname{disc}(\gamma))=-N^2\lvert\Phi_v(D_\varrho)\rvert^2\le0\), and with (1) it is \(0\), contradicting \(\operatorname{disc}(\gamma)\ne0\) since \(\Phi_v\) is injective. So \(D_{\varrho+1}\ne0\), and the third condition of cell rank \(\varrho+1\) holds by assumption.

(2) If \(\operatorname{disc}(\gamma)\ne0\), then \(\Phi_v(\operatorname{disc}(\gamma))\ne0\) for every \(v\), hence \(>0\) by (1), and \(\det Z\ne0\) by (3).

## References

1. Lean: `New.Filling.termDisc_pos_or_eq_zero`, `New.Filling.map_termDisc_eq_norm`, `New.Filling.hasCellRank_last` in `src/New/Spanning/Unfolding/Terms.lean`.
