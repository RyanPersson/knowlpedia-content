+++
id = "linear-algebra/squared-volume-factor"
title = "Squared volume factor of a linear map"
kind = "definition"
summary = "The Gram determinant of the images of an orthonormal basis measures the change in squared volume."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/linear-map", "linear-algebra/inner-product-space", "linear-algebra/gram-matrix", "linear-algebra/orthonormal-basis", "linear-algebra/conjugate-transpose", "linear-algebra/determinant", "shared-foundations/injective-function"]
+++

For a [[linear-algebra/linear-map|linear map]] \(T:V\to H\) between complex [[linear-algebra/inner-product-space|inner product spaces]] with \(d=\dim V<\infty\), its **squared volume factor** \(Z(T)\) is the [[linear-algebra/gram-matrix|Gram determinant]] of \(Te_1,\ldots,Te_d\) for any [[linear-algebra/orthonormal-basis|orthonormal basis]] \(e\) of \(V\). In dimension zero the empty determinant is one.

## Change of basis

For any ordered \(d\)-tuple \(w\) let \(A\) have the coordinates of its members as columns in \(e\). Write \(G\) for the Gram matrix of \(Te\), and \(A^*\) for the [[linear-algebra/conjugate-transpose|conjugate transpose]]. The Gram matrix of \(Tw\) is \(A^*GA\). By multiplicativity of the [[linear-algebra/determinant|determinant]],
\[
\det\operatorname{Gram}(Tw)=|\det A|^2 Z(T)=\det\operatorname{Gram}(w)\,Z(T).
\]
For another orthonormal basis, \(A^*A=I\), so \(|\det A|^2=1\). This proves independence of the chosen basis. If \(T\) is [[shared-foundations/injective-function|injective]], the Gram matrix of \(Te\) is positive definite and \(Z(T)>0\), since for every nonzero column \(a\) its quadratic form equals \(\|\sum_i a_i Te_i\|^2>0\).

## References

- [Change of Gram determinant under a linear map](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/GramDeterminant.lean#L60)
- [Twist volume](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L353)
