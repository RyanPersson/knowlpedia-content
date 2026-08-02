+++
id = "langlands/convolution-of-sheaves"
title = "Convolution of sheaves on the affine Grassmannian"
kind = "construction"
summary = "The sheaf obtained by external product on the convolution Grassmannian followed by proper pushforward along multiplication."
aliases = ["spherical convolution", "convolution product of spherical sheaves"]
domains = ["langlands", "representation-theory"]
section_mode = "progressive"
+++

Let \(\operatorname{Gr}_G\widetilde\times\operatorname{Gr}_G\) be the
convolution Grassmannian and let
\[
m:\operatorname{Gr}_G\widetilde\times\operatorname{Gr}_G
\longrightarrow\operatorname{Gr}_G
\]
compose the two successive modifications. For \(L^+G\)-equivariant
constructible complexes \(\mathcal F,\mathcal G\), their **convolution** is
\[
\mathcal F\star\mathcal G
=m_!\bigl(\mathcal F\widetilde\boxtimes\mathcal G\bigr).
\]

The map \(m\) is ind-proper on the relevant finite-dimensional supports, so
\(m_!=m_*\). With the Satake normalization, convolution preserves
[[langlands/perverse-sheaf|perverse sheaves]] and defines the tensor product
used in [[langlands/geometric-satake-equivalence|geometric Satake]].

## References

1. Ivan Mirković and Kari Vilonen, “Geometric Langlands duality and
   representations of algebraic groups over commutative rings,” *Annals of
   Mathematics* 166 (2007), 95–143.
   [arXiv](https://arxiv.org/abs/math/0401222).
