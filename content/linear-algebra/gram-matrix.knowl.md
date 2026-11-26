+++
id = "linear-algebra/gram-matrix"
title = "Gram matrix of a family of vectors"
kind = "definition"
summary = "The matrix of all pairwise inner products of an ordered family."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/inner-product-space"]
+++

For vectors \(v_1,\ldots,v_n\) in a real or complex [[linear-algebra/inner-product-space|inner product space]], the **Gram matrix** is \(G_{ij}=\langle v_i,v_j\rangle\), with the inner product conjugate-linear in the first variable in the complex case. Its [[linear-algebra/determinant|determinant]] is the squared volume of their parallelepiped in the real case.

## A repeated direction

For two unit vectors the [[linear-algebra/determinant|determinant]] is \(1-|\langle v_1,v_2\rangle|^2\). It is zero when the vectors lie on the same line and one when they are [[linear-algebra/orthogonality|orthogonal]].

## References

- [Lib/General/LinearAlgebra/GramDeterminant.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/GramDeterminant.lean)
