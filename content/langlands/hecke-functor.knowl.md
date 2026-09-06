+++
id = "langlands/hecke-functor"
title = "Geometric Hecke functor"
kind = "construction"
summary = "A pull-push functor on automorphic sheaves defined from the Hecke correspondence and a dual-group representation."
aliases = ["Hecke functor", "geometric Hecke operator"]
domains = ["langlands"]
prerequisites = ["langlands/geometric-satake-equivalence", "langlands/hecke-correspondence"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a smooth complex curve, let \(G\) be a connected reductive
complex group, and let \(V\) be a representation of \(\widehat G\). Via
[[langlands/geometric-satake-equivalence|geometric Satake]], \(V\) determines
a spherical kernel \(\mathcal K_V\) on the
[[langlands/hecke-correspondence|Hecke correspondence]]
\[
\operatorname{Bun}_G
\xleftarrow{\ h_{\mathrm{left}}\ }
\operatorname{Hecke}_G
\xrightarrow{\ (h_{\mathrm{right}},x)\ }
\operatorname{Bun}_G\times X.
\]
With right \(D\)-modules and the standard Satake normalization, the
**geometric Hecke functor** is the pull–tensor–push construction
\[
H_V(\mathcal F)=
(h_{\mathrm{right}},x)_*
\bigl(h_{\mathrm{left}}^!\mathcal F
\mathbin{\overset{!}{\otimes}}\mathcal K_V\bigr),
\]
giving
\[
H_V:D\text{-}\operatorname{mod}(\operatorname{Bun}_G)
\longrightarrow
D\text{-}\operatorname{mod}(\operatorname{Bun}_G\times X).
\]

## Tensor compatibility

The functors are compatible with tensor products:
\(H_{V\otimes W}\) is obtained from iterated [[langlands/hecke-modification|Hecke modification]] and fusion.
This factorization compatibility is what lets an eigenvalue be a
\(\widehat G\)-local system rather than an unrelated collection of vector
bundles.

## Other conventions

Left \(D\)-modules replace the displayed operations by their corresponding
left-module conventions. Reversing the two bundle projections gives the
inverse-modification convention. Cohomological shifts are absorbed into the
normalized Satake kernel \(\mathcal K_V\).

## References

1. Alexander Beilinson and Vladimir Drinfeld, *Quantization of Hitchin’s
   Integrable System and Hecke Eigensheaves*, preprint.
   [author manuscript](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf).
