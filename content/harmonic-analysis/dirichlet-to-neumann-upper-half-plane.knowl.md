+++
id = "harmonic-analysis/dirichlet-to-neumann-upper-half-plane"
title = "Dirichlet-to-Neumann operator on the upper half-plane"
kind = "construction"
summary = "The boundary operator sending Dirichlet data to the normal derivative of its harmonic Poisson extension."
aliases = ["upper-half-plane Dirichlet-to-Neumann map", "half-Laplacian on the line"]
domains = ["harmonic-analysis", "partial-differential-equations", "complex-analysis"]
prerequisites = ["harmonic-analysis/poisson-extension-upper-half-plane", "harmonic-analysis/hilbert-transform"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(u\) be the
[[harmonic-analysis/poisson-extension-upper-half-plane|Poisson extension]] of
sufficiently regular boundary data \(f\) on \(\mathbb R\). The
**Dirichlet-to-Neumann operator** sends \(f\) to the boundary normal derivative
\[
\Lambda f=-\partial_yu(\,\cdot\,+i0).
\]
With this outward-normal convention,
\[
\Lambda f=H(f')=(-\partial_x^2)^{1/2}f,
\]
where \(H\) is the [[harmonic-analysis/hilbert-transform|Hilbert transform]].

## Fourier symbol

The Poisson extension satisfies
\(\widehat u(\xi,y)=e^{-2\pi|\xi|y}\widehat f(\xi)\). Hence
\(\widehat{\Lambda f}(\xi)=2\pi|\xi|\widehat f(\xi)\) for the \(2\pi\) Fourier
normalization.

## Sign convention

Using the inward derivative \(+\partial_y\) replaces \(\Lambda\) by
\(-\Lambda\). Statements involving (H[-f']) use that alternative convention.

## References

1. Luis Caffarelli and Luis Silvestre, “An extension problem related to the fractional Laplacian,” *Communications in PDE* 32 (2007), 1245–1260. [DOI record](https://doi.org/10.1080/03605300600987306).
