+++
id = "linear-algebra/lattice-covolume"
title = "Covolume of a Euclidean lattice"
kind = "definition"
summary = "The volume of a fundamental parallelepiped of a full lattice."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-lattice", "linear-algebra/gram-matrix"]
+++

The **covolume** of a full [[linear-algebra/euclidean-lattice|lattice]] \(L\) in a finite-dimensional real [[linear-algebra/inner-product-space|inner product space]] is the volume of a fundamental parallelepiped. For a lattice basis \(e_1,\ldots,e_n\), it equals \(\sqrt{\det(\langle e_i,e_j\rangle)}\), the square root of the [[linear-algebra/gram-matrix|Gram determinant]].

## Passing to a sublattice

A sublattice of finite [[linear-algebra/integer-lattice-index|index]] \(k\) has \(k\) times the covolume. A change of lattice basis has [[linear-algebra/determinant|determinant]] \(\pm1\), so the formula is independent of the chosen basis.
