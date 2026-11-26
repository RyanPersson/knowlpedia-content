+++
id = "grh-lean/one-lift"
title = "The cost of one lift in the determinant ratio"
kind = "theorem"
summary = "A comparison operator relates one Gram determinant to special values and controlled projections."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/simultaneous-height-bound", "grh-lean/projection-denominators", "grh-lean/test-pairing"]
+++

For a regular twist family, the ratios \(Z_j(1)/Z_j(\xi_\iota^j)\) of the one-step Gram [[linear-algebra/determinant|determinants]] satisfy a [[arithmetic-geometry/simultaneous-height-bound|simultaneous height bound]]. Their product, together with the chain factors, bounds the height of \(Z(1)/Z(\xi_\iota)\).

## Proof

Form a comparison operator from a gluing map and its adjoint. Integral vectors give it a rank-one expansion. It preserves integrality away from the twist modulus, and its untwisted conjugates have a norm bound. Multiplying the lift [[linear-algebra/determinant|determinant]] by the determinant of the projected comparison operator leaves a quantity whose twist dependence is explicit in Hecke special values.

Use the [[grh-lean/projection-denominators|denominator estimate]] on that projection. For the special values a [[grh-lean/test-pairing|small-valuation test pairing]] bounds their inverse ratios. Sum the resulting logarithmic height estimates over \(j\). The chain identity brings the sum into [[grh-lean/long-forms|Theorem C]].

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#module=New.OneLift.LiftVolumeHeight).

## References

- [New/OneLift/LiftVolumeHeight.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean)
- [New/Determinant/Twist/LongForms.lean, heightLe_chainDeterminant_one_div](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L180)
