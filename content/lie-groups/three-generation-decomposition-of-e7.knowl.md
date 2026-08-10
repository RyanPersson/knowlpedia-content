+++
id = "lie-groups/three-generation-decomposition-of-e7"
title = "Three-generation decomposition of e7"
kind = "theorem"
summary = "After choosing generation root lines, e7 decomposes as sl6 plus a two-dimensional trivial module plus three 32-dimensional Standard Model generation modules."
aliases = ["three generations in e7 decomposition", "e7 equals sl6 plus C2 plus three generations", "E7 three-generation theorem"]
domains = ["lie-groups", "representation-theory", "mathematical-physics"]
section_mode = "progressive"
+++

Fix a good embedded \(\mathfrak g_{\mathrm{SM}}\subset\mathfrak e_7\), a compatible Cartan subalgebra, and a labeling of the three generation root lines. Then
\[
\mathfrak e_7
=\mathfrak{sl}_6^{\mathrm{SM}}
\oplus(\mathbb C\otimes_{\mathbb R}P)
\oplus V_1\oplus V_2\oplus V_3,
\]
where each \(V_k\) is the [[lie-groups/generation-module-as-even-exterior-algebra|32-dimensional generation module]]. Every summand is invariant under \(\mathfrak{sl}_6^{\mathrm{SM}}\) acting through the \(\mathfrak e_7\) bracket, and
\[
V_k\cong\Lambda^{\mathrm{even}}\mathbb C^6
\quad\text{as \(\mathfrak{sl}_6^{\mathrm{SM}}\)-modules},
\qquad
V_k\cong\Lambda\mathbb C^5
\quad\text{as \(\mathfrak{sl}_5^{\mathrm{SM}}\)-modules}.
\]
Hence each \(V_k\) restricts to one full Standard Model generation, including the two neutrino singlet states.

## What the direct sum means

The theorem is a direct-sum decomposition of the underlying vector space and of the \(\mathfrak{sl}_6^{\mathrm{SM}}\)-module:
\[
133=35+2+32+32+32.
\]
Only
\[
\mathfrak{sl}_6^{\mathrm{SM}}
\oplus(\mathbb C\otimes P)
\]
is asserted to be a Lie subalgebra; it is the [[lie-groups/intersection-of-three-a1-plus-d6-subalgebras|common intersection of the three \(A_1+D_6\) subalgebras]]. The \(V_k\) are invariant linear subspaces, not Lie subalgebras, and the displayed decomposition is not a direct sum of Lie algebras.

## Root-space content

The common Lie subalgebra consists of the full Cartan together with the \(30\) root spaces in \(\Phi_0\). Each
\[
V_k=\bigoplus_{r\in\{\pm\beta_k\}\sqcup\Phi_k}(\mathfrak e_7)_r
\]
contains \(30\) root spaces projected to \(\pm w_k\) and the two generation-root spaces projected to \(\pm\beta_k\). The [[lie-groups/e7-root-projection-trichotomy|root partition]], together with
\(A=\bigsqcup_{k=1}^3\{\pm\beta_k\}\), makes the seven root-index sets used here disjoint and exhaustive.

## Dependence on choices

The standard \(\mathfrak{sl}_6\) is intrinsic to the chosen good Standard Model embedding, but the splitting of the generation \(\mathfrak{sl}_3\) into its two Cartan directions and six root spaces is not. Therefore the individually named \(V_1,V_2,V_3\) require a Cartan choice and root-line labeling. Without those choices, the intrinsic statement is instead the [[lie-groups/e7-branching-under-a2-plus-a5|\(A_2+A_5\) branching rule]], in which the generation \(\mathfrak{sl}_3\) remains unbroken.

## Mathematical scope

This theorem is a representation-theoretic pattern inside the complex Lie algebra \(\mathfrak e_7\). By itself it does not specify a physical theory, spacetime spin representation, dynamics, symmetry breaking, or an explanation of observed particle masses and mixings.

## References

1. John C. Baez, “Three Generations in E7,” 2026, Theorem 13. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
2. Benjamin Nasmith, “An Exceptional Combinatorial Sequence and Standard Model Particles,” 2020. [arXiv:2012.03933](https://arxiv.org/abs/2012.03933).
3. T. Kugo and T. Yanagida, “Unification of Families Based on a Coset Space \(E_7/(SU(5)\times SU(3)\times U(1))\),” *Physics Letters B* 134 (1984), 313–317. [DOI record](https://doi.org/10.1016/0370-2693(84)90007-8).
