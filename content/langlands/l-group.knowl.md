+++
id = "langlands/l-group"
title = "Langlands \\(L\\)-group"
kind = "definition"
summary = "The complex dual group extended by the Weil or Galois action on its based root datum."
aliases = ["L-group", "Langlands group of a reductive group", "{}^L G"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/local-field", "langlands-letter/knowls/global-local-fields-completions", "langlands-letter/knowls/langlands-dual-group", "langlands/weil-group", "langlands-letter/knowls/pinned-automorphisms", "langlands-letter/knowls/roots-weights-weyl"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
[[algebra-fields-galois/local-field|local]] or [[langlands-letter/knowls/global-local-fields-completions|global field]] \(F\),
and let \(\widehat G\) be its pinned complex
[[langlands-letter/knowls/langlands-dual-group|Langlands dual group]]. The
**\(L\)-group** of \(G\) is

\[
{}^LG=\widehat G\rtimes W_F,
\]

where the [[langlands/weil-group|Weil group]] acts on \(\widehat G\) through
the [[langlands-letter/knowls/pinned-automorphisms|pinned action]] on its
[[langlands-letter/knowls/roots-weights-weyl|based root datum]]. It comes with
an exact sequence

\[
1\longrightarrow\widehat G\longrightarrow{}^LG
\longrightarrow W_F\longrightarrow1.
\]

For a split group the action is trivial, although the Weil-group factor and
projection remain part of the \(L\)-group.

## Galois and global variants

Many sources write \(\widehat G\rtimes\Gamma_F\), especially when the action
factors through a finite Galois quotient. For global questions, one may use an
appropriate global Weil group or a conjectural global Langlands group. These
versions carry different topology and extension data even when they induce the
same finite action on the root datum.

## \(L\)-homomorphisms

An \(L\)-homomorphism

\[
{}^LH\longrightarrow{}^LG
\]

is continuous, is compatible with the projections to the Weil group, and is
algebraic on the connected complex dual-group part. Such homomorphisms are
considered up to conjugation by \(\widehat G\) and are the input to
[[langlands-letter/knowls/langlands-functoriality-l-homomorphism|Langlands
functoriality]].

## Dependence on pinning

A pinning turns the outer Galois action on the dual group into an actual action.
Different compatible choices produce isomorphic \(L\)-groups, canonically only
up to [[algebra-groups/inner-automorphism|inner automorphism]]. Statements about parameters are therefore made up to
\(\widehat G\)-conjugacy.

## References

1. Armand Borel, “Automorphic \(L\)-functions,” in *Automorphic Forms,
   Representations and \(L\)-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 2, 1979, §§2–3.
2. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §2.1, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
