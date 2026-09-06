+++
id = "harmonic-analysis/langlands-classification-p-adic-group"
title = "Langlands classification for p-adic groups"
kind = "theorem"
summary = "Every irreducible admissible representation is the unique irreducible quotient of a standard module induced from tempered data."
aliases = ["p-adic Langlands classification", "Langlands quotient for a p-adic group", "standard module for a p-adic group"]
domains = ["harmonic-analysis", "langlands"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "algebraic-geometry-foundations/reductive-algebraic-group", "harmonic-analysis/admissible-representation-p-adic-group", "harmonic-analysis/normalized-parabolic-induction-p-adic-group", "algebraic-geometry-foundations/parabolic-subgroup", "algebraic-geometry-foundations/levi-subgroup", "harmonic-analysis/tempered-representation-p-adic-group", "algebra-representation-theory/character"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] and let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]]. The **Langlands classification** says that every irreducible
[[harmonic-analysis/admissible-representation-p-adic-group|admissible
representation]] \(\pi\) of \(G(F)\) is the unique
irreducible quotient of a
[[harmonic-analysis/normalized-parabolic-induction-p-adic-group|normalized
induced representation]]

\[
I_P^G(\tau\otimes\chi),
\]

where \(P=MN\) is a
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]]
with [[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]] \(M\),
\(\tau\) is an irreducible
[[harmonic-analysis/tempered-representation-p-adic-group|tempered
representation]] of \(M(F)\), and the real
[[algebra-representation-theory/character|unramified character]] \(\chi\) lies
in the chosen open positive Weyl chamber.  The induced representation is the
**standard module**, and its distinguished quotient is the **Langlands
quotient**.

The triple \((M,\tau,\chi)\) is unique up to \(G(F)\)-conjugacy once the
positive chamber convention is fixed.

## Boundary cases

If \(\chi=1\), the quotient is tempered and the data lie on the boundary of
the positive chamber.  Starting instead from an essentially
[[lie-groups/square-integrable-modulo-center-representation|square-integrable
representation]] yields an equivalent refinement of the
classification.

The result here is for reductive groups over nonarchimedean local fields.  The
real-group classification uses analogous standard modules but different
categories and analytic input.

## Relation to parameters

The extra \(\operatorname{SL}_2\) in a nonarchimedean
[[langlands/local-l-parameter|L-parameter]] records monodromy, while the
unbounded real part of the [[langlands/weil-group|Weil-group]] image
parallels the positive unramified
twist \(\chi\).  This relation guides the extension of tempered local
Langlands to all irreducible admissible representations.

## References

1. Robert P. Langlands, “On the classification of irreducible
   representations of real algebraic groups,” 1973; the nonarchimedean
   analogue follows the same standard-module formalism.
2. Allan J. Silberger, *Introduction to Harmonic Analysis on Reductive
   \(p\)-adic Groups*, Mathematical Notes 23, Princeton University Press,
   1979, Chapter 5.
