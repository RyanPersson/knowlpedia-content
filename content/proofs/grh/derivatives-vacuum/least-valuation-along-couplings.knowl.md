+++
id = "proofs/grh/derivatives-vacuum/least-valuation-along-couplings"
title = "Least valuations along couplings at an inert prime"
kind = "theorem"
summary = "At an inert prime p > 2, if a theta product with integral forms has the normal form with unit leading coefficients, then for a coupling family the least valuation over six copies in the degree of a product of couplings is at most -|j|, and with the factorials at most gamma_p |nu| - |j|."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.leastValLE_six_of_isCouplingFamily", "New.CMLattice.leastValLE_partnerDegree_of_isCouplingFamily", "New.CMLattice.exists_prod_rescale_rescale_thetaProd_eq", "New.CMLattice.isUnit_of_rescale_thetaProd_eq", "New.CMLattice.varpiValuation_mul_add_one_of_inert", "New.CMLattice.norm_pow_div_of_inert", "New.CMLattice.one_lt_norm_pow_div_of_inert"]
lean_files = ["src/New/Derivatives/Sharpness/Couplings.lean"]
proof_status = "full"
+++

Let \(d\) be a prime \(\equiv7\bmod8\), \(C\) a CM lattice for \(d\), \(p>2\) a prime inert in \(K\) (\(\chi_K(p)=-1\)), \(\iota_p\) a \(p\)-adic place. Let \(\Phi\), \(J\) be finite sets, \(\mu_i\) (\(i\in J\)) linear forms in the variables \(z_\tau\) (\(\tau\in\Phi\)) with \(\lvert\mu_{i,\tau}\rvert_p\le1\), \(m\in\mathbb{N}^J\), \(\Theta=\prod_i\theta(\mu_iz)^{m_i}\). Let \(\rho_p=1/(p^2-1)\) and \(\gamma_p=1/(p-1)-\rho_p=p/(p^2-1)\).

**Theorem.** Suppose \(\Theta\) [[?lean:New.HasNormalForm|has the normal form]] for a partner map \(\mathrm{pr}\): there are \(\varpi\in\mathbb{C}_p\) with \(\lvert\varpi\rvert_p=p^{-\rho_p}\), integral \(l_{a,b}\) and an integral series \(W\) with
\[ \Theta(\varpi z)=W\exp\Bigl(\frac{\varpi^{p+1}}{p}\,\Xi\Bigr), \]
\(\Xi\) the coupling sum over odd \(a\), and suppose \(l_{a,0}\) is a unit for all odd \(a\). Let \((\Phi_0,e)\) be a [[proofs/grh/derivatives-vacuum/coupling-family|coupling family]], \(j\colon\Phi\to\mathbb{N}\), \(\nu=\nu'+\nu''\) the degree of \(\prod_{\tau\in\Phi_0}(z_\tau^{p^{e_\tau}}z_{\tau^+})^{j_\tau}\). Then, for the [[proofs/grh/derivatives-vacuum/least-valuation-relation|least valuation]] of \((C,\mu,m)\),

1. \(\operatorname{val}_6(\nu)\le\dfrac{\lvert j\rvert}{p-1}-\lvert j\rvert-\rho_p\lvert\nu\rvert-v_p(\nu''!)\);
2. \(\operatorname{val}_6(\nu)\le-\lvert j\rvert\);
3. \(v_p(\nu'!)+v_p(\nu''!)+\operatorname{val}_6(\nu)\le\gamma_p\lvert\nu\rvert-\lvert j\rvert\).

## Proof

*Preparations.* \(\kappa=\varpi^{p+1}/p\) has \(\lvert\kappa\rvert_p=p^{\,1-(p+1)\rho_p}=p^{\,1-1/(p-1)}>1\) since \(p>2\). The constant term of \(W\) is \(\Theta(0)=1\), so \(W\) is a unit. By [[proofs/grh/derivatives-vacuum/six-scaled-copies-are-a-unit|the theorem on six scaled copies]] there is \(\delta\in\mathbb{Z}_p^6\), \(\delta_1=1\), with \(\Theta_\delta\in\mathcal{O}[\![y(\mu z)]\!]\) of constant term \(1\); by [[proofs/grh/derivatives-vacuum/integral-series-in-parameters-after-scaling|integrality after scaling]] \(U(z)=\Theta_\delta(\varpi z)=\prod_c\Theta(\delta_c\varpi z)\) is integral with constant term \(1\).

*1.* Apply [[proofs/grh/derivatives-vacuum/coefficient-of-a-product-of-couplings|the coefficient of a product of couplings]] to \(F(z)=\Theta(\varpi z)\): with \(G_\varpi=F(z'+z'')\prod_{c\ne0}F(\delta_cz')\), \(\lvert\nu''!\rvert_p\lvert[z'^{\nu'}z''^{\nu''}]G_\varpi\rvert_p=\lvert\kappa\rvert_p^{\lvert j\rvert}\). Now \(G_\varpi(z',z'')=G(\varpi z',\varpi z'')\) for \(G=\Theta(z'+z'')\prod_{c\ne0}\Theta(\delta_cz')\), so the coefficient of \(G_\varpi\) is \(\varpi^{\lvert\nu\rvert}\) times that of \(G\). Hence
\[ \bigl\lvert[z'^{\nu'}z''^{\nu''}]G\bigr\rvert_p=p^{\,(1-\frac1{p-1})\lvert j\rvert+\rho_p\lvert\nu\rvert+v_p(\nu''!)} . \]
The substitution is integral (\(\delta_c\in\mathbb{Z}_p\)), so rule 2 of [[proofs/grh/derivatives-vacuum/least-valuation-rules|the rules]] with all \(H_c=1\) gives 1.

*2.* Since each \(e_\tau\ge1\), \(\lvert\nu'\rvert=\sum p^{e_\tau}j_\tau\ge p\lvert j\rvert\), so \(\lvert\nu\rvert\ge(p+1)\lvert j\rvert\) and \(\rho_p\lvert\nu\rvert\ge\rho_p(p+1)\lvert j\rvert=\lvert j\rvert/(p-1)\). Drop \(v_p(\nu''!)\ge0\) in 1.

*3.* By Legendre, \(v_p(\nu'!)\le\lvert\nu'\rvert/(p-1)\), and \(\lvert\nu\rvert=\lvert\nu'\rvert+\lvert j\rvert\). So \(v_p(\nu'!)+\lvert j\rvert/(p-1)\le\lvert\nu\rvert/(p-1)\), and 1 gives \(v_p(\nu'!)+v_p(\nu''!)+\operatorname{val}_6(\nu)\le\lvert\nu\rvert/(p-1)-\rho_p\lvert\nu\rvert-\lvert j\rvert\).

## Remarks

In the Lean statement, 3 is written as a bound for \(\operatorname{val}_6(\nu)\) with the two factorial valuations moved to the right-hand side.

## References

1. Lean: `New.CMLattice.leastValLE_six_of_isCouplingFamily`, `New.CMLattice.leastValLE_partnerDegree_of_isCouplingFamily`, `New.CMLattice.exists_prod_rescale_rescale_thetaProd_eq`, `New.CMLattice.isUnit_of_rescale_thetaProd_eq`, `New.CMLattice.varpiValuation_mul_add_one_of_inert`, `New.CMLattice.norm_pow_div_of_inert`, `New.CMLattice.one_lt_norm_pow_div_of_inert` in `src/New/Derivatives/Sharpness/Couplings.lean`.
