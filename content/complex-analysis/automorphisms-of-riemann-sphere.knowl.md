+++
id = "complex-analysis/automorphisms-of-riemann-sphere"
title = "Automorphisms of the Riemann sphere"
kind = "theorem"
summary = "Every holomorphic automorphism of the Riemann sphere is a Möbius transformation."
aliases = ["holomorphic automorphisms of CP1"]
domains = ["complex-analysis", "differential-geometry"]
prerequisites = ["complex-analysis/riemann-sphere", "complex-analysis/mobius-transformation"]
dependency_review_count = 1
section_mode = "progressive"
+++

Every holomorphic automorphism of the [[complex-analysis/riemann-sphere|Riemann sphere]] is a [[complex-analysis/mobius-transformation|Möbius transformation]]. Hence
\[
\operatorname{Aut}_{\mathrm{hol}}(\mathbb P^1(\mathbb C))
\cong PGL_2(\mathbb C).
\]

## Proof idea

A holomorphic self-map of the sphere is a [[complex-analysis/rational-function|rational function]]. If it is bijective, its topological and algebraic degree is \(1\), so it is the quotient of two linear polynomials with nonzero determinant. Alternatively, use sharp three-transitivity to compose the automorphism with a Möbius map fixing \(0,1,\infty\), then show the resulting automorphism is the identity.

## Scope

Holomorphic **self-maps** of the sphere need not be automorphisms: every nonconstant rational function gives such a map, and maps of degree greater than \(1\) are branched coverings rather than bijections. Orientation-reversing conformal automorphisms are [[complex-analysis/anti-mobius-transformation|anti-Möbius]], not holomorphic.

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§8–9.
