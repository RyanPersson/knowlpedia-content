+++
id = "proofs/grh/spanning-core/second-moment-of-the-poincare-map"
title = "Second moment of the Poincaré map"
kind = "theorem"
summary = "The sum over the finite group of the squared Hilbert–Schmidt norms of P* s P is at most (1 + 9 b^-4) D_X^2 / (deg mass), and the target dimension times it is at most #G (1 + 9 b^-4) D_X^2."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.sum_hilbertSchmidtNorm_scaledPoincare_sq_le", "New.Data.targetDim_mul_sum_hilbertSchmidtNorm_sq_le"]
lean_files = ["src/New/Spanning/SecondMoment/SpanningTheorem.lean"]
proof_status = "outline"
+++

**Theorem (second moment).** Let \(D\) be admissible data, \(P\) the [[proofs/grh/spanning-core/scaled-poincare-map|scaled Poincaré map]], \(\rho\) the action of the finite group \(\bar G\) on the forms of principal level on \(Y_0\), \(b\) the scale and \(D_X\) the dimension of the source. Then, in [[proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map|Hilbert–Schmidt norm]],
\[
\sum_{s\in\bar G}\lVert P^*\rho(s)P\rVert_{\mathrm{HS}}^2\ \le\ \Bigl(1+\frac9{b^4}\Bigr)\frac{D_X^2}{\deg\cdot\mathrm{mass}_r}
\qquad\text{and}\qquad
d_{\mathrm{tar}}\sum_{s\in\bar G}\lVert P^*\rho(s)P\rVert_{\mathrm{HS}}^2\ \le\ \lvert\bar G\rvert\Bigl(1+\frac9{b^4}\Bigr)D_X^2 ,
\]
with \(\deg\), \(\mathrm{mass}_r\) and \(d_{\mathrm{tar}}\) as in [[proofs/grh/spanning-core/dimension-of-the-target|the dimension of the target]]. The quantity \(D_X^2/(\deg\cdot\mathrm{mass}_r)\) is the [[?lean:New.Filling.mainSecondMoment|main second moment]].

## Proof

*Outline.* The first inequality is [[?lean:New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le|`New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le`]] (area of `New/Spanning/Unfolding`), applied to \(P\), which has amplitude blocks by [[proofs/grh/spanning-core/unfolding-of-the-scaled-poincare-map|unfolding]], and to the unitary level representation; the sum over \(\bar G\) and the sum over the group with the places sorted by primes are the same sum. The second follows by multiplying with \(d_{\mathrm{tar}}\le\lvert\bar G\rvert\deg\,\mathrm{mass}_r\) ([[proofs/grh/spanning-core/dimension-of-the-target|dimension of the target]]); the factor \(\deg\cdot\mathrm{mass}_r>0\) cancels. \(\blacksquare\)

## References

1. Lean: `New.Data.sum_hilbertSchmidtNorm_scaledPoincare_sq_le`, `New.Data.targetDim_mul_sum_hilbertSchmidtNorm_sq_le` in `src/New/Spanning/SecondMoment/SpanningTheorem.lean`.
