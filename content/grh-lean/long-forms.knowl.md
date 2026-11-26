+++
id = "grh-lean/long-forms"
title = "Theorem C · Integral forms have a lower covolume bound"
kind = "theorem"
summary = "The product formula turns a bound on twisted denominators into an archimedean lower bound."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["grh-lean/auxiliary-forms", "grh-lean/regular-twists", "grh-lean/chain-determinant", "grh-lean/one-lift", "grh-lean/gram-bound"]
+++

Let \(n\ge(1-4/b^2)d_T\) independent target forms have [[arithmetic-geometry/twisted-lattice-index|index]] at most \(\Delta\) and [[arithmetic-geometry/twisted-lattice-covolume|logarithmic squared covolume]] at most \(V\). For the [[grh-lean/arithmetic-data|admissible data]] they satisfy \(d_T(H-3\ell)\le V+2\Delta\).

## Proof

Complete the family to a basis by [[grh-lean/auxiliary-forms|auxiliary forms]] whose denominators and conjugate norms are controlled. At each [[arithmetic-geometry/padic-comparison-place|comparison place]] choose a [[grh-lean/regular-twists|regular twist]]. Its chain is injective, and the [[grh-lean/chain-determinant|chain determinant identity]] reduces the comparison of its volume with the untwisted volume to estimates for [[grh-lean/one-lift|one lift at a time]].

Apply the [[grh-lean/gram-bound|Gram determinant product inequality]] to the full basis. The missing \(d_T-n\) vectors cost at most the allowed fraction of the total error. The bounds on the single lifts supply the main amount \(d_TH\). Accounting for the auxiliary vectors and the prime losses gives \(3d_T\ell\) as the total allowance.

## References

- [New/Determinant/Twist/LongForms.lean, integral_forms_long](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L214)
