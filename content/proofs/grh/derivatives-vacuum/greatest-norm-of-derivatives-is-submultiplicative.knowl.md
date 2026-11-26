+++
id = "proofs/grh/derivatives-vacuum/greatest-norm-of-derivatives-is-submultiplicative"
title = "The greatest norm of derivatives is submultiplicative"
kind = "lemma"
summary = "The greatest norm of the n-th derivatives of integral series in y is submultiplicative in n; equivalently the least valuation is superadditive."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.maxDerivNorm_add_le", "New.CMLattice.exists_norm_coeff_subst_add_le", "New.factorial_mul_coeff_subst_add", "New.coeff_subst_mul_subst"]
lean_files = ["src/New/Derivatives/Sharpness/OneCurve.lean"]
proof_status = "full"
+++

**Lemma.** With \(c_C\) as in [[proofs/grh/derivatives-vacuum/greatest-norm-of-derivatives|the definition]], \(c_C(m+n)\le c_C(m)\,c_C(n)\) for all \(m,n\).

## Proof

Let \(y^j\) attain \(c_C(m+n)\). Consider \(G(z_0,z_1)=y(z_0+z_1)^j\). For any series \(g\), the coefficient of \(z_0^mz_1^n\) in \(g(z_0+z_1)\) is \(\binom{m+n}{m}[z^{m+n}]g\), so
\[ (m+n)!\,[z^{m+n}]y^j=m!\,n!\,[z_0^mz_1^n]G . \]
By the integrality of the group law, \(y(z_0+z_1)\) is an integral power series in \(y(z_0)\) and \(y(z_1)\) ([[?lean:New.CMLattice.translatedY_add_mem_multiSeriesRing|addition formula]]), hence so is \(G\). By [[proofs/grh/derivatives-vacuum/largest-coefficient-among-integral-series|the lemma on largest coefficients]] there are \(a,b\) with
\[ \lvert[z_0^mz_1^n]G\rvert_p\le\lvert[z_0^mz_1^n]\,y(z_0)^ay(z_1)^b\rvert_p=\lvert[z^m]y^a\rvert_p\,\lvert[z^n]y^b\rvert_p . \]
Therefore \(c_C(m+n)\le\lvert m!\,[z^m]y^a\rvert_p\,\lvert n!\,[z^n]y^b\rvert_p\le c_C(m)c_C(n)\).

## References

1. Lean: `New.CMLattice.maxDerivNorm_add_le`, `New.CMLattice.exists_norm_coeff_subst_add_le`, `New.factorial_mul_coeff_subst_add`, `New.coeff_subst_mul_subst` in `src/New/Derivatives/Sharpness/OneCurve.lean`.
