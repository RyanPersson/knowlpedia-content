+++
id = "arithmetic-geometry/colength-of-lattices"
title = "Colength of a sublattice"
kind = "definition"
summary = "The length of the torsion quotient of two integral lattices."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/valuation-ring", "algebra-modules/elementary-divisor-theorem"]
+++

For full lattices \(L'\subset L\) of equal rank over a discrete [[algebra-fields-galois/valuation-ring|valuation ring]] \(\mathcal O\), the **colength** of \(L'\) in \(L\) is the length of the \(\mathcal O\)-module \(L/L'\), the number of simple factors in a [[algebra-modules/composition-series-module|composition series]].

## Computing the length

Write the inclusion in elementary-divisor form with diagonal entries \(\pi^{e_i}\), where \(\pi\) is a [[algebra-fields-galois/uniformizer|uniformizer]]. By the [[algebra-modules/elementary-divisor-theorem|elementary divisor theorem]] the colength is \(\sum_i e_i\), the [[algebra-fields-galois/valuation-on-a-field|valuation]] of the [[linear-algebra/determinant|determinant]] of an inclusion matrix.

## References

- [New/Reduction/Lattices/Colength.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Colength.lean)
