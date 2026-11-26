+++
id = "grh-lean/arithmetic-data"
title = "The arithmetic data and their scales"
kind = "document"
summary = "The field, places, weights and dimensions used in the two estimates."
domains = ["grh-lean"]
section_mode = "continuous"
prerequisites = ["arithmetic-geometry/abelian-cm-field", "arithmetic-geometry/root-discriminant", "arithmetic-geometry/theta-lift"]
+++

Fix a modulus \(q_0\) divisible by \(18480\) and a prime \(d\equiv q_0/2-1\bmod q_0\). The construction starts with \(K=\mathbb Q(\sqrt{-d})\). An auxiliary [[arithmetic-geometry/abelian-cm-field|abelian CM field]] \(E\) has \(f\) infinite places. A [[arithmetic-geometry/cm-type|CM type]] chooses one complex embedding over each infinite place. Its place classes distinguish a set \(\Phi_a\) above \(1\bmod q_0\) and a chosen sparse set \(\Phi_b\) above \(-1\bmod q_0\).

## The two cutoffs

The smaller cutoff is \(x\), the comparison cutoff \(x_1\), and \(a=xb\). The weight \(\kappa\) equals \(b\) on \(\Phi_b\) and \(a/x_1\) elsewhere. The chain has \(m\) [[arithmetic-geometry/theta-lift|theta lifts]] with \(\sqrt x\le m\le2\sqrt x\). Thus a bound on \(m\) times a remainder can yield a square-root saving. The [[arithmetic-geometry/root-discriminant|root discriminant]] of \(E\), the weights and the level determine the estimates for the lifts.

## The quantities compared

Write \(d_T\) for the target dimension and \(k\) for the source rank in the chain. A finite-place prime sum \(s_{\rm fin}\) and an archimedean jet size \(s_\infty\) enter
\[
 H=mk\sum_\tau\bigl(s_\infty(\kappa(\tau))-s_{\rm fin}(\kappa(\tau),\tau)\bigr).
\]
The total remainder \(R\) is the sum over \(\Phi_a\) of \(s_{\rm fin}(a,\tau)\) minus its expected main term at each place. The loss allowed per dimension is \(\ell=fa(\log b)^4\). The [[grh-lean/prime-identity|exact prime-sum identity]] and the [[grh-lean/main-inequality|comparison of covolumes]] explain why \(H\) disappears and \(R\) survives. The full admissibility conditions on levels, weights and places are in the linked Lean structures.

## References

- [New/Reduction/Data/AdmissibleData.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean)
- [New/Reduction/Data/Sizes.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Sizes.lean)
- [New/Reduction/PrimeSums.lean, mainAmount](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L62)
- [New/Reduction/PrimeSums.lean, totalRemainder](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L73)
