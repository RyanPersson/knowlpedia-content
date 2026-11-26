+++
id = "proofs/grh/derivatives-vacuum/coupling-family"
title = "Coupling families and the degrees of a product of couplings"
kind = "definition"
summary = "A set of places with odd exponents whose couplings z_tau^(p^e) z_(tau+) are each strictly the lowest among the selected couplings with the same partner, together with the two degrees of a product of such couplings."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsCouplingFamily", "New.powerDegree", "New.partnerDegree", "New.pairExponent", "New.couplingSubst", "New.powerDegree_apply_of_mem", "New.powerDegree_apply_of_notMem", "New.partnerDegree_apply", "New.degree_powerDegree", "New.degree_partnerDegree", "New.mapDomain_fst_pairExponent", "New.prod_factorial_pairExponent", "New.norm_couplingSubst_le_one"]
lean_files = ["src/New/Derivatives/Sharpness/Couplings.lean"]
+++

Let \(\Phi\) be a finite set (of places), \(p\) a prime, and \(\mathrm{pr}\colon\mathbb{N}\times\Phi\to\Phi\) a partner map, \(\mathrm{pr}_e(\tau)\) being the partner of \(\tau\) for the exponent \(e\). The variables are \(z_\tau\), \(\tau\in\Phi\). A **coupling** is a monomial \(z_\tau^{\,p^e}z_{\mathrm{pr}_e(\tau)}\).

A subset \(\Phi_0\subseteq\Phi\) with exponents \(e\colon\Phi\to\mathbb{N}\) is a **coupling family** if, writing \(\tau^+=\mathrm{pr}_{e_\tau}(\tau)\),

1. \(e_\tau\) is odd for all \(\tau\in\Phi_0\);
2. for \(\tau,\tau_1\in\Phi_0\) and odd \(e'\le e_\tau\): \(\mathrm{pr}_{e'}(\tau_1)=\tau^+\) implies \(\tau_1=\tau\) and \(e'=e_\tau\).

For \(j\colon\Phi\to\mathbb{N}\), the product \(\prod_{\tau\in\Phi_0}(z_\tau^{\,p^{e_\tau}}z_{\tau^+})^{j_\tau}\) has degree \(\nu=\nu'+\nu''\) with

* the **power degree** \(\nu'=\sum_{\tau\in\Phi_0}p^{e_\tau}j_\tau\,[\tau]\), of total degree \(\sum_{\tau\in\Phi_0}p^{e_\tau}j_\tau\);
* the **partner degree** \(\nu''=\sum_{\tau\in\Phi_0}j_\tau\,[\tau^+]\), of total degree \(\lvert j\rvert=\sum_{\tau\in\Phi_0}j_\tau\).

In two copies \(z',z''\) of the variables, the **pair exponent** of \((\nu',\nu'')\) is the exponent of \(z'^{\nu'}z''^{\nu''}\). For \(\delta_0,\dots,\delta_n\) the **coupling substitution** replaces \(z_0\) by \(\delta_0z'+z''\) and \(z_c\) by \(\delta_cz'\) for \(c\ne0\).

## References

1. Lean: `New.IsCouplingFamily`, `New.powerDegree`, `New.partnerDegree`, `New.pairExponent`, `New.couplingSubst`, `New.powerDegree_apply_of_mem`, `New.powerDegree_apply_of_notMem`, `New.partnerDegree_apply`, `New.degree_powerDegree`, `New.degree_partnerDegree`, `New.mapDomain_fst_pairExponent`, `New.prod_factorial_pairExponent`, `New.norm_couplingSubst_le_one` in `src/New/Derivatives/Sharpness/Couplings.lean`.
