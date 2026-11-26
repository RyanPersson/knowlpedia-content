+++
id = "arithmetic-geometry/matrix-clearing-an-index"
title = "Clearing a family into an integral module with bounded loss"
kind = "definition"
summary = "An integral change of rows carries a family into a submodule and has bounded determinant valuation."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/padic-comparison-place","algebra-fields-galois/valuation-ring","algebra-modules/submodule","linear-algebra/matrix","shared-foundations/p-adic-valuation","linear-algebra/determinant"]
+++

Fix a [[arithmetic-geometry/padic-comparison-place|comparison]] \(\iota\) over \(p\), with [[algebra-fields-galois/valuation-ring|valuation ring]] \(\mathcal O_\iota\). Let \(M\) be an \(\mathcal O_\iota\)-[[algebra-modules/submodule|submodule]] of a complex vector space and let \(y_1,\ldots,y_n\) be vectors. A [[linear-algebra/matrix|matrix]] \(U\in M_n(\mathcal O_\iota)\) **carries \(y\) into \(M\) with loss at most \(e\)** if every \(\sum_j U_{ij}y_j\) lies in \(M\) and
\[
|\iota(\det U)|_p\ge p^{-e}.
\]
The latter condition bounds the [[shared-foundations/p-adic-valuation|valuation]] of the [[linear-algebra/determinant|determinant]], with \(v_p(p)=1\).

## References

- [Local carrying matrices](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L75)
