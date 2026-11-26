+++
id = "arithmetic-geometry/twisted-lattice-determinant-inequality"
title = "A determinant inequality for twisted Hermitian lattices"
kind = "theorem"
summary = "The squared covolume and twice the index bound the determinant after accounting for the extra basis vectors and the change of twist."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/twisted-hermitian-lattice", "linear-algebra/inner-product-space", "shared-foundations/injective-function", "linear-algebra/squared-volume-factor", "convex-analysis/basis-hamel-basis-and-dimension", "arithmetic-geometry/twisted-lattice-covolume", "arithmetic-geometry/twisted-lattice-index", "algebra-fields-galois/field-automorphism", "arithmetic-geometry/padic-comparison-place", "arithmetic-geometry/simultaneous-height-bound", "arithmetic-geometry/matrix-clearing-an-index", "arithmetic-geometry/integral-vectors-for-a-family-of-twists", "arithmetic-geometry/local-index-bound-for-a-gram-determinant", "linear-algebra/gram-determinant-adjoining-vectors", "linear-algebra/conjugates-of-a-rational-gram-determinant", "arithmetic-geometry/constant-family-height-inequality"]
+++

In [[arithmetic-geometry/twisted-hermitian-lattice|twisted Hermitian lattice data]] on a finite-dimensional complex [[linear-algebra/inner-product-space|inner product space]] \(V\), suppose all lifts \(\Theta_t\) are [[shared-foundations/injective-function|injective]]. Write \(Z_t\) for the [[linear-algebra/squared-volume-factor|squared volume factor]] of \(\Theta_t\). Split a [[convex-analysis/basis-hamel-basis-and-dimension|basis]] of \(V\) into \(y_1,\ldots,y_n\) and \(z_1,\ldots,z_r\). Suppose the following bounds hold.

- The family \(y\) has [[arithmetic-geometry/twisted-lattice-covolume|logarithmic squared covolume at most \(c\)]] and [[arithmetic-geometry/twisted-lattice-index|logarithmic index at most \(\delta\)]].
- At every complex [[algebra-fields-galois/field-automorphism|automorphism]] \(\sigma\), each coordinate vector \(\sigma(\Theta_1 z_j)\) in the specified rational metric has squared length at most \(e^s\).
- There are scalars \(\gamma_t\ne0\) such that \(\gamma_t\Theta_t z_j\in L_{t,\iota}\) for every \(j\) and every [[arithmetic-geometry/padic-comparison-place|comparison]] \(\iota\) at which \(t\) is allowed.
- Choose one allowed \(t_\iota\) at each comparison. The families \((|\gamma_{t_\iota}|^{-2})_\iota\) and \((Z_1/Z_{t_\iota})_\iota\) have [[arithmetic-geometry/simultaneous-height-bound|simultaneous heights at most]] \(d\) and \(v\), respectively.

Then \(c+2\delta+r(s+d)+v\ge0\).

## Proof

Write \(w=(y,z)\) and \(D_t=\det\operatorname{Gram}(\Theta_t w)\). Since \(w\) is a basis and \(\Theta_1\) is injective, \(D_1>0\). The argument bounds this one scalar at the finite and infinite comparisons.

Fix \(\iota\) over \(p\) and put \(t=t_\iota\). The index supplies a [[arithmetic-geometry/matrix-clearing-an-index|clearing matrix]] at \(\iota\) and another at \(\bar\iota\), each with loss \(e_p\). They clear into the vectors [[arithmetic-geometry/integral-vectors-for-a-family-of-twists|integral for all allowed twists]]. Both matrices therefore work for this same \(t\), since \(\iota,\bar\iota\) lie over the same prime. The [[arithmetic-geometry/local-index-bound-for-a-gram-determinant|local Gram determinant bound]] gives
\[
\left|\iota\!\left(|\gamma_t|^{2r}D_t\right)\right|_p\le p^{2e_p}.
\]
For each finite set \(S\) of primes the index assumption gives \(\sum_{p\in S}e_p\log p\le\delta\). Taking multiplier \(1\), archimedean bound \(0\) and exponents \(2e_p\) in the height definition gives the family \((|\gamma_t|^{2r}D_t)_\iota\) height at most \(2\delta\).

The [[linear-algebra/squared-volume-factor|change of basis formula]] gives \(D_t=Z_t\det\operatorname{Gram}(w)\). All \(Z_t\) are positive, so at every \(\iota\) we obtain the identity
\[
D_1=\big(|\gamma_t|^{2r}D_t\big)\,\big(|\gamma_t|^{-2}\big)^r\,\frac{Z_1}{Z_t}.
\]
[[arithmetic-geometry/simultaneous-height-bound|Multiplying height witnesses]] adds their bounds, so the constant family \(D_1\) has height at most \(2\delta+rd+v\).

At a fixed automorphism, the first \(n\) coordinate vectors have Gram determinant at most \(e^c\). [[linear-algebra/gram-determinant-adjoining-vectors|Adjoining the \(r\) remaining vectors]] multiplies this by at most \(e^{rs}\). Thus the Gram determinant of the conjugated coordinates is at most \(e^{c+rs}\) at every automorphism. Because the metric is rational, the [[linear-algebra/conjugates-of-a-rational-gram-determinant|bound for conjugates of the determinant]] gives \(|\sigma D_1|\le e^{c+rs}\) as well.

Apply the [[arithmetic-geometry/constant-family-height-inequality|product formula for a nonzero constant family]] to \(D_1\). It gives \(0\le (c+rs)+(2\delta+rd+v)\), as claimed.

## References

- [Twisted determinant inequality, with a twist at each prime](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L477)
