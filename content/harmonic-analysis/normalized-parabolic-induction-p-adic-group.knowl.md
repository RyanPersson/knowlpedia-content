+++
id = "harmonic-analysis/normalized-parabolic-induction-p-adic-group"
title = "Normalized parabolic induction for a p-adic group"
kind = "definition"
summary = "Smooth parabolic induction with the half-modulus normalization."
aliases = ["normalized p-adic parabolic induction", "unitary parabolic induction for p-adic groups"]
domains = ["harmonic-analysis", "langlands", "lie-groups"]
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/nonarchimedean-local-field", "algebraic-geometry-foundations/parabolic-subgroup", "algebraic-geometry-foundations/levi-subgroup", "algebraic-geometry-foundations/unipotent-radical", "harmonic-analysis/smooth-representation-totally-disconnected-group", "harmonic-analysis/parabolic-modulus-character"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G=\mathbf G(F)\) for a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]], let \(P=MN\) be a
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]] with
[[algebraic-geometry-foundations/levi-subgroup|Levi factor]] \(M\) and
[[algebraic-geometry-foundations/unipotent-radical|unipotent radical]] \(N\),
and let \(\sigma\) be a
[[harmonic-analysis/smooth-representation-totally-disconnected-group|smooth
representation]] of \(M\), inflated across \(N\).
The **normalized parabolic induction** is

\[
i_P^G(\sigma)=\operatorname{Ind}_P^G
\bigl(\delta_P^{1/2}\otimes\sigma\bigr),
\]

where \(\delta_P\) is the
[[harmonic-analysis/parabolic-modulus-character|parabolic modulus character]].
The half-modulus factor makes induction carry unitary
representations to unitary representations.

## Function model

In the right-equivariant convention, the representation consists of locally
constant functions \(f:G\to V_\sigma\), with the usual support condition
modulo \(P\), satisfying

\[
f(gmn)=\delta_P(m)^{-1/2}\sigma(m)^{-1}f(g).
\]

The group \(G\) acts by [[lie-groups/left-translation|left translation]].

## Role in the Langlands classification

The [[harmonic-analysis/langlands-classification-p-adic-group|p-adic Langlands
classification]] says that every irreducible admissible representation is the
unique irreducible quotient of \(i_P^G(\tau\otimes\chi)\) for suitable
[[harmonic-analysis/tempered-representation-p-adic-group|tempered]]
\(\tau\) on a Levi subgroup
and a character \(\chi\) in a positive chamber. [[harmonic-analysis/supercuspidal-representation|Supercuspidal representations]]
provide the primitive inducing data further down the classification.

## Convention warning

Some authors build the factor \(\delta_P^{1/2}\) into the symbol
\(\operatorname{Ind}\), while others call that functor unnormalized induction.
Left-versus-right equivariance also reverses the displayed power. The invariant
content is the half-density correction.

## References

1. Joseph Bernstein and Andrei Zelevinsky, “Induced representations of
   reductive \(p\)-adic groups I,” *Annales scientifiques de l’École Normale
   Supérieure* 10 (1977), 441–472.
   [Numdam](https://www.numdam.org/item/ASENS_1977_4_10_4_441_0/).
2. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §1, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
