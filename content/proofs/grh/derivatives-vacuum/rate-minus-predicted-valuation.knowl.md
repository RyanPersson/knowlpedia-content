+++
id = "proofs/grh/derivatives-vacuum/rate-minus-predicted-valuation"
title = "The rate times the total weight minus the predicted valuation"
kind = "lemma"
summary = "gamma_p times the sum of the weights minus the predicted valuation S_p equals v(pi_p) times the sum over the places of the partner minimum sums."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.mul_sum_weight_sub_localPrimeSumTotal", "New.Data.summable_posPart_sub_weight"]
lean_files = ["src/New/Derivatives/Sharpness/NearPairs.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/partner-minimum-sum|the partner minimum sum]]. Let \(v(\pi_p)\) be the [[?lean:New.piPrimeValuation|valuation of \(\pi_p\)]], \(\gamma_p=v(\pi_p)\sum_{e\in I_p}p^{-e}\) the [[?lean:New.gammaPrime|rate]], and
\[ S_p=\sum_{\tau\in\Phi}v(\pi_p)\sum_{e\in I_p}\Bigl(\frac{\kappa(\tau)}{p^e}-\kappa([-p^e]\tau)\Bigr)^{+} \]
the [[?lean:New.Data.localPrimeSumTotal|predicted valuation]] (the total local prime sum at \(p\)).

**Lemma.** For every prime \(p\): the series defining \(S_p\) converge, and
\[ \gamma_p\sum_{\tau\in\Phi}\kappa(\tau)-S_p=v(\pi_p)\sum_{\tau\in\Phi}R_\tau . \]

## Proof

Convergence: \(0\le(y/p^e-\kappa)^+\le\lvert y\rvert/p^e\) as \(\kappa\ge0\). For the identity, at each \(\tau\) use \(\gamma_p\kappa(\tau)=v(\pi_p)\sum_{e\in I_p}\kappa(\tau)/p^e\) ([[?lean:New.hasSum_div_pow_positivePartnerExponents|the geometric sum over \(I_p\)]]) and \(y-(y-z)^+=\min(y,z)\) termwise.

## References

1. Lean: `New.Data.mul_sum_weight_sub_localPrimeSumTotal`, `New.Data.summable_posPart_sub_weight` in `src/New/Derivatives/Sharpness/NearPairs.lean`.
