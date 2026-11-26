+++
id = "proofs/grh/derivatives-divisibility/normal-form-of-theta-products"
title = "Normal form of theta products at non-split primes"
kind = "theorem"
summary = "At a prime not split in K, for every resolution of the identity by vectors integral above p, the product of the theta functions along the dagger forms, times any integral series in the y(u-dagger z), has the normal form for the partner rule of E."
aliases = ["normal form of theta products"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_hasNormalForm", "New.Parameters.piPrimeInt_dvd_sum_linearSeries_sub_coupling", "New.Parameters.dvd_pow_sub_sum_partner", "New.dvd_sum_subst_sub_couplingSum", "New.Parameters.norm_pow_succ_div_mul_piPrimeInt", "New.CMLattice.rescale_thetaProd_eq_mul_expSubst", "New.CMLattice.rescale_mem_range_of_mem_multiSeriesRing", "New.Parameters.norm_daggerForms_le_one", "New.coeff_subst_linearSeries", "New.rescale_subst_linearSeries", "New.expSubst_nsmul", "New.seriesToCp_subst", "New.rescale_subst_linearSeries_coe"]
lean_files = ["src/New/Derivatives/FormalGroup/ThetaProducts.lean"]
proof_status = "full"
+++

**Theorem (normal form of theta products).** Let \(E=K(\zeta)\) with its group \(\Phi\) of infinite places and CM type \((\Phi_\tau)\) (see the [[proofs/grh/derivatives-divisibility/field-setting|field \(E\)]]), and let \(C\) be the [[?lean:New.Parameters.cmCurve|CM lattice of the parameters]], with theta function \(\theta\) and coordinate \(y\). Let \(p\) be a prime with \(\chi_K(p)\ne1\) and a \(p\)-adic place \(\iota_p\). Then there are \(\varpi\in\mathbb{C}_p\) and \(\lambda_{e,j}\in\mathcal{O}\) \((e,j\ge0)\) with

* \(\lvert\varpi\rvert=p^{-\rho_p}\), and, if \(p\) is inert, \(\lambda_{e,0}\in\mathcal{O}^\times\) for all odd \(e\),

such that the following holds for all finite sets \(n\), \(J\). Let \((u_j)_{j\in J}\), \(u_j\in E^n\), with multiplicities \(m_j\), be a [[proofs/grh/derivatives-divisibility/resolution-of-the-identity|resolution of the identity]] all of whose coordinates \(u_{j,c}\) are [[proofs/grh/derivatives-divisibility/integral-above-p|integral above \(p\)]]. Let \(\mu_j\) be the coefficient vector of the dagger form \(u_j^\dagger z\), read in \(\mathbb{C}_p\) through \(\iota_p\), and let \(H\in\mathcal{O}[[y(\mu z)]]\) (see the [[proofs/grh/derivatives-divisibility/theta-product|theta product]]). Then the series
\[
F(z)=\prod_{j\in J}\theta(u_j^\dagger z)^{m_j}\cdot H(z)\ \in\ \mathbb{C}_p[[z_{(\tau,c)}:(\tau,c)\in\Phi\times n]]
\]
has the [[proofs/grh/derivatives-divisibility/normal-form|normal form]] with the data \((I_p^\circ,\operatorname{pr},\varpi,\lambda)\), where \(\operatorname{pr}_e\tau=-p^e\tau\) is the [[proofs/grh/derivatives-divisibility/partner-of-a-place|partner]].

Note that \(\varpi\) and \(\lambda\) depend only on the parameters, the level and \(p\) (and \(\iota_p\)), not on the resolution.

## Proof

Take \(\varpi\), \(\lambda\) and one-variable integral series \(\Xi,W\) from the [[proofs/grh/derivatives-divisibility/exponent-on-one-curve|exponent on one curve]]: \(\theta(\varpi t)=W(t)\exp(c_\varpi\Xi(t))\), \(\Xi(0)=0\), \(\Xi\equiv\sum_{e\in I_p^\circ}\sum_j\lambda_{e,j}(t^{p^e}t)^{p^j}\pmod{\pi_p}\). Fix a resolution as in the statement. The numbers \(\mu_{j,x}\) are integral; let \(L_j=\sum_x\mu_{j,x}z_x\in\mathcal{O}[[z]]\).

**Step 1: the shape of \(F(\varpi z)\).** Scaling all variables of \(f(L_j)\) by \(\varpi\) is the same as substituting \(L_j\) into \(f(\varpi t)\). Hence \(\theta(L_j)(\varpi z)=W(L_j)\exp\bigl(c_\varpi\Xi(L_j)\bigr)\), and, since \(\exp(g)^m=\exp(mg)\) and \(\exp\) turns sums into products,
\[
\prod_j\theta(L_j)^{m_j}(\varpi z)=\prod_jW(L_j)^{m_j}\cdot\exp\Bigl(c_\varpi\sum_jm_j\,\Xi(L_j)\Bigr).
\]
Also \(H(\varpi z)\) is integral: \(H=G(y(L_j)_j)\) with \(G\) integral, and \(y(\varpi t)\) is an integral series without constant term (fact 3 of the [[proofs/grh/derivatives-divisibility/cm-curve-setting|setting]]), so \(H(\varpi z)=G\bigl(y(\varpi t)|_{t=L_j}\bigr)\) is integral. Thus \(F(\varpi z)=W'\exp(c_\varpi\Xi')\) with \(W'\) integral and \(\Xi'=\sum_jm_j\Xi(L_j)\) integral without constant term.

