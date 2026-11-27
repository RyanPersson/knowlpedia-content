+++
id = "proofs/grh/spanning-unfolding-b/scalar-isometry"
title = "Scalar isometry"
kind = "definition"
summary = "A scalar of norm one, regarded as an isometry of a hermitian form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.scalarIsometry", "New.scalarIsometry_one", "New.val_scalarIsometry_inv_mul"]
lean_files = ["src/New/Spanning/Unfolding/SquareExpansion.lean"]
+++

Let \(R\) be a commutative ring with involution, \(J\) a square matrix over \(R\) and \(\zeta\in R\) with \(\zeta\bar\zeta=1\). The **scalar isometry** of \(\zeta\) is the element \(\zeta\cdot1\) of the [[?c:Unitary group of a hermitian form|unitary group]] \(U(J)\); its inverse is \(\bar\zeta\cdot1\), and \((\zeta\cdot1)^*J(\zeta\cdot1)=\bar\zeta\zeta J=J\).

## Properties

The scalar isometry of \(1\) is the identity, and for \(g\in U(J)\) the matrix of \((\zeta\cdot1)^{-1}g\) is \(\bar\zeta g\).

## References

1. Lean: `New.scalarIsometry` in `src/New/Spanning/Unfolding/SquareExpansion.lean`.
