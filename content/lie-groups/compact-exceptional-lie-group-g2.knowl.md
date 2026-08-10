+++
id = "lie-groups/compact-exceptional-lie-group-g2"
title = "Compact exceptional Lie group G2"
kind = "knowl"
summary = "The compact connected simple 14-dimensional Lie group of rank 2 that is the automorphism group of the real octonions."
aliases = ["compact-exceptional-lie-group-g2", "compact G2", "compact Lie group G2", "Aut(O)"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

The **compact exceptional Lie group \(G_2\)** is the compact connected simple [[lie-groups/compact-lie-group|Lie group]] of rank \(2\) and real dimension \(14\) whose [[lie-groups/root-system|root system]] has Dynkin type \(G_2\). It is both [[lie-groups/simply-connected-lie-group|simply connected]] and centerless. Its real [[lie-groups/lie-algebra|Lie algebra]] is the [[lie-groups/compact-real-form|compact real form]] of [[lie-groups/exceptional-lie-algebra-g2|\(\mathfrak g_2\)]].

Its distinguished representation is the faithful irreducible action on the seven-dimensional real vector space \(\operatorname{Im}\mathbb O\) of imaginary octonions.

## Octonion automorphisms

There is a natural isomorphism
\[
G_2\cong\operatorname{Aut}_{\mathbb R\text{-alg}}(\mathbb O).
\]
Every automorphism fixes \(1\), preserves [[nonassociative-algebra/octonion-conjugation-norm-and-inner-product|octonion conjugation]] and the norm, and hence acts orthogonally on \(\operatorname{Im}\mathbb O\). This realizes \(G_2\) as a closed subgroup of \(SO(7)\). Equivalently, it is the stabilizer of the alternating three-form
\[
\varphi(x,y,z)=\langle xy,z\rangle
\]
on \(\operatorname{Im}\mathbb O\), with a consistent choice of sign convention.

The use of the division octonions selects the compact form. Automorphisms of the split octonions form the split real group \(G_{2(2)}\), while complexification gives the complex [[algebraic-geometry-foundations/algebraic-group|algebraic group]] of type \(G_2\).

## The SU(3) stabilizer

The group \(G_2\) acts transitively on the [[linear-algebra/unit-sphere|unit sphere]] in \(\operatorname{Im}\mathbb O\). The stabilizer of a unit imaginary octonion \(i\), equivalently of the complex subalgebra \(\mathbb C=\operatorname{span}_{\mathbb R}\{1,i\}\), is isomorphic to \(SU(3)\). The [[linear-algebra/orthogonal-complement|orthogonal complement]] of this \(\mathbb C\) becomes its defining complex module, yielding
\[
\mathbb O\cong\mathbb C\oplus\mathbb C^3.
\]
This decomposition and its \(SU(3)\)-equivariant operations are the starting point for the octonion construction in the exceptional-Jordan-algebra setting.

## References

1. John C. Baez, "The Octonions," *Bulletin of the American Mathematical Society* 39 (2002), 145--205. [DOI](https://doi.org/10.1090/S0273-0979-01-00934-X).
2. John Frank Adams, *Lectures on Exceptional Lie Groups*, University of Chicago Press, 1996, Chapters 3--5. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/L/bo3683975.html).
3. Robert L. Bryant, "Metrics with exceptional holonomy," *Annals of Mathematics* 126 (1987), 525--576. [DOI](https://doi.org/10.2307/1971360).
4. John C. Baez and Paul Schwahn, *The Standard Model Gauge Group from the Exceptional Jordan Algebra*, 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
