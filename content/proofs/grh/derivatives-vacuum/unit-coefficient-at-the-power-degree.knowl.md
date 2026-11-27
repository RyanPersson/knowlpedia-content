+++
id = "proofs/grh/derivatives-vacuum/unit-coefficient-at-the-power-degree"
title = "The derivatives of the coupling sum have a unit coefficient at the power degree"
kind = "lemma"
summary = "For a coupling family, a series congruent to the product of the partial derivatives of the coupling sum in the partner variables, times a series with constant term one, has a unit coefficient at the power degree."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsCouplingFamily.norm_coeff_powerDegree", "New.IsCouplingFamily.isLowestTerm_pderiv_couplingSum", "New.isLowestTerm_zero_one"]
lean_files = ["src/New/Derivatives/Sharpness/Couplings.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/derivatives-vacuum/coupling-family|coupling families]]. Let \(l_{a,b}\in\mathcal{O}\) and let
\[ \Xi=\sum_{a\text{ odd}}\sum_{b\ge0}l_{a,b}\,\Gamma_a^{\,p^b},\qquad\Gamma_a=\sum_{\tau\in\Phi}z_\tau^{\,p^a}z_{\mathrm{pr}_a(\tau)} \]
be the [[?lean:New.couplingSum|coupling sum]] over the odd exponents.

**Lemma.** Let \((\Phi_0,e)\) be a coupling family and suppose \(l_{a,0}\) is a unit for every odd \(a\). Let \(j\colon\Phi\to\mathbb{N}\), let \(g\in\mathcal{O}[\![z]\!]\) with \(g\equiv\prod_{\tau\in\Phi_0}(\partial_{z_{\tau^+}}\Xi)^{j_\tau}\bmod\mathfrak{m}\), and \(U\in\mathcal{O}[\![z]\!]\) with \(U(0)=1\). Then the coefficient of \(z^{\nu'}\) in \(gU\) is a unit, \(\nu'\) the power degree.

## Proof

Work modulo \(\mathfrak{m}\) and set \(z_{\tau_1}=0\) for \(\tau_1\notin\Phi_0\) (this does not change the coefficient at \(\nu'\), which is supported on \(\Phi_0\)).

*Claim: for \(\tau\in\Phi_0\), the series \(\partial_{z_{\tau^+}}\Xi\) has [[proofs/grh/derivatives-vacuum/lowest-term-of-a-power-series|lowest term]] \(\bar l_{e_\tau,0}\,z_\tau^{\,p^{e_\tau}}\) for the total degree.* Modulo \(p\), the terms with \(b\ge1\) are \(p\)-th powers and have derivative \(0\), and the derivative of \(z_{\tau_1}^{p^a}z_{\mathrm{pr}_a(\tau_1)}\) in \(z_{\tau^+}\) is \(z_{\tau_1}^{p^a}\) if \(\mathrm{pr}_a(\tau_1)=\tau^+\) (the derivative in the factor \(z_{\tau_1}^{p^a}\) vanishes mod \(p\)). So the monomials occurring are \(z_{\tau_1}^{p^a}\) with \(a\) odd and \(\mathrm{pr}_a(\tau_1)=\tau^+\), and the coefficient of \(z_\tau^{p^{e_\tau}}\) is \(\bar l_{e_\tau,0}\); these two facts are proved in the chapter on derivatives that count primes, see [[proofs/grh/derivatives-divisibility/coupling-sum-derivatives|the derivatives of the coupling sum]] (Lean `New.residue_coeff_pderiv_couplingSum`, `New.exists_eq_single_of_residue_coeff_pderiv_ne_zero` in `NormalForm.lean`), and are not reproved here. A monomial \(z_{\tau_1}^{p^a}\) of degree \(\le p^{e_\tau}\) with \(\tau_1\in\Phi_0\) has \(a\le e_\tau\), so by condition 2 of a coupling family \(\tau_1=\tau\), \(a=e_\tau\).

By multiplicativity of lowest terms, \(\bar g\) has lowest term \(\prod_\tau\bar l_{e_\tau,0}^{\,j_\tau}z^{\nu'}\), and \(\bar U\) has lowest term \(1\); so the coefficient of \(z^{\nu'}\) in \(\overline{gU}\) is \(\prod_\tau\bar l_{e_\tau,0}^{\,j_\tau}\ne0\), since the \(l_{e_\tau,0}\) are units.

## References

1. Lean: `New.IsCouplingFamily.norm_coeff_powerDegree`, `New.IsCouplingFamily.isLowestTerm_pderiv_couplingSum`, `New.isLowestTerm_zero_one` in `src/New/Derivatives/Sharpness/Couplings.lean`.
