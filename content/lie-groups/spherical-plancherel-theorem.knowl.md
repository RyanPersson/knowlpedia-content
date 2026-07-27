+++
id = "lie-groups/spherical-plancherel-theorem"
title = "Spherical Plancherel theorem"
kind = "theorem"
summary = "The spherical Fourier transform is a unitary decomposition of K-invariant L2-functions on a noncompact symmetric space."
aliases = ["Plancherel formula for G/K", "spherical Fourier inversion"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a connected noncompact semisimple Lie group with finite center,
\(K\) a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]], and \(X=G/K\). For a \(K\)-invariant \(f\in L^1(X)\cap L^2(X)\),
define
\[
\widehat f(\lambda)=\int_X f(x)\varphi_{-\lambda}(x)\,dx ,
\]
where \(\varphi_\lambda\) is the normalized
[[harmonic-analysis/spherical-function|spherical function]]. Choose
compatible Haar and Lebesgue measures, and let \(d\bar\lambda\) denote the
pushforward to \(\mathfrak a^*/W\) of
\(|W|^{-1}d\lambda\), for the chosen Lebesgue measure on \(\mathfrak a^*\).
The **spherical Plancherel theorem** says that this transform extends to a
unitary map
\[
L^2(X)^K\longrightarrow
L^2\!\left(\mathfrak a^*/W,\,
 |c(\lambda)|^{-2}d\bar\lambda\right),
\]
where \(c\) is the
[[lie-groups/harish-chandra-c-function|Harish–Chandra c-function]].
Equivalently, the transform preserves inner products and admits spherical
Fourier inversion in the \(L^2\)-sense.

## Inversion formula

For sufficiently regular rapidly decreasing \(K\)-invariant \(f\), Fourier
inversion takes the pointwise form
\[
f(x)=C\int_{\mathfrak a^*}
 \widehat f(\lambda)\varphi_\lambda(x)
 |c(\lambda)|^{-2}\,d\lambda ,
\]
where \(C\) is determined by the chosen normalizations and includes the Weyl
group convention. Density then gives the unitary extension to all of
\(L^2(X)^K\). The theorem is the commutative, multiplicity-one part of the
nonabelian Plancherel decomposition
[Helgason, Chapter IV, §7](https://doi.org/10.1090/surv/039).

## Interpretation

The commuting algebra of \(G\)-invariant differential operators on \(X\) is
simultaneously diagonalized by the functions \(\varphi_\lambda\). The factor
\(|c(\lambda)|^{-2}\) is therefore not an arbitrary weight: it is the spectral
density forced by the asymptotics of those joint eigenfunctions. Passing to
\(\mathfrak a^*/W\) removes the redundancy
\(\varphi_{w\lambda}=\varphi_\lambda\).

## Examples and scope

For Euclidean space, viewed through its motion-group
[[lie-groups/gelfand-pair|Gelfand pair]], the
[[harmonic-analysis/spherical-transform|spherical transform]] of radial
functions becomes the Fourier–Bessel transform. On a real-rank-one
[[lie-groups/riemannian-symmetric-space-noncompact-type|noncompact symmetric space]], the spectral parameter is one-dimensional and the density is an
explicit quotient of gamma factors.

This statement concerns the \(K\)-invariant subspace of \(L^2(G/K)\), not the
full Plancherel decomposition of \(L^2(G)\). General \(K\)-types require
matrix-valued transforms and generalized \(c\)-functions.

## References

1. Sigurdur Helgason, *Groups and Geometric Analysis: Integral Geometry, Invariant Differential Operators, and Spherical Functions*, American Mathematical Society, 2000. [AMS record](https://doi.org/10.1090/surv/039). Relevant: Chapter IV, §7 on spherical Fourier inversion and the Plancherel formula.
2. Ramesh Gangolli and V. S. Varadarajan, *Harmonic Analysis of Spherical Functions on Real Reductive Groups*, Springer, 1988. [Publisher record](https://doi.org/10.1007/978-3-642-72956-0). Relevant: the spherical transform, wave packets, and Plancherel theory on real reductive groups.
