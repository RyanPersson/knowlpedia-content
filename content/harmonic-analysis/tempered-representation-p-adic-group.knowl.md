+++
id = "harmonic-analysis/tempered-representation-p-adic-group"
title = "Tempered representation of a p-adic group"
kind = "definition"
summary = "An irreducible admissible representation whose matrix coefficients have almost square-integrable decay."
aliases = ["p-adic tempered representation", "tempered smooth representation", "tempered representation of a reductive p-adic group"]
domains = ["harmonic-analysis", "langlands"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "algebraic-geometry-foundations/reductive-algebraic-group", "harmonic-analysis/admissible-representation-p-adic-group", "algebra-representation-theory/central-character", "algebra-groups/center-of-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] and let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]]. An irreducible
[[harmonic-analysis/admissible-representation-p-adic-group|admissible
representation]] \(\pi\) of \(G(F)\) with unitary
[[algebra-representation-theory/central-character|central character]] is
**tempered** if its matrix
coefficients belong to

\[
L^{2+\varepsilon}(G(F)/Z_G(F))
\qquad\text{for every }\varepsilon>0.
\]

Here \(Z_G\) is the [[algebra-groups/center-of-group|center]] of \(G\).
Equivalently, its unitary realization is weakly contained in the regular
representation.  For a nonunitary central character, one first makes the
standard unitary twist when that formulation is available.

## Position in the classification

Every
[[algebra-representation-theory/irreducible-representation|irreducible
representation]] that is
[[lie-groups/square-integrable-modulo-center-representation|square-integrable
modulo the center]] is tempered.  Tempered representations are the building
blocks in the
[[harmonic-analysis/langlands-classification-p-adic-group|p-adic Langlands
classification]]: general irreducibles are quotients of inductions of
tempered data twisted into a positive chamber.

## Parameter-side expectation

The [[langlands/local-langlands-correspondence|local Langlands
correspondence]] is expected to match tempered representations with bounded
[[langlands/local-l-parameter|L-parameters]].  For groups where local
Langlands is established, this is a theorem subject to the normalization of
the correspondence.

## References

1. Harish-Chandra, “Harmonic analysis on reductive \(p\)-adic groups,” in
   *Harmonic Analysis on Homogeneous Spaces*, Proceedings of Symposia in Pure
   Mathematics 26, 1973.
2. William Casselman, “Introduction to the theory of admissible
   representations of \(p\)-adic reductive groups,” unpublished notes, §§4–6.
   [UBC](https://personal.math.ubc.ca/~cass/research/pdf/p-adic-book.pdf).
