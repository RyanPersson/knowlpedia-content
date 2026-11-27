+++
id = "proofs/grh/spanning-core/one-pairing-on-the-open-cell"
title = "One pairing on the open cell, at all places together"
kind = "theorem"
summary = "The integral of a bounded frame-invariant function against the cut kernel W-flat(y) tensor W-flat(gamma^-1 y)* over all real places is bounded by the root of the product of the local pairing bounds plus a cut error."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.BesselSystem.enorm_integral_pairKernel_cut_le", "New.BesselSystem.piKernel", "New.BesselSystem.pairKernel", "New.BesselSystem.adjointIsometry", "New.BesselSystem.exists_isCompact_enorm_integral_piKernel_le", "New.BesselSystem.hasCompactSupport_and_enorm_integral_piKernel_le", "New.BesselSystem.inCut_of_piKernel_ne_zero", "New.BesselSystem.integrableOn_smul_piKernel", "New.BesselSystem.one_le_b"]
lean_files = ["src/New/Spanning/Bessel/OpenCellPairing.lean"]
proof_status = "full"
+++

Let \(\iota\) be a finite set (of places), \(\mathfrak s\) a shape, and \(X_v\) (\(v\in\iota\)) [[proofs/grh/spanning-core/bessel-system|Bessel systems]] for \((\mathfrak s,b,f)\) with index sets \(I_v\), functions \(W_v\), cuts \(W_v^\flat\), degrees \(\deg_v\). For \(\sigma\in\{\mathrm{full},\mathrm{cut}\}\), \(\gamma,y\in G_1^\iota\) and \(i,j\in\prod_vI_v\) define the **pair kernel**
\[
\mathcal K^\sigma_\gamma(y)_{(i,j)}=\prod_{v\in\iota}W^\sigma_{v,i_v}(y_v)\,\overline{W^\sigma_{v,j_v}(\gamma_v^{-1}y_v)} ,
\]
the matrix of \(W^\sigma(y)\otimes W^\sigma(\gamma^{-1}y)^*\) for the tensor product \(W^\sigma=\bigotimes_vW_v^\sigma\), regarded as a vector with the Hilbert–Schmidt (Euclidean) norm. Haar measure on \(G_1^\iota\) is the product measure.

