+++
id = "lie-groups/intersection-of-three-a1-plus-d6-subalgebras"
title = "Intersection of the three A1 + D6 subalgebras in e7"
kind = "theorem"
summary = "The three generation sl2 plus so12 subalgebras have common intersection sl6 plus the complexified generation plane; pairwise intersections already agree."
aliases = ["intersection of three sl2 plus so12 subalgebras", "common intersection of generation A1 D6 subalgebras"]
domains = ["lie-groups", "mathematical-physics"]
prerequisites = ["lie-groups/generation-plane", "lie-groups/lie-subalgebra", "lie-groups/standard-sl6-in-e7"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For the three generation root lines, set
\[
\mathfrak m_k
=\mathfrak{sl}_2(\beta_k)\oplus\mathfrak{so}_{12}(\beta_k)
\subset\mathfrak e_7.
\]
Then
\[
\mathfrak m_1\cap\mathfrak m_2\cap\mathfrak m_3
=\mathfrak{sl}_6^{\mathrm{SM}}
\oplus(\mathbb C\otimes_{\mathbb R}P),
\]
where \(P\) is the [[lie-groups/generation-plane|generation plane]]. In fact, for every \(i\ne k\),
\[
\mathfrak m_i\cap\mathfrak m_k
=\mathfrak m_1\cap\mathfrak m_2\cap\mathfrak m_3.
\]

These are equalities of embedded [[lie-groups/lie-subalgebra|Lie subalgebras]], not merely vector-space isomorphisms. On the right, the [[lie-groups/standard-sl6-in-e7|standard \(\mathfrak{sl}_6\)]] commutes with the two-dimensional abelian Cartan algebra \(\mathbb C\otimes P\), so the displayed sum is also a Lie-algebra direct sum.

## Root-space calculation

With \(\Phi_0\) and \(\Phi_k\) from the generation-plane partition,
\[
\mathfrak m_k
=\mathfrak h\oplus
\bigoplus_{r\in\{\pm\beta_k\}\sqcup\Phi_0\sqcup\Phi_k}
(\mathfrak e_7)_r.
\]
For \(i\ne k\), the only [[lie-groups/root-space|root spaces]] common to \(\mathfrak m_i\) and \(\mathfrak m_k\) are those indexed by \(\Phi_0\). The full Cartan \(\mathfrak h\) remains and splits as the Cartan of \(\mathfrak{sl}_6^{\mathrm{SM}}\) plus \(\mathbb C\otimes P\).

## Dependence on choices

The standard \(\mathfrak{sl}_6\) is intrinsic to the good Standard Model embedding, but the three \(\mathfrak m_k\) and the explicit Cartan factor \(\mathbb C\otimes P\) require a compatible Cartan choice. Relabeling the root lines permutes the \(\mathfrak m_k\) and leaves their common intersection unchanged.

## References

1. John C. Baez, “Three Generations in E7,” 2026, Proposition 7. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
