+++
id = "proofs/grh/spanning-core/open-cell-bound-exists"
title = "The open cell bound holds for every Bessel system"
kind = "theorem"
summary = "For gamma with frame Gram matrix in the open cell and a scale rho at which some point and its translate lie in the frame box, a Bessel system has an open cell bound."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.BesselSystem.exists_isOpenCellBound", "New.BesselSystem.exists_isKernelBound_gramSection", "New.BesselSystem.isL2Contraction_gramSection", "New.isL2Contraction_of_columns", "New.sum_enorm_sq_integral_mul_star", "New.BesselSystem.lintegral_indicator_mul_enorm_sq_le", "New.exists_mul_eq_mul_gramSection_mul", "New.scale_mul_le_pow", "New.toReal_inv_mul_mul_le"]
lean_files = ["src/New/Spanning/Bessel/OpenCellBound.lean"]
proof_status = "outline"
+++

**Theorem (open cell bound).** Let \(X\) be a [[proofs/grh/spanning-core/bessel-system|Bessel system]] for \((\mathfrak s,B,f)\), \(\gamma\in G_1\) with \(\mathsf g(Z(\gamma))>0\) (that is, [[proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry|frame Gram matrix]] in the [[proofs/grh/spanning-core/open-cell-of-frame-matrices|open cell]]), \(\rho\ge B\), and suppose some \(y\in G_1\) has \(y\) and \(\gamma^{-1}y\) in the [[proofs/grh/spanning-core/bessel-length|frame box]] of radius \(\rho\). Then there are a compact set \(A\), a finite measure \(\nu\) on \(G_1\), a probability measure \(m\) on \(U(\kappa)\times\mathsf U^0\) and a measurable map \(t\) from \(U(\kappa)\times\mathsf U^0\) to the fixer of the frame forming an [[proofs/grh/spanning-core/open-cell-bound|open cell bound]] for \((X,\gamma,\rho)\).

## Proof

*Outline.* Write \(Z=Z(\gamma)\), \(n=\varrho+1\), \(W\) for the full function.

*Step 1 (reduction to the section).* By the [[proofs/grh/spanning-core/fibres-of-the-frame-gram-map|fibres of the frame Gram map]], \(\gamma=uk\,\gamma_Z\,(u'k')^{-1}\). Put \(s=uk\in S\) and \(t(h,v)=u'k'h^{-1}v^{-1}\), which fixes the frame; then \(\gamma\,t(h,v)=s\,\gamma_Z\,(vh)^{-1}\).

*Step 2 (scale).* The entries of \(Z\) are at most \(\rho^2\) (frame Gram rules with the point \(y\)). Let \(M=\rho^{9n}/\mathsf g(Z)\); by [[proofs/grh/spanning-core/sizes-near-a-point-of-the-open-cell|part 3 of the size lemma]] \(\rho\le M\), and \(M^{-1}\le\mathsf g(Z)\). It suffices to produce the bound at the radius \(M\ge\rho\) with mass at most \(M^{10^5n^4}\lvert I\rvert^2/(\deg c_G(\mathsf g(Z)/2)^{k-1})\), which is the pairing bound.

*Step 3 (the sets).* Let \(M_0=M^{9n}\), \(P=(M_0^5)^n\). The library provides a **tube** (`New.RealPlace.exists_tube`, for \(T=M_0^5\ge8r\)): a compact \(A\subseteq G_1\) of norm \(\le T^{10}\le P^{20}\) and a measurable \(\Omega_0\subseteq\mathsf U^0\) of finite nonzero Haar measure with \(uy\in A\) for \(u\in\Omega_0\), \(\lVert y\rVert\le T\), and such that for each \(y\) the set of \(u\in\mathsf U^0\) with \(uy\in A\) has measure at most \(3\operatorname{vol}(\Omega_0)\). Let \(c=c_G(\mathsf g(Z)/2)^{k-1}\), \(\mu=\mu_c\) the [[proofs/grh/spanning-core/integral-over-the-section-orbit|fixer measure]], \(m\) the measure \(\mu\) conditioned on \(v\in\Omega_0\), \(K=P^{2000n^2}\lvert I\rvert/\deg\), and \(\nu=\mu(U(\kappa)\times\Omega_0)^{-1}K\cdot1_A\lVert W\rVert^2\,dy\).

