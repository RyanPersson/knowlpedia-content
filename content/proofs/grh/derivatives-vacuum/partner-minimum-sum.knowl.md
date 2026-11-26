+++
id = "proofs/grh/derivatives-vacuum/partner-minimum-sum"
title = "The partner minimum sum of a place"
kind = "definition"
summary = "The sum over the exponents e in I_p of the minimum of the weight of tau divided by p^e and the weight of the partner of tau at e."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.partnerMinSum", "New.Data.partnerMinTerm", "New.Data.partnerMinTerm_nonneg", "New.Data.partnerMinTerm_le_div", "New.Data.partnerMinSum_nonneg", "New.Data.summable_partnerMinTerm", "New.Data.partnerMinTerm_add_le", "New.Data.weight_of_notMem", "New.Data.weight_of_mem", "New.Data.b_le_weight"]
lean_files = ["src/New/Derivatives/Sharpness/NearPairs.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(\kappa\colon\Phi\to\mathbb{N}\) the [[?lean:New.Data.weight|weight]] (\(\kappa(\tau)=b\) at the \(b\)-places and \(a/x_1\) elsewhere, \(a=xb\)), \(p\) a prime and \(I_p\) the set of positive partner exponents. For \(\tau\in\Phi\),
\[ R_\tau=R_\tau(p)=\sum_{e\in I_p}\min\Bigl(\frac{\kappa(\tau)}{p^e},\ \kappa([-p^e]\tau)\Bigr). \]

## Properties

The terms are nonnegative and at most \(\kappa(\tau)/p^e\le b/2^e\), so the series converges.

## References

1. Lean: `New.Data.partnerMinSum`, `New.Data.partnerMinTerm`, `New.Data.partnerMinTerm_nonneg`, `New.Data.partnerMinTerm_le_div`, `New.Data.partnerMinSum_nonneg`, `New.Data.summable_partnerMinTerm`, `New.Data.partnerMinTerm_add_le`, `New.Data.weight_of_notMem`, `New.Data.weight_of_mem`, `New.Data.b_le_weight` in `src/New/Derivatives/Sharpness/NearPairs.lean`.
