+++
id = "proofs/grh/reduction-main/data-sizes"
title = "Sizes of the data"
kind = "lemma"
summary = "The size estimates for the scales, ranks, field invariants, weights, the principal level M, the number Omega and the level N that hold for all data."
aliases = ["sizes of the data"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.x_pow_le_x₁", "New.Data.x₁_pow_le_b", "New.Data.logX₁_pow_le_logB", "New.Data.logB_pow_le_x", "New.Data.m_sq_mem_Icc", "New.Data.towerExp_ne_zero", "New.Data.x₁_pow_le_sqrt_b", "New.Data.r_le_two_mul_k", "New.Data.m_pow_eq_two_pow_towerExp", "New.Data.m_pow_le_two_pow_l₀", "New.Data.f_mem_Icc", "New.Data.f_even", "New.Data.q₁_le", "New.Data.q₂_le", "New.Data.log_classNumber_le", "New.Data.a_div_x₁_mem_Icc", "New.Data.levelPrime_mem_Ioo", "New.Data.bigOmega_le_one", "New.Data.log_M_div_bigOmega_mem_Icc", "New.Data.abs_log_M_mul_rootDisc_le", "New.Data.M_mem_Icc", "New.Data.weight_mem_Icc", "New.Data.weight_le_b", "New.Data.weight_add_x_pow_le_two_mul_b", "New.Data.weight_le_liftWeight_sub", "New.Data.shiftedWeight_mem_Icc", "New.Data.log_shiftedWeight_le", "New.Data.liftWeight_le_weight_add", "New.Data.liftWeight_le_two_mul_b", "New.Data.log_liftWeight_le", "New.Data.logLevelTarget", "New.Data.logLevelTarget_eq_logLevelMin", "New.Data.logLevelTarget_mem_Icc", "New.Data.N_modEq_one", "New.Data.log_N_mem_Icc_logLevelTarget", "New.Data.log_N_mem_Icc"]
lean_files = ["src/New/Reduction/Data/Sizes.lean", "src/New/Reduction/Data/LevelAndTwists.lean", "src/New/Reduction/Data/Magnitudes.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(D\) be [[proofs/grh/reduction-main/data|data]], with the [[proofs/grh/reduction-main/data-derived-quantities|derived quantities]]. Then:

| Quantity | Estimate |
|---|---|
| scales | \(x^{10^6}\le x_1\), \(x_1^{10^6}\le b\), \((\log x_1)^6\le\log b\), \((\log b)^{100}\le x\), \(x_1^{3l_0^2}\le\sqrt b\) |
| \(m\), \(s\), \(l_0\) | \(x\le m^2\le4x\); \(s\ne0\); \(m^{22}=2^s\); \(m^{594}\le2^{l_0(s)}\) |
| \(f\), \(q_1\), \(q_2\) | \(m^{22}\le f\le q_1\le x^{12}\); \(f\) even; \(q_2(s)\le x^{33q_0d}\) |
| \(\mathrm{rd}_E\), class number | \(x^{10}\le\mathrm{rd}_E\le x^{12}\); \(\log h_E\le x^{30}\) |
| weights | \(x^{999}\le a/x_1\le\kappa(\sigma)\le a/x=b\); \(a/x_1\le b/x^{999}\); \(\kappa+x^{42}\le2b\) |
| shifted weights, \(i\le4m\) | \(\kappa\le\kappa^{(i)}\le\kappa+x^{42}\); \(\log\kappa^{(i)}\le\log\kappa+1/x\); \(\kappa\le\kappa_j-\Delta/2\); \(\kappa_j\le2b\) for \(j\le2m\) |
| \(M\), \(p_i\) | \(b^{20}\le M\le b^{22}\); \(b^2<p_i<N\) |
| \(\Omega\) | \(x^{-13}\le\Omega\le1\); \(20\log b\le\log(M/\Omega)\le23\log b\); \(\lvert\log(M\,\mathrm{rd}_E/2\pi)\rvert\le23\log b\) |
| \(N\) | \(m\log b\le\log N_-\le24m\log b\); \(\log N_-\le\log N\le\log N_-+\sqrt{\log b}\); \(m\log b\le\log N\le30m\log b\); \(N\ge b^{101}\); \(N\equiv1\pmod{q_1d}\) |

## Proof

Outline. The first four estimates of the first row restate (S2)–(S5) after exponentiating. The fifth also uses the tower exponent: \(l_0\le81s\) and \(s\le32\log x\le\log x_1\), so \(3l_0^2\log x_1\le3\cdot81^2(\log x_1)^3\le\tfrac12(\log x_1)^6\le\tfrac12\log b\), as \(\log x_1\) is large. \(m^{22}=2^s\) is (R1); \(m^{594}=(m^{22})^{27}=2^{27s}\le2^{l_0}\) as \(27s<l_0\). \(f=\operatorname{towerDeg}(s)\varphi(q_0)\) ([[proofs/grh/reduction-main/field-e-properties|properties of \(E\)]]) lies between \(2^s\) and \(q_0\operatorname{towerDeg}(s)=q_1\), and is even because \(s\ne0\). The weights: \(\kappa\in\{a/x,a/x_1\}\), and \(\log(a/x_1)=\log x+\log b-\log x_1\) with (S3), (S4). \(M=p_0p_1\) with (L2). \(\log N\): (L4) with the bounds for \(\log N_-\) proved in [[proofs/grh/reduction-main/data-exist|existence of the data]] and \(\sqrt{\log b}\le6m\log b\). The class number bound uses a Minkowski-type bound \(h_E\le(2^n\lvert d_E\rvert)^{n+1}\), \(n=[E:\mathbb Q]=2f\) (`classNumber_le`, asserted). The bounds \(x^{10}\le\mathrm{rd}_E\le x^{12}\) are proved in another chapter, [[proofs/grh/derivatives-divisibility/size-of-the-different|size of the different]] (`New.Data.rootDisc_mem_Icc` in `src/New/Derivatives/Field/ChosenPlaces.lean`): \(\mathrm{rd}_E^{\,f}\) is the product over the infinite places of the absolute values of a generator of the different, each in \([x^{10},x^{12}]\). All remaining estimates are comparisons of exponents by the [[proofs/grh/reduction-main/log-bound-calculus|calculus of logarithmic bounds]] and are asserted with the Lean declarations listed in the front matter; I checked the statements, not each numerical comparison.

## References

1. Lean: the declarations in the front matter, in `src/New/Reduction/Data/Sizes.lean`, `src/New/Reduction/Data/LevelAndTwists.lean` and `src/New/Reduction/Data/Magnitudes.lean`.
