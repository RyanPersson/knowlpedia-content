+++
id = "nonassociative-algebra/conjugated-cross-product-on-c3"
title = "Conjugated cross product on C³"
kind = "definition"
summary = "The SU(3)-equivariant conjugate-bilinear cross product on complex three-space."
aliases = ["Hermitian cross product", "conjugate cross product on C3", "conjugated complex cross product"]
domains = ["nonassociative-algebra"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For \(u,v\in\mathbb C^3\), their **conjugated cross product** is
\[
 u\mathbin{\overline\times}v=\overline{u\times v},
\]
where \(u\times v\) is the usual coordinate cross product extended complex-bilinearly and the bar denotes componentwise complex conjugation. Equivalently,
\[
 (u\mathbin{\overline\times}v)_i
 =\sum_{j,k=1}^{3}\varepsilon_{ijk}\,\overline{u_j}\,\overline{v_k}.
\]

## Linearity and orthogonality

The operation is real-bilinear and conjugate-linear in each argument over \(\mathbb C\):
\[
 (\lambda u)\mathbin{\overline\times}v
 =\overline\lambda\,(u\mathbin{\overline\times}v),
 \qquad
 u\mathbin{\overline\times}(\lambda v)
 =\overline\lambda\,(u\mathbin{\overline\times}v).
\]
It is alternating. With the Hermitian inner product convention
\[
 \langle u,v\rangle=\sum_{i=1}^{3}\overline{u_i}v_i,
\]
one has
\[
 \langle u,u\mathbin{\overline\times}v\rangle
 =\langle v,u\mathbin{\overline\times}v\rangle=0
\]
and the norm identity
\[
 |\langle u,v\rangle|^2
 +\lVert u\mathbin{\overline\times}v\rVert^2
 =\lVert u\rVert^2\lVert v\rVert^2.
\]

## Why the conjugation is present

The ordinary complex-bilinear cross product naturally takes values in the dual representation: for \(g\in SL(3,\mathbb C)\),
\[
 (gu)\times(gv)=g^{-T}(u\times v).
\]
For \(g\in SU(3)\), one has \(\overline{g^{-T}}=g\). Componentwise conjugation therefore turns the output into the defining representation, so
\[
 g(u\mathbin{\overline\times}v)
 =(gu)\mathbin{\overline\times}(gv)
 \qquad(g\in SU(3)).
\]
This equivariance is precisely what makes the [[nonassociative-algebra/octonions-as-complex-vectors|\(\mathbb C\oplus\mathbb C^3\) octonion product]] compatible with the standard \(SU(3)\)-action.

## Convention warning

The bar is part of the operation, not decoration. Omitting it produces a different map and breaks the displayed \(SU(3)\)-equivariance in the defining representation. The inner product convention is also important: here it is conjugate-linear in the first argument and linear in the second.

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235). Relevant: §2, especially Lemma 3.
2. John C. Baez, “Octonions and the Standard Model (Part 2),” 2020. [The n-Category Café](https://golem.ph.utexas.edu/category/2020/07/octonions_and_the_standard_mod_1.html). Relevant: the Hermitian cross product and \(\mathbb C\oplus\mathbb C^3\) multiplication convention.
