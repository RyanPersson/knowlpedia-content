+++
id = "langlands/lafforgue-global-parameterization"
title = "Vincent Lafforgue global parameterization"
kind = "knowl"
summary = "The canonical decomposition of cuspidal automorphic forms over a function field by semisimple global Langlands parameters."
aliases = ["Lafforgue parameterization", "global Langlands parameterization for reductive groups over function fields", "Vincent Lafforgue theorem"]
domains = ["langlands", "number-theory", "representation-theory"]
prerequisites = ["algebra-fields-galois/global-function-field", "algebraic-geometry-foundations/smooth-projective-curve", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands/automorphic-form", "algebra-groups/conjugacy-class", "langlands-letter/knowls/semisimple-element-and-class", "langlands/global-langlands-parameter", "langlands-letter/knowls/galois-extension-and-group", "langlands-letter/knowls/langlands-dual-group", "langlands/l-group", "langlands/rigid-inner-twist"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F=\mathbb F_q(X)\) be the
[[algebra-fields-galois/global-function-field|function field]] of
a [[algebraic-geometry-foundations/smooth-projective-curve|smooth projective
geometrically connected curve]], let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]], and fix level and central data. The **Vincent Lafforgue global
parameterization** is a canonical decomposition of the finite-dimensional
space of cuspidal [[langlands/automorphic-form|automorphic forms]]

\[
\mathcal A_{\mathrm{cusp}}
=
\bigoplus_\sigma \mathcal H_\sigma
\]

indexed by [[algebra-groups/conjugacy-class|conjugacy classes]] of continuous
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]] global
\(\ell\)-adic [[langlands/global-langlands-parameter|Langlands parameters]]
\(\sigma\), unramified away from the level.

For split \(G\),

\[
\sigma:
\operatorname{Gal}(\overline F/F)
\longrightarrow
\widehat G(\overline{\mathbb Q}_\ell).
\]

The source is the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
of \(F\), and \(\widehat G\) is the
[[langlands-letter/knowls/langlands-dual-group|Langlands dual group]].

For nonsplit \(G\), the target and projection condition use the
[[langlands/l-group|\(L\)-group]]; the automorphic side naturally includes
the relevant [[langlands/rigid-inner-twist|inner forms]].

## Characterizing property

For every unramified place \(v\) and every algebraic representation \(V\)
of \(\widehat G\), the spherical Hecke operator attached to \(V\) acts on
\(\mathcal H_\sigma\) through the scalar

\[
\operatorname{tr}\!\left(V(\sigma(\operatorname{Frob}_v))\right),
\]

with
[[langlands-letter/knowls/frobenius-unramified|Frobenius]] and
[[langlands/satake-parameter|Satake]] normalizations chosen consistently.

## Construction

Cohomology of multiple-leg [[langlands/g-shtuka|\(G\)-shtukas]],
[[langlands/geometric-satake-equivalence|geometric Satake]],
[[langlands/partial-frobenius-on-shtukas|partial Frobenius]], and
[[langlands/coalescence-of-shtuka-legs|coalescence]] produce the commuting
[[langlands/excursion-algebra|excursion algebra]]. Its generalized
characters reconstruct the semisimple parameters and define the displayed
summands.

## Exact scope

This is the automorphic-to-Galois direction for arbitrary [[algebraic-geometry-foundations/reductive-algebraic-group|reductive groups]]
over global function fields. It is stronger than merely attaching
almost-all [[langlands/satake-parameter|Satake classes]], but it is not a
general bijection between
individual [[langlands/automorphic-representation|automorphic representations]] and parameters and does not provide
the missing [[langlands/arthur-multiplicity-formula|Arthur multiplicity formulas]]. For
\(\operatorname{GL}_n\), Drinfeld and Laurent Lafforgue prove the fuller
correspondence.

The decomposition is \(\ell\)-adic; independence of \(\ell\) in the broad
general setting is an additional conjectural issue.

## References

1. Vincent Lafforgue, “Chtoucas pour les groupes réductifs et
   paramétrisation de Langlands globale,” *JAMS* 31 (2018), 719–891.
   [arXiv](https://arxiv.org/abs/1209.5352).
2. Vincent Lafforgue, “Introduction to chtoucas for reductive groups and to
   the global Langlands parameterization.”
   [arXiv](https://arxiv.org/abs/1404.6416).
