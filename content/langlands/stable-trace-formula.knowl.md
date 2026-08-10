+++
id = "langlands/stable-trace-formula"
title = "Stable trace formula"
kind = "knowl"
summary = "The decomposition of the invariant trace formula into stable distributions on a group and its endoscopic groups."
aliases = ["stabilized trace formula", "stabilization of the trace formula", "stable Arthur trace formula"]
domains = ["langlands", "harmonic-analysis", "number-theory"]
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

where \(\mathfrak e\) ranges over elliptic endoscopic data,
\(f^{\mathfrak e}\) is an endoscopic transfer of \(f\), and
\(\widehat S^{H_{\mathfrak e}}\) is a stable distribution for the
endoscopic group. The actual formula includes Levi, central, and measure
data suppressed here.

## Why stabilization is needed

The invariant trace formula is invariant under conjugating a [[functional-analysis/test-function-space|test function]],
but its individual geometric terms can distinguish rational conjugacy
classes inside one [[langlands/stable-conjugacy|stable class]]. On the
spectral side, individual characters inside an \(L\)-packet are likewise
unstable.

Fourier analysis on the cohomological obstruction groups separates these
unstable terms into \(\kappa\)-pieces. Endoscopic transfer identifies each
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
quasi-splitness, central-character, test-function, or characteristic
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
