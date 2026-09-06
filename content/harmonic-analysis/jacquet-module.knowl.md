+++
id = "harmonic-analysis/jacquet-module"
title = "Jacquet module"
kind = "definition"
summary = "The unipotent coinvariants of a smooth representation, normalized to be adjoint to parabolic induction."
aliases = ["Jacquet functor", "normalized Jacquet module", "parabolic restriction"]
domains = ["harmonic-analysis", "langlands", "algebra-representation-theory"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "algebraic-geometry-foundations/reductive-algebraic-group", "algebraic-geometry-foundations/parabolic-subgroup", "algebraic-geometry-foundations/levi-subgroup", "algebraic-geometry-foundations/unipotent-radical", "harmonic-analysis/smooth-representation-totally-disconnected-group", "harmonic-analysis/parabolic-modulus-character"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]], let \(G\) be a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]], and write \(P=MN\) for a
[[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]] with
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]] \(M\) and
[[algebraic-geometry-foundations/unipotent-radical|unipotent radical]] \(N\).
For a
[[harmonic-analysis/smooth-representation-totally-disconnected-group|smooth
representation]] \((\pi,V)\) of \(G(F)\), its **unnormalized Jacquet
module** along \(P\) is the \(N(F)\)-coinvariant space

\[
V_N=V/\langle\pi(n)v-v:n\in N(F),\ v\in V\rangle.
\]

It is naturally a smooth representation of \(M(F)\).  The **normalized
Jacquet module** is

\[
r_P^G(V)=\delta_P^{-1/2}\otimes V_N,
\]

where \(\delta_P\) is the
[[harmonic-analysis/parabolic-modulus-character|parabolic modulus character]].

## Adjointness

With compatible normalizations,
[[harmonic-analysis/normalized-parabolic-induction-p-adic-group|normalized
parabolic induction]] \(i_P^G\) is left adjoint to \(r_P^G\).
Bernstein's second adjointness theorem gives \(r_{\overline P}^G\), for the
opposite parabolic \(\overline P\), as a left adjoint to \(i_P^G\).

An irreducible
[[harmonic-analysis/admissible-representation-p-adic-group|admissible
representation]] is
[[harmonic-analysis/supercuspidal-representation|supercuspidal]] exactly when
all of its Jacquet modules for proper parabolic subgroups vanish.

## Exactness

Over complex coefficients the Jacquet functor is exact on smooth
representations of a reductive \(p\)-adic group.  This is substantially
stronger than arbitrary coinvariants and is one reason it is central to the
structure theory of parabolic induction.

## References

1. I. N. Bernstein and A. V. Zelevinsky, “Induced representations of
   reductive \(p\)-adic groups. I,” *Annales scientifiques de l'École Normale
   Supérieure* 10 (1977), 441–472.
   [Numdam](https://www.numdam.org/articles/10.24033/asens.1333/).
2. William Casselman, “Introduction to the theory of admissible
   representations of \(p\)-adic reductive groups,” unpublished notes, §4.
   [UBC](https://personal.math.ubc.ca/~cass/research/pdf/p-adic-book.pdf).
