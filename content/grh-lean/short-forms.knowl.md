+++
id = "grh-lean/short-forms"
title = "Theorem A · A spanning family with short lifts"
kind = "theorem"
summary = "Uniform bounds on the conjugate squared norms and the finite-place index of translated images."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["grh-lean/seesaw-chain", "grh-lean/finite-gain", "grh-lean/archimedean-size", "arithmetic-geometry/twisted-lattice-index"]
+++

For [[grh-lean/arithmetic-data|admissible data]], integral forms span the ramified source even after requiring that every translated, projected image have untwisted lift of squared norm at most \(\exp(H-mR+\ell)\) under every conjugation. For a family of these images from translates \(T\), the [[arithmetic-geometry/twisted-lattice-index|index]] is bounded by \(2|T|\dim(S)\,fa(\log b)^3\), where \(S\) is the ramified source.

## Proof

Start with the short integral generators of the source. The [[grh-lean/seesaw-chain|seesaw calculation]] writes their lower-chain images as a composite lift on which both estimates can be made. [[grh-lean/finite-gain|Local divisibility]] supplies a normalization by the prime gains. The [[grh-lean/archimedean-size|archimedean jet estimate]] bounds every conjugate. The logarithm of the normalization cancels the sum of the finite gains. The remaining upper bound is \(H-mR+\ell\), uniformly in the translate.

For the index, at each prime change the source lattice by a matrix of controlled [[linear-algebra/determinant|determinant]] that makes the images integral. The bound on its [[algebra-modules/elementary-divisor-theorem|elementary divisors]] adds over translates and scales with the source dimension. The prime-weighted sum of the local losses is at most \(fa(\log b)^3\) before the factor \(2|T|\dim(S)\).

## References

- [New/Reduction/ShortAndEnough.lean, span_short_integralRamified_eq_top](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L254)
- [New/Reduction/ShortAndEnough.lean, indexLe_normalizedPoincare](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L373)
