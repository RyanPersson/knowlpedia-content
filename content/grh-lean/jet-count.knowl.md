+++
id = "grh-lean/jet-count"
title = "Counting the valuation of a theta jet"
kind = "theorem"
summary = "A change of variables and the factorial valuation explain the appearance of prime powers."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/theta-jet", "analytic-number-theory/von-mangoldt-function"]
+++

For a local [[harmonic-analysis/dirichlet-theta-series|theta series]] in the integral normal form of the construction, differentiation along a product of minors gives a lower bound on the [[algebra-fields-galois/valuation-on-a-field|valuation]] of the [[harmonic-analysis/theta-jet|jet]]. The bound counts the minor shapes, with an explicit correction for the change of variables.

## Proof

Choose coordinates that make the relevant couplings integral in the requested degree after multiplying by a power of the local [[algebra-fields-galois/uniformizer|uniformizer]]. For an integral series the derivative of order \(j\) in one variable contains \(j!\). Its [[analytic-number-theory/legendre-factorial-valuation|factorial valuation]] \(\sum_{e\ge1}\lfloor j/p^e\rfloor\) counts the multiples of \(p^e\). Apply the count to the boxes in the products of minors, then subtract the valuation lost through the chain rule. Marked columns have a separate correction. Multiplication by \(\log p\) gives the weights of the [[analytic-number-theory/von-mangoldt-function|von Mangoldt function]] on [[analytic-number-theory/prime-power|prime powers]].

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#source=New.Derivatives.Divisibility.Count:707).

## References

- [New/Derivatives/Divisibility/Count.lean, norm_jet_minorProd_le_of_hasNormalForm](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L707)
- [New/Derivatives/Divisibility/Count.lean, norm_jet_minorProd_le_of_charges](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L662)
