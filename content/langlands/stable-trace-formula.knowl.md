+++
id = "langlands/stable-trace-formula"
title = "Stable trace formula"
kind = "knowl"
summary = "The decomposition of the invariant trace formula into stable distributions on a group and its endoscopic groups."
aliases = ["stabilized trace formula", "stabilization of the trace formula", "stable Arthur trace formula"]
domains = ["langlands", "harmonic-analysis", "number-theory"]
prerequisites = ["langlands/arthur-selberg-trace-formula", "langlands/endoscopic-datum", "langlands/endoscopic-transfer", "langlands/stable-distribution", "algebraic-geometry-foundations/levi-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **stable trace formula** is the endoscopic reorganization of the
invariant [[langlands/arthur-selberg-trace-formula|Arthur trace formula]]
into distributions that depend only on stable conjugacy and stable packet
data.

Schematically,

\[
I^G(f)
=
\sum_{\mathfrak e}
\iota(G,\mathfrak e)\,
\widehat S^{H_{\mathfrak e}}(f^{\mathfrak e}),
\]

where \(\mathfrak e\) ranges over elliptic
[[langlands/endoscopic-datum|endoscopic data]], \(f^{\mathfrak e}\) is an
[[langlands/endoscopic-transfer|endoscopic transfer]] of \(f\), and
\(\widehat S^{H_{\mathfrak e}}\) is a
[[langlands/stable-distribution|stable distribution]] for the endoscopic
group. The actual formula includes
[[algebraic-geometry-foundations/levi-subgroup|Levi]], central, and measure
data suppressed here.

## Why stabilization is needed

The invariant trace formula is invariant under conjugating a
[[harmonic-analysis/test-function-space-local-group|test function]],
but its individual geometric terms can distinguish rational conjugacy
classes inside one [[langlands/stable-conjugacy|stable class]]. On the
spectral side, individual characters inside an \(L\)-packet are likewise
unstable.

Fourier analysis on the
[[langlands-letter/knowls/nonabelian-h1-galois-cohomology|cohomological
obstruction groups]] separates these unstable terms into
[[langlands/kappa-orbital-integral|\(\kappa\)-pieces]]. Endoscopic transfer identifies each
piece with a stable distribution on an endoscopic group.

## Inputs

Stabilization uses:

- [[langlands/stable-orbital-integral|stable orbital integrals]];
- [[langlands/endoscopic-datum|endoscopic data]];
- normalized [[langlands/transfer-factor|transfer factors]];
- local and global [[langlands/endoscopic-transfer|transfer]];
- the [[langlands/fundamental-lemma|fundamental lemma]] and its weighted
  variants.

## Status and scope

Arthur developed the stabilization of the general invariant trace formula,
initially conditional on fundamental lemmas that are now theorems in the
required standard settings. Specialized stable formulas may impose
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-splitness]],
[[algebra-representation-theory/central-character|central-character]],
test-function, or characteristic
hypotheses. “The stable trace formula” names this framework and its precise
instances, not one hypothesis-free finite sum.

## Consequences

Stable comparison makes packet characters visible and underlies Arthur's
classification for symplectic and [[lie-groups/orthogonal-group|orthogonal groups]], Mok's classification
for quasi-split unitary groups, and many cases of automorphic transfer.

## References

1. James Arthur, “A stable trace formula III: proof of the main theorems,”
   *Annals of Mathematics* 158 (2003), 769–873.
   [Clay copy](https://www.claymath.org/library/cw/arthur/pdf/55.pdf).
2. James Arthur, “An introduction to the trace formula,” §§27–29.
   [Clay Mathematics Proceedings](https://www.claymath.org/library/cw/arthur/pdf/61.pdf).
