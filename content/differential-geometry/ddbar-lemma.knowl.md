+++
id = "differential-geometry/ddbar-lemma"
title = "The ∂∂̄-lemma"
kind = "definition"
summary = "On a compact Kähler manifold, a pure-type closed form that is exact in one standard complex is ∂∂̄-exact."
aliases = ["ddbar lemma", "d d-c lemma"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a compact [[differential-geometry/kahler-manifold|Kähler manifold]], and let \(\alpha\) be a complex-valued form of pure type \((p,q)\) with \(d\alpha=0\). The **\(\partial\bar\partial\)-lemma** states that the following are equivalent: \(\alpha\) is \(d\)-exact, \(\partial\)-exact, \(\bar\partial\)-exact, or \(\partial\bar\partial\)-exact. Thus, whenever any of the first three conditions holds, there is a \((p-1,q-1)\)-form \(\beta\) such that
\[
\alpha=\partial\bar\partial\beta.
\]
The compactness and Kähler hypotheses are essential parts of this statement; the lemma can fail on general [[differential-geometry/complex-manifold|complex manifolds]].

## Equivalent formulations

In terms of images and kernels on all complex-valued forms, one common formulation is
\[
\ker\partial\cap\ker\bar\partial\cap
(\operatorname{im}\partial+\operatorname{im}\bar\partial)
=\operatorname{im}(\partial\bar\partial).
\]
With the convention \(d^c=i(\bar\partial-\partial)\) from the [[differential-geometry/d-c-operator|\(d^c\)-operator]], this is equivalently expressed through
\[
\operatorname{im}d\cap\ker d^c
=\operatorname{im}(dd^c)
=\ker d\cap\operatorname{im}d^c.
\]
These formulations differ only by the nonzero scalar relating \(dd^c\) and \(\partial\bar\partial\).

## Structure and consequences

The lemma identifies several apparently different notions of triviality. In particular, Bott–Chern cohomology maps isomorphically to [[differential-geometry/dolbeault-cohomology|Dolbeault cohomology]] in each bidegree, while the direct sum of its \((p,q)\)-groups with \(p+q=k\) maps isomorphically to degree-\(k\) [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology]]. It also ensures that this Hodge decomposition is independent of the chosen [[differential-geometry/kahler-metric|Kähler metric]]. Demailly proves these consequences in [Chapter VI, §8.2, Lemma 8.6 and Corollary 8.7].

## Conventions and scope

The pure-type formulation requires \(d\alpha=0\). Merely assuming \(\bar\partial\alpha=0\) does not make \(d\)-, \(\partial\)-, and \(\bar\partial\)-exactness equivalent. Compact non-Kähler complex manifolds provide genuine failures, so this lemma must not be applied from complex structure alone.

## References

1. Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, 2012. [Author-hosted text](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Relevant: Chapter VI, §8.2, especially Lemma 8.6 and Corollary 8.7.
