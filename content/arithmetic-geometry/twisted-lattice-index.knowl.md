+++
id = "arithmetic-geometry/twisted-lattice-index"
title = "Logarithmic index bound in a twisted lattice"
kind = "definition"
summary = "The total determinant loss required to make a finite family simultaneously integral at every allowed twist."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/twisted-hermitian-lattice", "arithmetic-geometry/padic-comparison-place", "linear-algebra/determinant"]
+++

For a family \(y_1,\ldots,y_n\) in [[arithmetic-geometry/twisted-hermitian-lattice|twisted Hermitian lattice data]], **index at most \(\delta\)** means that there are \(e_p\ge0\) with \(\sum_{p\in S} e_p\log p\le\delta\) for every [[shared-foundations/finite-set|finite set]] of primes \(S\). For each [[arithmetic-geometry/padic-comparison-place|comparison]] \(\iota\) over \(p\), a single matrix \(U\in M_n(\mathcal O_\iota)\) must make every row combination \(\sum_j U_{ij}y_j\) integral for all allowed twists and satisfy \(|\iota(\det U)|_p\ge p^{-e_p}\).

## Why the determinant matters

A clearing matrix can multiply vectors by arbitrarily large [[analytic-number-theory/prime-power|prime powers]]. The lower bound on its [[linear-algebra/determinant|determinant]] limits the cost of clearing the denominators.

## References

- [New/Reduction/Lattices/TwistedLattice.lean, IndexLe](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L159)
