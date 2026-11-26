+++
id = "grh-lean/auxiliary-forms"
title = "Completing a nearly full family to a basis"
kind = "theorem"
summary = "A spanning reserve of vectors with bounded denominators and conjugate sizes controls missing dimensions."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/theta-seesaw", "harmonic-analysis/automorphic-period"]
+++

For the target there are nonzero scalars \(\gamma_\xi\), with \(\gamma_1=1\), and a spanning set of forms \(z\) such that \(\gamma_\xi\Theta_\xi z\) is integral away from the twist modulus and each conjugate of \(\Theta_1z\) has squared norm at most \(\exp(2x_1^2b^2)\).

## Proof

Start with restrictions of short forms. Pair their chain of lifts with delta forms, which read off individual values. Use successive [[harmonic-analysis/theta-seesaw|exchanges of theta lifts]] on a square grid to express each pairing as a scalar times a final [[harmonic-analysis/automorphic-period|period]]. Bound the denominators of this period away from the modulus and its conjugate size at the trivial twist. The product of the exchange factors gives \(\gamma_\xi\). Project to the good target. Linear algebra can now complete any independent family by exactly the missing number of these vectors.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#module=New.Determinant.AuxiliaryForms.SpanningForms).

## References

- [New/Determinant/AuxiliaryForms/SpanningForms.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/SpanningForms.lean)
- [New/Determinant/Twist/LongForms.lean, exists_span_isAuxiliaryForm_eq_top](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L59)
