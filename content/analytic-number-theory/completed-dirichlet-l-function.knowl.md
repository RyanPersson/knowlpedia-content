+++
id = "analytic-number-theory/completed-dirichlet-l-function"
title = "Completed primitive Dirichlet L-function"
kind = "definition"
summary = "The primitive Dirichlet L-function multiplied by its conductor and gamma factors in the classical normalization."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/primitive-dirichlet-character","analytic-number-theory/dirichlet-conductor","analytic-number-theory/dirichlet-character-parity","complex-analysis/complex-gamma-function","analytic-number-theory/dirichlet-l-function","analytic-number-theory/riemann-zeta-function"]
+++

For a [[analytic-number-theory/primitive-dirichlet-character|primitive Dirichlet character]] \(\chi\) of [[analytic-number-theory/dirichlet-conductor|conductor]] \(q\) and [[analytic-number-theory/dirichlet-character-parity|parity]] \(a\), the **completed Dirichlet \(L\)-function** in classical normalization is
\[
\Lambda(s,\chi)=(q/\pi)^{(s+a)/2}\,\Gamma((s+a)/2)\,L(s,\chi),
\]
with the [[complex-analysis/complex-gamma-function|complex gamma function]] and the [[analytic-number-theory/dirichlet-l-function|Dirichlet \(L\)-function]]. The factor multiplying \(L\) is finite and nonzero for \(\Re s>0\).

## Modulus one

Here \(a=0\) and \(L(s,\chi)=\zeta(s)\), the [[analytic-number-theory/riemann-zeta-function|Riemann zeta function]]. The completed function is \(\pi^{-s/2}\Gamma(s/2)\zeta(s)\).

## References

- [Completed functions and reflection of zeros](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L61)
