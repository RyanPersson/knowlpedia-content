+++
id = "proofs/grh/spanning-unfolding-b/vanishing-of-the-term-discriminant"
title = "The discriminant vanishes exactly when the two frames share a vector"
kind = "theorem"
summary = "The discriminant of a rational isometry is zero if and only if the span of the frame and the span of its image have a nonzero intersection."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.termDisc_eq_zero_iff", "New.Filling.termDisc_eq_zero_iff_exists", "New.Filling.frameImage_mulVec_eq_zero_iff"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) and \(\gamma\in G(E)\) with [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|discriminant]] \(\operatorname{disc}(\gamma)\). The following are equivalent:

1. \(\operatorname{disc}(\gamma)=0\);
2. there are \(x,y\in E^{\varrho+1}\) with \(y\ne0\) and \(f\cdot x=\gamma f\cdot y\);
3. \(\langle f_0,\dots,f_\varrho\rangle\cap\langle\gamma f_0,\dots,\gamma f_\varrho\rangle\ne0\).

## Proof

(2)\(\Leftrightarrow\)(3): the vectors \(\gamma f_0,\dots,\gamma f_\varrho\) are linearly independent, since \(\gamma\) is invertible and the frame vectors are distinct basis vectors; so \(\gamma f\cdot y\ne0\) if and only if \(y\ne0\).

(1)\(\Leftrightarrow\)(2): let \(Z=Z(\gamma)\).

*Case \(\det Z=0\).* Then \(\operatorname{disc}(\gamma)=0\) by [[proofs/grh/spanning-unfolding-b/term-discriminant-is-totally-positive-or-zero|the dichotomy for the discriminant]]. And there is \(y\ne0\) with \(Zy=0\); by [[proofs/grh/spanning-unfolding-b/link-isometry-on-the-moved-frame|part 4 of the theorem on the moved frame]], \(\gamma f\cdot y=f\cdot x\) for some \(x\). So both (1) and (2) hold.

*Case \(\det Z\ne0\).* By Cramer's rule there is \(c\) with \(Zc=(0,\dots,0,\det Z)\) and \(c_\varrho=D_\varrho\) ([[?lean:New.exists_mulVec_eq_single_det|last column of the adjugate]]). With \(y_0\) the \(X_0\)-part of \(\gamma f\cdot c\), part 2 of the same theorem gives \(\operatorname{disc}(\gamma)=N\langle y_0,y_0\rangle\). Since \(N\ne0\) and the form on \(X_0\) is anisotropic, \(\operatorname{disc}(\gamma)=0\) if and only if \(y_0=0\), if and only if \(\gamma f\cdot c\) is a combination of the frame (part 3). If so, (2) holds with \(y=c\ne0\) (as \(Zc\ne0\)). Conversely, let \(f\cdot x=\gamma f\cdot y\) with \(y\ne0\). Then \(Zy=(0,\dots,0,-Nx_\varrho)\) by [[proofs/grh/spanning-unfolding-b/norm-identity-for-combinations-of-the-moved-frame|the norm identity lemma]], so \(y=t\,c\) with \(t=-Nx_\varrho/\det Z\), because \(Z\) is invertible; \(t\ne0\) as \(y\ne0\). The \(X_0\)-part of \(\gamma f\cdot y=f\cdot x\) vanishes, hence so does that of \(\gamma f\cdot c\), i.e. \(y_0=0\).

## References

1. Lean: `New.Filling.termDisc_eq_zero_iff`, `New.Filling.termDisc_eq_zero_iff_exists`, `New.Filling.frameImage_mulVec_eq_zero_iff` in `src/New/Spanning/Unfolding/Link.lean`.
