+++
id = "linear-algebra/mixed-gram-determinant-inequality"
title = "Cauchy–Schwarz inequality for Gram determinants"
kind = "theorem"
summary = "The determinant pairing of two families is bounded by the geometric mean of their Gram determinants."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/inner-product-space","linear-algebra/gram-matrix","linear-algebra/gram-schmidt-orthogonalization","linear-algebra/orthogonal-projection","linear-algebra/hadamard-gram-bound","linear-algebra/determinant"]
+++

For two ordered families \(v=(v_1,\ldots,v_n)\) and \(w=(w_1,\ldots,w_n)\) in a complex [[linear-algebra/inner-product-space|inner product space]], let \(M_{ij}=\langle v_i,w_j\rangle\). Then
\[
|\det M|^2\le\det\operatorname{Gram}(v)\,\det\operatorname{Gram}(w),
\]
where each factor is a [[linear-algebra/gram-matrix|Gram determinant]].

## Proof

If either family is dependent, its relation makes the rows or columns of \(M\) dependent and both sides vanish. Otherwise use [[linear-algebra/gram-schmidt-orthogonalization|Gram–Schmidt]] to choose orthonormal bases \(u,t\) of the two spans. Write \(v=uA,\ w=tB\) using columns of coefficients, and \(C_{ij}=\langle u_i,t_j\rangle\). Then \(M=A^*CB\), while the two Gram determinants are \(|\det A|^2\) and \(|\det B|^2\).

Column \(j\) of \(C\) gives the coordinates of the [[linear-algebra/orthogonal-projection|orthogonal projection]] of \(t_j\) onto the span of \(u\). Its squared length is at most \(\|t_j\|^2=1\), by orthogonality of the projection and the residual vector. [[linear-algebra/hadamard-gram-bound|Hadamard's inequality]] for the columns of \(C\) gives \(|\det C|^2=\det(C^*C)\le1\). Taking [[linear-algebra/determinant|determinants]] of \(A^*CB\) proves the claim.

## References

- [The determinant pairing inequality](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/GramDeterminant.lean#L129)
