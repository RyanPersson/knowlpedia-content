+++
id = "harmonic-analysis/supercuspidal-representation"
title = "Supercuspidal representation"
kind = "definition"
summary = "An irreducible admissible p-adic representation with no contribution from a proper parabolic subgroup."
aliases = ["supercuspidal representation of a reductive p-adic group", "supercuspidal"]
domains = ["harmonic-analysis", "langlands", "lie-groups"]
section_mode = "progressive"
+++

Let \(G=\mathbf G(F)\) for a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]]. An irreducible
[[harmonic-analysis/admissible-representation-p-adic-group|admissible smooth
representation]] \(\pi\) of \(G\) is **supercuspidal** if its
[[harmonic-analysis/jacquet-module|Jacquet module]]
along every proper [[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]] of \(\mathbf G\) is zero. Equivalently,
\(\pi\) is not a subquotient of parabolic induction from a proper
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]].

## Matrix-coefficient criterion

After fixing a [[algebra-representation-theory/central-character|central
character]], \(\pi\) is supercuspidal exactly when its
[[harmonic-analysis/coefficient-function|matrix coefficients]] are compactly supported modulo the center of \(G\). This
criterion explains the term “cuspidal”: proper parabolic constant terms
vanish.

## Position in the classification

Supercuspidal representations are the primitive inputs for the
[[harmonic-analysis/bernstein-decomposition|Bernstein decomposition]] and the
[[harmonic-analysis/langlands-classification-p-adic-group|p-adic Langlands
classification]]. [[harmonic-analysis/normalized-parabolic-induction-p-adic-group|Parabolic induction]] from supercuspidal
representations of Levi subgroups generates every irreducible smooth
representation through subquotients, but a supercuspidal representation
itself does not arise from a proper Levi.

Every supercuspidal representation is
[[lie-groups/square-integrable-modulo-center-representation|square-integrable
modulo the center]], but
not every essentially discrete-series representation is supercuspidal.

## Parameter-side warning

A “supercuspidal [[langlands/local-l-parameter|Langlands parameter]]” is usually a discrete parameter with
trivial Deligne monodromy. The assertion that it corresponds precisely to
supercuspidal representations is part of the local correspondence and needs
hypotheses; it is not the definition above.

## References

1. Colin J. Bushnell and Guy Henniart, *The Local Langlands Conjecture for
   \(\mathrm{GL}(2)\)*, Springer, 2006, Chapter 1.
   [DOI](https://doi.org/10.1007/3-540-31511-X).
2. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §1.2, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
