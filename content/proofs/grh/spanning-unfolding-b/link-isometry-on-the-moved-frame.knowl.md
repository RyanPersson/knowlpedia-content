+++
id = "proofs/grh/spanning-unfolding-b/link-isometry-on-the-moved-frame"
title = "The link isometry on combinations of the moved frame"
kind = "theorem"
summary = "A combination of the moved frame orthogonal to the isotropic frame vectors is sent by the link isometry to a multiple of the positive vector; this gives an exact norm identity and a criterion for lying in the span of the frame."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.linkIsometry_frameImage_mulVec", "New.Filling.mul_dotProduct_comp_indexX₀_eq_sub", "New.Filling.exists_frameImage_eq_iff", "New.Filling.exists_frameImage_eq_of_frameProducts_mulVec_eq_zero"]
lean_files = ["src/New/Spanning/Unfolding/Link.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\), \(\gamma\in G(E)\), \(c\in E^{\varrho+1}\) and \(c'\in E\) such that the frame products satisfy \(Z(\gamma)c=(0,\dots,0,c')\). Put \(y=\gamma f\cdot c\), with \(X_0\)-part \(y_0\).

1. The [[proofs/grh/spanning-unfolding-b/link-isometry|link isometry]] satisfies \(\Upsilon_\gamma\bigl(y_0+c_\varrho z^+\bigr)=-(c'/N)\,z^+\).
2. \(N\langle y_0,y_0\rangle=c'\bar c'-N^2c_\varrho\bar c_\varrho\), where \(\langle y_0,y_0\rangle=\sum_{i\in\kappa}\overline{(y_0)_i}(y_0)_i\).
3. \(y\) is a combination of the frame \(f\) if and only if \(y_0=0\).
4. If \(c'=0\), i.e. \(Z(\gamma)c=0\), then \(y\) is a combination of the frame.

## Proof

(1) By [[proofs/grh/spanning-unfolding-b/norm-identity-for-combinations-of-the-moved-frame|the norm identity]], \(y\) has no \(e^*\)-part and \(y_z=-c'/N\). Also \(\gamma^{-1}y=f\cdot c\) has no \(e^*\)-part, no \(X_0\)-part, and \(z\)-coordinate \(c_\varrho\). So \(y\in(A+\gamma A)^\perp\), and its pair in the link has source \(y_0+c_\varrho z^+\) and target \(0+y_zz^+\) ([[proofs/grh/spanning-unfolding-b/positive-space-and-link-maps|source and target]]).

(2) [[proofs/grh/spanning-unfolding-b/link-is-graph-of-link-isometry|\(\Upsilon_\gamma\) preserves \(h^+\)]]; comparing the norms of the two sides of (1): \(N\,\overline{(c'/N)}(c'/N)=\langle y_0,y_0\rangle+N\bar c_\varrho c_\varrho\). Multiply by \(N\).

(3) If \(y=f\cdot x\), its \(X_0\)-coordinates vanish. Conversely, if \(y_0=0\), then \(y\) has neither \(X_0\)- nor \(e^*\)-coordinates, so it is the combination of the frame with its own coordinates.

(4) By (1), \(\Upsilon_\gamma(y_0+c_\varrho z^+)=0\); \(\Upsilon_\gamma\) is injective, so \(y_0=0\), and (3) applies.

## References

1. Lean: `New.Filling.linkIsometry_frameImage_mulVec`, `New.Filling.mul_dotProduct_comp_indexX₀_eq_sub`, `New.Filling.exists_frameImage_eq_iff`, `New.Filling.exists_frameImage_eq_of_frameProducts_mulVec_eq_zero` in `src/New/Spanning/Unfolding/Link.lean`.
