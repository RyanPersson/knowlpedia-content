+++
id = "proofs/grh/derivatives-vacuum/degree-near-the-weights"
title = "Degrees near the weights"
kind = "definition"
summary = "A degree l on the places with weight(tau) <= l_tau <= weight(tau) + x^42 at every place."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsNearWeights", "New.Data.le_two_mul_b"]
lean_files = ["src/New/Derivatives/Sharpness/Cases.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with [[?lean:New.Data.weight|weights]] \(\kappa(\tau)\), \(\tau\in\Phi\), and size parameter \(x\). A degree \(l=(l_\tau)_{\tau\in\Phi}\in\mathbb{N}^\Phi\) is **near the weights** if
\[ \kappa(\tau)\le l_\tau\le\kappa(\tau)+x^{42}\qquad\text{for all }\tau\in\Phi. \]

## Properties

Then \(l_\tau\le2b\) for all \(\tau\), since \(\kappa(\tau)+x^{42}\le2b\) ([[?lean:New.Data.weight_add_x_pow_le_two_mul_b|a scale inequality]]).

## References

1. Lean: `New.Data.IsNearWeights`, `New.Data.le_two_mul_b` in `src/New/Derivatives/Sharpness/Cases.lean`.
