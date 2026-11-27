+++
id = "proofs/grh/derivatives-vacuum/copy-substitution"
title = "Substitution of a linear combination of copies of the variables"
kind = "construction"
summary = "The substitution F(z) to F(sum_k a_k z_k) into copies z_k of the variables, with the formula for its coefficients as multinomial multiples of the coefficients of F."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.copySubst", "New.copySubst_apply", "New.pderiv_copySubst", "New.map_copySubst", "New.killCompl_copySubst", "New.rescale_copySubst", "New.coeff_copySubst", "New.prod_factorial_mul_coeff_copySubst", "New.prod_factorial_mapDomain_fst", "New.mapDomain_fst_apply", "New.norm_coeff_copySubst_le"]
lean_files = ["src/New/Derivatives/Sharpness/LeastValuation.lean"]
+++

Let \(R\) be a commutative ring, \(X\) and \(K\) finite sets and \(a\in R^K\). The **copy substitution** is the \(R\)-algebra map
\[ R[\![z_x:x\in X]\!]\to R[\![z_{x,k}:(x,k)\in X\times K]\!],\qquad F\mapsto F\Bigl(\sum_{k\in K}a_k\,z_{\cdot,k}\Bigr), \]
substituting \(\sum_ka_kz_{x,k}\) for \(z_x\). For an exponent \(\gamma\) on \(X\times K\) write \(\bar\gamma\) for the exponent on \(X\) with \(\bar\gamma_x=\sum_k\gamma_{x,k}\).

## Properties

0. (Chain rule, over any commutative ring.) Writing \(S_a\) for the copy substitution, \(\partial_{z_{x,k}}S_a(F)=a_k\,S_a(\partial_{z_x}F)\) as an identity of power series. Iterating and evaluating at \(0\): \(\gamma!\,[z^\gamma]S_a(F)=a^\gamma\,\bar\gamma!\,[z^{\bar\gamma}]F\) in \(R\), with \(a^\gamma=\prod_{(x,k)}a_k^{\gamma_{x,k}}\).
1. If \(R\) is a domain of characteristic zero,
\[ [z^\gamma]\,F\Bigl(\sum_ka_kz_k\Bigr)=\prod_{(x,k)}a_k^{\gamma_{x,k}}\cdot\prod_{x}\binom{\bar\gamma_x}{(\gamma_{x,k})_k}\cdot[z^{\bar\gamma}]F, \]
with multinomial coefficients. (By property 0; cancel \(\gamma!\), which is possible in a domain of characteristic zero, and use \(\bar\gamma!=\gamma!\cdot\prod_x\binom{\bar\gamma_x}{\gamma_{x,\cdot}}\).)
2. Hence over \(\mathbb{C}_p\) with all \(\lvert a_k\rvert_p\le1\): \(\lvert[z^\gamma]F(\sum a_kz_k)\rvert_p\le\lvert[z^{\bar\gamma}]F\rvert_p\).
3. Setting all copies but the \(k\)-th to zero gives \(F(a_kz)\); the copy substitution commutes with rescaling all variables by a constant and with change of coefficients.

## References

1. Lean: `New.copySubst`, `New.copySubst_apply`, `New.pderiv_copySubst`, `New.map_copySubst`, `New.killCompl_copySubst`, `New.rescale_copySubst`, `New.coeff_copySubst`, `New.prod_factorial_mul_coeff_copySubst`, `New.prod_factorial_mapDomain_fst`, `New.mapDomain_fst_apply`, `New.norm_coeff_copySubst_le` in `src/New/Derivatives/Sharpness/LeastValuation.lean`.
