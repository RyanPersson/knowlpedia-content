+++
id = "arithmetic-geometry/local-index-bound-for-a-gram-determinant"
title = "The local index bound for a Gram determinant"
kind = "theorem"
summary = "Clearing at conjugate comparisons costs one determinant factor at each comparison."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/padic-comparison-place", "linear-algebra/inner-product-space", "arithmetic-geometry/matrix-clearing-an-index", "linear-algebra/gram-matrix", "linear-algebra/block-matrix", "algebra-fields-galois/valuation-ring", "linear-algebra/determinant"]
+++

Let \(\iota\) be a [[arithmetic-geometry/padic-comparison-place|comparison]] over \(p\), and put \(\bar\iota(x)=\iota(\bar x)\). In a complex [[linear-algebra/inner-product-space|inner product space]] fix local modules \(L_\iota,L_{\bar\iota}\) with \(\langle L_{\bar\iota},L_\iota\rangle\subseteq\mathcal O_\iota\). Let \(y=(y_1,\ldots,y_n)\), \(z=(z_1,\ldots,z_r)\). Assume both conditions below.

- At each comparison a [[arithmetic-geometry/matrix-clearing-an-index|matrix carries \(y\) into the corresponding module with loss at most \(e\)]].
- For a scalar \(\gamma\), every \(\gamma z_j\) belongs to both modules.

Writing \(D=\det\operatorname{Gram}(y,z)\) for the [[linear-algebra/gram-matrix|Gram determinant]], one has
\[
\left|\iota\big((\bar\gamma\gamma)^rD\big)\right|_p\le p^{2e}.
\]

## Proof

Choose clearing matrices \(U\) at \(\iota\) and \(U'\) at \(\bar\iota\). Extend them to [[linear-algebra/block-matrix|block diagonal matrices]] \(A=\operatorname{diag}(U,\gamma I_r)\) and \(A'=\operatorname{diag}(U',\gamma I_r)\). They act by row combinations on the ordered list \(w=(y,z)\). The rows of \(A'w\) lie in \(L_{\bar\iota}\) and those of \(Aw\) lie in \(L_\iota\). Thus every entry of the matrix \((\langle(A'w)_i,(Aw)_j\rangle)_{ij}\) lies in the [[algebra-fields-galois/valuation-ring|valuation ring]] \(\mathcal O_\iota\). Its determinant also lies there since it is an integral polynomial in the entries.

The inner product is conjugate-linear in its first variable. The matrix just formed equals \(\overline{A'}\,\operatorname{Gram}(w)\,A^{\mathsf T}\). Its [[linear-algebra/determinant|determinant]] is
\[
\overline{\det U'}\,\det U\,(\bar\gamma\gamma)^rD .
\]
The first two factors have product of \(p\)-adic absolute values at least \(p^{-2e}\), since \(|\iota(\overline{\det U'})|_p=|\bar\iota(\det U')|_p\). The whole product has absolute value at most one. Division gives the claimed bound.

## References

- [Clearing the two families and bounding the determinant](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L412)
