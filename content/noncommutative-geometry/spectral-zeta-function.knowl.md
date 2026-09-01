+++
id = "noncommutative-geometry/spectral-zeta-function"
title = "Spectral zeta function of a spectral triple"
kind = "definition"
summary = "A Dirichlet-type trace function that records the spectral growth of the Dirac operator in a spectral triple."
aliases = ["Dirac zeta function", "zeta_D", "zeta function of D"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/spectral-triple", "operator-algebras/operator-trace"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((\mathcal A,H,D)\) be a [[noncommutative-geometry/spectral-triple|spectral triple]]. Write \(|D|^{-s}\) for the complex power that is zero on \(\ker D\) and equals \(\lambda^{-s}\) on the positive spectral value \(\lambda\). The **spectral zeta function** is
\[
\zeta_D(s)=\operatorname{Tr}(|D|^{-s})
\]
at those \(s\in\mathbb C\) for which \(|D|^{-s}\) is trace class, using the [[operator-algebras/operator-trace|canonical operator trace]]. More generally, for a bounded operator \(b\), the weighted spectral zeta function is \(\zeta_b(s)=\operatorname{Tr}(b|D|^{-s})\) wherever the product is trace class. Meromorphic continuations, when they exist, are continuations of these initially convergent functions.

## Convergence and spectral growth

If the nonzero eigenvalues of \(|D|\), repeated with multiplicity, are
\(\lambda_1\leq\lambda_2\leq\cdots\), then
\[
\zeta_D(s)=\sum_{n}\lambda_n^{-s}
\]
in its half-plane of absolute convergence. Thus the convergence abscissa
measures eigenvalue growth. Finite-dimensional kernels do not affect that
growth, but the convention on \(\ker D\) must be fixed before negative powers
are written.

## Heat-kernel relation

For \(\operatorname{Re}s\) sufficiently large, Mellin transformation gives
\[
\Gamma(s/2)\zeta_D(s)
=\int_0^\infty t^{s/2-1}
\operatorname{Tr}\!\left(e^{-tD^2}-P_{\ker D}\right)\,dt.
\]
This relation connects small-time heat asymptotics with poles and residues of
the zeta function. Under regularity and suitable asymptotic hypotheses,
weighted zeta functions are the analytic input for the dimension spectrum and
local index formula.

## Conventions and scope

**Warning.** Authors also study
\(\operatorname{Tr}(b(1+D^2)^{-s/2})\), which avoids a separate kernel
convention. It has the same high-energy behavior as the displayed function but
is not literally the same holomorphic function. A pole set belongs to a
specified family of weighted zeta functions; it cannot be inferred from
\(\zeta_D\) alone without additional hypotheses.

## References

1. A. Connes and H. Moscovici, “The Local Index Formula in Noncommutative Geometry,” *Geometric and Functional Analysis* 5 (1995), 174–243. [DOI record](https://doi.org/10.1007/BF01895667). Relevant: §II on zeta functions, residues, and dimension spectrum.
2. J. M. Gracia-Bondía, J. C. Várilly, and H. Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [Publisher record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: §10.5 on spectral dimension and zeta functions.
