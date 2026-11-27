+++
id = "proofs/grh/spanning-core/norm-bound-from-the-length-at-the-section"
title = "A norm bound from the Bessel length at the Gram section"
kind = "lemma"
summary = "If the moved frame at z is bounded and gamma_Z z has bounded Bessel length, then z has bounded operator norm."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_le_of_besselLength_gramSection_mul_le", "New.inv_apply_eStar_eq_sum_frameVector", "New.norm_inv_mul_le_of_besselLength_le", "New.RealPlace.sectionCoeff_castSucc_castSucc", "New.RealPlace.sectionCoeff_last_castSucc"]
lean_files = ["src/New/Spanning/Bessel/OpenCellBound.lean"]
proof_status = "full"
+++

**Lemma.** Let \(n=\varrho+1\), \(M\ge8n\), \(R\ge M^{9n}\), and let \(Z\) be an \(n\times n\) matrix with \(\mathsf g(Z)\ge M^{-1}\) and \(\lVert Z^{-1}\rVert\le R\). Let \(z\in G_1\) lie in the [[proofs/grh/spanning-core/bessel-length|frame box]] of radius \(M\).

1. If \(\ell(\gamma_Zz)\le M\) ([[proofs/grh/spanning-core/bessel-length|Bessel length]] at the [[proofs/grh/spanning-core/gram-section|Gram section]]), then \(\lVert z\rVert\le R^5\).
2. If \(s\in S\), \(v\in\mathsf U^0\), \(h\in U(\kappa)\) and \(\ell\bigl(s\gamma_Z(vh)^{-1}z\bigr)\le M\), then \(\lVert v^{-1}z\rVert\le R^5\).

**Column formula.** For \(Z\in\Omega\), \(w\in\mathsf U\), \(z\in G_1\), \(a\le\varrho\), and \(Z'=Z(w\gamma_Z)\):
\[
z^{-1}e_a^*=\sum_{i\le\varrho+1}\bigl((Z'^*)^{-1}\bigr)_{ia}\,(w\gamma_Zz)^{-1}f_i+\sum_{i\le\varrho}\tfrac12\,(Z^{-1})_{i,\varrho+1}\bigl((Z^*)^{-1}\bigr)_{\varrho+1,a}\,z^{-1}f_i .
\]

## Proof

*Column formula.* Put \(V=z^{-1}\), \(N=V\gamma_Z^{-1}\), \(L=Nw^{-1}\), so \(V=N\,M(Z,Z^*)\) with the matrix \(M\) of the Gram section, and \(N\,S(Z,Z^*)=VF\) (since \(MF=S\)). Insert the definition of \(M\) and take the column at \(e_a^*\): \(F^*e_a^*=0\) and \(F'^*e_a^*\) is the \(a\)-th coordinate vector, on which \(\delta(s^{-1})\) acts trivially; the terms \(Ne_a^*\) cancel, leaving
\[
Ve_a^*=\bigl(NF(Z^*)^{-1}\bigr)_{\cdot a}-\bigl(VF\,Y(Z^*,Z)\bigr)_{\cdot a} .
\]
The entries of \(Y(Z^*,Z)\) in column \(a\le\varrho\) are \(-\tfrac12(Z^{-1})_{i,\varrho+1}((Z^*)^{-1})_{\varrho+1,a}\) for \(i\le\varrho\) and \(0\) for \(i=\varrho+1\). Finally \(w\) maps the span of the frame to itself by its unitriangular frame matrix \(m\), and \(Z=m^*Z'\) ([[proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry|frame Gram rules]]), so \(NF(Z^*)^{-1}=LF\,m\,(Z^*)^{-1}=LF\,(Z'^*)^{-1}\); and the columns of \(LF\) are the moved frame at \(w\gamma_Zz\).

(1) \(Z\in\Omega\) as \(\mathsf g(Z)>0\). Choose \(w\in\mathsf U\) with \(\lVert w\gamma_Zz\rVert\le M\) (Property 2 of the Bessel length) and put \(y=w\gamma_Zz\); its moved frame vectors have length \(\le M\). The matrix \(Z'=Z(w\gamma_Z)\) has entries bounded by \(\lVert y^{-1}f_a\rVert\lVert z^{-1}f_b\rVert\le M^2\) (frame Gram rules with the point \(y\), since \((w\gamma_Z)^{-1}y=z\)), and \(\mathsf g(Z')=\mathsf g(Z)\) (library statement `New.Filling.frameDisc_frameGram_inv_mul_mul_of_mem_besselU`: the frame discriminant is unchanged under multiplication by elements of \(\mathsf U\)). By [[proofs/grh/spanning-core/sizes-near-a-point-of-the-open-cell|sizes in the open cell]], \(\lVert Z'^{-1}\rVert\le R\). The column formula gives
\[
\lVert z^{-1}e_a^*\rVert\le(\varrho+1)R\cdot R+\varrho\cdot\tfrac12R\cdot R\cdot R\le R^4 ,
\]
using \(M\le R\) and \(\varrho+1+\varrho R/2\le R^2\). Also \(\lVert z^{-1}f_a\rVert\le M\le R^4\). By the [[proofs/grh/spanning-core/norm-bound-from-frame-and-dual-columns|norm bound from the frame and dual columns]], \(\lVert z\rVert+1\le8(\varrho+1)R^4\le R^5\).

(2) \(\ell\) is left \(S\)-invariant, so \(\ell(\gamma_Z(vh)^{-1}z)\le M\). The element \((vh)^{-1}\) fixes the frame, so \((vh)^{-1}z\) lies in the frame box of radius \(M\); by (1) \(\lVert(vh)^{-1}z\rVert\le R^5\), and \(v^{-1}z=h\cdot(vh)^{-1}z\) with \(h\) unitary. \(\blacksquare\)

## References

1. Lean: `New.inv_apply_eStar_eq_sum_frameVector`, `New.norm_le_of_besselLength_gramSection_mul_le`, `New.norm_inv_mul_le_of_besselLength_le` in `src/New/Spanning/Bessel/OpenCellBound.lean`.
