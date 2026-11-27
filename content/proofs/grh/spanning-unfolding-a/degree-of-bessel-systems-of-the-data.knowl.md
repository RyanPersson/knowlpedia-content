+++
id = "proofs/grh/spanning-unfolding-a/degree-of-bessel-systems-of-the-data"
title = "The degree of the Bessel systems of admissible data"
kind = "proposition"
summary = "The Bessel degree is the product over places and over k-1 <= l < r of prod_{i<l}(s_i - s_l)/l!, and its logarithm is bounded on both sides in terms of the weights."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.log_filling_besselDegree_mem_Icc", "New.Data.filling_besselDegree_eq_exp_sum", "New.Data.targetParameter_sub_mem_Icc"]
lean_files = ["src/New/Spanning/Unfolding/FillingAdmissible.lean"]
proof_status = "outline"
+++

**Proposition.** Let \(D\) be [[?lean:New.Data|admissible data]] with ranks \(k\le r\), \(m=r-k+1\), \(f\) [[?c:Infinite place of a number field|infinite places]], scale \(x\); let \(\varsigma_i(v)\) (\(0\le i<r\)) be the entries of the [[?lean:New.Data.targetParameter|target parameter]] at the infinite place \(v\), \(W_v\) the [[?lean:New.Data.weight|weight]] at \(v\), and \(\deg=\prod_v\deg_v\) the [[?lean:New.Filling.besselDegree|Bessel degree]] of the [[?lean:New.Data.filling|filling data]]. Then:

1. for \(i<l\), \(1\le\varsigma_i(v)-\varsigma_l(v)\le w_{l+2-k}(v)\), where \(w_j(v)\) is the [[?lean:New.Data.liftWeight|lift weight]] (and \(l+2-k\) is read as \(0\) if negative);
2. \(\displaystyle\deg=\prod_v\prod_{l=k-1}^{r-1}\frac{\prod_{i<l}\bigl(\varsigma_i(v)-\varsigma_l(v)\bigr)}{l!}\);
3. \(\displaystyle\sum_vm(k-1)\log W_v\ \le\ \log\deg+f\sum_{l=k-1}^{r-1}\log l!\ \le\ \sum_vm\,r\Bigl(\log W_v+\frac1x\Bigr).\)

## Proof

1. The entries of the target parameter are strictly decreasing integers ([[?lean:New.Data.targetParameter_strictAnti|monotonicity of the target parameter]]), which gives the lower bound. The upper bound is read off from the explicit formula (\(\varsigma_i=k/2-1-i\) for \(i<k-1\) and \(\varsigma_i=\Delta/2-w_{i+2-k}\) otherwise; [[?lean:New.Data.targetParameter_eq|formula for the target parameter]]). *In the source this is a single automated case check; it is asserted here.*

2. The degree of the Bessel system at \(v\) is the value of Weyl's dimension polynomial at the doubled parameter ([[?lean:New.Filling.IsDiscreteSeriesBessel.deg_eq|degree of a discrete series Bessel system]]), i.e. \(\prod_{l<r}\prod_{i<l}(\varsigma_i-\varsigma_l)/l!\). For \(l<k-1\) the differences are \(l-i\), \(i<l\), with product \(l!\), so these factors are \(1\). *The identification of the degree with this product (reindexing of the roots by the numbering of the basis) is asserted from the source.*

3. By 2, \(\log\deg+f\sum_l\log l!=\sum_v\sum_{l=k-1}^{r-1}\sum_{i<l}\log(\varsigma_i(v)-\varsigma_l(v))\), and there are \(m\) values of \(l\). *Lower bound:* all terms are \(\ge0\) by 1; keep the \(k-1\) terms \(i<k-1\), for which \(\varsigma_i-\varsigma_l\ge W_v\) (from the formula and [[?lean:New.Data.weight_le_liftWeight_sub|the weight is below the shifted lift weights]]). *Upper bound:* each of the \(l<r\) terms is at most \(\log w_{l+2-k}(v)\le\log W_v+1/x\) ([[?lean:New.Data.log_liftWeight_le|logarithm of the lift weights]]).

## References

1. Lean: `New.Data.log_filling_besselDegree_mem_Icc` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
2. Lean: `New.Data.filling_besselDegree_eq_exp_sum` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
3. Lean: `New.Data.targetParameter_sub_mem_Icc` in `src/New/Spanning/Unfolding/FillingAdmissible.lean`.
