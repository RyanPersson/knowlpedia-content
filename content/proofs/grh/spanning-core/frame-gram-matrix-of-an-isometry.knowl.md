+++
id = "proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry"
title = "The frame Gram matrix of an isometry at a real place"
kind = "lemma"
summary = "The matrix of products of the frame with its image under an isometry, its expression through moved frames, and its behaviour under the Bessel groups."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.realFrameGram_eq_inner", "New.realFrameGram_mul_of_mem_besselFixer", "New.realFrameGram_eq_frameMatrix_mul", "New.norm_realFrameGram_le_mul"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
proof_status = "full"
+++

In the setting of the [[proofs/grh/spanning-core/bessel-length|Bessel length]], the [[?lean:New.realFrameGram|frame Gram matrix]] of \(\gamma\in G_1\) is the \((\varrho+1)\times(\varrho+1)\) complex matrix \(Z(\gamma)_{ab}=h(f_a,\gamma f_b)\), where \(h(v,w)=v^*Jw\).

**Lemma.** For \(\gamma,y\in G_1\):

1. \(Z(\gamma)_{ab}=h\bigl(y^{-1}f_a,\ y^{-1}\gamma f_b\bigr)\), and \(y^{-1}\gamma f_b\) is the moved frame vector at \(\gamma^{-1}y\). Hence \(\lvert Z(\gamma)_{ab}\rvert\le\lVert y^{-1}f_a\rVert\cdot\lVert(\gamma^{-1}y)^{-1}f_b\rVert\).
2. If \(s\in G_1\) fixes every frame vector, \(Z(s\gamma)=Z(\gamma)=Z(\gamma s)\).
3. If \(s\) lies in the Bessel unipotent group \(\mathsf U\), with frame matrix \(m\), then \(Z(y)=m^*\,Z(sy)\).

## Proof

(1) \(y^{-1}\) preserves \(h\). The bound follows from \(\lVert J\rVert=1\) and Cauchy–Schwarz. (2) \(h(f_a,s\gamma f_b)=h(s^{-1}f_a,\gamma f_b)=h(f_a,\gamma f_b)\), and \(\gamma sf_b=\gamma f_b\). (3) This is the case \(x'=s\), \(x=1\) of the library rule `New.frameGram_inv_mul_mul`: for \(x,x'\in\mathsf U\) with frame matrices \(m,m'\), \(Z(x'^{-1}\gamma x)=m'^*Z(\gamma)m\) (because \(x\) maps the span of the frame to itself by \(m\)); apply it to \(\gamma=sy\). \(\blacksquare\)

## References

1. Lean: `New.realFrameGram_eq_inner`, `New.realFrameGram_mul_of_mem_besselFixer`, `New.realFrameGram_eq_frameMatrix_mul`, `New.norm_realFrameGram_le_mul` in `src/New/Spanning/Bessel/Basic.lean`.
