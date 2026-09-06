+++
id = "langlands/hecke-correspondence"
title = "Hecke correspondence"
kind = "definition"
summary = "The moduli correspondence relating two G-bundles by a modification at a point of the curve."
aliases = ["Hecke stack", "geometric Hecke correspondence"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/smooth-projective-curve", "langlands/hecke-modification"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a [[algebraic-geometry-foundations/smooth-projective-curve|smooth projective curve]]. The **Hecke stack**
\(\operatorname{Hecke}_G\) classifies tuples
\((x,E,E',\beta)\), where \(x\in X\), \(E,E'\in\operatorname{Bun}_G(X)\), and
\(\beta\) is a [[langlands/hecke-modification|Hecke modification]] from \(E\)
to \(E'\) at \(x\).

It forms a correspondence
\[
\operatorname{Bun}_G
\xleftarrow{\ h_{\mathrm{left}}\ }
\operatorname{Hecke}_G
\xrightarrow{\ (h_{\mathrm{right}},\,x)\ }
\operatorname{Bun}_G\times X.
\]
Interchanging “left” and “right” is a convention; formulas must use one
choice consistently.

## Bounded correspondence

For each [[langlands/dominant-coweight|dominant coweight]] \(\lambda\), a closed substack
\(\operatorname{Hecke}_{G,\leq\lambda}\) bounds the relative position by
\(\lambda\). More generally, a spherical sheaf on the [[langlands/affine-grassmannian|affine Grassmannian]]
provides a kernel on the Hecke stack.

## Use

Pull-push along this correspondence defines a
[[langlands/hecke-functor|geometric Hecke functor]]. Because these maps are
maps of stacks, derived pullback, pushforward, and shifts are part of the
construction.

## References

1. A. Beilinson and V. Drinfeld, *Quantization of Hitchin’s Integrable System
   and Hecke Eigensheaves*, preprint.
   [author manuscript](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf).
