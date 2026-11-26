+++
id = "grh-lean/riemann-hypothesis"
title = "The Riemann hypothesis in Mathlib’s formulation"
kind = "theorem"
summary = "The exported theorem has Mathlib’s RiemannHypothesis as its precise type."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/riemann-hypothesis", "grh-lean/zeta-zeros"]
+++

Mathlib’s [[analytic-number-theory/riemann-hypothesis|Riemann hypothesis]] holds in the formal development.

## Proof

Unfold the proposition `RiemannHypothesis`. It asks that a zero of \(\zeta\) other than the negative even integers and the point \(1\) have real part \(1/2\). This is exactly [[grh-lean/zeta-zeros|the zeta zero statement]]. In Lean one proof inhabits both propositions by definitional equality.

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#module=Statements).

## References

- [Statements.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean)
- [Main.lean, riemannHypothesis](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L5)
