+++
id = "analytic-number-theory/polya-vinogradov"
title = "Pólya–Vinogradov inequality"
kind = "theorem"
summary = "An interval sum of a nonprincipal Dirichlet character is bounded uniformly in the interval."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/principal-dirichlet-character"]
+++

There is an absolute \(C>0\) such that, for every nonprincipal [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\bmod q\) and integers \(M,N\) with \(N\ge1\),
\[
 \left|\sum_{M<n\le M+N}\chi(n)\right|\le C\sqrt q\log(2q).
\]
The [[analytic-number-theory/principal-dirichlet-character|principal character]] is excluded.

## References

- [Lib/Analytic/PolyaVinogradov.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PolyaVinogradov.lean)
