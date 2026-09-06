+++
id = "langlands/weil-deligne-group"
title = "Weil–Deligne group"
kind = "definition"
summary = "The local Weil group augmented by monodromy, presented either with an additive factor or an auxiliary SL_2."
aliases = ["Weil-Deligne group", "local Langlands group", "W_F prime"]
domains = ["langlands", "algebra-fields-galois"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "algebraic-geometry-foundations/group-scheme", "langlands/weil-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]]. The **Weil–Deligne group** is the
semidirect-product [[algebraic-geometry-foundations/group-scheme|group scheme]]

\[
W'_F=W_F\ltimes\mathbb G_a,
\qquad
w x w^{-1}=|w|_F x,
\]

where \(W_F\) is the [[langlands/weil-group|Weil group]] and
\(|\cdot|_F\) is normalized using geometric Frobenius. A finite-dimensional
representation of \(W'_F\) is equivalently a
[[langlands/weil-deligne-representation|Weil–Deligne representation]]
\((r,N)\).

## The \(W_F\times\mathrm{SL}_2\) presentation

For complex [[langlands/local-l-parameter|Langlands parameters]] one often writes the local Langlands group as

\[
L_F=W_F\times\mathrm{SL}_2(\mathbb C).
\]

An algebraic action of \(\mathrm{SL}_2(\mathbb C)\) packages the nilpotent
monodromy operator \(N\). Passing between the two presentations includes a
standard \(|w|_F^{1/2}\)-twist, so the associated Weil action is not obtained by
merely restricting a parameter to \(W_F\).

## Scope

For \(F=\mathbb R\) or \(\mathbb C\), local Langlands parameters use the
archimedean Weil group itself; the auxiliary \(\mathrm{SL}_2\) factor is a
nonarchimedean feature. [[langlands/arthur-parameter|Arthur parameters]] introduce a different
\(\mathrm{SL}_2\) factor and must not be conflated with Deligne monodromy.

## References

1. Pierre Deligne, “Les constantes des équations fonctionnelles des fonctions
   \(L\),” in *Modular Functions of One Variable II*, Lecture Notes in
   Mathematics 349, 1973. [DOI](https://doi.org/10.1007/BFb0067048).
2. Jayce R. Getz, *An Introduction to Automorphic Representations*, §10.2.
   [Author notes](https://sites.math.duke.edu/~jgetz/aut_reps.pdf).
