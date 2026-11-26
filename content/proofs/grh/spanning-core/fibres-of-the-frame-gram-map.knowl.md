+++
id = "proofs/grh/spanning-core/fibres-of-the-frame-gram-map"
title = "Fibres of the frame Gram matrix over the open cell"
kind = "lemma"
summary = "An element of the real unitary group with frame Gram matrix Z in the open cell is the Gram section at Z up to frame-fixing factors on both sides."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.exists_eq_mul_gramSection_mul", "New.RealPlace.conjTranspose_framePair_mul_mul"]
lean_files = ["src/New/Spanning/Bessel/GramSection.lean"]
proof_status = "full"
+++

**Lemma.** Let \(Z\in\Omega\) (the [[proofs/grh/spanning-core/open-cell-of-frame-matrices|open cell]]) and let \(\gamma\in G_1\) have [[proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry|frame Gram matrix]] \(Z(\gamma)=Z\). Then
\[
\gamma=u\,k\,\gamma_Z\,(u'\,l)^{-1},
\]
where \(\gamma_Z\) is the [[proofs/grh/spanning-core/gram-section|Gram section]], \(u,u'\) are [[?lean:New.RealPlace.unipotentOf|unipotent elements \(\mathrm{unipotentOf}(q)\)]] of the group \(\mathsf U^0\) of frame-fixing elements of the Bessel unipotent group, and \(k,l\in U(\kappa)\) act on \(X_0\) (embedded in \(G_1\)). All four factors fix the frame.

## Proof

For \(s\in G_1\) consider the \(2(\varrho+1)\) vectors \((F\mid sF)\), the frame and its image. By the [[proofs/grh/spanning-core/frame-discriminant|Gram determinant of two frames]] their Gram matrix is \(\begin{pmatrix}C&Z(s)\\Z(s)^*&C\end{pmatrix}\) with determinant \(\pm\mathsf g_1(Z(s))\). For \(s=\gamma\) and \(s=\gamma_Z\) we have \(Z(s)=Z\) ([[proofs/grh/spanning-core/gram-section-is-a-section|section property]]), and \(\mathsf g(Z)>0\) as \(Z\in\Omega\). So the two families have the same invertible Gram matrix (in particular each is linearly independent). By [[?c:Witt's extension theorem|Witt's theorem]] for the nondegenerate hermitian form \(h\) (library statement `New.witt`), there is \(g\in G_1\) with \(g(F\mid\gamma F)=(F\mid\gamma_ZF)\), that is, \(gF=F\) and \(g\gamma F=\gamma_ZF\). Then \(\gamma_Z^{-1}g\gamma\) also fixes the frame. An element of \(G_1\) that fixes every frame vector is of the form \(k\,u^{-1}\) with \(u\in\mathsf U^0\), \(k\in U(\kappa)\) (library statement `New.RealPlace.exists_embedH_eq_of_fix_frameCols`). So \(g=k_1u_1^{-1}\) and \(\gamma_Z^{-1}g\gamma=l_1u_2^{-1}\), whence
\[
\gamma=g^{-1}\gamma_Z\,l_1u_2^{-1}=u_1k_1^{-1}\,\gamma_Z\,(u_2l_1^{-1})^{-1}.\qquad\blacksquare
\]

## References

1. Lean: `New.RealPlace.exists_eq_mul_gramSection_mul` in `src/New/Spanning/Bessel/GramSection.lean`.
