+++
id = "proofs/grh/spanning-core/open-cell-of-frame-matrices"
title = "Open cell of frame Gram matrices"
kind = "definition"
summary = "The open set of invertible (rho+1)x(rho+1) complex matrices whose inverse has last diagonal entry of modulus less than one; equivalently where the frame discriminant is positive."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.invCorner", "New.Shape.openCell", "New.RealPlace.oneSubNormSqInvCorner", "New.RealPlace.IsBoundedInCell", "New.RealPlace.mem_openCell_iff", "New.RealPlace.gramDiscReal_eq_norm_det_sq_mul", "New.RealPlace.isOpen_openCell", "New.RealPlace.continuous_gramDiscReal", "New.RealPlace.conjTranspose_mem_openCell_iff", "New.RealPlace.invCorner_conjTranspose", "New.RealPlace.oneSubNormSqInvCorner_pos"]
lean_files = ["src/New/Spanning/Bessel/GramSection.lean"]
+++

Let \(\varrho\ge0\) and let \(Z\) be a complex \((\varrho+1)\times(\varrho+1)\) matrix. If \(Z\) is invertible, write \(\xi(Z)=(Z^{-1})_{\varrho+1,\varrho+1}\) for the last diagonal entry of its inverse, and \(\nu(Z)^2=1-\lvert\xi(Z)\rvert^2\). The **open cell** is
\[
\Omega=\{\,Z\ :\ \det Z\neq0,\ \lvert\xi(Z)\rvert<1\,\}.
\]
For \(P\in\mathbb{R}\), \(Z\) is **bounded in the cell by \(P\)** if \(Z\in\Omega\) and \(\lVert Z^{-1}\rVert\le P\), \(\lVert Z\rVert\le P\), \(1/\nu(Z)\le P\) ([[linear-algebra/operator-norm|operator norms]]).

## Properties

Let \(\mathsf g(Z)=\lvert\det Z\rvert^2-\lvert D_\varrho\rvert^2\) be the real [[proofs/grh/spanning-core/frame-discriminant|frame discriminant]], \(D_\varrho\) the leading minor of order \(\varrho\).

1. For invertible \(Z\): \(\xi(Z)=D_\varrho/\det Z\) and \(\mathsf g(Z)=\lvert\det Z\rvert^2\,\nu(Z)^2\).
2. \(Z\in\Omega\iff\mathsf g(Z)>0\). Hence \(\Omega\) is open, as \(\mathsf g\) is a polynomial in the real and imaginary parts of the entries.
3. \(\xi(Z^*)=\overline{\xi(Z)}\), and \(Z\in\Omega\iff Z^*\in\Omega\).

## Proof

(1) is Cramer's rule. (2) For invertible \(Z\) use (1); if \(\det Z=0\) then \(\mathsf g(Z)=-\lvert D_\varrho\rvert^2\le0\) and \(Z\notin\Omega\). (3) \((Z^*)^{-1}=(Z^{-1})^*\). \(\blacksquare\)

## References

1. Lean: `New.Shape.openCell`, `New.RealPlace.invCorner`, `New.RealPlace.oneSubNormSqInvCorner`, `New.RealPlace.IsBoundedInCell`, `New.RealPlace.mem_openCell_iff` in `src/New/Spanning/Bessel/GramSection.lean`.
