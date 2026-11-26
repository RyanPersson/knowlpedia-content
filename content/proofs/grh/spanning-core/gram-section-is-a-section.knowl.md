+++
id = "proofs/grh/spanning-core/gram-section-is-a-section"
title = "The Gram section is a measurable section of the frame Gram matrix"
kind = "theorem"
summary = "For Z in the open cell the explicit matrix is an isometry with frame Gram matrix Z; the section is measurable and real differentiable on the open cell."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.sectionMatrix_isometry", "New.RealPlace.realFrameGram_gramSection", "New.RealPlace.frameCols_gram_sectionMatrix", "New.RealPlace.sectionMatrix_mul_frameCols", "New.RealPlace.measurable_gramSection", "New.RealPlace.differentiableAt_sectionMatrix", "New.RealPlace.differentiableAt_sectionMatrix_uncurry", "New.RealPlace.conjTranspose_actOnCols_mul_mul", "New.RealPlace.frameCols_gram_frameCols", "New.RealPlace.frameCols_gram_dualFrameCols", "New.RealPlace.realFrameGram_eq_conjTranspose_mul", "New.RealPlace.one_sub_invCorner_mul_mem_slitPlane"]
lean_files = ["src/New/Spanning/Bessel/GramSection.lean"]
proof_status = "outline"
+++

**Theorem.** With the notation of the [[proofs/grh/spanning-core/gram-section|Gram section]] and \(J\) the Gram matrix of \(h\):

1. For every \((\varrho+1)\times(\varrho+1)\) matrix \(Z\) for which the formulas make sense (in Lean: every \(Z\), with the conventions for inverses of singular matrices), \(M(Z,Z^*)F=S(Z,Z^*)\) and \(F^*J\,M(Z,Z^*)\,F=Z\).
2. For \(Z\in\Omega\), \(M(Z,Z^*)^*\,J\,M(Z,Z^*)=J\); so \(\gamma_Z\in G_1\) is well defined.
3. For \(Z\in\Omega\), the [[proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry|frame Gram matrix]] of \(\gamma_Z\) is \(Z(\gamma_Z)=Z\).
4. \((Z,W)\mapsto M(Z,W)\) is holomorphic on \(\Omega\times\Omega\); \(Y\mapsto M(Y,Y^*)\) is real differentiable at every point of \(\Omega\); and \(Z\mapsto\gamma_Z\) is Borel measurable on all matrices.

## Proof

(1) \(F^*F=1\), \(F'^*F=0\), so \(M F=F+(S-F)=S\). The Gram products are \(F^*JF=\delta(0)-1=\operatorname{diag}(0,\dots,0,-1)\) and \(F^*JF'=\delta(0)\). Hence \(F^*JS=\bigl((\delta(0)-1)Y+\delta(0)\delta(s)\bigr)Z\). The factor \(\delta(0)-1\) keeps only the last row \((0,\dots,0,-1)\) of \(Y\) and negates it, and \(\delta(0)\delta(s)=\delta(0)\); the sum is the identity matrix. So \(F^*JMF=Z\).

(2) *Outline.* Let \(C=(F\mid F')\); its \(2\varrho+2\) columns are orthonormal basis vectors, and \(J\) preserves their span, acting there by \(J_C=C^*JC\) and by the identity on the orthogonal complement (the span of the \(x_i\), \(i\ne k_0\)). Put \(\Delta=\delta(1/\nu(Z))\) and
\[
x=\begin{pmatrix}Z^{-1}&Y(Z^*,Z)\Delta\\0&1\end{pmatrix},\qquad y=\begin{pmatrix}Y(Z,Z^*)&(Z^*)^{-1}\Delta\\ \delta(\nu(Z))&0\end{pmatrix}.
\]
Then \(M(Z,Z^*)=1-CC^*+C\,yx^{-1}C^*\) (direct expansion of the definition, using the inverse of the block triangular \(x\)). The operation \(A\mapsto1-CC^*+CAC^*\) is compatible with congruence, so it suffices that \((yx^{-1})^*J_C(yx^{-1})=J_C\), i.e. \(y^*J_Cy=x^*J_Cx\). This last identity is an identity between polynomials in the entries of \(Z^{-1}\), their conjugates and \(\nu(Z)^{\pm1}\), given \(\nu(Z)^2=1-\lvert\xi(Z)\rvert^2\); the Lean proof verifies it entry by entry by automation (`simp` and `grind`), and we do not reproduce the computation. (It says that the columns of \(x\), namely \(FZ^{-1}\) and the dual family for \(Z^*\), and those of \(y\), the dual family for \(Z\) and \(F(Z^*)^{-1}\), have the same Gram matrix.)

(3) By (1), as \(Z(\gamma)=F^*J\gamma F\).

(4) For \(Z,W\in\Omega\), \(\lvert\xi(Z)\xi(W)\rvert<1\), so \(1-\xi(Z)\xi(W)\) lies in the slit plane where the principal square root is holomorphic and nonzero; all entries of \(M\) are polynomials in the entries of \(Z,Z^{-1},W^{-1}\), \(s\) and \(s^{-1}\). Restricting to the real subspace \(W=Z^*\) gives real differentiability (and \(\Omega\) is stable under \(Z\mapsto Z^*\)). Measurability: \(Z\mapsto M(Z,Z^*)\) is continuous on the open set \(\Omega\) and \(\gamma_Z\) is constant off \(\Omega\). \(\blacksquare\)

## References

1. Lean: `New.RealPlace.sectionMatrix_isometry`, `New.RealPlace.frameCols_gram_sectionMatrix`, `New.RealPlace.realFrameGram_gramSection`, `New.RealPlace.measurable_gramSection`, `New.RealPlace.differentiableAt_sectionMatrix` in `src/New/Spanning/Bessel/GramSection.lean`.
