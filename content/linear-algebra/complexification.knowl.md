+++
id = "linear-algebra/complexification"
title = "Complexification"
kind = "definition"
summary = "The complex vector space obtained from a real vector space by extending scalars to the complex numbers."
aliases = ["complexification of a real vector space", "complexified vector space"]
domains = ["linear-algebra"]
section_mode = "progressive"
+++

Let \(V\) be a real [[linear-algebra/vector-space|vector space]]. Its **complexification** is the complex vector space
\[
V_{\mathbb C}:=V\otimes_{\mathbb R}\mathbb C,
\]
formed as an [[algebra-modules/tensor-product|algebraic tensor product]] by extending scalars from the [[shared-foundations/real-numbers|real numbers]] to the [[shared-foundations/complex-numbers-c|complex numbers]]. The canonical real-linear map \(V\to V_{\mathbb C}\) sends \(v\) to \(v\otimes1\). Every element has a unique expression
\[
v\otimes1+w\otimes i,
\qquad v,w\in V,
\]
usually abbreviated \(v+iw\). If \(V\) is finite-dimensional, then
\[
\dim_{\mathbb C}V_{\mathbb C}=\dim_{\mathbb R}V.
\]

## Universal property

For every complex vector space \(W\), restriction along \(V\to V_{\mathbb C}\) gives a natural bijection
\[
\operatorname{Hom}_{\mathbb C}(V_{\mathbb C},W)
\cong
\operatorname{Hom}_{\mathbb R}(V,W),
\]
where \(W\) on the right is regarded as a real vector space. Explicitly, a real-linear map \(f:V\to W\) extends uniquely to the complex-linear map
\[
f_{\mathbb C}(v\otimes z)=z\,f(v).
\]
This characterizes complexification independently of a basis.

## Conjugation and real form

Complexification carries a canonical conjugation
\[
\overline{v\otimes z}=v\otimes\overline z.
\]
Its fixed-point subspace is the embedded copy of \(V\). Conversely, a complex vector space equipped with an antilinear involution is the complexification of its fixed real subspace.

Any real-linear map \(T:V\to W\) complexifies to \(T_{\mathbb C}:V_{\mathbb C}\to W_{\mathbb C}\), defined by \(T_{\mathbb C}(v\otimes z)=T(v)\otimes z\). This construction preserves compositions, direct sums, tensor products, kernels, and images.

## Remarks

One must distinguish complexifying a real vector space from merely forgetting or restoring scalar structure. If \(V\) is already complex and \(V_{\mathbb R}\) denotes its underlying real vector space, then
\[
(V_{\mathbb R})_{\mathbb C}\cong V\oplus\overline V,
\]
not just \(V\). The two summands correspond to the \(+i\) and \(-i\) [[linear-algebra/eigenspace|eigenspaces]] of the complexified original complex structure.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Section 1.2, complexification and complex-linear decompositions.
