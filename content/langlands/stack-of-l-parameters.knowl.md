+++
id = "langlands/stack-of-l-parameters"
title = "Stack of local L-parameters"
kind = "knowl"
summary = "The quotient stack of continuous dual-group-valued Weil cocycles by dual-group conjugation."
aliases = ["stack of L-parameters", "moduli stack of Langlands parameters", "spectral parameter stack"]
domains = ["langlands", "algebraic-geometry-foundations", "representation-theory"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "langlands/weil-group", "langlands-letter/knowls/langlands-dual-group", "langlands-letter/knowls/pinned-automorphisms", "algebraic-geometry-foundations/reductive-algebraic-group", "algebraic-geometry-foundations/algebraic-stack", "langlands/l-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]], let \(W_E\) be its [[langlands/weil-group|Weil group]], and let the
[[langlands-letter/knowls/langlands-dual-group|dual group]] \(\widehat G\)
carry the [[langlands-letter/knowls/pinned-automorphisms|pinned]]
\(W_E\)-action determined by a
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(E\)-group]] \(G\). The **stack of local \(L\)-parameters** is the
[[algebraic-geometry-foundations/algebraic-stack|quotient stack]]

\[
\operatorname{LocSys}_{\widehat G}(W_E)
=
[Z^1(W_E,\widehat G)/\widehat G],
\]

where \(Z^1(W_E,\widehat G)\) is the moduli scheme of suitably continuous
\(1\)-cocycles and \(\widehat G\) acts by conjugation.

A cocycle \(\phi\) is equivalently a homomorphism
\(W_E\to{}^LG\) into the [[langlands/l-group|\(L\)-group]] whose projection
to \(W_E\) is the identity.

## Why a stack

The [[algebra-groups/stabilizer|stabilizer]] of a point is the
[[algebra-groups/centralizer|centralizer]]

\[
S_\phi=\operatorname{Cent}_{\widehat G}(\phi).
\]

Keeping this [[algebra-groups/automorphism-group|automorphism group]] is
necessary for [[langlands/component-group-of-l-parameter|packet
enhancements]] and
categorical actions. The coarse conjugacy-class set loses it, and the
invariant-function spectrum can identify nonclosed orbits with their
[[langlands-letter/knowls/semisimple-element-and-class|semisimplifications]].

## Algebraic construction

For \(\ell\neq p\) and a coefficient ring \(\Lambda\), continuity must be
formulated uniformly in families. Fargues–Scholze use condensed
\(1\)-cocycles. The resulting \(Z^1(W_E,\widehat G)\) is a union of open
and closed [[algebraic-geometry-foundations/affine-scheme|affine schemes]] indexed by sufficiently deep wild-inertia
quotients; each finite-depth piece is a flat local complete intersection
under their hypotheses.

## Parameter content

This stack records Weil-group cocycles. In the Fargues–Scholze
semisimplified correspondence it does not retain a separate monodromy
operator or Deligne \(\operatorname{SL}_2\). Thus it should not be
identified without qualification with the moduli of full
[[langlands/weil-deligne-representation|Weil–Deligne parameters]].

## Spectral role

Global functions on the stack form the
[[langlands/spectral-bernstein-center|spectral Bernstein center]], while
[[algebraic-geometry-foundations/perfect-complex|Perfect complexes]] on it
act on sheaves on
\(\operatorname{Bun}_G\) through the
[[langlands/spectral-action|spectral action]].

## References

1. Laurent Fargues and Peter Scholze, “Geometrization of the local Langlands
   correspondence,” Chapters VIII and I.8.
   [arXiv](https://arxiv.org/abs/2102.13459).
2. Jean-François Dat, David Helm, Robert Kurinczuk, and Gilbert Moss,
   “Moduli of Langlands parameters,” 2020.
   [arXiv](https://arxiv.org/abs/2009.06708).
