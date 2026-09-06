+++
id = "lie-groups/harish-chandra-c-function"
title = "Harish–Chandra c-function"
kind = "definition"
summary = "The meromorphic coefficient governing spherical-function asymptotics and spherical Plancherel density."
aliases = ["c-function", "spherical scattering coefficient"]
domains = ["lie-groups", "harmonic-analysis"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/iwasawa-decomposition", "lie-groups/restricted-root-system", "harmonic-analysis/haar-measure"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a connected noncompact semisimple [[fiber-bundles/lie-group|Lie group]] with finite center,
\(G=KAN\) an [[lie-groups/iwasawa-decomposition|Iwasawa decomposition]], and
\(\overline N\) the opposite nilpotent subgroup. Write
\(H(g)\in\mathfrak a\) for the Iwasawa projection and let \(\rho\) be half
the sum of the positive
[[lie-groups/restricted-root-system|restricted roots]], counted with
multiplicity. The **Harish–Chandra \(c\)-function** is
\[
c(\lambda)=\int_{\overline N}
 e^{-(i\lambda+\rho)(H(\overline n))}\,d\overline n
\]
where the integral converges, then extended meromorphically to
\(\mathfrak a_{\mathbb C}^*\). The
[[harmonic-analysis/haar-measure|Haar measure]] is normalized so that
\(c(-i\rho)=1\).

## Asymptotic meaning

For regular \(\lambda\), the elementary
[[harmonic-analysis/spherical-function|spherical function]]
\(\varphi_\lambda\) has, deep in the positive Weyl chamber, an expansion whose
leading exponential terms are indexed by the
[[lie-groups/restricted-weyl-group|restricted Weyl group]]. The coefficient
of the term with spectral parameter \(w\lambda\) is
\(c(w\lambda)\). This asymptotic characterization and the integral definition
agree with the stated normalizations.

## Product formula and Plancherel density

The Gindikin–Karpelevich formula factors \(c(\lambda)\) into rank-one factors,
one for each indivisible positive restricted root; those factors are explicit
ratios of gamma functions involving the root multiplicities. On the real
spectral axis, the spherical Plancherel measure is, up to the compatible
normalizing constant,
\[
|c(\lambda)|^{-2}\,d\lambda.
\]
Thus zeros and poles of the meromorphic continuation encode both
intertwining-operator phenomena and the analytic weight in spherical Fourier
inversion.

## Example and scope

In real rank one, the product formula has a single rank-one factor, so
\(c(\lambda)\) is a quotient of gamma functions. For higher rank, the factors
assemble according to the restricted root system.

The displayed integral fixes one common sign convention for
\(\varphi_\lambda\). Replacing \(\lambda\) by \(-\lambda\), changing the
positive chamber, or rescaling Haar measure changes the printed formula and
normalization but not the resulting Plancherel theory. This scalar spherical
\(c\)-function should be distinguished from generalized matrix-valued
\(c\)-functions for nonspherical \(K\)-types.

## References

1. Sigurdur Helgason, *Groups and Geometric Analysis: Integral Geometry, Invariant Differential Operators, and Spherical Functions*, American Mathematical Society, 2000. [AMS record](https://doi.org/10.1090/surv/039). Relevant: Chapter IV, §§6–7 on spherical-function asymptotics, the \(c\)-function, and the Plancherel formula.
2. Harish-Chandra, “Spherical Functions on a Semisimple Lie Group I,” *American Journal of Mathematics* 80 (1958), 241–310, and “II,” 553–613. [Part I JSTOR record](https://www.jstor.org/stable/2372786). Relevant: the asymptotic expansion and Plancherel density for elementary spherical functions.
