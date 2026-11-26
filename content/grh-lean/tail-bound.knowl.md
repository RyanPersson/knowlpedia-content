+++
id = "grh-lean/tail-bound"
title = "Why the remainder at the second cutoff is small"
kind = "theorem"
summary = "Fixed-modulus prime sums provide arbitrarily high inverse powers of the logarithm."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/prime-number-theorem-progressions", "analytic-number-theory/partial-summation"]
+++

For fixed odd prime \(d\) coprime to \(q\), the [[analytic-number-theory/prime-remainder-in-progression|remainder]] at \(y\) is \(O_{d,q,A}((\log y)^{-A})\) for every fixed positive integer \(A\).

## Proof

The [[analytic-number-theory/prime-number-theorem-progressions|prime number theorem in fixed progressions]] supplies arbitrarily many inverse powers of \(\log y\) for the weighted counting function. Split the coefficient \(1-(n/d)\) into [[complex-analysis/residue|residue]] classes modulo a common modulus. Apply [[analytic-number-theory/partial-summation|partial summation]] to the weight \(1/n-1/y\). The main term integrates to a logarithm and a constant, and the integral of the error has a tail of the claimed size by taking enough powers at the outset. At \(y=x_1\), an inverse power of \(\log x_1\) is a negative power of \(x\).

[Unfold the Lean statements and subproofs](/grh-lean/declarations/#module=New.Reduction.Zeros.PrimeNumberTheorem).

## References

- [New/Reduction/Zeros/PrimeNumberTheorem.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean)
