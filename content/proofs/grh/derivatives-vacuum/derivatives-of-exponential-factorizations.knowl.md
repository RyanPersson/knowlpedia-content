+++
id = "proofs/grh/derivatives-vacuum/derivatives-of-exponential-factorizations"
title = "Derivatives of a series W exp(kappa Xi) with kappa of negative valuation"
kind = "lemma"
summary = "For integral W, Xi with W a unit and kappa of absolute value greater than one, differentiating a product of copies of F = W exp(kappa Xi) in the linearly occurring copy of the variables multiplies by kappa for each derivative, up to an integral factor congruent to the product of the derivatives of Xi."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_pderiv_mul_expSubst", "New.exists_pderiv_mul_eq_smul", "New.exists_jet_mul_prod_X", "New.pderiv_prod_copySubst_couplingSubst", "New.exists_jet_prod_copySubst_couplingSubst", "New.coeff_prod_copySubst_rescale", "New.monomial_mul_prod_X_partner"]
lean_files = ["src/New/Derivatives/Sharpness/Couplings.lean"]
proof_status = "full"
+++

Let \(p\) be a prime, \(\mathcal{O}\) the valuation ring of \(\mathbb{C}_p\) with maximal ideal \(\mathfrak{m}\), and \(X\) a finite set of variables.

**Lemma.** Let \(W,\Xi\in\mathcal{O}[\![z_x]\!]\) with \(W\) a unit and \(\Xi(0)=0\), let \(\kappa\in\mathbb{C}_p\) with \(\lvert\kappa\rvert_p>1\), and \(F=W\exp(\kappa\Xi)\). Let \(\delta_0=1,\delta_1,\dots,\delta_n\in\mathbb{C}_p\) and
\[ G(z',z'')=F(z'+z'')\prod_{c\ne0}F(\delta_cz') \]
(the product of the [[proofs/grh/derivatives-vacuum/copy-substitution|copy substitutions]] of \(F\) for the [[proofs/grh/derivatives-vacuum/coupling-family|coupling substitution]]). Let \(t_i\in X\), \(i\in T\), a finite family. Then there is \(g\in\mathcal{O}[\![z',z'']\!]\) with
\[ g(z',0)\equiv\prod_{i\in T}\partial_{t_i}\Xi\ (z')\pmod{\mathfrak{m}},\qquad\Bigl(f(\partial)\prod_{i\in T}\partial_{z''_{t_i}}G\Bigr)(0)=\kappa^{\lvert T\rvert}\bigl(f(\partial)(gG)\bigr)(0) \]
for every polynomial \(f\) over \(\mathbb{C}_p\).

## Proof

*Logarithmic derivative of \(F\).* \(\partial_xF=(\kappa\,\partial_x\Xi+B)F\) with \(B=\partial_xW/W\) integral, as \(W\) is a unit.

*Logarithmic derivative of \(G\) in \(z''\).* Only the factor \(F(z'+z'')\) involves \(z''\), so \(\partial_{z''_x}G=(\kappa A_x+B')G\) with \(A_x=(\partial_x\Xi)(z'+z'')\) and \(B'=B(z'+z'')\) integral.

*One step.* If \(\partial G=(\kappa A+B)G\) and \(g\) is integral, then \(\partial(gG)=\kappa\,g'G\) with
\[ g'=gA+\kappa^{-1}(\partial g+gB), \]
which is integral and \(\equiv gA\bmod\mathfrak{m}\) because \(\lvert\kappa^{-1}\rvert_p<1\).

*Induction on \(\lvert T\rvert\).* Starting from \(g=1\) and applying the step for each \(i\in T\) gives \(\prod_{i\in T}\partial_{z''_{t_i}}G=\kappa^{\lvert T\rvert}gG\) with \(g\equiv\prod_iA_{t_i}\bmod\mathfrak{m}\); the Lean statement expresses this identity after applying \(f(\partial)\) and evaluating at \(0\). Setting \(z''=0\) in \(A_{t_i}\) gives \(\partial_{t_i}\Xi(z')\).

## References

1. Lean: `New.exists_pderiv_mul_expSubst`, `New.exists_pderiv_mul_eq_smul`, `New.exists_jet_mul_prod_X`, `New.pderiv_prod_copySubst_couplingSubst`, `New.exists_jet_prod_copySubst_couplingSubst`, `New.coeff_prod_copySubst_rescale`, `New.monomial_mul_prod_X_partner` in `src/New/Derivatives/Sharpness/Couplings.lean`.
