+++
id = "arithmetic-geometry/covolume-bound-from-twist-estimates"
title = "A lower covolume bound from estimates on twists"
kind = "theorem"
summary = "A spanning set of controlled lifts and bounds on two height families give a lower bound for a nearly full family."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/twisted-hermitian-lattice","linear-algebra/squared-volume-factor","arithmetic-geometry/twisted-lattice-covolume","arithmetic-geometry/twisted-lattice-index","arithmetic-geometry/padic-comparison-place","arithmetic-geometry/simultaneous-height-bound","linear-algebra/complete-basis-from-spanning-set","arithmetic-geometry/twisted-lattice-determinant-inequality"]
+++

Let \(V\) have dimension \(D\) and [[arithmetic-geometry/twisted-hermitian-lattice|twisted Hermitian lattice data]] with injective lifts. Write \(Z_t\) for their [[linear-algebra/squared-volume-factor|squared volume factors]]. Let \(y_1,\ldots,y_n\) be independent, with [[arithmetic-geometry/twisted-lattice-covolume|squared covolume bound \(c\)]] and [[arithmetic-geometry/twisted-lattice-index|index bound \(\delta\)]], both logarithmic. Fix real parameters \(b>0\), \(x_1\ge0\), \(E\ge b\) and \(H\). Assume all of the following.

- A spanning set \(S\) of \(V\) has squared length after the untwisted lift at most \(\exp(2x_1^2b^2)\) at every conjugate in the rational coordinates. There are scalars \(\gamma_t\ne0\) such that \(\gamma_t\Theta_t z\in L_{t,\iota}\) for all \(z\in S\) whenever \(t\) is allowed at the [[arithmetic-geometry/padic-comparison-place|comparison]] \(\iota\).
- There is a choice of allowed \(t_\iota\) such that the [[arithmetic-geometry/simultaneous-height-bound|simultaneous height bounds]] for \(|\gamma_{t_\iota}|^{-2}\) and \(Z_1/Z_{t_\iota}\) are respectively \(b\) and \(D(b+E-H)\).
- The dimension deficit satisfies \((D-n)(2x_1^2b^2+b)\le Db\).

Then \(D(H-3E)\le c+2\delta\).

## Proof

[[linear-algebra/complete-basis-from-spanning-set|Complete the independent family to a basis]] with \(r=D-n\) members of \(S\). The spanning-set hypotheses give the length and integrality bounds on these auxiliary vectors for the [[arithmetic-geometry/twisted-lattice-determinant-inequality|twisted determinant inequality]]. Applying it to the chosen twists yields
\[
 0\le c+2\delta + r(2x_1^2 b^2+b)+D(b+E-H).
\]
The dimension deficit bounds the third term by \(Db\). Rearranging gives \(D(H-E-2b)\le c+2\delta\), and \(b\le E\) implies \(H-3E\le H-E-2b\). Multiplying by \(D\ge0\) gives the claimed constant.

## References

- [The final deduction in the lower bound for integral forms](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L214)
- [Dimension deficit and cost of auxiliary forms](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L120)
