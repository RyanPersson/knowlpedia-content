+++
id = "langlands-letter/knowls/semisimple-element-and-class"
title = "Semisimple element and conjugacy class"
kind = "knowl"
summary = "An algebraic-group element whose image in a faithful representation is diagonalizable."
aliases = ["semisimple-element-and-class", "Semisimple Element and Semisimple Conjugacy Class"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/semisimple-element-and-class.md"
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/algebraic-group", "algebraic-geometry-foundations/algebraically-closed-field", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/maximal-torus-weight-lattice", "algebra-groups/conjugacy-class"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a linear [[algebraic-geometry-foundations/algebraic-group|algebraic group]] over an [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]].
An element \(g\in G\) is **semisimple** if its image under one, equivalently
every, faithful algebraic representation is a semisimple linear operator.
Over \(\mathbb C\), this means diagonalizable.

In a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]], an element is semisimple exactly when it
lies in a
[[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]]. Its
[[algebra-groups/conjugacy-class|conjugacy class]] is Zariski closed.

## Jordan decomposition

Every element \(g\) has a commuting Jordan decomposition

\[
g=g_sg_u=g_ug_s
\]

with \(g_s\) semisimple and \(g_u\) unipotent. Invariant regular functions
on \(G\) take the same values on \(g\) and \(g_s\), so the affine conjugacy
quotient records the semisimple class.

## Rational versus geometric conjugacy

If \(G\) is defined over a non-algebraically-closed field \(F\), elements of
\(G(F)\) that are conjugate over \(\overline F\) need not be conjugate over
\(F\). For [[langlands/strongly-regular-semisimple-element|strongly regular semisimple elements]] this distinction is
organized by [[langlands/stable-conjugacy|stable conjugacy]] and
[[langlands-letter/knowls/nonabelian-h1-galois-cohomology|Galois
cohomology]].

## Examples

- In \(\operatorname{GL}_n(\mathbb C)\), semisimple elements are precisely
  the diagonalizable matrices.
- A unipotent matrix other than the identity is not semisimple, even though
  all of its eigenvalues are \(1\).

## Langlands role

[[langlands/satake-parameter|Satake]] and
[[langlands/local-l-parameter|Langlands parameters]] are taken up to
semisimple conjugacy because
[[langlands-letter/knowls/characters-separate-semisimple-classes|characters
and invariant functions detect closed orbits]]. A semisimplified parameter
can lose [[algebra-fields-galois/inertia-subgroup|inertia]] or
[[langlands/weil-deligne-representation|monodromy]] information, so
“semisimple” is not a harmless adjective.

## References

1. T. A. Springer, *Linear Algebraic Groups*, second edition, Birkhäuser,
   1998.
