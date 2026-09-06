+++
id = "langlands/coalescence-of-shtuka-legs"
title = "Coalescence of shtuka legs"
kind = "knowl"
summary = "The fusion isomorphism relating shtuka cohomology before and after several legs are identified."
aliases = ["coalescence isomorphism", "fusion of shtuka legs", "merging shtuka legs"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
prerequisites = ["langlands/g-shtuka", "langlands/affine-grassmannian", "langlands/geometric-satake-equivalence"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\zeta:I\to J\) be a map of finite sets. It defines a diagonal map

\[
\Delta_\zeta:X^J\longrightarrow X^I,
\qquad
(x_j)_{j\in J}\longmapsto(x_{\zeta(i)})_{i\in I}.
\]

**Coalescence of shtuka legs** is the canonical fusion isomorphism that
identifies the pullback of the \(I\)-leg shtuka cohomology along
\(\Delta_\zeta\) with the \(J\)-leg cohomology in which all legs in one
fiber of \(\zeta\) have merged.

## Representation-theoretic label

If \(W\) is a representation of the
[[langlands-letter/knowls/langlands-dual-group|dual group]]
\(\widehat G^I\), restriction along

\[
\widehat G^J\longrightarrow\widehat G^I,
\qquad
(g_j)\longmapsto(g_{\zeta(i)})
\]

gives a representation \(W^\zeta\) of \(\widehat G^J\). Writing
\(\mathcal H_{I,W}\) for the relevant cohomology sheaf, coalescence has the
form

\[
\Delta_\zeta^*\mathcal H_{I,W}
\simeq
\mathcal H_{J,W^\zeta}.
\]

## Geometric origin

The isomorphism comes from the factorization or fusion structure of the
Beilinson–Drinfeld [[langlands/affine-grassmannian|affine Grassmannian]] and the
[[langlands/geometric-satake-equivalence|geometric Satake equivalence]].
It remains meaningful on diagonals where modifications collide; it is more
than the evident identification on the open locus of distinct legs.

## Excursion-operator role

Starting with no legs, an invariant vector
\(x:\mathbf 1\to W\) creates several coincident legs. Coalescence separates
or groups the representation labels,
[[langlands/partial-frobenius-on-shtukas|partial Frobenius]] supplies
independent Galois actions, and a covector
\(\xi:W\to\mathbf 1\) annihilates the legs.
Functoriality of coalescence is essential for the relations among
[[langlands/excursion-operator|excursion operators]].

## References

1. Vincent Lafforgue, “Chtoucas pour les groupes réductifs et
   paramétrisation de Langlands globale,” Chapter 4.
   [arXiv](https://arxiv.org/abs/1209.5352).
2. Beilinson and Drinfeld, *Quantization of Hitchin's Integrable System and
   Hecke Eigensheaves*, factorization construction.
