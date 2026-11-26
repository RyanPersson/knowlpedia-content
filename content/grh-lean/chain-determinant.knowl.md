+++
id = "grh-lean/chain-determinant"
title = "Comparing a chain determinant with one-step determinants"
kind = "theorem"
summary = "Exchange identities cancel twist-independent factors and prove positivity of the determinant."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["linear-algebra/gram-matrix", "arithmetic-geometry/theta-lift"]
+++

Write \(Z(\xi)=\det(\Theta_\xi^*\Theta_\xi)\) for the full chain of [[arithmetic-geometry/theta-lift|theta lifts]] on the good target. It is positive, and its ratio to \(Z(1)\) is a product of ratios for single lifts and an explicit power of the norm of the twist modulus.

## Proof

Pair the chain with its adjoint and commute the lift maps through the triangular array one square at a time. The local exchange identities express its inner product through those of the single lifts with common scalar factors. On the good [[harmonic-analysis/hecke-eigensystem|Hecke components]] the rank identities permit passage to [[linear-algebra/gram-matrix|Gram determinants]]. Positivity gives injectivity. Dividing the identity at \(\xi\) by the identity at \(1\) eliminates factors independent of the twist. The remaining one-step ratios are exactly the quantities estimated in [[grh-lean/one-lift|the height bound]].

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.Determinant.Chain.NormOfChain:109).

## References

- [New/Determinant/Chain/NormOfChain.lean, chainDeterminant_pos](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/NormOfChain.lean#L109)
- [New/Determinant/Chain/NormOfChain.lean, exists_div_chainDeterminant_one_eq](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/NormOfChain.lean#L396)
- [New/Determinant/Chain/ChainNorms.lean, exists_isTriangle](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/ChainNorms.lean#L590)
