+++
id = "grh-lean/strip-zeros"
title = "Zeros of Dirichlet L-functions in the open strip"
kind = "theorem"
summary = "Reflect a zero to recover the other inequality for its real part."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["grh-lean/half-plane", "analytic-number-theory/dirichlet-functional-equation"]
+++

For any [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\) of positive modulus, a zero \(s\) of its [[analytic-number-theory/dirichlet-l-function|\(L\)-function]] with \(0<\Re s<1\) satisfies \(\Re s=1/2\).

## Proof

The [[analytic-number-theory/dirichlet-functional-equation|functional equation]], together with the change of level for an imprimitive character, sends the zero to a zero of \(L(1-s,\chi^{-1})\). In the open strip the [[real-analysis/gamma-function|gamma factor]] is finite and nonzero. Apply [[grh-lean/half-plane|half-plane nonvanishing]] to both zeros. The first gives \(\Re s\le1/2\), the second \(1-\Re s\le1/2\).

## References

- [New/Main.lean, New.zeros_on_line](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L28)
- [Main.lean, LFunction_eq_zero_re](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L17)
- [Lib/Analytic/ZeroSymmetry.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean)
