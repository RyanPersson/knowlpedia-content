+++
id = "nonassociative-algebra/frame-decomposition-of-hermitian-jordan-algebras"
title = "Frame decomposition of Hermitian Jordan algebras"
kind = "construction"
summary = "The diagonal-line and off-diagonal-pair decomposition of H_3(K) determined by its standard Jordan frame."
aliases = ["six-space decomposition of H3(K)", "Jordan frame decomposition of Hermitian matrices"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
+++

Let \(\mathbb K\) be a normed real division algebra and let
\((e_1,e_2,e_3)\) be the standard [[nonassociative-algebra/jordan-frame|Jordan
frame]] of \(H_3(\mathbb K)\). Write \(\xi_{ij}(x)\) for the Hermitian matrix
whose \(ij\)-entry is \(x\), whose \(ji\)-entry is \(x^*\), and whose other
entries vanish. Then there is an orthogonal direct sum
\[
H_3(\mathbb K)
=\bigoplus_{i=1}^3\mathbb R e_i
\;\oplus\;
\xi_{12}(\mathbb K)\oplus\xi_{23}(\mathbb K)\oplus\xi_{31}(\mathbb K).
\]
For \(\mathbb K=\mathbb O\), this is the underlying vector-space
decomposition of the [[nonassociative-algebra/exceptional-jordan-algebra|Albert
algebra]].

## Relation to Peirce spaces

If \((i,j,k)\) is a permutation of \((1,2,3)\), then
\[
\mathbb R e_i=J_1(e_i),
\qquad
\xi_{ij}(\mathbb K)=J_{1/2}(e_i)\cap J_{1/2}(e_j),
\]
and
\[
J_0(e_k)
=\mathbb R e_i\oplus\mathbb R e_j\oplus\xi_{ij}(\mathbb K).
\]
Thus the decomposition simultaneously refines the three
[[nonassociative-algebra/peirce-decomposition|Peirce decompositions]].

## Multiplication between pair spaces

With a cyclic choice of indices and a compatible convention for the maps
\(\xi_{ij}\), matrix multiplication gives
\[
\xi_{ij}(x)\circ\xi_{jk}(y)=\tfrac12\,\xi_{ik}(xy).
\]
Changing which entry receives \(x\) rather than \(x^*\) changes the displayed
conjugations and order, but not the structural point: multiplying adjacent
pair spaces lands in the third pair space. In the octonionic case these three
eight-dimensional spaces carry the vector and two [[lie-groups/half-spin-representation|half-spin representations]]
under the frame-fixing \(\mathrm{Spin}(8)\).

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026, §4. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000, Chapters 5–7. [Publisher record](https://doi.org/10.1007/978-3-662-12622-6).
