+++
id = "proofs/grh/upper-elementary-divisors/power-packing"
title = "Packing forms into powers of the variables"
kind = "construction"
summary = "A family of forms, one for each class of exponents modulo m, is packed into one polynomial by substituting m-th powers and multiplying by a monomial of the class; for m a power of q the substitution of m-th powers commutes with the twisted action, and a translate of the packed polynomial is the sum of the translated forms in m-th powers times the translated class monomials."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.powerPacking", "New.residueExponent", "New.coeff_powerPacking", "New.sum_residueExponent_mem_Icc", "New.FrobeniusCycle.polyAction_powerPacking", "New.FrobeniusCycle.polyAction_commute_expand", "New.FrobeniusCycle.embedding_pow_q_pow", "New.FrobeniusCycle.exists_eq_add_of_coeff_polyAction_powerPacking", "New.FrobeniusCycle.sum_mem_Icc_of_coeff_polyAction_powerPacking", "New.FrobeniusCycle.weight_defectWeight_le_of_coeff_polyAction_powerPacking", "New.FrobeniusCycle.sum_eq_of_coeff_polyAction_monomial"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/DefectCount.lean"]
+++

Let \(K\) be a field, \(N\ge1\), \(k,n\ge0\), \(m\ge1\), and \(a\) an index below \(k\). A **class** is a function \(u\colon\{0..k-1\}\times\mathbb{Z}/N\to\{0,\dots,m-1\}\). Its **representative exponent** \(\gamma_u\) is \(u\) with \(m\bigl(k-\lfloor d_s/m\rfloor\bigr)\) added at the index \((a,s)\) for each letter \(s\), where \(d_s=\sum_bu(b,s)\). Thus \(\gamma_u\equiv u\pmod m\) and the degree of \(\gamma_u\) in each letter lies in \([mk,mk+m]\). For a family \(F=(F_u)_u\) of coefficient vectors \(F_u\colon\mathcal{E}(N,k,n)\to K\), the **packing** is
\[
\operatorname{pack}(F)=\sum_uF_u(x^{m})\cdot x^{\gamma_u},\qquad F_u(x^{m})=\sum_\beta F_{u,\beta}\,x^{m\beta}.
\]
It is \(K\)-linear in \(F\), and the coefficient of \(\operatorname{pack}(F)\) at \(m\beta+\gamma_u\) is \(F_{u,\beta}\) (exponents \(m\delta+\gamma_v\) with \(v\ne u\) lie in another class modulo \(m\)); in particular \(\operatorname{pack}\) is injective.

## Properties

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,K)\) with \(K\) of characteristic \(p\), and \(m=q^{j}\).

1. *Translation.* For \(g\in\mathrm{GL}_k(W)\): \(g\cdot\operatorname{pack}(F)=\sum_u(\rho_n(g)F_u)(x^{m})\cdot(g\cdot x^{\gamma_u})\). Indeed \(f\mapsto f(x^{m})\) commutes with the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted action]]: the \(m\)-th power map is additive in characteristic \(p\) and fixes every \(\iota_s(y)\) (\(\iota_s(y)^{q}=\iota_s(y)\) by the Frobenius congruence around the cycle).
2. *Shape of exponents.* If \(x^{\alpha}\) occurs in \(g\cdot\operatorname{pack}(F)\), then \(\alpha=m\delta+\varepsilon\) with \((\rho_n(g)F_u)_\delta\ne0\) for some \(u\) and \(\varepsilon\) of degree in \([mk,mk+m]\) in each letter (the action preserves the degree in each letter). Hence \(\alpha\) has degree in \([m(n+k),m(n+k+1)]\) in each letter.
3. *Defect.* If moreover all \(F_u\) satisfy the [[proofs/grh/upper-elementary-divisors/translate-conditions|defect conditions]] for the root \((a,a')\), the zero ideal and the threshold \(h\), and \(g\) is block diagonal with blocks of sizes \(a'\), \(k-a'\), then \(\operatorname{def}_{i,a,a'}(\alpha)\le m(h+2(k+1))\) for every letter \(i\): \(\operatorname{def}(\delta)\le h\) by the conditions, and \(\lvert\operatorname{def}(\varepsilon)\rvert\le2(mk+m)\) by the [[proofs/grh/upper-elementary-divisors/defect-weight-bounds|bound on defects]].

## References

1. Lean: `New.powerPacking`, `New.residueExponent`, `New.coeff_powerPacking`, `New.sum_residueExponent_mem_Icc`, `New.FrobeniusCycle.polyAction_powerPacking`, `New.FrobeniusCycle.polyAction_commute_expand`, `New.FrobeniusCycle.embedding_pow_q_pow`, `New.FrobeniusCycle.exists_eq_add_of_coeff_polyAction_powerPacking`, `New.FrobeniusCycle.sum_mem_Icc_of_coeff_polyAction_powerPacking`, `New.FrobeniusCycle.weight_defectWeight_le_of_coeff_polyAction_powerPacking`, `New.FrobeniusCycle.sum_eq_of_coeff_polyAction_monomial` in `src/New/UpperBound/ElementaryDivisors/DefectCount.lean`.
