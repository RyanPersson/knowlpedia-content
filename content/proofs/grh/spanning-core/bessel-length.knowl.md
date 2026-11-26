+++
id = "proofs/grh/spanning-core/bessel-length"
title = "Bessel length of a point of the real unitary group"
kind = "definition"
summary = "The infimum of the operator norm of s y plus one over s in the Bessel subgroup."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.besselLength", "New.besselLength_nonneg", "New.frameBox", "New.besselLength_le_norm_mul_add_one", "New.RealPlace.exists_norm_le_of_besselLength_le", "New.besselLength_besselS_mul", "New.besselLength_le_norm_inv_mul_mul_besselLength", "New.continuous_besselLength", "New.norm_frameVector_le", "New.frameVector_mul_of_mem_besselFixer", "New.frameVector_eq_sum"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
+++

Let \(\mathfrak s\) be a [[?lean:New.Shape|shape]]: a number \(\varrho\) of hyperbolic planes and a finite index set \(\kappa\) (of size \(k\)). Let \(h\) be the hermitian form on \(\mathbb{C}^{2\varrho+k+1}\) with basis \(e_1,\dots,e_\varrho;\ x_i\ (i\in\kappa),\ z;\ e_1^*,\dots,e_\varrho^*\) in which \(h(e_a,e_b^*)=\delta_{ab}\), \(h(x_i,x_j)=\delta_{ij}\), \(h(z,z)=-1\) and all other products of basis vectors vanish; let \(G_1\) be its [[?lean:New.Shape.G₁|unitary group]], and \(S\subseteq G_1\) the [[?lean:New.Shape.Form.besselS|Bessel subgroup]]. The **frame** is \(f=(f_1,\dots,f_{\varrho+1})=(e_1,\dots,e_\varrho,z)\). Norms of matrices are [[linear-algebra/operator-norm|operator norms]] for the Euclidean norm in which the basis is orthonormal.

The **Bessel length** of \(y\in G_1\) is
\[
\ell(y)=\inf_{s\in S}\bigl(\lVert s\,y\rVert+1\bigr).
\]
For \(\rho\in\mathbb{R}\), the **frame box** of radius \(\rho\) is the set of \(y\in G_1\) with \(\lVert y^{-1}f_a\rVert\le\rho\) for all \(a\); the vector \(y^{-1}f_a\) is the \(a\)-th [[?lean:New.frameVector|moved frame vector]] at \(y\).

## Properties

Let \(\mathsf U\subseteq S\) be the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]] and \(H\cong U(\kappa)\) the unitary group of \(X_0=\langle x_i\rangle\), embedded in \(G_1\).

1. \(\ell(sy)=\ell(y)\) for \(s\in S\), and \(\ell(y)\ge1\).
2. If \(\ell(y)\le T\), there is \(u\in\mathsf U\) with \(\lVert uy\rVert\le T\).
3. \(\ell(y)\le\lVert x^{-1}y\rVert\,\ell(x)\) for \(x,y\in G_1\); consequently \(\ell\) is continuous on \(G_1\).
4. \(\lVert y^{-1}f_a\rVert\le\lVert y\rVert\).
5. The moved frame at \(sy\) equals that at \(y\) if \(s\) fixes every frame vector; and for \(s\in\mathsf U\), \(y^{-1}f_a=\sum_bm_{ba}\,(sy)^{-1}f_b\), where \(m=(m_{ba})\) is the [[?lean:New.frameMatrix|frame matrix]] of \(s\) (its submatrix on the rows and columns of the frame, which is upper unitriangular).

## Proof

Throughout, \(\lVert g\rVert=\lVert g^{-1}\rVert\ge1\) for \(g\in G_1\) (as \(g^{-1}=Jg^*J\) with \(J\) the Gram matrix, a unitary involution; and \(1=\lVert gg^{-1}\rVert\le\lVert g\rVert^2\)).

(1) Right translation by \(s\) permutes \(S\). (4) \(y^{-1}f_a\) is the image of a unit vector under \(y^{-1}\). (5) The first claim is \((sy)^{-1}f_a=y^{-1}s^{-1}f_a\). For the second, \(s\) maps the span of the frame to itself by the matrix \(m\) (library lemma `New.submatrix_mul_besselFrame`), so \(y^{-1}f_a=(sy)^{-1}sf_a=\sum_bm_{ba}(sy)^{-1}f_b\).

(2) There is \(s\in S\) with \(\lVert sy\rVert+1<T+1\). Every element of \(S\) is a product \(u\,h\) with \(u\in\mathsf U\), \(h\in H\) (`New.exists_besselU_mul_toBesselH`); write \(s^{-1}=uh\), so \(u^{-1}=hs\). As \(h\) is a unitary matrix, \(\lVert u^{-1}y\rVert=\lVert hsy\rVert=\lVert sy\rVert<T\).

(3) For \(s\in S\): \(\lVert sy\rVert+1\le\lVert sx\rVert\lVert x^{-1}y\rVert+\lVert x^{-1}y\rVert\); take the infimum over \(s\). Continuity at \(y\): \(\ell(y)/\lVert x^{-1}y\rVert\le\ell(x)\le\lVert y^{-1}x\rVert\ell(y)\), and both bounds tend to \(\ell(y)\) as \(x\to y\). \(\blacksquare\)

## References

1. Lean: `New.besselLength`, `New.frameBox` and the lemmas of the section `SizeFunction` in `src/New/Spanning/Bessel/Basic.lean`.
