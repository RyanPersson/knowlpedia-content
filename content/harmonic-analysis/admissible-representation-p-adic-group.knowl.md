+++
id = "harmonic-analysis/admissible-representation-p-adic-group"
title = "Admissible representation of a p-adic group"
kind = "definition"
summary = "A smooth representation whose compact-open fixed spaces are finite-dimensional."
aliases = ["admissible smooth representation", "admissible p-adic representation"]
domains = ["harmonic-analysis", "langlands", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-profinite-group|locally profinite group]]. A
[[harmonic-analysis/smooth-representation-totally-disconnected-group|smooth]]
complex representation \(V\) of \(G\) is **admissible** if

\[
\dim_{\mathbb C}V^K<\infty
\]

for every compact open subgroup \(K\leq G\). For a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
\(\mathbf G\) over a [[langlands-letter/knowls/global-local-fields-completions|nonarchimedean local field]], local Langlands concerns
irreducible admissible representations of \(G=\mathbf G(F)\).

## Why compact-open fixed spaces appear

Each \(V^K\) is a finite-dimensional module over the
[[harmonic-analysis/hecke-algebra-locally-compact-group-pair|Hecke algebra]]
\(\mathcal H(G,K)\). Admissibility is therefore the nonarchimedean analogue of
finite \(K\)-multiplicities for representations of real reductive groups, but
the two definitions live in different representation categories.

## Scope

For reductive \(p\)-adic groups, every irreducible smooth complex
representation is admissible. This theorem uses reductivity and is false for
arbitrary locally profinite groups, so admissibility remains part of the
standard statement of the local correspondence.

## References

1. Joseph Bernstein and Andrei Zelevinsky, “Induced representations of
   reductive \(p\)-adic groups I,” *Annales scientifiques de l’École Normale
   Supérieure* 10 (1977), 441–472.
   [Numdam](https://www.numdam.org/item/ASENS_1977_4_10_4_441_0/).
2. Tasho Kaletha, “Representations of reductive groups over local fields,”
   2022. [arXiv](https://arxiv.org/abs/2201.07741).
