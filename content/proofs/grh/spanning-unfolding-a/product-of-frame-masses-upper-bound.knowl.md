+++
id = "proofs/grh/spanning-unfolding-a/product-of-frame-masses-upper-bound"
title = "Upper bound for the product of the frame masses"
kind = "theorem"
summary = "The product of the frame masses over the infinite places is at most N^(kf) mass_k / mass_r up to a factor close to one."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.prod_frameMass_mul_le", "New.Data.log_pow_div_pow_sub_one_le", "New.Data.sum_two_div_two_pow_le_log_sub", "New.Data.abs_sum_log_mass_ratio_sub_le"]
lean_files = ["src/New/Spanning/Unfolding/FrameMass.lean"]
proof_status = "full"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]] with field \(E\) having \(f\) [[?c:Infinite place of a number field|infinite places]], level prime \(N\), scale \(b\) and ranks \(k\le r\). Let \(\operatorname{fr}_v\) be the [[proofs/grh/spanning-unfolding-a/frame-mass|frame mass]] at the infinite place \(v\) and \(\operatorname{mass}_l\) the [[?lean:New.mass|mass]] of the genus of \(\mathcal{O}_E^l\). Then
\[
\Bigl(\prod_{v}\operatorname{fr}_v\Bigr)\cdot\operatorname{mass}_r\cdot\Bigl(\frac{N^k}{N^k-1}\Bigr)^{2f}\;\le\;\bigl(1+b^{-9}\bigr)\,N^{kf}\,\operatorname{mass}_k .
\]
Equivalently \(\prod_v\operatorname{fr}_v\le(1+b^{-9})(1-N^{-k})^{2f}N^{kf}\operatorname{mass}_k/\operatorname{mass}_r\).

## Proof

Put \(S=\prod_{i=k}^{r-1}\prod_v\operatorname{sph}_{i+1}(v)>0\), with \(\operatorname{sph}\) the [[proofs/grh/spanning-unfolding-a/unit-sphere-mass|mass of the unit sphere]]; then \(\prod_v\operatorname{fr}_v=N^{kf}S\), and the masses are positive. It suffices to prove
\[
\log S+\log\operatorname{mass}_r+2f\log\frac{N^k}{N^k-1}\le\log(1+b^{-9})+\log\operatorname{mass}_k .\tag{1}
\]

*Telescoping.* Write \(\log\operatorname{mass}_r-\log\operatorname{mass}_k=\sum_{i=k}^{r-1}(\log\operatorname{mass}_{i+1}-\log\operatorname{mass}_i)\). By property 5 of the sphere mass, for each \(k\le i<r\),
\[
\log\operatorname{mass}_{i+1}-\log\operatorname{mass}_i+\log\prod_v\operatorname{sph}_{i+1}(v)\le\frac{2}{2^\varrho},
\]
so that \(\log\operatorname{mass}_r-\log\operatorname{mass}_k+\log S\le(r-k)\,2/2^{\varrho}\).

*The error budget.* The size calculus of the data ([[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic bounds]]) gives
\[
(r-k)\frac{2}{2^\varrho}+2f\cdot\frac2N\le\frac{2b^{-9}}{b^{-9}+2},
\]
and \(2y/(y+2)\le\log(1+y)\) for \(y\ge0\). Hence \((r-k)\,2/2^\varrho\le\log(1+b^{-9})-2f\cdot\frac2N\).

*The factor at \(N\).* Since \(N\ge2\) and \(k\ge1\), \(N^k\ge N\) and \(N^k-1>0\); by \(\log y\le y-1\),
\[
\log\frac{N^k}{N^k-1}\le\frac{1}{N^k-1}\le\frac{2}{N},
\]
the last inequality being \(N\le 2N^k-2\). Thus \(2f\log\frac{N^k}{N^k-1}\le 2f\cdot\frac2N\).

Adding the three displays gives (1). Exponentiating and multiplying by \(N^{kf}\) gives the theorem.

## Remarks

The same summation gives the two-sided statement recorded in the source: the sum over \(k\le i<r\) of \(\log\operatorname{mass}_{i+1}-\log\operatorname{mass}_i-f\bigl((i+\tfrac12)\log\mathrm{rd}_E+\log i!-(i+1)\log2\pi\bigr)\) has absolute value at most \(\log(1+b^{-9})-2f\cdot\frac2N\).

## References

1. Lean: `New.Data.prod_frameMass_mul_le` in `src/New/Spanning/Unfolding/FrameMass.lean`.
2. Lean: `New.Data.log_pow_div_pow_sub_one_le` in `src/New/Spanning/Unfolding/FrameMass.lean`.
3. Lean: `New.Data.sum_two_div_two_pow_le_log_sub` in `src/New/Spanning/Unfolding/FrameMass.lean`.
4. Lean: `New.Data.abs_sum_log_mass_ratio_sub_le` in `src/New/Spanning/Unfolding/FrameMass.lean`.
