+++
id = "analytic-number-theory/polar-laplace-transform"
title = "Polar continuation of a weighted Laplace transform"
kind = "definition"
summary = "A transform with prescribed simple-pole residues."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/laplace-transform", "complex-analysis/meromorphic-function", "complex-analysis/residue"]
+++

A measurable \(E:\mathbb R\to\mathbb R\) **has a polar transform with residues \(r:\mathbb C\to\mathbb C\)** if some real \(C\) and [[complex-analysis/meromorphic-function|meromorphic function]] \(\Phi\) on \(\mathbb C\) satisfy
\[
 |E(v)|\le Ce^v\quad(v\ge0),\qquad
 \Phi(s)=\int_0^\infty E(v)e^{(1-s)v}\,dv\quad(\Re s>2),
\]
and for every \(\rho\) with \(\Re\rho>0\), \(\lim_{s\to\rho,\ s\ne\rho}(s-\rho)\Phi(s)=r(\rho)\). The integral is a shifted [[harmonic-analysis/laplace-transform|Laplace transform]]. The limit permits at most a simple pole and gives its [[complex-analysis/residue|residue]].

## References

- [Lib/Analytic/EntireLFunction.lean, IsPolar](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean#L76)
