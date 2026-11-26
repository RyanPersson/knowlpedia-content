+++
id = "proofs/grh/derivatives-vacuum/valuation-bound-at-large-inert-primes"
title = "The valuation bound on twelve copies at an inert prime above k"
kind = "lemma"
summary = "At an inert prime p > k, for a tight frame of length M and a degree near the weights, v(l!) + val_12(l) <= S_p + 2 sum of v(B_tau)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.leastValLE_twelve_of_lt", "New.Data.padicValNat_factorial_sub_min_le", "New.Data.powerDegree_add_partnerDegree_le_of_k_lt", "New.Data.div_le_lossFactorCount", "New.Data.posPart_le_localPrimeSum", "New.Data.partner_bijective"]
lean_files = ["src/New/Derivatives/Sharpness/Cases.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/least-valuation-zero-at-inert-primes|the lemma at inert primes]]; \(n^\sharp\), \(B(\cdot)\) are the [[proofs/grh/derivatives-vacuum/loss-product|loss factor count and loss product]], \(v=v_p\).

**Lemma.** Let \(p>k\) be inert in \(K\), \((w,c)\) a tight frame of length \(M\), and \(l\) a degree [[proofs/grh/derivatives-vacuum/degree-near-the-weights|near the weights]]. Then
\[ \operatorname{val}_{12}(l)\le S_p+2\sum_\tau v(B(l_\tau))-\sum_\tau v(l_\tau!). \]

## Proof

Write \(\tau^+=[-p]\tau\); \(\tau\mapsto\tau^+\) is a bijection of \(\Phi\). Put \(i_\tau=\lfloor(l_\tau-n^\sharp)^+/p\rfloor\) and \(j_\tau=\min(i_\tau,l_{\tau^+})\).

*Couplings.* All places with exponents \(e_\tau=1\) form a [[proofs/grh/derivatives-vacuum/coupling-family|coupling family]] (the only odd \(e'\le1\) is \(1\), and \(\tau\mapsto\tau^+\) is injective). Since \(l_\tau\le2b\) and \(p>k\): \(i_\tau\le2b/k\le n^\sharp\). The degree \(\nu'+\nu''\) of \(\prod_\tau(z_\tau^pz_{\tau^+})^{j_\tau}\) is \(\le l\): at \(t=\tau^+\) it is \(p\,j_t+j_\tau\le(l_t-n^\sharp)^++\min(n^\sharp,l_t)\le l_t\). Write \(l=\nu'+\nu''+\eta\).

*Least valuation.* \(p\ge13>2\) (non-split primes are \(\ge13\)). By [[proofs/grh/derivatives-vacuum/normal-form-along-a-tight-frame|the normal form along the frame]], integrality of the forms, and [[proofs/grh/derivatives-vacuum/least-valuation-along-couplings|least valuations along couplings]] (part 2), \(\operatorname{val}_6(\nu'+\nu'')\le-\sum_\tau j_\tau\). By [[proofs/grh/derivatives-vacuum/least-valuation-zero-at-inert-primes|the lemma at inert primes]], \(\operatorname{val}_6(\eta)\le0\). Hence \(\operatorname{val}_{12}(l)\le-\sum_\tau j_\tau\).

*Comparison at one place.* It remains to show \(v(l_\tau!)-j_\tau\le S_{p,\tau}+2v(B(l_\tau))\), where \(S_{p,\tau}\) is the local prime sum at \(\tau\) (\(S_p=\sum_\tau S_{p,\tau}\)). By the properties of the loss product and one step of Legendre's formula,
\[ v(l_\tau!)\le v((l_\tau-n^\sharp)^+!)+v(B)=i_\tau+v(i_\tau!)+v(B)\le i_\tau+2v(B), \]
because \(i_\tau\le n^\sharp\) gives \(v(i_\tau!)\le v(n^\sharp!)\le v(B)\). Next \(l_\tau-n^\sharp\le\kappa(\tau)\) (as \(l_\tau\le\kappa(\tau)+x^{42}\) and \(x^{42}\le n^\sharp\)), so \(i_\tau\le\kappa(\tau)/p\); and \(l_{\tau^+}\ge\kappa(\tau^+)\). Thus
\[ i_\tau-j_\tau=(i_\tau-l_{\tau^+})^+\le\Bigl(\frac{\kappa(\tau)}{p}-\kappa(\tau^+)\Bigr)^+\le S_{p,\tau}, \]
the last being the term \(e=1\) of the local prime sum (\(v(\pi_p)=1\) as \(p\ne d\)).

## References

1. Lean: `New.Data.leastValLE_twelve_of_lt`, `New.Data.padicValNat_factorial_sub_min_le`, `New.Data.powerDegree_add_partnerDegree_le_of_k_lt`, `New.Data.div_le_lossFactorCount`, `New.Data.posPart_le_localPrimeSum`, `New.Data.partner_bijective` in `src/New/Derivatives/Sharpness/Cases.lean`.
