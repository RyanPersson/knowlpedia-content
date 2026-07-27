+++
id = "harmonic-analysis/schwartz-bruhat-space-adeles"
title = "Schwartz–Bruhat space on the adeles"
kind = "definition"
summary = "The restricted tensor product of the local Schwartz–Bruhat spaces over all places of a global field."
aliases = ["adelic Schwartz space", "adelic test functions", "restricted tensor product of Schwartz-Bruhat spaces"]
domains = ["harmonic-analysis", "number-theory"]
section_mode = "progressive"
+++

Let \(F\) be a number field and \(\mathbb A_F\) its ring of adeles. The **Schwartz–Bruhat space on the adeles** is
\[
\mathcal S(\mathbb A_F)
=\mathcal S(F_\infty)\,\widehat\otimes\!
\bigotimes_{v\nmid\infty}'\mathcal S(F_v),
\]
where \(\mathcal S(F_\infty)\) is the Schwartz space of the
finite-dimensional real vector space
\(F_\infty=\prod_{v\mid\infty}F_v\). The finite-place factor is the
[[harmonic-analysis/restricted-tensor-product-test-functions|restricted
tensor product]] of the local
[[harmonic-analysis/schwartz-bruhat-space-local-field|Schwartz–Bruhat
spaces]] relative to \(1_{\mathcal O_v}\). Finite sums of products of local
functions form a dense algebraic subspace; at several archimedean places
they need not exhaust the completed space \(\mathcal S(F_\infty)\).

## Fourier transform

Choose a nontrivial additive character \(\psi:\mathbb A_F/F\to\mathbb T\) and compatible local [[harmonic-analysis/haar-measure|Haar measures]]. The adelic Fourier transform factors on elementary tensors:
\[
\widehat{\bigotimes_v f_v}=\bigotimes_v\widehat f_v.
\]
For the standard unramified data, \(\widehat{1_{\mathcal O_v}}=1_{\mathcal O_v}\) at almost every finite place, so the transform preserves the restricted tensor product. With self-dual measures it is an automorphism of \(\mathcal S(\mathbb A_F)\) and satisfies Fourier inversion [Weil, Chapter II](https://doi.org/10.1007/978-3-662-05978-4).

## Basic examples

For \(F=\mathbb Q\), there is one archimedean factor, and a typical
elementary function is
\[
f_\infty\otimes\bigotimes_p f_p,
\]
where \(f_\infty\in\mathcal S(\mathbb R)\), each \(f_p\) is locally constant and compactly supported on \(\mathbb Q_p\), and \(f_p=1_{\mathbb Z_p}\) for all but finitely many primes. The constant function \(1\) on \(\mathbb A_{\mathbb Q}\) is not in the space because its archimedean factor is not rapidly decreasing.

## Role in global harmonic analysis

The space \(\mathcal S(\mathbb A_F)\) supplies the test functions in adelic
Poisson summation and Tate's zeta integrals. The restricted tensor-product
description makes a global integral factor into local integrals when both
the function and measure are factorizable. This factorization is algebraic
for elementary tensors and extends by linearity and continuity to the
completed archimedean factor and the standard locally convex LF topology.

## Conventions and scope

For a global function field there are no archimedean factors, and the same definition uses locally constant compactly supported functions at every place. Some sources denote this space by \(\mathcal S(\mathbb A)\) or \(\mathcal D(\mathbb A)\). It is not the ordinary Euclidean [[functional-analysis/schwartz-space|Schwartz space]] on a finite-dimensional real vector space.

## References

1. André Weil, *Basic Number Theory*, 2nd ed., Springer, 1973. [DOI record](https://doi.org/10.1007/978-3-662-05978-4). Relevant: Chapter II, adelic Schwartz functions and Fourier analysis.
2. John Tate, “Fourier Analysis in Number Fields and Hecke's Zeta-Functions,” in J. W. S. Cassels and A. Fröhlich, eds., *Algebraic Number Theory*, Academic Press, 1967, 305–347. [Author-hosted scan](https://www.jmilne.org/math/Documents/TateThesis.pdf). Relevant: §§2.2–2.4, adelic test functions, Fourier transform, and zeta integrals.
