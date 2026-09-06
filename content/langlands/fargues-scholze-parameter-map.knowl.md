+++
id = "langlands/fargues-scholze-parameter-map"
title = "Fargues-Scholze parameter map"
kind = "knowl"
summary = "The theorem attaching a unique semisimple local L-parameter to an irreducible smooth representation."
aliases = ["Fargues–Scholze parameter", "Fargues Scholze semisimple local Langlands correspondence", "Fargues-Scholze L-parameter"]
domains = ["langlands", "representation-theory", "number-theory"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "algebraic-geometry-foundations/reductive-algebraic-group", "harmonic-analysis/smooth-representation-totally-disconnected-group", "algebra-groups/conjugacy-class", "langlands-letter/knowls/semisimple-element-and-class", "langlands/weil-group", "langlands/l-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] of residue characteristic \(p\), let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(E\)-group]], and let
\(\ell\neq p\). After the coefficient and square-root-of-\(q\)
normalizations in Fargues–Scholze theory, every irreducible
[[harmonic-analysis/smooth-representation-totally-disconnected-group|smooth]]
\(\overline{\mathbb Q}_\ell\)-representation \(\pi\) of \(G(E)\) has a
canonically attached [[algebra-groups/conjugacy-class|conjugacy class]] of
continuous
[[langlands-letter/knowls/semisimple-element-and-class|semisimple parameter]]

\[
\varphi_\pi^{\mathrm{FS}}:
W_E\longrightarrow{}^LG(\overline{\mathbb Q}_\ell).
\]

Here \(W_E\) is the [[langlands/weil-group|Weil group]] and \({}^LG\) is
the [[langlands/l-group|\(L\)-group]]. This is the
**Fargues–Scholze parameter map**.

## Construction

The [[langlands/spectral-bernstein-center|spectral Bernstein center]] acts
on the ordinary [[harmonic-analysis/bernstein-center|Bernstein center]]
through local [[langlands/excursion-operator|excursion operators]].
[[algebra-representation-theory/schurs-lemma|Schur's lemma]] evaluates those central operators on an irreducible
representation. The resulting system of invariant scalars reconstructs a
unique semisimple \(L\)-parameter.

## Proven compatibilities

The map agrees with [[langlands/local-class-field-theory|local class field
theory]] for tori and, for
\(\operatorname{GL}_n\), with the semisimplification of the established
[[langlands/local-langlands-correspondence-for-gln|local Langlands
correspondence]]. It is compatible with products,
[[algebra-representation-theory/central-character|central characters]],
twists, [[langlands-letter/knowls/contragredient-representation|contragredients]],
restriction along maps inducing an isomorphism on
adjoint groups, [[algebraic-geometry-foundations/weil-restriction|Weil
restriction]], and
[[harmonic-analysis/normalized-parabolic-induction-p-adic-group|normalized
parabolic induction]] in the
precise formulations of the theorem.

## Exact limitation

The construction is **not** an unconditional full refined local Langlands
correspondence for every \(G\). The parameter is semisimple: it does not in
general recover the
[[langlands/weil-deligne-representation|monodromy operator or the Deligne
\(\operatorname{SL}_2\)]], and it does not prove surjectivity, finite packets,
packet enhancements, endoscopic character identities, or all expected
local factors in full generality.

For \(\operatorname{GL}_n\), compatibility with parabolic induction and the
[[harmonic-analysis/supercuspidal-representation|supercuspidal
correspondence]] identifies it with the usual semisimple
parameter for every irreducible smooth representation.

## Geometric refinement

The parameter map is a decategorified consequence of sheaves on
\(\operatorname{Bun}_G\) and the
[[langlands/spectral-action|spectral action]]. The conjectural categorical
equivalence is designed to recover centralizer representations and hence
refined packet structure beyond the semisimple map.

## References

1. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” Theorem I.9.6 and Chapter IX.
   [arXiv](https://arxiv.org/abs/2102.13459).
2. Naoki Imai, “On the geometrization of the local Langlands
   correspondence,” 2024. [arXiv](https://arxiv.org/abs/2408.16571).
