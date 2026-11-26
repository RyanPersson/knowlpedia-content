+++
id = "linear-algebra/gram-determinant-adjoining-vectors"
title = "Gram determinant after adjoining vectors"
kind = "theorem"
summary = "Adjoining vectors multiplies the Gram determinant by at most the product of their squared lengths."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/inner-product-space", "linear-algebra/gram-matrix", "linear-algebra/gram-schmidt-orthogonalization", "linear-algebra/orthogonal-projection"]
+++

For finite ordered families \(v=(v_1,\ldots,v_n)\), \(z=(z_1,\ldots,z_r)\) in a real or complex [[linear-algebra/inner-product-space|inner product space]], their [[linear-algebra/gram-matrix|Gram determinants]] satisfy
\[
\det\operatorname{Gram}(v,z)\le
\det\operatorname{Gram}(v)\prod_{j=1}^r\|z_j\|^2 .
\]

## Proof

If \(v,z\) together are dependent, the determinant on the left is zero, and the right side is nonnegative. Otherwise [[linear-algebra/gram-schmidt-orthogonalization|orthogonalize]] in the order \(v_1,\ldots,v_n,z_1,\ldots,z_r\), without normalizing. Each subtraction uses only earlier vectors, so the triangular change of columns has determinant one. It preserves every prefix Gram determinant by the transformation \(G\mapsto A^*GA\).

In the resulting diagonal matrix the first \(n\) entries have product \(\det\operatorname{Gram}(v)\). For the [[linear-algebra/orthogonal-projection|orthogonal projection]] \(P_j\) onto the span of all preceding vectors, the next diagonal entry is \(\|z_j-P_jz_j\|^2=\|z_j\|^2-\|P_jz_j\|^2\). Multiplication gives the bound.

## References

- [Adjoining vectors to a covolume estimate](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L330)
