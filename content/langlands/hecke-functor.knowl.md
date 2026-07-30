+++
id = "langlands/hecke-functor"
title = "Geometric Hecke functor"
kind = "construction"
summary = "A pull-push functor on automorphic sheaves defined from the Hecke correspondence and a dual-group representation."
aliases = ["Hecke functor", "geometric Hecke operator"]
domains = ["langlands"]
section_mode = "progressive"
+++

Let \(V\) be a representation of \(\widehat G\). Via
[[langlands/geometric-satake-equivalence|geometric Satake]], \(V\) determines
a spherical kernel \(\mathcal K_V\) on the
[[langlands/hecke-correspondence|Hecke correspondence]]. Pulling an
automorphic \(D\)-module \(\mathcal F\) to the Hecke stack, tensoring with
\(\mathcal K_V\), and pushing to
\(\operatorname{Bun}_G\times X\) defines the **Hecke functor**
\[
H_V:D\text{-}\operatorname{mod}(\operatorname{Bun}_G)
\longrightarrow
D\text{-}\operatorname{mod}(\operatorname{Bun}_G\times X).
\]

## Tensor compatibility

The functors are compatible with tensor products:
\(H_{V\otimes W}\) is obtained from iterated Hecke modification and fusion.
This factorization compatibility is what lets an eigenvalue be a
\(\widehat G\)-local system rather than an unrelated collection of vector
bundles.

## Conventions

The exact formula includes cohomological shifts, left-versus-right
\(D\)-module conventions, and a choice of which bundle projection is the
source. Those normalizations do not change the organizing pull-kernel-push
construction.

## References

1. Alexander Beilinson and Vladimir Drinfeld, *Quantization of Hitchin’s
   Integrable System and Hecke Eigensheaves*, preprint.
   [author manuscript](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf).
