+++
id = "proofs/grh/derivatives-vacuum/six-scaled-copies-are-a-unit"
title = "Six scaled copies of a theta product multiply to a unit"
kind = "theorem"
summary = "There are p-adic integers delta_0 = 1, delta_1, ..., delta_5 with squares summing to zero, and for such scales the product of the scaled copies Theta(delta_c z) is a unit of the ring of integral series in the parameters, with constant term 1."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.exists_scaledThetaProd_mem_mul_eq_one", "New.CMLattice.scaledThetaProd", "New.CMLattice.prod_rescale_theta_mem", "New.CMLattice.scaledThetaProd_mem", "New.CMLattice.exists_scaledThetaProd_mul_eq_one", "New.CMLattice.scaledThetaProd_eq_prod_subst", "New.CMLattice.constantCoeff_scaledThetaProd", "New.padicInt_sum_four_squares"]
lean_files = ["src/New/Derivatives/Sharpness/LeastValuation.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/derivatives-vacuum/least-valuation-relation|the least valuation relation]]; \(d\) is a prime \(\equiv7\bmod8\). For \(\delta=(\delta_1,\dots,\delta_n)\in\mathbb{Z}_p^n\) the **scaled theta product** is \(\Theta_\delta(z)=\prod_c\Theta(\delta_cz)\).

**Theorem.**

1. If \(\sum_c\delta_c^2=0\), then \(u(z)=\prod_c\theta(\delta_cz)\) lies in \(\mathcal{O}[\![y]\!]\), and \(\Theta_\delta\) lies in \(\mathcal{O}[\![y(\mu z)]\!]\) and has an inverse there.
2. There is \(\delta=(\delta_0,\dots,\delta_5)\in\mathbb{Z}_p^6\) with \(\delta_0=1\) and \(\sum_c\delta_c^2=0\) (the six-tuples are indexed from \(0\), as in the Lean source and in the knowls that use this theorem); for it \(\Theta_\delta\) is a unit of \(\mathcal{O}[\![y(\mu z)]\!]\) with constant term \(1\).

## Proof

1. With \(g=-\log\theta\) we have \(\theta=\exp(-g)\), so
\[ u=\exp\Bigl(-\sum_cg(\delta_cz)\Bigr)=\prod_c\exp\bigl(\delta_c^2g(z)-g(\delta_cz)\bigr), \]
because \(\sum_c\delta_c^2g=0\). Each factor \(\exp(a^2g(z)-g(az))\), \(a\in\mathbb{Z}_p\), lies in \(\mathcal{O}[\![y]\!]\): this is a result of the formal-group chapter (Lean `New.CMLattice.expSubst_sub_rescale_mem`: \(\exp(s\,g(z)-g(\delta z))\in\mathcal{O}[\![y]\!]\) for every pair \((\delta,s)\) in the closure in \(\mathbb{C}_p^2\) of the pairs \((\iota_p\alpha,\iota_p(\alpha\bar\alpha))\), \(\alpha\in\mathcal{O}_K\); this closure contains the pairs \((k,k^2)\), \(k\in\mathbb{N}\), hence \((a,a^2)\) for \(a\in\mathbb{Z}_p\) by density of \(\mathbb{N}\) in \(\mathbb{Z}_p\)); it is asserted here. So \(u\in\mathcal{O}[\![y]\!]\). Since \(u(0)=1\) is a unit, \(u\) has an inverse \(v\in\mathcal{O}[\![y]\!]\) (an integral power series in \(y\) with unit constant term is invertible; Lean `IsSeriesGenerator.exists_mul_eq_one`). Exchanging products, \(\Theta_\delta=\prod_ju(\mu_jz)^{m_j}\), which lies in \(\mathcal{O}[\![y(\mu z)]\!]\) with inverse \(\prod_jv(\mu_jz)^{m_j}\).

2. Every element of \(\mathbb{Z}_p\) is a sum of four squares: the set of sums of four squares is the continuous image of the compact \(\mathbb{Z}_p^4\), hence closed, and contains the dense subset \(\mathbb{N}\) by [[?c:Lagrange's four-square theorem|Lagrange's four-square theorem]]. Write \(-1=a_1^2+\dots+a_4^2\) and take \((\delta_0,\dots,\delta_5)=(1,a_1,a_2,a_3,a_4,0)\).

## References

1. Lean: `New.CMLattice.exists_scaledThetaProd_mem_mul_eq_one`, `New.CMLattice.scaledThetaProd`, `New.CMLattice.prod_rescale_theta_mem`, `New.CMLattice.scaledThetaProd_mem`, `New.CMLattice.exists_scaledThetaProd_mul_eq_one`, `New.CMLattice.scaledThetaProd_eq_prod_subst`, `New.CMLattice.constantCoeff_scaledThetaProd`, `New.padicInt_sum_four_squares` in `src/New/Derivatives/Sharpness/LeastValuation.lean`.
