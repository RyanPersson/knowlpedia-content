+++
id = "grh-lean/test-pairing"
title = "A test form detects the size of a lifted line"
kind = "theorem"
summary = "An integral pairing which does not vanish too deeply bounds an inverse special value."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/theta-jet", "harmonic-analysis/hecke-eigensystem"]
+++

For a main pair and a prime away from the twist modulus there is an integral test form, orthogonal to the [[harmonic-analysis/false-lift-subspace|false lifts]], whose pairing with the rank-one lift has bounded [[algebra-fields-galois/valuation-on-a-field|valuation]].

## Proof

Build the form from class sums on four blocks. The [[grh-lean/jet-sharpness|sharpness of the jet estimate]] supplies local factors attaining the required [[harmonic-analysis/theta-jet|jet valuation]], so the pairing survives to the predicted precision. Orthogonality removes the false lifted types. Project onto the line of the actual lift and use the known denominator of its projection. Comparing that pairing with the squared norm of the lifted line bounds the inverse special-value ratio at the chosen prime. Combining the local bounds with the conjugate size estimate gives its height bound.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.OneLift.HeckeValues.TwistedValueHeights:700).

## References

- [New/OneLift/HeckeValues/TwistedValueHeights.lean, exists_isTestForm_le_norm_inner_trivialLift](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean#L700)
- [New/OneLift/HeckeValues/TwistedValueHeights.lean, heightLe_inv_ratio](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean#L860)
- [New/Derivatives/Sharpness/BoundAttained.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean)
