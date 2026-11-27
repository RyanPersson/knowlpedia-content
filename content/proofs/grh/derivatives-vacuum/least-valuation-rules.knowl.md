+++
id = "proofs/grh/derivatives-vacuum/least-valuation-rules"
title = "Rules for least valuations"
kind = "lemma"
summary = "Least valuations are subadditive in the number of copies and the degree, are bounded by valuations of coefficients after integral substitutions of copies or integral rescalings, and may be computed with monomials in the parameters."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.LeastValLE.add", "New.CMLattice.leastValLE_of_copySubst", "New.CMLattice.leastValLE_of_rescale", "New.CMLattice.LeastValLE.exists_monomial"]
lean_files = ["src/New/Derivatives/Sharpness/LeastValuation.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/least-valuation-relation|the least valuation relation]].

**Lemma.**

1. If \(\operatorname{val}_n(\nu)\le r\) and \(\operatorname{val}_{n'}(\nu')\le r'\), then \(\operatorname{val}_{n+n'}(\nu+\nu')\le r+r'\).
2. Let \(K\) be a finite set, \(A_{c,k}\in\mathbb{C}_p\) with \(\lvert A_{c,k}\rvert_p\le1\) (\(1\le c\le n\), \(k\in K\)), \(H_c\in\mathcal{O}[\![y(\mu z)]\!]\), and \(\gamma\) an exponent on \(X\times K\). If the coefficient of \(z^\gamma\) in \(\prod_c(H_c\Theta)(\sum_kA_{c,k}z_k)\) ([[proofs/grh/derivatives-vacuum/copy-substitution|copy substitutions]]) has absolute value \(\ge p^{-r}\), then \(\operatorname{val}_n(\bar\gamma)\le r\).
3. If \(H_c\in\mathcal{O}[\![y(\mu z)]\!]\) and \(\delta_c\in\mathbb{C}_p\) with \(\lvert\delta_c\rvert_p\le1\) (\(1\le c\le n\)), and the coefficient of \(z^\nu\) in \(\prod_c(H_c\Theta)(\delta_cz)\) has absolute value \(\ge p^{-r}\), then \(\operatorname{val}_n(\nu)\le r\).
4. If \(\operatorname{val}_n(\nu)\le r\), the witnesses \(H_c\) can be taken to be monomials \(\prod_jy(\mu_jz)^{e_{c,j}}\) with \(\lvert e_c\rvert\le\lvert\nu\rvert\).

## Proof

1. Concatenate the witnesses and multiply the two inequalities.

2. The coefficient of a product is a finite sum over decompositions \(\gamma=\sum_c\beta_c\) of products of coefficients; by the ultrametric inequality one term has absolute value \(\ge p^{-r}\). By property 2 of the copy substitution each factor is bounded by \(\lvert[z^{\bar\beta_c}](H_c\Theta)\rvert_p\), and \(\sum_c\bar\beta_c=\bar\gamma\).

3. The case of 2 with a single copy (\(K\) a point).

4. For each \(\alpha_c\) apply [[proofs/grh/derivatives-vacuum/largest-coefficient-among-integral-series|the lemma on largest coefficients]] with \(s=\Theta\): a monomial of degree \(\le\lvert\alpha_c\rvert\le\lvert\nu\rvert\) has a coefficient at \(\alpha_c\) at least as large as that of \(H_c\Theta\).

## References

1. Lean: `New.CMLattice.LeastValLE.add`, `New.CMLattice.leastValLE_of_copySubst`, `New.CMLattice.leastValLE_of_rescale`, `New.CMLattice.LeastValLE.exists_monomial` in `src/New/Derivatives/Sharpness/LeastValuation.lean`.
