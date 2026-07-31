+++
id = "harmonic-analysis/weil-integration-formula"
title = "Weil integration formula"
kind = "theorem"
summary = "The Weil integration formula decomposes integration on a locally compact group into integration along a closed subgroup and over its homogeneous space."
aliases = ["quotient integral formula", "integration over G/H"]
domains = ["harmonic-analysis", "measure-theory", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact Hausdorff group]], let \(H\) be a closed subgroup, and choose left [[harmonic-analysis/haar-measure|Haar measures]] \(dg\) and \(dh\). There are a positive continuous function \(\rho:G\to(0,\infty)\), satisfying
\[
\rho(gh)=\rho(g)\frac{\Delta_H(h)}{\Delta_G(h)},
\]
and a regular measure \(d\dot g\) on the
[[harmonic-analysis/locally-compact-homogeneous-space|locally compact
homogeneous space]] \(G/H\) such that every \(f\in C_c(G)\) satisfies
\[
\int_G f(g)\rho(g)\,dg
=\int_{G/H}\int_H f(gh)\,dh\,d\dot g.
\]
This is the **Weil integration formula** for the stated choices and conventions.

## Invariant quotient measures

The quotient \(G/H\) admits a nonzero \(G\)-invariant regular measure exactly when
\[
\Delta_G|_H=\Delta_H.
\]
Under this condition one may take \(\rho=1\), so the formula becomes a literal decomposition of Haar integration into integration along the fibers \(gH\) and integration over the quotient. The quotient measure is then unique up to a positive scalar; its normalization changes inversely when the Haar measure on \(H\) is rescaled [Folland, Chapter 2].

## Role of the rho-function

When the modular functions do not agree on \(H\), no invariant quotient measure exists. The rho-function compensates for this mismatch and produces a [[harmonic-analysis/quasi-invariant-measure|quasi-invariant measure class]] on \(G/H\). Different admissible rho-functions give equivalent quotient measures, so constructions based only on the measure class, such as the corresponding unitary quotient representation, do not depend on an accidental choice of density.

## Standard cases and conventions

If \(H\) is compact, both \(\Delta_H\) and \(\Delta_G|_H\) are trivial, hence \(G/H\) has an invariant measure. Taking \(H=\{e\}\) recovers integration on \(G\), while \(H=G\) reduces the outer integral to a one-point quotient.

**Warning.** Formulas written with right Haar measure, left cosets \(H\backslash G\), or the reciprocal convention for the [[harmonic-analysis/modular-function|modular function]] move or invert the factor \(\rho\). These are convention changes, not contradictory theorems.

## References

1. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 2, rho-functions, quotient measures, and Weil's formula.
2. E. Hewitt and K. A. Ross, *Abstract Harmonic Analysis*, Volume I, Springer, 1963. [DOI record](https://doi.org/10.1007/978-3-662-40409-6). Relevant: invariant integration on homogeneous spaces.
