+++
id = "harmonic-analysis/laplace-transform"
title = "One-sided Laplace transform"
kind = "definition"
summary = "The exponential integral of a function on the nonnegative real axis."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/exponential-function"]
+++

For a [[measure-theory/locally-integrable-function|locally integrable]] function \(f:[0,\infty)\to\mathbb C\), its **one-sided Laplace transform** is \(\mathcal L f(s)=\int_0^\infty f(t)e^{-st}\,dt\) wherever the integral converges absolutely. The [[real-analysis/exponential-function|exponential]] weights the values of \(f\) at large \(t\).

## A pole from a growth rate

For \(f(t)=e^{at}\) with \(a\) real, integration gives \((s-a)^{-1}\) on \(\operatorname{Re}s>a\). Its [[complex-analysis/meromorphic-function|meromorphic continuation]] has a simple pole at \(a\).

## References

- [Lib/Analytic/Landau.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean)