**Theorem (one pairing).** Let \(n=\varrho+1\), and for each \(v\) let \(\mathsf g(Z(\gamma_v))>0\), \(\rho_v\ge b^{6n+2}\), and suppose there is \(y'\) with \(y'_v\) and \(\gamma_v^{-1}y'_v\) in the [[proofs/grh/spanning-core/bessel-length|frame box]] of radius \(\rho_v\). Let \(\varphi\colon G_1^\iota\to\mathbb{C}\) be measurable with \(\lvert\varphi\rvert\le1\), invariant under left multiplication by tuples of elements fixing the frame, and such that \(\varphi(y)\mathcal K^{\mathrm{cut}}_\gamma(y)\ne0\) implies that every \(y_v\) lies in the frame box of radius \(\rho_v\). Then \(\varphi\,\mathcal K_\gamma^{\mathrm{cut}}\) has compact support and
\[
\Bigl\lVert\int\varphi(y)\,\mathcal K^{\mathrm{cut}}_\gamma(y)\,dy\Bigr\rVert\le\sqrt{\prod_v\mathrm{PB}_v}+\int\lvert\varphi(y)\rvert\,\bigl\lVert\mathcal K^{\mathrm{full}}_\gamma(y)-\mathcal K^{\mathrm{cut}}_\gamma(y)\bigr\rVert\,dy ,
\]
where \(\mathrm{PB}_v\) is the [[proofs/grh/spanning-core/local-bounds-of-a-bessel-function|pairing bound]] at \(\gamma_v\) with parameters \(\deg_v,\rho_v,\lvert I_v\rvert\).

## Proof

*Step 0 (adjoint).* Let \(\Pi^\sigma_\gamma(z)_{(i,j)}=\prod_vW^\sigma_{v,i_v}(\gamma_vz_v)\overline{W^\sigma_{v,j_v}(z_v)}\). Then \(\mathcal K^\sigma_\gamma(y)\) is the conjugate transpose of \(\Pi^\sigma_{\gamma^{-1}}(y)\), and conjugate transposition is a real-linear isometry of the Hilbert–Schmidt norm commuting with integrals. Moreover \(Z(\gamma^{-1})=Z(\gamma)^*\) (library statement `New.Filling.frameGram_inv`), so \(\mathsf g(Z(\gamma_v^{-1}))=\mathsf g(Z(\gamma_v))\) and the pairing bounds agree. Hence it suffices to prove the statement for \(\Pi\) with \(\gamma\) in place of \(\gamma^{-1}\) (the hypotheses on \(y'\) are symmetric: use \(\gamma^{-1}y'\)), and \(\bar\varphi\) in place of \(\varphi\).

*Step 1 (the full kernel after a shift).* At each \(v\) take an [[proofs/grh/spanning-core/open-cell-bound-exists|open cell bound]] \((A_v,\nu_v,m_v,t_v)\) for \((X_v,\gamma_v,\rho_v)\) (note \(\rho_v\ge b\) as \(b\ge1\)). The contraction property multiplies over a finite product (library statement `New.IsL2Contraction.pi`: for product measures and product kernels), so with \(N(x)=\bigl\lVert\int_{\prod A_v}\varphi(z)\,\Pi^{\mathrm{full}}_\gamma\bigl(t(x)z\bigr)dz\bigr\rVert^2\), using the invariance of \(\varphi\) under the shifts,
\[
\int N(x)\,d\textstyle\prod_vm_v\le\int\lvert\varphi\rvert^2d\prod_v\nu_v\le\prod_v\nu_v(G_1)\le\prod_v\mathrm{PB}_v .
\]
As \(\prod m_v\) is a probability measure, some \(x\) outside any given null set has \(N(x)\) at most the mean; choose it also such that property 4 of the open cell bounds holds at \(x\). With \(t=t(x)\) (a tuple fixing the frames) and \(A=\prod A_v\), compact:
\[
\Bigl\lVert\int_A\varphi(tz)\Pi^{\mathrm{full}}_\gamma(tz)\,dz\Bigr\rVert\le\sqrt{\textstyle\prod_v\mathrm{PB}_v},
\]
and \(A\) contains every \(z\) with \(z_v\) in the frame box of radius \(\rho_v\) and \(\ell(\gamma_vt_vz_v)\le\rho_v\) for all \(v\).

*Step 2 (the cut kernel lives on \(tA\)).* If \(\varphi(tz)\Pi^{\mathrm{cut}}_\gamma(tz)\ne0\) then: by hypothesis \(t_vz_v\) is in the frame box, hence so is \(z_v\) (as \(t_v\) fixes the frame); and \(W_v^\flat(\gamma_vt_vz_v)\neq0\) forces \(\ell(\gamma_vt_vz_v)\le b^{6n+2}\le\rho_v\) ([[proofs/grh/spanning-core/cut-pair-of-bessel-functions|cut pair]], property 4). So \(z\in A\). Thus \(\varphi\Pi^{\mathrm{cut}}_\gamma\) is supported in the compact set \(tA\), and by invariance of Haar measure \(\int\varphi\Pi^{\mathrm{cut}}_\gamma=\int_A(\varphi\Pi^{\mathrm{cut}}_\gamma)(tz)\,dz\).

*Step 3.* On \(A\) write cut \(=\) full \(-\) (full \(-\) cut); the kernels are continuous, so integrable on \(A\). The first term is bounded by Step 1, the second by \(\int\lvert\varphi\rvert\lVert\Pi^{\mathrm{full}}_\gamma-\Pi^{\mathrm{cut}}_\gamma\rVert\) over all of \(G_1^\iota\) (translation invariance). \(\blacksquare\)

## References

1. Lean: `New.BesselSystem.enorm_integral_pairKernel_cut_le`, `New.BesselSystem.exists_isCompact_enorm_integral_piKernel_le`, `New.BesselSystem.hasCompactSupport_and_enorm_integral_piKernel_le` in `src/New/Spanning/Bessel/OpenCellPairing.lean`.
