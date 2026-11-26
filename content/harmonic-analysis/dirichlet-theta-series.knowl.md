+++
id = "harmonic-analysis/dirichlet-theta-series"
title = "Theta series of a Dirichlet character"
kind = "definition"
summary = "A Dirichlet character supplies the coefficients of a Gaussian theta sum."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character"]
+++

For a [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\bmod q\) with \(\chi(-1)=(-1)^a\), \(a\in\{0,1\}\), one normalization of its **theta series** is
\[
 \theta_\chi(t)=\sum_{n\ge1}n^a\chi(n)e^{-\pi n^2 t/q},\qquad t>0.
\]

## Change of variables

Positive and two-sided summation conventions differ by a constant and sometimes the term at zero. A [[harmonic-analysis/mellin-transform|Mellin transform]] turns the Gaussian weight into a [[real-analysis/gamma-function|gamma factor]] and the character sum into the [[analytic-number-theory/dirichlet-l-function|Dirichlet \(L\)-function]].

## References

- [Lib/Analytic/DirichletTheta.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean)
