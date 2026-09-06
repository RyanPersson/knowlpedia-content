+++
id = "langlands-letter/knowls/langlands-functoriality-l-homomorphism"
title = "Langlands functoriality and L-homomorphisms"
kind = "knowl"
summary = "An L-group homomorphism predicting compatible transfer of local parameters and global automorphic representations."
aliases = ["langlands-functoriality-l-homomorphism", "Langlands Functoriality and \\(L\\)-Homomorphisms"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/langlands-functoriality-l-homomorphism.md"
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/local-field", "langlands-letter/knowls/global-local-fields-completions", "langlands/l-group", "langlands/weil-group", "langlands-letter/knowls/langlands-dual-group", "algebra-groups/conjugacy-class"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G'\) and \(G\) be connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive groups]] over a
[[algebra-fields-galois/local-field|local]] or [[langlands-letter/knowls/global-local-fields-completions|global field]] \(F\). An **\(L\)-homomorphism** between their
[[langlands/l-group|\(L\)-groups]] is a map

\[
\omega:{}^LG'\longrightarrow{}^LG
\]

\(\omega\) commutes with the projections to the
[[langlands/weil-group|Weil]] or Galois factor and is algebraic on the
[[langlands-letter/knowls/langlands-dual-group|dual-group]] identity
components. It is considered up to
[[algebra-groups/conjugacy-class|\(\widehat G\)-conjugacy]] and may require
the standard admissibility
conditions.

## Parameter-level statement

The most direct operation is composition:

\[
\varphi'\longmapsto\omega\circ\varphi'.
\]

Locally, functoriality predicts that the
[[langlands/l-packet|\(L\)-packet]] for the
[[langlands/local-l-parameter|local \(L\)-parameter]] \(\varphi'\) transfers
to representations in the packet for \(\omega\circ\varphi'\). For groups
with nontrivial packets this is not naturally a function from one individual
representation to one individual representation without additional data.

## Global transfer

Globally, if \(\pi'\) is an [[langlands/automorphic-representation|automorphic representation]] of \(G'(\mathbb A_F)\),
functoriality predicts an automorphic representation or packet on
\(G(\mathbb A_F)\) whose unramified [[langlands/satake-parameter|Satake parameters]] satisfy

\[
c(\pi_v)\sim\omega(c(\pi_v'))
\]

at almost every place. A complete transfer should also have the expected
ramified and archimedean local behavior.

## L-functions

For \(r:{}^LG\to\operatorname{GL}(V)\), the identity between incomplete
[[langlands-letter/knowls/euler-product-and-local-factor|Euler products]]

\[
L^S(s,\pi,r)
=
L^S(s,\pi',r\circ\omega)
\]

follows formally from matching almost-all unramified parameters. Equality
of incomplete \(L\)-functions alone does not establish the full local or
packet-level transfer.

## Status and methods

General functoriality remains conjectural. Established families arise from
cyclic base change and automorphic induction,
[[langlands/endoscopic-transfer|endoscopic classification]],
theta correspondences, converse theorems,
[[langlands/arthur-selberg-trace-formula|trace-formula comparisons]], and
specific symmetric-power or tensor-product constructions. Endoscopy is a
structured part of functoriality, not the whole principle.

## Relation to the letter

This is the letter's second broad question. Its unramified formulation
already contains the modern parameter-level idea; the later theory adds
local packets, [[langlands/stable-trace-formula|stable trace formulas]], [[langlands/arthur-parameter|Arthur parameters]], and explicit
theorem-status boundaries.

## References

1. Robert P. Langlands, “Problems in the theory of automorphic forms,”
   1970. [IAS copy](https://publications.ias.edu/sites/default/files/problems-in-the-theory-of-automorphic-forms_rpl.pdf).
2. James Arthur, “The principle of functoriality,” 2002.
   [Clay copy](https://www.claymath.org/library/cw/arthur/pdf/57.pdf).