**Step 2: the coupling.** Let \(e\in I_p^\circ\). We claim
\[
\sum_jm_j\,L_j^{\,p^e}L_j\equiv\Gamma_e=\sum_{(\tau,c)}z_{(\tau,c)}^{p^e}z_{(\operatorname{pr}_e\tau,c)}\pmod{\pi_p}.
\]
Since \(\pi_p\mid p\), \(p^e\)-th powers are [[?lean:New.dvd_sum_pow_sub_sum|additive modulo \(\pi_p\)]]: \(L_j^{p^e}\equiv\sum_x\mu_{j,x}^{p^e}z_x^{p^e}\). By the [[proofs/grh/derivatives-divisibility/partner-of-a-place|lemma on partners]] (part 2), \(\mu_{j,(\tau,c)}^{p^e}=\iota_p(\overline{\Phi_\tau(u_{j,c})})^{p^e}\equiv\nu_{j,(\tau,c)}:=\iota_p\bigl(\Phi_{\operatorname{pr}_e\tau}(u_{j,c})\bigr)\). Therefore
\[
\sum_jm_jL_j^{p^e}L_j\equiv\sum_{x=(\tau,c)}z_x^{p^e}\sum_jm_j\,\nu_{j,x}L_j=\sum_{x=(\tau,c)}z_x^{p^e}\,z_{(\operatorname{pr}_e\tau,c)},
\]
the last step by property 2 of a resolution of the identity at the pair \((\operatorname{pr}_e\tau,c)\).

**Step 3: the exponents add up to a coupling sum.** Substituting \(L_j\) into the congruence for \(\Xi\) (substitution is continuous and preserves divisibility by \(\pi_p\)), \(\Xi(L_j)\equiv\sum_{e\in I_p^\circ}\sum_{j'}\lambda_{e,j'}\bigl(L_j^{p^e}L_j\bigr)^{p^{j'}}\). For fixed \((e,j')\), additivity of \(p^{j'}\)-th powers (a term with multiplicity \(m_j\) being \(m_j\) equal terms) and Step 2 give
\[
\sum_jm_j\bigl(L_j^{p^e}L_j\bigr)^{p^{j'}}\equiv\Bigl(\sum_jm_jL_j^{p^e}L_j\Bigr)^{p^{j'}}\equiv\Gamma_e^{\,p^{j'}}\pmod{\pi_p}.
\]
Summing the locally finite families, \(\Xi'\equiv\Xi_{I_p^\circ,\operatorname{pr},\lambda}\pmod{\pi_p}\), the [[proofs/grh/derivatives-divisibility/coupling-sum|coupling sum]].

**Step 4.** The valuation of \(c_\varpi\pi_p\) is \((p+1)\rho_p-1+v(\pi_p)\), which equals \(\tfrac{1}{p-1}\) both for inert \(p\) (\(\tfrac{p+1}{p^2-1}-1+1\)) and for \(p=d\) (\(\tfrac{p+1}{2(p-1)}-1+\tfrac12\)). So \(\lvert c_\varpi\pi_p\rvert=p^{-1/(p-1)}\), and [[proofs/grh/derivatives-divisibility/normal-form-modulo-pi|the exponent need only be known modulo \(\pi_p\)]]: \(F\) has the normal form. \(\blacksquare\)

## References

1. Lean: `New.Parameters.exists_hasNormalForm` and the lemmas before it in `src/New/Derivatives/FormalGroup/ThetaProducts.lean`.
