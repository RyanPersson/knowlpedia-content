+++
id = "proofs/grh/spanning-core/frame-discriminant"
title = "The frame discriminant and the Gram determinant of two frames"
kind = "theorem"
summary = "The quantity |det Z|^2 - N^2 |D_rho|^2 of the frame Gram matrix is, up to sign, the Gram determinant of the frame together with its image under an isometry."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.frameDisc", "New.det_gram_framePair", "New.gram_framePair", "New.det_fromBlocks_single", "New.det_eq_add_of_row_eq_add", "New.framePair", "New.isotropicFramePair", "New.RealPlace.gramDiscReal"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
proof_status = "full"
+++

Let \(R\) be a commutative ring with involution, \(N\in R\), and \(Z\) a \((\varrho+1)\times(\varrho+1)\) matrix over \(R\) with leading principal minor \(D_\varrho\) of order \(\varrho\). The **frame discriminant** is
\[
\mathsf g_N(Z)=\det Z\cdot\overline{\det Z}-N^2\,D_\varrho\overline{D_\varrho} .
\]
At a real place one takes \(R=\mathbb{C}\), \(N=1\): \(\mathsf g(Z)=\lvert\det Z\rvert^2-\lvert D_\varrho\rvert^2\in\mathbb{R}\).

**Theorem.** Let \(\bar N=N\), let \(h\) be the form of \(\varrho\) hyperbolic pairs with middle block \(\operatorname{diag}(1,\dots,1,-N)\), \(\gamma\) an isometry of \(h\), \(f=(e_1,\dots,e_\varrho,z)\) the frame and \(Z=Z(\gamma)=(h(f_a,\gamma f_b))\). Then the Gram matrix of the \(2(\varrho+1)\) vectors \((f,\gamma f)\) is
\[
\begin{pmatrix}C&Z\\ Z^*&C\end{pmatrix},\qquad C=\text{the matrix with the single nonzero entry }-N\text{ at }(\varrho+1,\varrho+1),
\]
and its determinant is \((-1)^{\varrho+1}\,\mathsf g_N(Z)\).

## Proof

The Gram matrix of \(f\) is \(C\) (the \(e_a\) are isotropic and orthogonal to \(z\), \(h(z,z)=-N\)); the same holds for \(\gamma f\) since \(\gamma\) is an isometry; the mixed blocks are \(Z\) and \(Z^*\) as \(h\) is hermitian.

*Determinant of a bordered block matrix.* For \(n\times n\) matrices \(Z,W\), an index \(i\) and a scalar \(c\), let \(C_i\) have the single entry \(c\) at \((i,i)\). Then
\[
\det\begin{pmatrix}Z&C_i\\ C_i&W\end{pmatrix}=\det Z\det W-c^2\operatorname{adj}(Z)_{ii}\operatorname{adj}(W)_{ii} .
\]
Indeed, the determinant is additive in row \(i\) of the upper half: that row is \((Z_i\mid 0)+(0\mid c\,\epsilon_i)\). The first part gives a block lower triangular matrix with determinant \(\det Z\det W\). In the second part split row \(i\) of the lower half as \((0\mid W_i)+(c\,\epsilon_i\mid0)\): the first piece gives a block triangular matrix whose upper left block has a zero row, so determinant \(0\); in the second piece exchange the two rows \(i\) (sign \(-1\)) to get a block diagonal matrix with blocks \(Z\) and \(W\) with row \(i\) replaced by \(c\,\epsilon_i\), of determinants \(c\operatorname{adj}(Z)_{ii}\) and \(c\operatorname{adj}(W)_{ii}\).

Now \(\begin{pmatrix}C&Z\\ Z^*&C\end{pmatrix}=\begin{pmatrix}Z&C\\ C&Z^*\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\), and the exchange matrix has determinant \((-1)^{\varrho+1}\). With \(i=\varrho+1\), \(c=-N\), \(W=Z^*\): \(\operatorname{adj}(Z)_{ii}=D_\varrho\) and \(\operatorname{adj}(Z^*)_{ii}=\overline{D_\varrho}\), \(\det Z^*=\overline{\det Z}\). \(\blacksquare\)

## References

1. Lean: `New.frameDisc`, `New.gram_framePair`, `New.det_fromBlocks_single`, `New.det_gram_framePair`, `New.RealPlace.gramDiscReal` in `src/New/Spanning/Bessel/Basic.lean`.
