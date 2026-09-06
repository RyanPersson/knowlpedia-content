+++
id = "langlands/tate-nakayama-duality"
title = "Tate–Nakayama duality"
kind = "theorem"
summary = "Duality identifying Galois cohomology of a local torus with characters of the component group of its dual torus."
aliases = ["Tate-Nakayama duality", "local Tate–Nakayama pairing", "Tate-Nakayama pairing"]
domains = ["langlands", "algebra-fields-galois", "algebra-homological"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "langlands-letter/knowls/langlands-dual-group", "langlands-letter/knowls/galois-extension-and-group", "langlands-letter/knowls/nonabelian-h1-galois-cohomology", "algebra-groups/abelian-group", "topology/connected-component"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) be a [[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]], let
\(T\) be an \(F\)-torus, and let \(\widehat T\) be its complex
[[langlands-letter/knowls/langlands-dual-group|dual torus]] with
[[langlands-letter/knowls/galois-extension-and-group|Galois action]]. **Local
Tate–Nakayama duality** gives a canonical perfect pairing

\[
H^1(F,T)\times\pi_0(\widehat T^{\Gamma_F})
\longrightarrow\mathbb Q/\mathbb Z.
\]

Equivalently,

\[
H^1(F,T)\simeq
\operatorname{Hom}\!\left(
\pi_0(\widehat T^{\Gamma_F}),\mathbb Q/\mathbb Z
\right).
\]

Here \(H^1(F,T)\) is
[[langlands-letter/knowls/nonabelian-h1-galois-cohomology|Galois cohomology]]
(an [[algebra-groups/abelian-group|abelian group]] in this torus case), and
\(\pi_0(\widehat T^{\Gamma_F})\) is the
[[topology/connected-component|component group]] of the fixed-point subgroup
of the dual torus.

## Cohomological origin

For a finite Galois splitting extension \(L/F\), cup product with the local
fundamental class relates Tate cohomology of the
[[langlands-letter/knowls/maximal-torus-weight-lattice|character lattice]] to
Tate cohomology of \(L^\times\). Passing through the
character/cocharacter duality
of \(T\) yields the displayed pairing.  Archimedean and global versions have
modified targets and exact sequences.

## Use in endoscopy

The pairing turns the set of rational
[[algebra-groups/conjugacy-class|conjugacy classes]] inside a
[[langlands/stable-conjugacy|stable conjugacy class]] into a finite Fourier
space.  Characters on that space define
[[langlands/kappa-orbital-integral|kappa orbital integrals]] and appear in the
normalization of [[langlands/endoscopic-transfer|endoscopic transfer]].

## References

1. John Tate, “The cohomology groups \(H^i(G,S)\),” in *Algebraic Number
   Theory*, Academic Press, 1967, 257–268.
2. Robert E. Kottwitz, “Stable trace formula: elliptic singular terms,”
   *Mathematische Annalen* 275 (1986), 365–399.
