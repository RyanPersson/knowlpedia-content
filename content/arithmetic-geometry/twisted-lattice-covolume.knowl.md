+++
id = "arithmetic-geometry/twisted-lattice-covolume"
title = "Logarithmic squared covolume bound"
kind = "definition"
summary = "A simultaneous upper bound on Gram determinants at the complex conjugates of the untwisted coordinates."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/twisted-hermitian-lattice", "linear-algebra/gram-matrix"]
+++

In [[arithmetic-geometry/twisted-hermitian-lattice|twisted Hermitian lattice data]], let \(v_i\) be the coordinate vector of the untwisted lift \(\Theta_1 y_i\). The family has **logarithmic squared covolume at most \(c\)** if for every [[algebra-fields-galois/field-automorphism|field automorphism]] \(\sigma\) of \(\mathbb C\) the [[linear-algebra/gram-matrix|Gram determinant]] of the vectors \(\sigma(v_i)\), taken using the specified rational metric, is at most \(e^c\).

## A bound from lengths

If each conjugate has squared length at most \(e^u\), [[linear-algebra/hadamard-gram-bound|Hadamard’s inequality]] gives \(c=nu\) for a family of \(n\) vectors. The use of a Gram [[linear-algebra/determinant|determinant]] accounts for measuring squared volume.

## Squared volume

For a full [[linear-algebra/euclidean-lattice|Euclidean lattice]] with a basis of vectors, the Gram determinant is the square of its [[linear-algebra/lattice-covolume|ordinary covolume]]. Taking its logarithm explains the squared convention.

## References

- [New/Reduction/Lattices/TwistedLattice.lean, CovolumeLe](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L275)
