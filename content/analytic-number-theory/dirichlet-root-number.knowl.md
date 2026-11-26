+++
id = "analytic-number-theory/dirichlet-root-number"
title = "Root number of a primitive Dirichlet character"
kind = "definition"
summary = "The unit-modulus scalar in the reflection law of the completed Dirichlet L-function."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/primitive-dirichlet-character","analytic-number-theory/dirichlet-conductor","analytic-number-theory/dirichlet-character-parity","analytic-number-theory/dirichlet-gauss-sum"]
+++

The **root number** of a [[analytic-number-theory/primitive-dirichlet-character|primitive Dirichlet character]] \(\chi\) of [[analytic-number-theory/dirichlet-conductor|conductor]] \(q\) and [[analytic-number-theory/dirichlet-character-parity|parity]] \(a\) is \(\epsilon_\chi=\tau(\chi)/(i^a\sqrt q)\), where \(\tau\) is the [[analytic-number-theory/dirichlet-gauss-sum|Gauss sum]] with positive exponential. Its absolute value is one by the Gauss sum norm formula.

## References

- [The Gauss sum phase in the theta transformation](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L399)
