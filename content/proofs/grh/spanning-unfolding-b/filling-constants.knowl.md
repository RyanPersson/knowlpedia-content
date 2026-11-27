+++
id = "proofs/grh/spanning-unfolding-b/filling-constants"
title = "Constants of a filling datum"
kind = "notation"
summary = "The frame scales, the unipotent covolume, the Siegel constant, the source dimension, the main and identity second moments, the tail scale and the box radius of a filling datum."
aliases = ["unipotent covolume", "Siegel constant of a filling datum", "main second moment", "identity second moment", "tail scale", "frame scale product"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.frameScaleSq", "New.Filling.frameScaleProd", "New.Filling.unipotentCovolume", "New.Filling.siegelConst", "New.Filling.sourceDim", "New.Filling.besselDegree", "New.Filling.mainSecondMoment", "New.Filling.unipotentOrder", "New.Filling.scaledSiegelConst", "New.Filling.identitySecondMoment", "New.Filling.tailScale", "New.Filling.frameBoxRadius", "New.Filling.frameScaleSq_pos", "New.Filling.frameScaleProd_pos", "New.Filling.unipotentCovolume_pos", "New.Filling.besselDegree_pos", "New.Filling.abs_realM_eq", "New.Filling.realM_ne_zero"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) of shape \((\varrho,\kappa,k_0)\), with \(k=\lvert\kappa\rvert\), \(n=\varrho+1\), \(r=2\varrho+k+1\), \(f\) the number of infinite places, \(D_E\) the [[algebra-fields-galois/number-field-discriminant|discriminant]] of \(E\), and \(\kappa_v\) the real numbers of the [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|scales]]. Put \(\operatorname{vol}(\widehat{\mathcal{O}})=2^{r_2}/\sqrt{\lvert D_E\rvert}\), with \(r_2\) the number of complex places ([[?lean:New.volÔ|volume of the integral adeles]]). The following numbers are attached to \(S\).

| Symbol | Definition | Name |
|---|---|---|
| \(\lambda_{v,a}\) | \(\kappa_v^{2(\varrho-a)}/N\), for \(0\le a\le\varrho\) | squared frame scale |
| \(\Lambda\) | \(\prod_v\prod_{a=0}^{\varrho}\lambda_{v,a}^{\,k+2(\varrho-a)}\) | frame scale product |
| \(\operatorname{cov}_{\mathsf U}\) | \(\bigl(M^{\varrho(2\varrho+2k+1)}/N^{k}\bigr)^{f}\cdot\operatorname{vol}(\widehat{\mathcal{O}})^{-\varrho(\varrho+k)}\cdot\lvert D_E\rvert^{\varrho/4}\big/\Lambda\) | unipotent covolume |
| \(c_S\) | \(\bigl(\pi^k/((k-1)!\,N^k)\bigr)^{f}\cdot\lvert D_E\rvert^{1/4}\cdot\operatorname{vol}(\widehat{\mathcal{O}})^{k}\) | Siegel constant |
| \(\dim_S\) | \(\lvert\mathcal{C}\rvert\cdot\lvert I\rvert\), with \(\mathcal{C}\) the [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|classes]] and \(I\) the Bessel coordinates | source dimension |
| \(\deg\) | \(\prod_v\deg(\mathcal{B}_v)\), the product of the degrees of the Bessel systems | Bessel degree |
| \(\mathcal{M}_{\mathrm{main}}\) | \(\dim_S^2\big/\bigl(\deg\cdot\operatorname{mass}(r)\bigr)\), with \(\operatorname{mass}(r)\) the [[?lean:New.mass|mass]] of the genus of the standard lattice of rank \(r\) | main second moment |
| \(\lvert\bar{\mathsf U}\rvert\) | \(M^{f\varrho(2k+2\varrho+1)}\) | unipotent order |
| \(a_*\) | \(\lvert\bar R_0\rvert\cdot M^{f\varrho(2k+2\varrho+1)}\cdot\lvert\mathcal{C}\rvert\cdot c_S\), with \(\bar R_0\) the [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|reduced image]] of the [[?lean:New.Shape.Form.besselS|Bessel subgroup]] | scaled Siegel constant |
| \(\mathcal{M}_{\mathrm{id}}\) | \(\lvert\bar R_0\rvert\cdot\dim_S\) | identity second moment |
| \(\tau\) | \(b^{kf/4}\) | tail scale |
| \(\rho_{\mathrm{box}}\) | \(b^{37n}\) | frame box radius |

The numbers \(\lambda_{v,a}\), \(\Lambda\), \(\operatorname{cov}_{\mathsf U}\) and \(\deg\) are positive.

## Remarks

The exponent in \(\operatorname{cov}_{\mathsf U}\) arises as \(d=\sum_{a<\varrho}(2a+k+1)=\varrho(\varrho+k)\), with \(2d+\varrho=\varrho(2\varrho+2k+1)\). The name of \(\operatorname{cov}_{\mathsf U}\) records its role: for every class \(c\) it is the covolume of \(\mathsf{U}_c(M)\) in the real unipotent group ([[?lean:New.Filling.lintegral_classCutoff_eq_unipotentCovolume|covolume of the class unipotent group]]); the definition itself is just the displayed number. Positivity: \(\kappa_v\ne0\) and the exponent \(2(\varrho-a)\) is even, \(N>0\), \(M>0\), \(D_E\neq0\), and each Bessel system has positive degree.

With \(\lvert D_E\rvert=\mathrm{rd}_E^{2f}\) and \(\operatorname{vol}(\widehat{\mathcal{O}})=(2/\mathrm{rd}_E)^f\) for the totally complex field \(E\), one has \(c_S=\bigl((2\pi)^k\,\mathrm{rd}_E^{1/2-k}/((k-1)!\,N^k)\bigr)^f\).

## References

1. Lean: `New.Filling.frameScaleProd`, `New.Filling.unipotentCovolume`, `New.Filling.siegelConst`, `New.Filling.sourceDim`, `New.Filling.mainSecondMoment`, `New.Filling.scaledSiegelConst`, `New.Filling.identitySecondMoment`, `New.Filling.tailScale`, `New.Filling.frameBoxRadius` in `src/New/Spanning/Unfolding/Setup.lean`.
