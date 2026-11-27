+++
id = "proofs/grh/reduction-main/inverse-ratio-height"
title = "The height of Z(1)/Z(xi) for a regular family of twists"
kind = "theorem"
summary = "There is a family of m-fold twists with small ratios for which Z(1)/Z(xi_iota) has height at most d_T (b + f a log^4 b - h_main)."
aliases = ["inverse ratio", "heightLe_chainDeterminant_one_div", "single lifts at good twists"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div", "New.Data.exists_chainDeterminant_one_div_eq", "New.Data.heightLe_chainDeterminant_one_div"]
lean_files = ["src/New/Determinant/Twist/LongForms.lean"]
proof_status = "full"
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]], \(d_T\) the dimension of the target, \(Z(\vartheta)\) the [[?lean:New.Data.chainDeterminant|chain determinant]] and \(Z_j(\vartheta^j):=\det(u^*u)\) the [[?lean:New.Data.liftDeterminant|lift determinant]], where \(u\) is the \(j\)-th single lift \(W_j\to V_j\) for the character \(\vartheta^j\) *restricted to the good forms on \(W_j\)* (the [[proofs/grh/reduction-main/regular-family-of-twists|good lift]]; the same restriction at the trivial twist), for an [[proofs/grh/reduction-main/m-fold-twist|\(m\)-fold twist]] \(\vartheta\). Put \(F=f\,a\,(\log b)^4\).

**Theorem.**

1. **(Single lifts at good twists.)** There is a family \(\theta=(\theta_\iota)\) of \(m\)-fold twists with [[proofs/grh/reduction-main/regular-family-of-twists|small ratios]] such that for every \(1\le j\le m\) the family \(\iota\mapsto Z_j(1)/Z_j(\theta_\iota^{\,j})\) has [[proofs/grh/reduction-main/height-bound|height at most]] \(d_T\bigl(F/m-k\,h_{\mathrm{dir}}\bigr)\).
2. **(Inverted factorisation.)** There is an integer \(e\) such that for every \(m\)-fold twist \(\vartheta\)
\[
\frac{Z(1)}{Z(\vartheta)}=\Bigl(\mathrm{Nm}Q(\vartheta)^{e/2}\prod_{1\le i<j\le m}\operatorname{quot}_{i,j}(\vartheta)\Bigr)^{-d_T}\cdot\prod_{j=1}^m\frac{Z_j(1)}{Z_j(\vartheta^j)} ,
\]
with the [[?lean:New.Data.quotientRatio|quotient ratios]] \(\operatorname{quot}_{i,j}\).
3. **(The inverse ratio.)** If \(\theta\) has small ratios and satisfies the height bounds of (1), then \(\iota\mapsto Z(1)/Z(\theta_\iota)\) has height at most \(d_T\bigl(b+F-h_{\mathrm{main}}\bigr)\).

## Proof

Complete relative to the quoted results.

(1) Take a [[?lean:New.exists_isRegularFamily|regular family]] \(\theta\). By the [[?lean:New.Data.heightLe_liftDeterminant_ratio|cost of one lift]], \(Z_j(1)/Z_j(\theta_\iota^j)\) has height at most \(d_T\,k\,(\log b\cdot\operatorname{budget}-h_{\mathrm{dir}})\), and \(k\log b\cdot\frac{fa\log^3b}{mk}=F/m\).

(2) Invert the [[?lean:New.Data.exists_chainDeterminant_pos_and_div_chainDeterminant_one_eq|factorisation of the chain determinant]], \(Z(\vartheta)/Z(1)=(\cdots)^{d_T}\prod_jZ_j(\vartheta^j)/Z_j(1)\).

(3) By the [[?lean:New.Data.HasSmallRatios.heightLe_inv_rpow_mul_prod_quotientRatio|height of the quotient ratios]] the inverse of the scalar in (2) has height at most \(m^2tx_1\le b\). By the power and product rules of [[proofs/grh/reduction-main/height-calculus|the calculus of heights]] and (2), the height of \(Z(1)/Z(\theta_\iota)\) is at most
\[
d_T\,b+\sum_{j=1}^m d_T\bigl(F/m-k\,h_{\mathrm{dir}}\bigr)=d_T\bigl(b+F-mk\,h_{\mathrm{dir}}\bigr)=d_T(b+F-h_{\mathrm{main}}).
\]

## References

1. Lean: `New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div`, `New.Data.exists_chainDeterminant_one_div_eq`, `New.Data.heightLe_chainDeterminant_one_div` in `src/New/Determinant/Twist/LongForms.lean`.
