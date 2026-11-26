+++
id = "grh-lean/archimedean-size"
title = "Archimedean size of the jets"
kind = "theorem"
summary = "Factorial growth and a CM period give a common normalization for prime and infinite places."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/theta-jet", "arithmetic-geometry/chowla-selberg-period", "asymptotics/stirlings-approximation"]
+++

In the [[grh-lean/arithmetic-data|arithmetic data]], the archimedean jet-size term for derivative order \(j\) is \(s_\infty(j)=\log(j!)+j\log(M/\Omega)\). It bounds contributions of the rows in the composite lift together with the prescribed losses.

## Proof

Estimate each [[harmonic-analysis/theta-jet|jet]] at every conjugate, then sum the row estimates through the chain. [[asymptotics/stirlings-approximation|Stirling’s formula]] controls \(\log(j!)\). The [[arithmetic-geometry/chowla-selberg-period|CM period]] contributes the logarithmic derivative also present in the expected prime sum. Their common constant disappears on subtraction. The level is chosen so that the residual term involving the geometric mean weight and the [[arithmetic-geometry/root-discriminant|root discriminant]] is absorbed by the level term. Projection to the good target contributes a bounded additional factor.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.UpperBound.Size.ArchimedeanSize:436).

## References

- [New/UpperBound/Size/ArchimedeanSize.lean, weylNormSq_compositeLift_le](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean#L436)
- [New/UpperBound/Size/ArchimedeanSize.lean, jetSize_sub_mainPrimeSum_le](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean#L74)
- [New/UpperBound/Size/Estimates.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean)
