+++
id = "proofs/grh/derivatives-vacuum/valuation-bound-at-small-non-split-primes"
title = "The valuation bound on twelve copies at a non-split prime at most k"
kind = "lemma"
summary = "At a non-split prime p <= k, for a tight frame of length M with a vector of unit linear form and a degree near the weights, v(l!) + val_12(l) <= S_p + sum of v(B_tau)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.leastValLE_twelve_localPrimeSumTotal_of_le", "New.Data.gammaPrime_mul_degree_sub_le_localPrimeSumTotal_add", "New.Data.isCouplingFamily_of_isNearPair", "New.Data.powerDegree_add_partnerDegree_le_of_isNearPair", "New.Data.leastValLE_six_of_isNearPair", "New.Data.sum_padicValNat_factorial_le_add", "New.chiK_eq_neg_one_of_ne"]
lean_files = ["src/New/Derivatives/Sharpness/Cases.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/valuation-bound-at-large-inert-primes|the lemma at large inert primes]]; \(f=\lvert\Phi\rvert\).

**Lemma.** Let \(p\le k\) be a prime with \(\chi_K(p)\ne1\), \((w,c)\) a tight frame of length \(M\) with \(\lvert\mu_{i_0,\tau}\rvert_p=1\) for some \(i_0\) and all \(\tau\), and \(l\) a degree near the weights. Then
\[ \operatorname{val}_{12}(l)\le S_p+\sum_\tau v(B(l_\tau))-\sum_\tau v(l_\tau!). \]

## Proof

Note \(p\ge13\). Let \(\Phi_0\) be the set of starts of [[proofs/grh/derivatives-vacuum/near-pair|near pairs]]; by [[proofs/grh/derivatives-vacuum/near-pairs-are-disjoint|disjointness]] each \(\tau\in\Phi_0\) has a unique exponent \(e_\tau\). Put \(j_\tau=\lfloor l_\tau/p^{e_\tau}\rfloor\) for \(\tau\in\Phi_0\) and \(j_\tau=0\) otherwise; \(\tau^+=[-p^{e_\tau}]\tau\).

*Step 1: \((\Phi_0,e)\) is a coupling family.* The \(e_\tau\) are odd. If \(\tau,\tau_1\in\Phi_0\), \(e'\le e_\tau\) is odd and \([-p^{e'}]\tau_1=\tau^+\), then \((\tau_1,e')\) is a near pair (\(e'\in I_p\), \(2e'\le2e_\tau<l_0\), start and end are \(b\)-places) with the same end as \((\tau,e_\tau)\), so \(\tau_1=\tau\), \(e'=e_\tau\).

*Step 2: \(\nu'+\nu''\le l\).* At \(t\in\Phi_0\): \(t\) is not an end, so the degree is \(p^{e_t}j_t\le l_t\). At \(t\notin\Phi_0\): \(\nu'_t=0\) and \(t\) is the end of at most one pair \((\tau,e_\tau)\); then \(t\) is a \(b\)-place and \(\nu''_t=j_\tau\le l_\tau/p^{e_\tau}\le2b/2=b=\kappa(t)\le l_t\). Write \(l=\nu'+\nu''+\eta\).

*Step 3: least valuation.* If \(\Phi_0=\emptyset\) then \(\nu'=\nu''=0\) and \(\operatorname{val}_6(0)\le0\). Otherwise \(p\) is inert and by [[proofs/grh/derivatives-vacuum/normal-form-along-a-tight-frame|the normal form]] and [[proofs/grh/derivatives-vacuum/least-valuation-along-couplings|least valuations along couplings]] (part 3),
\[ \operatorname{val}_6(\nu'+\nu'')\le\gamma_p\lvert\nu'+\nu''\rvert-\lvert j\rvert-v(\nu'!)-v(\nu''!). \]
By [[proofs/grh/derivatives-vacuum/least-valuation-with-a-unit-form|the bound with a unit form]], \(\operatorname{val}_6(\eta)\le\gamma_p\lvert\eta\rvert-v(\eta!)\). Adding, \(\operatorname{val}_{12}(l)\le\gamma_p\lvert l\rvert-\lvert j\rvert-v(\nu'!)-v(\nu''!)-v(\eta!)\).

*Step 4: factorials.* By [[proofs/grh/derivatives-vacuum/legendre-bounds-for-the-data|the Legendre bounds]] at each place (\(l_\tau\le2b\), \(p\ge3\)): \(v(l!)\le v(\nu'!)+v(\nu''!)+v(\eta!)+3f(\log b+2)\).

*Step 5: comparison with \(S_p\).* We claim \(\gamma_p\lvert l\rvert-\lvert j\rvert+3f(\log b+2)\le S_p+\sum_\tau v(B(l_\tau))\). Since \(\gamma_p\le1\) and \(l_\tau\le\kappa(\tau)+x^{42}\): \(\gamma_p\lvert l\rvert\le\gamma_p\sum_\tau\kappa(\tau)+fx^{42}\). By [[proofs/grh/derivatives-vacuum/rate-minus-predicted-valuation|the identity for the rate]] and \(v(\pi_p)\le1\): \(\gamma_p\sum\kappa(\tau)-S_p\le\sum_\tau R_\tau\). By [[proofs/grh/derivatives-vacuum/bound-for-the-partner-minimum-sum|the bound for \(R_\tau\)]] with \(c=j_\tau\) (for a near pair, \(\kappa(\tau)/p^{e_\tau}\le l_\tau/p^{e_\tau}<j_\tau+1\)): \(R_\tau\le j_\tau+1+l_0a/x_1+2b/(kp)\). So at each place
\[ 3(\log b+2)+x^{42}+R_\tau-j_\tau\le3(\log b+2)+x^{42}+1+l_0\frac{a}{x_1}+\frac{2b}{kp}\le v(B(l_\tau)) \]
by [[proofs/grh/derivatives-vacuum/errors-covered-by-the-loss-product|the lemma on errors]]. Summing over \(\tau\) gives the claim.

Steps 3–5 combine to the assertion.

## References

1. Lean: `New.Data.leastValLE_twelve_localPrimeSumTotal_of_le`, `New.Data.gammaPrime_mul_degree_sub_le_localPrimeSumTotal_add`, `New.Data.isCouplingFamily_of_isNearPair`, `New.Data.powerDegree_add_partnerDegree_le_of_isNearPair`, `New.Data.leastValLE_six_of_isNearPair`, `New.Data.sum_padicValNat_factorial_le_add`, `New.chiK_eq_neg_one_of_ne` in `src/New/Derivatives/Sharpness/Cases.lean`.
