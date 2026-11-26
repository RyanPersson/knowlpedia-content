+++
id = "arithmetic-geometry/product-formula"
title = "Product formula for a number field"
kind = "theorem"
summary = "The normalized local absolute values of a nonzero element multiply to one."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/place-of-global-field", "algebra-fields-galois/number-field"]
+++

For a [[algebra-fields-galois/number-field|number field]] \(K\) and \(a\in K^\times\), the **product formula** says \(\prod_v|a|_v=1\), using one factor for each [[algebra-fields-galois/place-of-global-field|place]]. Use the ordinary absolute value at a real place, its square at a complex place, and \(|a|_{\mathfrak p}=(\#\mathcal O_K/\mathfrak p)^{-\operatorname{ord}_{\mathfrak p}(a)}\) at a finite place. Only finitely many factors differ from one.

## A rational example

For \(a=12\) the nontrivial factors are \(12\), \(2^{-2}\), and \(3^{-1}\). Taking logarithms gives \(\log12-2\log2-\log3=0\). In a [[algebra-fields-galois/number-field|number field]], factoring the principal fractional ideal and taking its norm gives the same cancellation against the [[arithmetic-geometry/archimedean-size|archimedean factors]].

## References

- [New/Reduction/Lattices/Heights.lean, log_product_formula](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L53)
