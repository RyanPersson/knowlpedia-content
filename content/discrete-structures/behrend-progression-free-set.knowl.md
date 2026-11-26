+++
id = "discrete-structures/behrend-progression-free-set"
title = "Three-term-progression-free set"
kind = "definition"
summary = "A set in an additive group containing no nonconstant three-term arithmetic progression."
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["algebra-groups/abelian-group"]
+++

A subset \(A\) of an additive [[algebra-groups/abelian-group|abelian group]] is **three-term-progression-free** if \(a,a+h,a+2h\in A\) implies \(h=0\).

## Behrend’s construction

Choose lattice points on one Euclidean sphere in a box and encode their coordinates as digits in a sufficiently large base. There is no carry in an equation \(u+w=2v\). Strict convexity of the sphere forces a midpoint on the sphere to equal its two endpoints. One radius contains many of the points in the box. Weighted midpoint conditions can be handled with a base allowing the relevant coefficients.

## References

- [New/Reduction/Data/Existence.lean, exists_three_term_free](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L80)
