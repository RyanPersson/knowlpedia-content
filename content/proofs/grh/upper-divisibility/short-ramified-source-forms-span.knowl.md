+++
id = "proofs/grh/upper-divisibility/short-ramified-source-forms-span"
title = "Short ramified source forms span"
kind = "theorem"
summary = "The ramified source forms are spanned by forms that are integral at every prime and whose conjugates have squared norm at most the exponential of the error unit."
aliases = ["short source forms span"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.span_isShort_ramifiedSourceForms_eq_top", "New.Data.span_isShort_eq_top", "New.Data.isShort_ramifyingOp", "New.Data.sum_height_mul_columnCount_le", "New.span_setOf_mem_eq_top_of_eq_range"]
lean_files = ["src/New/UpperBound/Size/ShortColumns.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], with \(f\) infinite places of \(E\) and [[?lean:New.Data.errorUnit|error unit]] \(\mathrm{err}=f\,a\,(\log b)^3\).

1. The space \(\mathcal S\) of source forms is spanned by its [[proofs/grh/upper-divisibility/short-form|\(B\)-short]] elements for \(B=e^{\mathrm{err}}/4^{f}\).
2. The space \(\mathcal S^{\mathrm{ram}}\) of [[proofs/grh/upper-divisibility/ramified-source-forms|ramified source forms]] is spanned by its \(e^{\mathrm{err}}\)-short elements.

## Proof

(1) Apply the theorem that [[proofs/grh/upper-divisibility/short-forms-span-at-a-free-level|short forms span at a free level]] to the level of stage \(0\), which is free ([[?lean:New.Data.classAut_levelX_zero_eq_bot|`classAut_levelX_zero_eq_bot`]]), with the natural number \(q_1d\), which lies in the different of \(E\) ([[?lean:New.Parameters.conductor_mem_differentIdeal|`conductor_mem_differentIdeal`]]). The rank of \(X_0\) is \(k\). In the weight of \(X_0\) the only columns of height below \(k\) are of height \(1\), and there are at most \(a\) of them at each place (\(a\) at an a-place, none elsewhere); so the number of boxes in columns of height below \(k\) is at most \(fa\), and one may take \(M=kf+fa\). The constant is \(C=6q_1d(fk)^2\), and the required inequality
\[
4^{f}\bigl(6q_1d(fk)^2\bigr)^{6(kf+fa)}\le e^{\mathrm{err}}
\]
is one of the size comparisons of the data, obtained from the logarithmic bounds of [[?lean:New.Data.le_of_hasLogBound|`le_of_hasLogBound`]].

(2) By the [[proofs/grh/upper-divisibility/ramified-source-forms-are-the-image-of-the-ramifying-operator|description as an image]], \(\mathcal S^{\mathrm{ram}}\) is the image of \(R=\prod_{w\mid\pi_N}(1-z_w)\). Each scalar matrix \(z_w\) is integral, so by the property of short forms under \(\varphi\mapsto\varphi-k\varphi\), each factor multiplies the bound by at most \(4\); there are \(f\) factors, so \(R\) maps \(e^{\mathrm{err}}/4^{f}\)-short forms to \(e^{\mathrm{err}}\)-short forms. The image of a spanning set under \(R\) spans the image of \(R\), and it consists of short ramified forms. \(\blacksquare\)

*Status.* The freeness of the level, the membership of \(q_1d\) in the different, and the numerical inequality are quoted from other files.

## Remarks

This is the first half of Theorem A (short forms) of the reading guide; it is used in [[?lean:New.Data.span_short_integralRamified_eq_top|`span_short_integralRamified_eq_top`]].

## References

1. Lean: `New.Data.span_isShort_ramifiedSourceForms_eq_top`, `New.Data.span_isShort_eq_top`, `New.Data.isShort_ramifyingOp` in `src/New/UpperBound/Size/ShortColumns.lean`.
