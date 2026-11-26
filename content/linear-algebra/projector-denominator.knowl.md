+++
id = "linear-algebra/projector-denominator"
title = "Denominator of a lattice projection"
kind = "definition"
summary = "The least valuation needed to clear the entries of a projection on an integral lattice."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/orthogonal-projection", "algebra-fields-galois/uniformizer"]
+++

Let \(L\) be a full lattice over a discrete [[algebra-fields-galois/valuation-ring|valuation ring]] with [[algebra-fields-galois/uniformizer|uniformizer]] \(\pi\), and \(P\) an idempotent linear map on its fraction-field span. The **denominator exponent of \(P\) on \(L\)** is the least integer \(a\ge0\) for which \(\pi^aP(L)\subseteq L\).

## Computing it

In an integral basis this clears the denominators of all entries of the matrix of \(P\). The same definition applies to an [[linear-algebra/orthogonal-projection|orthogonal projection]] after the scalar field and integral lattice have been specified.

## References

- [New/OneLift/TestedForms.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean)
