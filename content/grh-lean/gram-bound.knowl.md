+++
id = "grh-lean/gram-bound"
title = "Why the logarithmic index enters twice"
kind = "theorem"
summary = "The product formula applied to a full Gram determinant compares every finite cost with archimedean size."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/twisted-hermitian-lattice", "arithmetic-geometry/twisted-lattice-covolume", "arithmetic-geometry/twisted-lattice-index", "arithmetic-geometry/product-formula"]
+++

In the [[arithmetic-geometry/twisted-hermitian-lattice|twisted-lattice determinant inequality]], a [[arithmetic-geometry/twisted-lattice-index|logarithmic index bound]] \(\Delta\) contributes \(2\Delta\) when paired with an upper bound on the [[arithmetic-geometry/twisted-lattice-covolume|logarithmic squared covolume]]. The comparison also includes the heights of the twist-volume ratio and any auxiliary vectors completing the basis.

## Proof

Complete the given vectors to a basis. At each finite [[arithmetic-geometry/padic-comparison-place|comparison place]] change the first vectors by an integral matrix \(A\) that clears their denominators, and scale the auxiliary vectors as required. The [[linear-algebra/gram-matrix|Gram matrix]] of a changed basis is \(A^*GA\), so its [[linear-algebra/determinant|determinant]] changes by \(\overline{\det A}\det A\). The negative logarithm of its local absolute value therefore charges the index twice.

The integral twisted Gram determinant has bounded denominators. The [[arithmetic-geometry/product-formula|product formula]], expressed through the simultaneous height inequality, compares it to the untwisted determinant. At the infinite places use the covolume bound for the original vectors and [[linear-algebra/hadamard-gram-bound|Hadamard’s inequality]] for the added vectors. Combining the finite and infinite estimates gives the stated cost.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.Reduction.Lattices.TwistedLattice:477).

## References

- [New/Reduction/Lattices/TwistedLattice.lean, covolume_add_index_nonneg](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L477)
