+++
id = "langlands-letter/knowls/borel-mostow-semisimple-normalizer"
title = "Semisimple representatives in a torus normalizer"
kind = "knowl"
summary = "The normalizer theorem used in the letter to place semisimple elements of a disconnected reductive extension in standard torus data."
aliases = ["borel-mostow-semisimple-normalizer", "Borel–Mostow Normalizer Representative (Semisimple Class)"]
domains = ["langlands-letter"]
prerequisites = ["algebraic-geometry-foundations/algebraic-group", "langlands-letter/knowls/semisimple-element-and-class", "langlands-letter/knowls/maximal-torus-weight-lattice", "algebra-groups/normalizer"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "langlands-letter/knowls/borel-mostow-semisimple-normalizer.md"
section_mode = "progressive"
+++

Let \(H\) be a complex linear [[algebraic-geometry-foundations/algebraic-group|algebraic group]] whose identity component
\(H^\circ\) is reductive. A
[[langlands-letter/knowls/semisimple-element-and-class|semisimple element]]
\(s\in H\) normalizes some
[[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]] of
\(H^\circ\). Since maximal tori of \(H^\circ\) are
\(H^\circ\)-conjugate, after conjugation one may place \(s\) in the
[[algebra-groups/normalizer|normalizer]]

\[
N_H(T)
\]

of a fixed maximal torus \(T\subset H^\circ\).

## Based data

A representative in \(N_H(T)\) induces an automorphism of the [[lie-groups/root-system|root system]].
Composing with a Weyl-group element can arrange preservation of a chosen
positive system when the induced component admits such a representative.
This is a statement about a component and its
[[langlands/twisted-conjugacy|twisted conjugacy]], not the
ordinary assertion that every semisimple element of a connected group lies
in \(T\).

## Connected special case

If \(H\) is connected reductive, every semisimple element is conjugate into
\(T\) itself. Its ordinary [[algebra-groups/conjugacy-class|conjugacy class]] is then a Weyl orbit in \(T\).

## Langlands role

This is the normalizer-representative principle used in the letter for a
disconnected group such as
[[langlands-letter/knowls/langlands-dual-group|\(\widehat G\)]]
\(\rtimes\Gamma\).
In an [[langlands/l-group|\(L\)-group]], an
[[langlands/satake-parameter|unramified parameter]] lies in a
[[langlands-letter/knowls/frobenius-unramified|Frobenius]] coset
\(\widehat G\rtimes\operatorname{Frob}\). Conjugacy inside that coset is a
[[langlands/twisted-conjugacy|twisted-conjugacy problem]]. A
torus-normalizer representative makes the
root-theoretic Satake description possible, but modern formulations use the
invariant quotient of the Frobenius fiber rather than treating the coset as
a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]].

## Attribution warning

The source letter invokes Borel–Mostow in a specific disconnected
algebraic-group setting. Variants in the literature have different
hypotheses on the component group and on semisimplicity. The connected
special case above is unconditional; any stronger “dominant
representative” assertion should be cited with its exact version.

## References

1. A. Borel and G. D. Mostow, “On semi-simple automorphisms of Lie
   algebras,” *Annals of Mathematics* 61 (1955), 389–405.
   [DOI](https://doi.org/10.2307/1969815).
2. T. A. Springer, *Linear Algebraic Groups*, second edition, Birkhäuser,
   1998, §§7–8.
