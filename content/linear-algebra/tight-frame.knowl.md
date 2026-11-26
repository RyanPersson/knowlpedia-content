+++
id = "linear-algebra/tight-frame"
title = "Finite tight frame"
kind = "definition"
summary = "A family whose sum of squared inner products is a fixed multiple of the squared norm."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/inner-product-space"]
+++

In a finite-dimensional real or complex [[linear-algebra/inner-product-space|inner product space]] \(V\), a **tight frame** is a finite family \(w_i\) for which there is \(A>0\) such that \(\sum_i|\langle v,w_i\rangle|^2=A\|v\|^2\) for every \(v\in V\).

## Operator form

The sum of the rank-one operators \(v\mapsto\langle w_i,v\rangle w_i\) is \(A\) times the identity, using the convention that the second argument is linear. A vector with integral multiplicity can be repeated that many times.

## References

- [New/Derivatives/Sharpness/BoundAttained.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean)
