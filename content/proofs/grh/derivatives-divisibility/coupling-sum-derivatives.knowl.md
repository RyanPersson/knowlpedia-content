+++
id = "proofs/grh/derivatives-divisibility/coupling-sum-derivatives"
title = "Derivatives of a coupling sum modulo p"
kind = "lemma"
summary = "If 0 is not in S, the partial derivatives of the coupling sum are congruent modulo p to combinations of pure p^e-th powers of the variables whose partner is the variable of differentiation."
aliases = ["partner power sum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.partnerPowerSum", "New.dvd_pderiv_pow_pow", "New.dvd_pderiv_coupling_sub", "New.dvd_pderiv_couplingSum_sub", "New.residue_coeff_pderiv_couplingSum_eq", "New.residue_coeff_pderiv_couplingSum", "New.exists_eq_single_of_residue_coeff_pderiv_ne_zero", "New.summable_smul_partnerPowerSum"]
lean_files = ["src/New/Derivatives/Divisibility/NormalForm.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\Xi=\Xi_{S,\operatorname{pr},\lambda}\) be a [[proofs/grh/derivatives-divisibility/coupling-sum|coupling sum]] in the variables \(z_x\), \(x\in\Phi\times c\), and suppose \(0\notin S\). For \(y\in\Phi\times c\) and \(e\ge0\) define the **partner power sum**
\[
\Pi_{e,y}=\sum_{\substack{x=(\tau,i)\\ (\operatorname{pr}_e\tau,\,i)=y}} z_x^{\,p^e}.
\]
Then, as integral power series,
\[
\frac{\partial\Xi}{\partial z_y}\equiv\sum_{e\in S}\lambda_{e,0}\,\Pi_{e,y}\pmod p .
\]
Consequently, modulo the maximal ideal \(\mathfrak{m}\) of \(\mathcal{O}\):

1. the only monomials of \(\partial\Xi/\partial z_y\) with a coefficient outside \(\mathfrak{m}\) are of the form \(z_x^{p^e}\) with \(e\in S\) and \(y=(\operatorname{pr}_e\tau,i)\) the partner of \(x=(\tau,i)\);
2. for \(e\in S\) and \(x=(\tau,i)\), the coefficient of \(z_x^{p^e}\) in \(\partial\Xi/\partial z_{(\operatorname{pr}_e\tau,i)}\) is congruent to \(\lambda_{e,0}\).

## Proof

The partial derivative is continuous for coefficientwise convergence, so it may be applied term by term to \(\Xi=\sum_{e\in S}\sum_j\lambda_{e,j}\Gamma_e^{p^j}\). The sum \(\sum_{e\in S}\lambda_{e,0}\Pi_{e,y}\) is locally finite, as \(\Pi_{e,y}\) has order at least \(p^e\).

For \(n\ge1\) and any integral series \(G\), \(\partial(G^{p^n})/\partial z_y=p^nG^{p^n-1}\,\partial G/\partial z_y\equiv0\pmod p\). This disposes of the terms with \(j\ge 1\). For \(j=0\) and \(e\in S\) (so \(e\ge1\)), the Leibniz rule applied to \(\Gamma_e=\sum_{x=(\tau,i)}z_x^{p^e}z_{(\operatorname{pr}_e\tau,i)}\) gives
\[
\frac{\partial\Gamma_e}{\partial z_y}=\sum_x\frac{\partial z_x^{p^e}}{\partial z_y}\,z_{(\operatorname{pr}_e\tau,i)}+\sum_{x:\ (\operatorname{pr}_e\tau,i)=y}z_x^{p^e}\equiv\Pi_{e,y}\pmod p .
\]
Since a locally finite sum of series divisible by \(p\) is divisible by \(p\), the congruence follows.

For the consequences, \(p\in\mathfrak m\), so coefficients may be compared modulo \(\mathfrak m\) on the right-hand side. A monomial of \(\Pi_{e,y}\) is some \(z_x^{p^e}\) with \((\operatorname{pr}_e\tau,i)=y\), which is 1. For 2, the monomial \(z_x^{p^e}\) has degree \(p^e\), so it does not occur in \(\Pi_{e',y}\) for \(e'\ne e\), and it occurs in \(\Pi_{e,(\operatorname{pr}_e\tau,i)}\) with coefficient \(1\). \(\blacksquare\)

## Remarks

This lemma is not needed for the divisibility bound; the source uses it only for the sharpness of the bound.

## References

1. Lean: `New.partnerPowerSum`, `New.dvd_pderiv_couplingSum_sub`, `New.residue_coeff_pderiv_couplingSum`, `New.exists_eq_single_of_residue_coeff_pderiv_ne_zero` in `src/New/Derivatives/Divisibility/NormalForm.lean`.
