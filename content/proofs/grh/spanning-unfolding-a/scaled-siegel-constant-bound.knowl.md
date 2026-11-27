+++
id = "proofs/grh/spanning-unfolding-a/scaled-siegel-constant-bound"
title = "The scaled Siegel constant is bounded by the main second moment"
kind = "lemma"
summary = "For admissible data, |S-bar| |U-bar| n_X c_S is at most (1 + b^-9) M deg c_G^f / vol^n (cov Lambda / d)^2."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.scaledSiegelConst_le"]
lean_files = ["src/New/Spanning/Unfolding/FillingAdmissible.lean"]
proof_status = "full"
+++

**Lemma.** Let \(D\) be [[?lean:New.Data|admissible data]] with [[?lean:New.Data.filling|filling data]] \(S_D\), \(f\) [[?c:Infinite place of a number field|infinite places]], \(n=\varrho+1\). Let \(a_{*}=\lvert\bar{\mathsf S}\rvert\cdot\lvert\bar{\mathsf U}\rvert\cdot n_X\cdot c_S\) be the [[?lean:New.Filling.scaledSiegelConst|scaled Siegel constant]] (\(\bar{\mathsf S},\bar{\mathsf U}\) the reductions of the Bessel subgroup and of the unipotent group, \(n_X\) the number of classes, \(c_S\) the [[?lean:New.Filling.siegelConst|Siegel constant]]). Then
\[
a_{*}\le(1+b^{-9})\,\mathcal M\,\deg\,\frac{c_G^{\,f}}{\operatorname{vol}(\widehat{\mathcal O})^{n}}\Bigl(\frac{\operatorname{cov}_{\mathsf U}\,\Lambda}{d}\Bigr)^{2},
\]
where \(\mathcal M\) is the main second moment, \(\deg\) and \(d\) the degree and the number of coordinates of the Bessel systems, \(c_G\) the [[?lean:New.Shape.openCellConst|open cell constant]], \(\operatorname{cov}_{\mathsf U}\) the [[?lean:New.Filling.unipotentCovolume|unipotent covolume]] and \(\Lambda\) the [[?lean:New.Filling.frameScaleProd|product of frame scales]]. This is the last of the [[?lean:New.Filling.IsAdmissible|standing hypotheses]].

## Proof

We show that \(a_{*}\) equals \(\lvert\bar H\rvert\,n_X\prod_v\operatorname{fr}_vd_v^2/\deg_v\) times the factor \(\sigma=\deg\,c_G^f\operatorname{vol}(\widehat{\mathcal O})^{-n}(\operatorname{cov}_{\mathsf U}\Lambda/d)^2\); the lemma then follows from the first of the [[proofs/grh/spanning-unfolding-a/mean-value-bounds-for-the-main-second-moment|mean value bounds]].

- By the theorem on the [[proofs/grh/spanning-unfolding-a/reduced-bessel-group|reduced Bessel group]], \(\lvert\bar{\mathsf S}\rvert=\lvert\bar H\rvert\lvert\bar{\mathsf U}\rvert\), so \(a_{*}=\lvert\bar H\rvert\,n_X\,\lvert\bar{\mathsf U}\rvert^2c_S\).
- With \(\delta=\varrho(\varrho+k)=\sum_{a<\varrho}(2a+k+1)\), the definition of the covolume gives \(\operatorname{cov}_{\mathsf U}\Lambda=\lvert\bar{\mathsf U}\rvert\,N^{-kf}\operatorname{vol}(\widehat{\mathcal O})^{-\delta}\lvert\operatorname{disc}E\rvert^{\varrho/4}\), because \(\lvert\bar{\mathsf U}\rvert=M^{f\varrho(2k+2\varrho+1)}=M^{f(2\delta+\varrho)}\) ([[proofs/grh/spanning-unfolding-a/reduced-unipotent-group|order of the reduced unipotent group]]).
- Hence \(\lvert\bar H\rvert n_X\bigl(\prod_v\operatorname{fr}_v\bigr)\frac{d^2}{\deg}\,\sigma=\lvert\bar H\rvert n_X\lvert\bar{\mathsf U}\rvert^2\cdot\bigl(\prod_v\operatorname{fr}_v\bigr)c_G^f\lvert\operatorname{disc}E\rvert^{\varrho/2}\cdot N^{-2kf}\operatorname{vol}(\widehat{\mathcal O})^{-(n+2\delta)}\).
- By the identity for the [[proofs/grh/spanning-unfolding-a/product-of-frame-masses-and-open-cell-constant|product of the frame masses]], \(\bigl(\prod_v\operatorname{fr}_v\bigr)c_G^f\lvert\operatorname{disc}E\rvert^{\varrho/2}=c_SN^{2kf}\operatorname{vol}(\widehat{\mathcal O})^{\varrho+1+2\delta}\), and \(n=\varrho+1\). So the expression equals \(\lvert\bar H\rvert n_X\lvert\bar{\mathsf U}\rvert^2c_S=a_{*}\).

## References

1. Lean: `New.Data.scaledSiegelConst_le` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