*Step 4 (contraction).* By the size lemma (part 2), on the ball of radius \(P^{-6}\) about \(Z\) the matrices are bounded in the cell by \(P\) and have \(\mathsf g\ge\mathsf g(Z)/2\). Since \(P\ge B^5\) and \(P\ge8r\), \(W\) has the Schur bound with constants \(P\), \(\lvert I\rvert/\deg\), and the [[proofs/grh/spanning-core/sobolev-bound-at-the-gram-section|Sobolev bound at the section]] gives, for every integrable measurable \(\beta\) supported in \(A\),
\[
\int_{v\in\Omega_0}\Bigl\lVert\int\beta(y)W(\gamma_Z(vh)^{-1}y)\,dy\Bigr\rVert^2d\mu\le K\int\lvert\beta\rvert^2 .
\]
To pass to the kernels: for integrable \(\psi\) and \(s,t\in S\), \(\sum_{i,j}\lvert\int\psi(y)W_i(sgy)\overline{W_j(ty)}dy\rvert^2=\sum_j\lVert\int\psi(y)\overline{W_j(y)}\,W(gy)\,dy\rVert^2\), because the norm of \(\int\beta(y)W(agy)dy\) does not depend on \(a\in S\) (library statement `New.IsBesselFunction.enorm_integral_besselS_mul`), applied once in each tensor factor. Applying the displayed bound to the weights \(\beta_j=1_A\varphi\overline{W_j}\) and summing over \(j\) (\(\sum_j\lvert\beta_j\rvert^2=1_A\lvert\varphi\rvert^2\lVert W\rVert^2\)) gives the contraction for \(m\), Haar measure on \(A\) and \(\nu\).

*Step 5 (mass of \(\nu\)).* By the [[proofs/grh/spanning-core/unfolding-bound-on-the-real-group|unfolding bound]] with \(\varphi=1_A\) (orbit mass \(\le3\operatorname{vol}\Omega_0\), frame matrices bounded by \(P^{20}\cdot P^{20}\)) and \(\int\lVert W\rVert^2d\mu_{\mathsf U\backslash G_1}=\lvert I\rvert\): \(\int_A\lVert W\rVert^2\le M_0^5\operatorname{vol}(\Omega_0)\,(M P^{40})^{2n^2}\lvert I\rvert\) (using \(3\le M_0^5\), \(2\le M\)). Since \(\mu(U(\kappa)\times\Omega_0)=c\operatorname{vol}(\Omega_0)\), the volume cancels and \(\nu(G_1)\le P^{2000n^2}M_0^5(MP^{40})^{2n^2}\lvert I\rvert^2/(\deg c)\); the power of \(M\) is \(M^{93600n^4+2n^2+45n}\le M^{10^5n^4}\).

*Step 6 (capture).* If \(v\in\Omega_0\), \(z\) is in the frame box of radius \(M\) and \(\ell(s\gamma_Z(vh)^{-1}z)\le M\), then by the [[proofs/grh/spanning-core/norm-bound-from-the-length-at-the-section|norm bound at the section]] (with \(R=M_0\), \(\lVert Z^{-1}\rVert\le M_0\)) \(\lVert v^{-1}z\rVert\le M_0^5=T\), hence \(z=v(v^{-1}z)\in A\).

Steps taken from the library without proof here: the existence of tubes and the invariance of the norm of the mean under \(S\). \(\blacksquare\)

## References

1. Lean: `New.BesselSystem.exists_isOpenCellBound`, `New.BesselSystem.exists_isKernelBound_gramSection`, `New.BesselSystem.isL2Contraction_gramSection`, `New.isL2Contraction_of_columns` in `src/New/Spanning/Bessel/OpenCellBound.lean`.
