+++
id = "proofs/grh/spanning-unfolding-a/ratio-of-main-and-identity-second-moments"
title = "The ratio of the main second moment to the identity second moment"
kind = "theorem"
summary = "The ratio equals d (N^k-1)^f mass_k / (deg mass_r |U-bar|) and lies between b^(11kf) and (M / b^6)^(kf)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.mainSecondMoment_div_identitySecondMoment_mem_Icc", "New.Data.mainSecondMoment_div_identitySecondMoment_eq", "New.Data.abs_log_mainSecondMoment_div_identitySecondMoment_sub_le"]
lean_files = ["src/New/Spanning/Unfolding/FillingAdmissible.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]] with [[?lean:New.Data.filling|filling data]] \(S_D\); \(M=p_0p_1\), \(b\) the scale, \(k\) the rank of \(X_0\), \(f\) the number of [[?c:Infinite place of a number field|infinite places]]. Let \(\mathcal M\) be the [[?lean:New.Filling.mainSecondMoment|main second moment]] and \(\mathcal I=\lvert\bar{\mathsf S}\rvert\cdot n_Xd\) the [[?lean:New.Filling.identitySecondMoment|identity second moment]]. Then:

1. \(\dfrac{\mathcal M}{\mathcal I}=\dfrac{d\,(N^k-1)^f\operatorname{mass}_k}{\deg\cdot\operatorname{mass}_r\cdot\lvert\bar{\mathsf U}\rvert}\);
2. \(\Bigl\lvert\log\dfrac{\mathcal M}{\mathcal I}-\Bigl(fk\bigl(\log M-\tfrac{15}{2}\log b\bigr)+\log\bigl(d\,((k-1)!)^{f}\bigr)\Bigr)\Bigr\rvert\le\tfrac14fk\log b\);
3. \(b^{11kf}\le\dfrac{\mathcal M}{\mathcal I}\le\Bigl(\dfrac{M}{b^{6}}\Bigr)^{kf}\).

## Proof

**1.** \(\mathcal M/\mathcal I=n_Xd/(\lvert\bar{\mathsf S}\rvert\deg\operatorname{mass}_r)\) (the source dimension \(n_Xd\) is positive). Insert \(\lvert\bar{\mathsf S}\rvert=\lvert\bar H\rvert\lvert\bar{\mathsf U}\rvert\) ([[proofs/grh/spanning-unfolding-a/reduced-bessel-group|reduced Bessel group]]) and \(n_X=\lvert\bar H\rvert(N^k-1)^f\operatorname{mass}_k\) ([[proofs/grh/spanning-unfolding-a/number-of-classes-of-the-source-level|number of classes]]).

**2.** *(Outline.)* Take logarithms in 1 with \(\lvert\bar{\mathsf U}\rvert=M^{f\varrho(2k+2\varrho+1)}\) and insert:

- the two-sided bound for \(\log\deg+f\sum_{l=k-1}^{r-1}\log l!\) ([[proofs/grh/spanning-unfolding-a/degree-of-bessel-systems-of-the-data|degree of the Bessel systems]]);
- the approximate mass formula summed over \(k\le i<r\) (remark of the [[proofs/grh/spanning-unfolding-a/product-of-frame-masses-upper-bound|upper bound for the frame masses]]), which gives \(\log\operatorname{mass}_k-\log\operatorname{mass}_r\) up to \(\log(1+b^{-9})\) in terms of \(\log\mathrm{rd}_E\), \(\log2\pi\) and \(\sum_{i=k}^{r-1}\log i!\);
- the range of the level, \(\lambda\le\log N\le\lambda+\sqrt{\log b}\) with \(\lambda\) the [[?lean:New.Data.logLevelTarget|target for the logarithm of the level]] ([[?lean:New.Data.log_N_mem_Icc_logLevelTarget|range of \(\log N\)]]), and \(0\le\log\frac{N^k}{N^k-1}\le2/N\).

All sums of \(\log i!\) cancel except \(f\log(k-1)!\). The remaining quantity is linear in \(\log M\), \(\log\mathrm{rd}_E\), \(\log\pi\), \(\log b\), the \(\log W_v\) and \(1/x\); by the definition of \(\lambda\) the main terms combine to \(fk(\log M-\frac{15}{2}\log b)\), and the rest is bounded by \(\frac14fk\log b\) through one inequality of the size calculus of the data ([[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic bounds]]). **This step is asserted here**: in the source (the declaration named in the last reference) it is a long automated linear-arithmetic verification, which I did not reproduce by hand; in particular I did not open the definition of \(\lambda\).

**3.** By the lemma on the [[proofs/grh/spanning-unfolding-a/number-of-bessel-coordinates|number of Bessel coordinates]], \(0\le\log(d((k-1)!)^f)\le\frac54fk\log b\). The size calculus gives \(b^{19}\le M\), so \(fk\log M\ge19fk\log b\). From 2:
\[
\log\frac{\mathcal M}{\mathcal I}\ge fk\bigl(19-\tfrac{15}{2}-\tfrac14\bigr)\log b\ge11fk\log b,\qquad\log\frac{\mathcal M}{\mathcal I}\le fk\log M+fk\bigl(-\tfrac{15}{2}+\tfrac54+\tfrac14\bigr)\log b=fk(\log M-6\log b).
\]

## References

1. Lean: `New.Data.mainSecondMoment_div_identitySecondMoment_mem_Icc` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
2. Lean: `New.Data.mainSecondMoment_div_identitySecondMoment_eq` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
3. Lean: `New.Data.abs_log_mainSecondMoment_div_identitySecondMoment_sub_le` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
4. The step asserted without proof above is proved in Lean by `New.Data.abs_log_mainSecondMoment_div_identitySecondMoment_sub_le`.
