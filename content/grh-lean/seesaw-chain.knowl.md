+++
id = "grh-lean/seesaw-chain"
title = "Identifying the two chains of lifts"
kind = "theorem"
summary = "Moving a period across successive theta kernels expresses the lower chain as an upper-chain calculation."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/theta-seesaw", "harmonic-analysis/automorphic-poincare-series", "harmonic-analysis/automorphic-period"]
+++

For the ramified source and the chosen normalization of the [[harmonic-analysis/automorphic-poincare-series|Poincaré map]], applying the chain of [[arithmetic-geometry/theta-lift|theta lifts]] on the target agrees with a composite lift of a suitable finite chain datum on the source.

## Proof

Pair the lower chain with a test form on its last definite unitary group. Unfold the Poincaré series and move the [[harmonic-analysis/automorphic-period|period integral]] across the first pair using the [[harmonic-analysis/theta-seesaw|theta seesaw identity]]. At each step the finite variables give a weighted sum over classes and the real integral is evaluated separately. Repeat through all \(m\) pairs. At the top the pairing reads the restriction of the source-side composite. The common scalar is incorporated in the normalization. Equality against every test form identifies the two vectors.

## References

- [New/UpperBound/Seesaw/SeesawIdentity.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean)
- [New/Reduction/ShortAndEnough.lean, exists_lowerChain_poincare_eq](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L217)
