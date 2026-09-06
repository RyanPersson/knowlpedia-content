+++
id = "nonassociative-algebra/octonions-as-complex-vectors"
title = "Octonions as complex vectors"
kind = "construction"
summary = "The real-algebra model of the octonions on C ⊕ C³ with an SU(3)-equivariant product."
aliases = ["C plus C3 model of octonions", "complex vector model of octonions", "O equals C plus C3"]
domains = ["nonassociative-algebra"]
prerequisites = ["linear-algebra/vector-space", "nonassociative-algebra/octonion-algebra", "nonassociative-algebra/conjugated-cross-product-on-c3", "nonassociative-algebra/octonion-conjugation-norm-and-inner-product", "linear-algebra/orthogonal-complement", "nonassociative-algebra/real-normed-division-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

As a real [[linear-algebra/vector-space|vector space]], the [[nonassociative-algebra/octonion-algebra|octonions]] can be written
\[
 \mathbb O\cong\mathbb C\oplus\mathbb C^3.
\]
Using the Hermitian product \(\langle u,v\rangle=\sum_i \overline{u_i}v_i\), conjugate-linear in its first argument, and the [[nonassociative-algebra/conjugated-cross-product-on-c3|conjugated cross product]] \(u\mathbin{\overline\times}v=\overline{u\times v}\), define multiplication by
\[
 (a,u)(b,v)
 =
 \left(
 ab-\langle u,v\rangle,
 \overline a\,v+b u+u\mathbin{\overline\times}v
 \right),
\]
where all scalar-vector products on the right are the ordinary complex scalar action. This is the convention used in the cited construction; in particular, conjugation falls on the scalar \(a\) from the left factor.

## Why this is an octonion algebra

The identity is \((1,0)\), conjugation is
\[
 (a,u)^*=(\overline a,-u),
\]
and the squared norm is
\[
 \lVert(a,u)\rVert^2=|a|^2+\langle u,u\rangle.
\]
The cross-product norm identity gives
\[
 \lVert(a,u)(b,v)\rVert
 =\lVert(a,u)\rVert\,\lVert(b,v)\rVert.
\]
This makes \(\mathbb C\oplus\mathbb C^3\) an eight-dimensional [[nonassociative-algebra/real-normed-division-algebra|real normed division algebra]], so [[nonassociative-algebra/hurwitz-theorem|Hurwitz's theorem]] identifies it with \(\mathbb O\).

## Geometric origin of the splitting

Choose a unit imaginary octonion \(i\). Then \(\operatorname{span}_{\mathbb R}\{1,i\}\) is an embedded copy of \(\mathbb C\), and its [[linear-algebra/orthogonal-complement|orthogonal complement]] is six-dimensional. In the displayed convention, right multiplication by \(i\) equips that complement with the complex structure corresponding to ordinary multiplication by \(i\) on \(\mathbb C^3\); left multiplication corresponds to multiplication by \(-i\). The resulting decomposition is orthogonal for the [[nonassociative-algebra/octonion-conjugation-norm-and-inner-product|octonion inner product]].

## Convention warning

This is a direct sum of **real** vector spaces and the product is real-bilinear, not complex-bilinear. In particular, the second component contains \(\overline a\,v\), not \(a v\), and contains the conjugate \(\overline{u\times v}\), not the ordinary cross product. Moving the conjugate-linear slot of the Hermitian inner product or choosing the opposite complex structure changes several terms at once; such variants can still describe an isomorphic octonion algebra but must not be mixed term by term.

## Symmetry

The standard action \(g(a,u)=(a,gu)\) of \(SU(3)\) preserves every operation in the product, hence acts by octonion automorphisms and fixes the \(\mathbb C\) summand pointwise. This realizes the [[nonassociative-algebra/su3-stabilizer-of-a-complex-octonion-subalgebra|\(SU(3)\) stabilizer of a chosen complex octonion subalgebra]].

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235). Relevant: §2 and Lemma 3.
2. John C. Baez, “Octonions and the Standard Model (Part 2),” 2020. [The n-Category Café](https://golem.ph.utexas.edu/category/2020/07/octonions_and_the_standard_mod_1.html). Relevant: the explicit \(\mathbb C\oplus\mathbb C^3\) multiplication convention.
3. Ichiro Yokota, *Exceptional Lie Groups*, Lecture Notes in Mathematics 2369, Springer, 2025. [arXiv:0902.0431](https://arxiv.org/abs/0902.0431). Relevant: Theorem 1.9.1 and the structures underlying the construction.
