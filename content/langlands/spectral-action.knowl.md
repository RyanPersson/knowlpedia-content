+++
id = "langlands/spectral-action"
title = "Fargues-Scholze spectral action"
kind = "knowl"
summary = "The action of perfect complexes on the local parameter stack on sheaves over the stack of G-bundles."
aliases = ["spectral action", "action of the stack of L-parameters", "Fargues–Scholze spectral action"]
domains = ["langlands", "representation-theory", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/perfect-complex", "langlands/stack-of-l-parameters", "algebraic-geometry-foundations/lisse-ell-adic-sheaf", "langlands/g-bundle-on-fargues-fontaine-curve"]
dependency_review_count = 1
section_mode = "progressive"
+++

In Fargues–Scholze theory, the **spectral action** is a monoidal action

\[
\operatorname{Perf}\!\left(
[Z^1(W_E,\widehat G)/\widehat G]
\right)
\curvearrowright
D_{\mathrm{lis}}(\operatorname{Bun}_G)
\]

of [[algebraic-geometry-foundations/perfect-complex|perfect complexes]] on
the
[[langlands/stack-of-l-parameters|stack of local \(L\)-parameters]] on the
derived category of
[[algebraic-geometry-foundations/lisse-ell-adic-sheaf|lisse
\(\ell\)-adic sheaves]] on the stack of
[[langlands/g-bundle-on-fargues-fontaine-curve|\(G\)-bundles on the
Fargues–Fontaine curve]].

Precise coefficient rings and compactness conditions are part of the
theorem.

## Construction principle

[[langlands/geometric-satake-equivalence|Geometric Satake]] supplies
[[langlands/hecke-functor|Hecke functors]] indexed by representations of the
[[langlands-letter/knowls/langlands-dual-group|dual group]]
\(\widehat G^I\), and the leg divisors carry independent
[[langlands/weil-group|Weil-group]]
actions. Their compatibility for all finite sets \(I\) satisfies the
relations of perfect complexes on the cocycle stack. This categorical
upgrade packages the local [[langlands/excursion-operator|excursion operators]].

## Consequences

Taking endomorphisms of the tensor unit gives the map from the
[[langlands/spectral-bernstein-center|spectral Bernstein center]] to the
ordinary [[harmonic-analysis/bernstein-center|Bernstein center]]. The action
also decomposes the sheaf category
according to connected components of the parameter stack.

For a point \(\phi\) with
[[algebra-groups/centralizer|centralizer]] \(S_\phi\), the fiber category remembers
representations of \(S_\phi\), which is the structure expected to encode the
members of an [[langlands/l-packet|\(L\)-packet]] across the groups
\(G_b(E)\).

## Theorem versus categorical conjecture

The spectral action itself is constructed. A much stronger conjecture says
that acting on a Whittaker sheaf gives a fully faithful functor from
[[algebraic-geometry-foundations/perfect-complex|perfect complexes]] on the
parameter stack and extends to an equivalence between an
appropriate coherent spectral category and the automorphic sheaf category.
That categorical local Langlands equivalence is not proved in full
generality.

## References

1. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” Chapters VIII–X.
   [arXiv](https://arxiv.org/abs/2102.13459).
