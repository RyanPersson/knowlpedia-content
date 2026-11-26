+++
id = "proofs/grh/upper-elementary-divisors/deep-forms-have-heavy-monomial"
title = "A nonzero deep form has a monomial of large weight"
kind = "theorem"
summary = "Over a field of characteristic p, a nonzero form all of whose translates have depth at least tau has a monomial whose weighted degree in the deep variables is at least tau, deep variables weighing 1/P or 1/P^(2r)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.exists_le_weight_of_mem_deepForms", "New.FrobeniusCycle.specializeShallow_polyOfCoeffs_mem_vanishingIdeal_pow", "New.FrobeniusCycle.map_polyOfCoeffs_mem_pow_of_mem_deepForms", "New.FrobeniusCycle.letterRep_mulVec_eq_zero_of_mem_deepForms", "New.FrobeniusCycle.exists_eq_of_mem_support_specializeShallow", "New.FrobeniusCycle.specializeShallow_polyOfCoeffs_ne_zero"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Depth.lean"]
proof_status = "full"
+++

**Theorem.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,K)\), \(N\ge1\), with \(K\) a field of characteristic \(p\), and let \(k,n,r,\tau\ge0\) with \(2r\le k\). Let \(F\ne0\) lie in the space \(\mathcal{D}_n(r,\tau)\) of [[proofs/grh/upper-elementary-divisors/translate-conditions|deep forms]]. Then there is an exponent \(\beta\in\mathcal{E}(N,k,n)\) with \(F_\beta\ne0\) and
\[
\tau\le\sum_{v\ \text{deep for }r}\frac{\beta(v)}{\kappa(v)},\qquad\kappa(x_{b,s})=\begin{cases}P^{2r}&b\ge2r\\ P&b<2r.\end{cases}
\]

## Proof

Write \(k=2r+m\), let \(L\) be the fraction field of \(K[x_{b,s}]\), \(x\) the inclusion, and use the [[proofs/grh/upper-elementary-divisors/unipotent-points-for-deep-forms|unipotent points]] \(z_y\), \(y\in\kappa_W^{\mathcal{P}}\), and the specialisation \(\operatorname{sp}\). Let \(f=\operatorname{sp}\bigl(\sum_\beta F_\beta x^{\beta}\bigr)\in L[x_{b,s}]\); \(f\ne0\) because \(\operatorname{sp}\) is injective.

*\(f\) vanishes to order \(\tau\) at each \(z_y\).* Let \(g=g_y\) and \(G=\rho_n(g)F\). Since \(F=\rho_n(g^{-1})G\), the form of \(F\) is \(g^{-1}\cdot\sum_\beta G_\beta x^{\beta}=\sum_\beta G_\beta\prod_v(g^{-1}\cdot v)^{\beta(v)}\). As \(F\) is deep, \(G_\beta=0\) unless \(\operatorname{depth}_r(\beta)\ge\tau\). For deep \(v\), \(\operatorname{sp}(g^{-1}\cdot v)=v-z_y(v)\) lies in the maximal ideal \(\mathfrak{m}_y\subseteq L[x_{b,s}]\) of the point \(z_y\). So each term \(\operatorname{sp}(G_\beta)\prod_v\operatorname{sp}(g^{-1}v)^{\beta(v)}\) with \(G_\beta\ne0\) lies in \(\mathfrak{m}_y^{\operatorname{depth}_r(\beta)}\subseteq\mathfrak{m}_y^{\tau}\), and \(f\in\mathfrak{m}_y^{\tau}\).

*A monomial of large cost.* We use the following statement ([[?lean:New.exists_le_weight_of_mem_vanishingIdeal_pow|combinatorial Nullstellensatz with multiplicity]], proved in the library part of the development): *let \(L\) be a field, \(\kappa(u)\ge1\) integers attached to finitely many variables \(u\), and \((z_t)_{t\in S}\) pairwise distinct points indexed by a finite set with \(\prod_u\kappa(u)\le\#S\); suppose for each \(u\) there is a polynomial \(G_u\) whose monomials have cost \(\sum_u\alpha(u)/\kappa(u)<1\) with \(G_u(z_t)=z_t(u)^{\kappa(u)}\) for all \(t\). Then every nonzero polynomial \(f\) lying in \(\mathfrak{m}_{z_t}^{d}\) for all \(t\) has a monomial of cost at least \(d\).* Its hypotheses hold for the points \(z_y\): they are distinct and satisfy the equations by the [[proofs/grh/upper-elementary-divisors/points-satisfy-low-power-equations|lemma on low powers]], and \(\prod_v\kappa(v)\le q^{r(m+1)}=\#\kappa_W^{\mathcal{P}}\). Hence \(f\) has a monomial \(x^{\alpha}\) of cost \(\ge\tau\).

*Back to \(F\).* Expanding, \(f=\sum_\beta c_\beta\prod_{v\text{ deep}}v^{\beta(v)}\) with \(c_\beta=x\bigl(F_\beta\prod_{v\text{ not deep}}v^{\beta(v)}\bigr)\), so \(\alpha\) is the deep part of some \(\beta\) with \(F_\beta\ne0\). Variables that are not deep do not occur in \(\alpha\), so the cost of \(\alpha\) is \(\sum_{v\text{ deep}}\beta(v)/\kappa(v)\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.exists_le_weight_of_mem_deepForms`, `New.FrobeniusCycle.specializeShallow_polyOfCoeffs_mem_vanishingIdeal_pow`, `New.FrobeniusCycle.map_polyOfCoeffs_mem_pow_of_mem_deepForms`, `New.FrobeniusCycle.letterRep_mulVec_eq_zero_of_mem_deepForms`, `New.FrobeniusCycle.exists_eq_of_mem_support_specializeShallow`, `New.FrobeniusCycle.specializeShallow_polyOfCoeffs_ne_zero` in `src/New/UpperBound/ElementaryDivisors/Depth.lean`.
2. The head of the Lean file Lib/General/Algebra/MultivariatePolynomials.lean describes the input as a form of the combinatorial Nullstellensatz with multiplicity.
