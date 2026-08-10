+++
id = "langlands/strongly-regular-semisimple-element"
title = "Strongly regular semisimple element"
kind = "knowl"
summary = "A semisimple element of a reductive group whose centralizer is a maximal torus."
aliases = ["strongly regular semisimple", "strongly regular element", "regular semisimple element with torus centralizer"]
domains = ["langlands", "algebraic-geometry-foundations", "representation-theory"]
section_mode = "progressive"
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a field \(F\). An element
\(\gamma\in G(F)\) is **strongly regular semisimple** if it is
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]] and its
[[algebra-groups/centralizer|centralizer]]

\[
G_\gamma=\{g\in G:g\gamma=\gamma g\}
\]

is a [[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]]
of \(G\).

## Regular versus strongly regular

For a connected reductive group in characteristic zero, regular semisimple
elements have torus centralizer, so the two phrases are often used
interchangeably. In greater generality, “regular” can be defined by minimal
centralizer dimension while “strongly regular” also requires the centralizer
to be a torus. The stronger phrase avoids ambiguity in endoscopy.

For the [[lie-groups/lie-algebra|Lie algebra]], \(X\in\mathfrak g(F)\) is strongly regular semisimple
when its centralizer \(G_X\) is a maximal torus.

## Examples

A matrix in \(\operatorname{GL}_n(F)\) is strongly regular semisimple exactly
when its [[linear-algebra/characteristic-polynomial|characteristic polynomial]] is separable of degree \(n\), equivalently
when it has \(n\) distinct eigenvalues over an [[algebra-fields-galois/algebraic-closure|algebraic closure]].

A regular diagonal element in a split reductive group is strongly regular
when no root takes the value \(1\) on it. In the Lie algebra, the analogous
condition is \(\alpha(X)\neq 0\) for every
[[langlands-letter/knowls/roots-weights-weyl|root]].

## Why this locus is used

On the strongly regular semisimple locus:

- [[algebra-groups/conjugacy-class|conjugacy classes]] are controlled by maximal tori;
- centralizer quotients carry natural invariant measures;
- [[langlands/orbital-integral|orbital integrals]] are well behaved;
- [[langlands/stable-conjugacy|stable conjugacy]] splits into finitely many
  rational conjugacy classes over a
  [[langlands-letter/knowls/global-local-fields-completions|local field]];
- [[langlands/endoscopic-transfer|endoscopic transfer]] compares matching classes on different groups.

Singular semisimple and unipotent terms still occur in the trace formula, but
their distributions require additional limiting and weighted constructions.

## References

1. Robert E. Kottwitz, “Stable trace formula: cuspidal tempered terms,”
   *Duke Mathematical Journal* 51 (1984), 611–650.
   [DOI](https://doi.org/10.1215/S0012-7094-84-05129-9).
2. Ngô Bảo Châu, “Survey on the fundamental lemma,” §1.3.
   [PDF](https://math.uchicago.edu/~ngo/survey.pdf).
