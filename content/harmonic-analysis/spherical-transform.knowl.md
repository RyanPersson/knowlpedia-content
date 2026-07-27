+++
id = "harmonic-analysis/spherical-transform"
title = "Spherical Fourier transform"
kind = "definition"
summary = "The scalar transform of a bi-invariant function obtained by integrating it against elementary spherical functions."
aliases = ["spherical transform", "Harish-Chandra spherical transform"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a connected semisimple
[[fiber-bundles/lie-group|Lie group]] with finite center, let \(K\) be a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]], and fix a left
[[harmonic-analysis/haar-measure|Haar measure]] on \(G\). For an integrable
\(K\)-bi-invariant function \(f\), its **spherical Fourier transform** is
\[
\mathcal Sf(\lambda)=\int_G f(g)\varphi_{-\lambda}(g)\,dg,
\]
where \(\varphi_\lambda\) is the normalized
[[harmonic-analysis/spherical-function|elementary spherical function]] with
spectral parameter \(\lambda\) in the complexified dual of a maximal abelian
subspace of the noncompact Cartan component. The transform is Weyl-invariant
in \(\lambda\). The sign on \(\lambda\) is conventional and is chosen to
match the stated inversion convention.

## Diagonalizing spherical convolution

For \(K\)-bi-invariant integrable functions \(f\) and \(h\),
\[
\mathcal S(f*h)(\lambda)
=\mathcal Sf(\lambda)\mathcal Sh(\lambda).
\]
Thus the spherical transform is the scalar Fourier transform of the
commutative convolution algebra associated with the
[[lie-groups/gelfand-pair|Gelfand pair]] \((G,K)\).
The multiplicative property follows from the product formula for spherical
functions [Helgason, Chapter IV, §§2–3](https://doi.org/10.1090/surv/039).

## Inversion and Plancherel measure

On suitable test functions, \(f\) is recovered by integrating
\(\mathcal Sf(\lambda)\varphi_\lambda\) against the spherical Plancherel
measure. For the standard real parameter space, that measure has density
proportional to \(\lvert c(\lambda)\rvert^{-2}\), where \(c\) is the
[[lie-groups/harish-chandra-c-function|Harish-Chandra \(c\)-function]]. This
is the radial, commutative part of the
nonabelian Plancherel formula.

## Schwartz-space theorem

On the \(K\)-bi-invariant
[[harmonic-analysis/harish-chandra-schwartz-space|Harish-Chandra Schwartz space]], the transform is a topological algebra isomorphism onto an explicitly
described Weyl-invariant Schwartz space. The Trombi–Varadarajan theorem gives
the corresponding \(L^p\)-Schwartz versions and their holomorphic spectral
domains [Trombi–Varadarajan, main theorem](https://doi.org/10.2307/1970861).

## References

1. Sigurdur Helgason, *Groups and Geometric Analysis: Integral Geometry, Invariant Differential Operators, and Spherical Functions*, American Mathematical Society, 2000. [AMS record](https://doi.org/10.1090/surv/039). Relevant: Chapter IV on spherical functions, spherical transforms, inversion, and Plancherel theory.
2. P. C. Trombi and V. S. Varadarajan, “Spherical Transforms on Semisimple Lie Groups,” *Annals of Mathematics* 94 (1971), 246–303. [DOI record](https://doi.org/10.2307/1970861). Relevant: the main Schwartz-space isomorphism theorem.
