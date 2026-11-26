+++
id = "arithmetic-geometry/simultaneous-height-bound"
title = "Simultaneous height bound for a family of scalars"
kind = "definition"
summary = "One nonzero scalar clears the finite-place sizes of a family at a bounded total logarithmic cost."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/padic-comparison-place", "arithmetic-geometry/archimedean-size"]
+++

Let \(y_\iota\in\mathbb C\) be indexed by all [[arithmetic-geometry/padic-comparison-place|comparisons]] \(\iota\) at all primes \(p\). Its **height is at most \(c\)** if there exist \(H\in\mathbb C^\times\), \(\alpha\in\mathbb R\), and \(h_p\ge0\) satisfying all three conditions.

- Every [[algebra-fields-galois/field-automorphism|field automorphism]] \(\sigma\) of \(\mathbb C\) gives the [[arithmetic-geometry/archimedean-size|size bound]] \(|\sigma H|\le e^\alpha\).
- At each comparison over \(p\), \(|\iota(Hy_\iota)|_p\le p^{h_p}\).
- For every [[shared-foundations/finite-set|finite set]] \(S\) of primes, \(\alpha+\sum_{p\in S}h_p\log p\le c\).

## Multiplication

For two families multiply the witnesses \(H\), add the two archimedean bounds, and add the corresponding \(h_p\). This proves that bounds for the two heights add when the families are multiplied pointwise.

## References

- [New/Reduction/Lattices/Heights.lean, HeightLe](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L41)
