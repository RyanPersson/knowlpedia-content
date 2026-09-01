+++
id = "langlands/hitchin-fibration"
title = "Hitchin fibration"
kind = "definition"
summary = "The map sending a Higgs field to the invariant-polynomial coefficients of its characteristic data."
aliases = ["Hitchin map", "Hitchin system", "Hitchin morphism"]
domains = ["langlands", "algebraic-geometry-foundations", "differential-geometry"]
prerequisites = ["algebraic-geometry-foundations/smooth-projective-curve", "algebraic-geometry-foundations/reductive-algebraic-group", "lie-groups/lie-algebra", "algebraic-geometry-foundations/principal-g-bundle-on-scheme", "linear-algebra/characteristic-polynomial"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(X\) be a
[[algebraic-geometry-foundations/smooth-projective-curve|smooth projective
curve]], let \(G\) be a
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), and let \(D\) be a
line bundle on \(X\). A \(D\)-valued \(G\)-Higgs bundle is a pair
\((E,\varphi)\) consisting of an
[[algebraic-geometry-foundations/principal-g-bundle-on-scheme|algebraic
principal \(G\)-bundle]] and a section

\[
\varphi\in H^0(X,\operatorname{ad}(E)\otimes D).
\]

If \(f_1,\ldots,f_r\) generate
\(k[\mathfrak g]^G\) with degrees \(d_1,\ldots,d_r\), the **Hitchin fibration**
is

\[
h:\operatorname{Higgs}_{G,D}
\longrightarrow
\mathcal A_{G,D}:=
\bigoplus_{i=1}^r H^0(X,D^{\otimes d_i}),
\qquad
(E,\varphi)\longmapsto(f_i(\varphi))_i.
\]

For \(G=\operatorname{GL}_n\), it records the coefficients of the
[[linear-algebra/characteristic-polynomial|characteristic polynomial]] of
\(\varphi\).

## Fibers and spectral data

Over the [[langlands/strongly-regular-semisimple-element|regular semisimple]]
locus, a fiber is controlled by a cameral or spectral cover and a Picard
[[algebraic-geometry-foundations/algebraic-stack|stack]] of regular
[[algebra-groups/centralizer|centralizers]]. Singular fibers
encode degenerations of this abelianized geometry.

## Fundamental lemma

The Hitchin fibration globalizes the local geometry of
[[langlands/affine-springer-fiber|affine Springer fibers]].  Ngô's support
theorem and comparison of the relevant endoscopic parts of its cohomology
yield the [[langlands/fundamental-lemma|fundamental lemma]].

## References

1. Nigel Hitchin, “Stable bundles and integrable systems,” *Duke Mathematical
   Journal* 54 (1987), 91–114.
2. Ngô Bảo Châu, “Le lemme fondamental pour les algèbres de Lie,”
   *Publications Mathématiques de l'IHÉS* 111 (2010), 1–169.
   [Numdam](https://www.numdam.org/item/PMIHES_2010__111__1_0/).
