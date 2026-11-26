+++
id = "proofs/grh/derivatives-divisibility/normal-form-integrality"
title = "Integrality in low degrees of a series with the normal form"
kind = "proposition"
summary = "If F has the normal form and a substitution Z makes the couplings Gamma_e(Z), e in S, e at most log_p B, divisible by a suitable pi, then F(varpi Z) is integral in degrees at most B."
aliases = ["integrality criterion for the normal form"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HasNormalForm.norm_coeff_subst_le_one", "New.dvd_coeff_subst_couplingSum", "New.le_order_subst_coupling_pow"]
lean_files = ["src/New/Derivatives/Divisibility/NormalForm.lean"]
proof_status = "full"
+++

**Proposition.** Let \(F\) have the [[proofs/grh/derivatives-divisibility/normal-form|normal form]] with the data \((S,\operatorname{pr},\varpi,\lambda)\), in the variables \(z_x\), \(x\in\Phi\times c\). Let \(\pi\in\mathcal{O}\) satisfy \(\lvert c_\varpi\pi\rvert\le p^{-1/(p-1)}\) with \(c_\varpi=\varpi^{p+1}/p\). Let \(Z_x\) be integral series without constant term, in any variables, and let \(B\ge 0\) be an integer such that
\[
\Gamma_e(Z)\equiv 0\pmod{\pi}\qquad\text{for all } e\in S \text{ with } e\le\lfloor\log_p B\rfloor ,
\]
where \(\Gamma_e\) is the [[proofs/grh/derivatives-divisibility/coupling|coupling]] (and \(\lfloor\log_p 0\rfloor=0\)). Then every coefficient of \(F((\varpi Z_x)_x)\) in a degree \(\le B\) has norm at most \(1\).

## Proof

Put \(\Xi=\Xi_{S,\operatorname{pr},\lambda}\).

*Step 1: \(\pi\) divides the coefficients of \(\Xi(Z)\) in the degrees \(\le B\).* By the [[proofs/grh/derivatives-divisibility/coupling-sum|coupling sum]], \(\Xi(Z)=\sum_{e\in S}\sum_j\lambda_{e,j}\Gamma_e(Z)^{p^j}\), a locally finite sum of integral series; so it suffices to treat each term. If \(e\le\lfloor\log_pB\rfloor\), then \(\pi\) divides \(\Gamma_e(Z)\) by hypothesis, hence its power \(\Gamma_e(Z)^{p^j}\) (as \(p^j\ge 1\)). If \(e>\lfloor\log_pB\rfloor\), then \(p^e>B\); the series \(\Gamma_e\) has order at least \(p^e+1\), substitution of series without constant term does not lower the order, and neither does taking a power with positive exponent, so \(\Gamma_e(Z)^{p^j}\) has order at least \(p^e+1>B\) and its coefficients in the degrees \(\le B\) vanish.

*Step 2.* The series \(\Xi(Z)\) is integral without constant term. By Step 1 and the [[proofs/grh/derivatives-divisibility/normal-form-modulo-pi|bound for the exponential of a divisible series]], the coefficients of \(\exp(c_\varpi\Xi(Z))\) in the degrees \(\le B\) have norm at most \(1\).

*Step 3.* By [[proofs/grh/derivatives-divisibility/normal-form-substitution|substitution into the normal form]], \(F(\varpi Z)=W'\exp(c_\varpi\Xi(Z))\) with \(W'\) integral. The coefficient of \(F(\varpi Z)\) at a multi-index \(m\) of degree \(\le B\) is the sum of the products \(W'_{d_1}\cdot\exp(c_\varpi\Xi(Z))_{d_2}\) over \(d_1+d_2=m\); here \(d_2\le m\) has degree \(\le B\), so each product has norm at most \(1\), and so has the sum by the ultrametric inequality. \(\blacksquare\)

## References

1. Lean: `New.HasNormalForm.norm_coeff_subst_le_one`, `New.dvd_coeff_subst_couplingSum`, `New.le_order_subst_coupling_pow` in `src/New/Derivatives/Divisibility/NormalForm.lean`.
