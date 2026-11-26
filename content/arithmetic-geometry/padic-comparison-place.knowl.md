+++
id = "arithmetic-geometry/padic-comparison-place"
title = "Comparison of complex and p-adic scalars"
kind = "definition"
summary = "A prime and an abstract field isomorphism transporting its p-adic absolute value to the complex coefficient field."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/p-adic-field", "algebra-fields-galois/algebraic-closure"]
+++

A **complex to \(p\)-adic comparison** is a pair \((p,\iota)\) consisting of a prime \(p\) and an abstract [[algebra-fields-galois/field-isomorphism|field isomorphism]] \(\iota:\mathbb C\overset{\sim}{\longrightarrow}\overline{\mathbb Q_p}\). Here the target is an [[algebra-fields-galois/algebraic-closure|algebraic closure]] of the [[algebra-fields-galois/p-adic-field|\(p\)-adic field]]. Pulling back its absolute value gives the [[algebra-fields-galois/valuation-ring|valuation ring]] \(\mathcal O_\iota=\{z:|\iota z|_p\le1\}\).

## Conjugating a comparison

The conjugate comparison is \(\bar\iota(z)=\iota(\bar z)\). This convention allows a Hermitian pairing to test one vector at \(\bar\iota\) and the other at \(\iota\). The isomorphism is algebraic and carries no compatibility with the usual complex topology.

## References

- [New/Reduction/Lattices/Heights.lean, PrimePadicIso](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L30)
