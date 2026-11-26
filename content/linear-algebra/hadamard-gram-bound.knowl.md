+++
id = "linear-algebra/hadamard-gram-bound"
title = "Hadamard’s Gram determinant inequality"
kind = "theorem"
summary = "The Gram determinant of a finite family is bounded above by the product of the squared vector norms."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/gram-matrix", "linear-algebra/orthogonal-projection"]
+++

If \(v_1,\ldots,v_n\) are vectors in an [[linear-algebra/inner-product-space|inner product space]] and \(G\) is their [[linear-algebra/gram-matrix|Gram matrix]], then
\[
0\le\det G\le\prod_{i=1}^n\|v_i\|^2 .
\]

## Proof

If the vectors are dependent the [[linear-algebra/determinant|determinant]] is zero. Otherwise [[linear-algebra/gram-schmidt-orthogonalization|orthogonalize the family]] by subtracting from \(v_i\) its [[linear-algebra/orthogonal-projection|orthogonal projection]] onto the span of the earlier vectors. This triangular change of family has determinant one, so it preserves the Gram determinant. The new Gram matrix is diagonal, and each diagonal entry is at most \(\|v_i\|^2\).

## References

- [Lib/General/LinearAlgebra/GramDeterminant.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/GramDeterminant.lean)
