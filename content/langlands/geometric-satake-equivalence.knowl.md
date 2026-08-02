+++
id = "langlands/geometric-satake-equivalence"
title = "Geometric Satake equivalence"
kind = "theorem"
summary = "The tensor category of spherical perverse sheaves on Gr_G is equivalent to representations of the Langlands dual group."
aliases = ["geometric Satake correspondence"]
domains = ["langlands", "representation-theory"]
section_mode = "progressive"
+++

Let \(k\) be an [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]], let \(G\) be a connected reductive
group over \(k\), and choose a characteristic-zero coefficient field \(E\)
and an appropriate sheaf theory (for example, \(E=\mathbb C\) for classical
sheaves when \(k=\mathbb C\), or \(E=\overline{\mathbb Q}_\ell\) with
\(\ell\ne\operatorname{char}k\) in the étale setting). The **geometric Satake
equivalence** identifies the convolution tensor category of
\(G\lbrack\!\lbrack t\rbrack\!\rbrack\)-equivariant
\(E\)-[[langlands/perverse-sheaf|perverse sheaves]] on the
[[langlands/affine-grassmannian|affine Grassmannian]]
\(\operatorname{Gr}_G\) with
\[
\operatorname{Rep}_E(\widehat G_E),
\]
the tensor category of finite-dimensional algebraic \(E\)-representations of
the split reductive \(E\)-group with root datum dual to that of \(G\), the
[[langlands-letter/knowls/langlands-dual-group|Langlands dual group]].

Under these characteristic-zero hypotheses, the
[[langlands/intersection-cohomology-complex|intersection-cohomology complex]]
of the [[langlands/affine-schubert-variety|affine Schubert variety]] indexed
by a [[langlands/dominant-coweight|dominant coweight]] \(\lambda\)
corresponds to the irreducible \(\widehat G\)-representation of highest
weight \(\lambda\).

## Coefficients and versions

The classical statement uses perverse sheaves with characteristic-zero
coefficients and the fiber functor of global cohomology. There are integral,
modular, motivic, and derived versions with distinct technical hypotheses and
sometimes a non-semisimple representation category. The tensor structure
comes from [[langlands/convolution-of-sheaves|convolution]], not pointwise
tensor product.

## Role in geometric Langlands

Geometric Satake turns local modifications of \(G\)-bundles into
[[langlands/hecke-functor|Hecke functors]] indexed by representations of
\(\widehat G\).

## References

1. Ivan Mirković and Kari Vilonen, “Geometric Langlands duality and
   representations of algebraic groups over commutative rings,” *Annals of
   Mathematics* 166 (2007), 95–143.
   [arXiv](https://arxiv.org/abs/math/0401222).
