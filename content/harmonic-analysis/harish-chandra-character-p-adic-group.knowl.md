+++
id = "harmonic-analysis/harish-chandra-character-p-adic-group"
title = "Harish–Chandra character of a p-adic representation"
kind = "theorem"
summary = "The invariant distribution character of an admissible p-adic representation and its regular-semisimple representing function."
aliases = ["p-adic Harish-Chandra character", "distribution character of a p-adic representation", "Harish-Chandra character for p-adic groups"]
domains = ["harmonic-analysis", "langlands"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/nonarchimedean-local-field", "harmonic-analysis/admissible-representation-p-adic-group", "harmonic-analysis/test-function-space-local-group", "harmonic-analysis/distribution-local-group", "harmonic-analysis/haar-measure"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
over a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] \(F\), and let \(\pi\) be an
[[harmonic-analysis/admissible-representation-p-adic-group|admissible
representation]] of \(G(F)\). For a
[[harmonic-analysis/test-function-space-local-group|test function]]
\(f\in C_c^\infty(G(F))\), the operator

\[
\pi(f)=\int_{G(F)} f(g)\pi(g)\,dg
\]

has finite rank.  The **Harish–Chandra distribution character** is

\[
\Theta_\pi(f)=\operatorname{tr}\pi(f).
\]

It is a
[[harmonic-analysis/distribution-local-group|conjugation-invariant
distribution]]—that is, a continuous linear functional on the
nonarchimedean test-function space—and is independent of the chosen
[[harmonic-analysis/haar-measure|Haar measure]] once the test-function measure
convention is fixed.

## Regularity theorem

Harish–Chandra's regularity theorem says that \(\Theta_\pi\) is represented by
a locally integrable conjugation-invariant function on \(G(F)\).  This
function is locally constant on the
[[langlands/strongly-regular-semisimple-element|regular semisimple locus]].
The same symbol
\(\Theta_\pi(g)\) usually denotes that representing function there.

Near singular elements the character has a local expansion in Fourier
transforms of nilpotent
[[langlands/orbital-integral|orbital integrals]]. Thus the distribution is the
primary object; pointwise values are available on the regular set, not on
every element by definition.

## Character identities

[[langlands/endoscopic-transfer|Endoscopic transfer]] and local Langlands often
produce identities between
sums of these characters over an [[langlands/l-packet|L-packet]] and
[[langlands/stable-distribution|stable distributions]] on an endoscopic group.
These are distributional identities and depend on the normalization of
[[langlands/transfer-factor|transfer factors]].

## References

1. Harish-Chandra, “Admissible invariant distributions on reductive
   \(p\)-adic groups,” in *Lie Theories and Their Applications*, Queen's
   Papers in Pure and Applied Mathematics 48, 1978.
2. Stephen DeBacker, “Homogeneity results for invariant distributions of a
   reductive \(p\)-adic group,” *Annales scientifiques de l'École Normale
   Supérieure* 35 (2002), 391–422.
   [Numdam](https://www.numdam.org/item/ASENS_2002_4_35_3_391_0/).
