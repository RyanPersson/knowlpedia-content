+++
id = "langlands/local-class-field-theory"
title = "Local class field theory"
kind = "theorem"
summary = "The reciprocity isomorphism between a local field's multiplicative group and the abelianization of its Weil group."
aliases = ["local reciprocity", "local Artin reciprocity", "local reciprocity map"]
domains = ["langlands", "algebra-fields-galois", "number-theory"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "langlands/weil-group", "langlands-letter/knowls/galois-extension-and-group", "langlands-letter/knowls/frobenius-unramified", "algebra-commutative/dvr", "algebra-fields-galois/inertia-subgroup", "langlands-letter/knowls/euler-product-and-local-factor"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] \(F\),
**local class field theory** supplies a canonical topological isomorphism

\[
\operatorname{rec}_F:F^\times\xrightarrow{\sim}W_F^{\mathrm{ab}},
\]

where \(W_F\) is the [[langlands/weil-group|Weil group]].  Equivalently, after
profinite completion it identifies
\(\widehat{F^\times}\) with the abelianization of the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
\(G_F^{\mathrm{ab}}\).

This page uses the
**[[langlands-letter/knowls/frobenius-unramified|geometric Frobenius
normalization]]**: a [[algebra-commutative/dvr|uniformizer]] maps to geometric
Frobenius in \(W_F/I_F\), where \(I_F\) is the
[[algebra-fields-galois/inertia-subgroup|inertia subgroup]]. Authors using
arithmetic Frobenius take the inverse reciprocity map, so the normalization
must be checked in formulas for
[[langlands-letter/knowls/euler-product-and-local-factor|local factors]].

## Finite extensions

For every finite abelian extension \(L/F\), reciprocity induces

\[
F^\times/N_{L/F}(L^\times)
\xrightarrow{\sim}\operatorname{Gal}(L/F).
\]

Under this isomorphism open finite-index subgroups of \(F^\times\) correspond
to finite abelian extensions of \(F\).  Norm subgroups, ramification groups,
and unit filtrations are thereby translated into Galois-theoretic data.

## Langlands interpretation

For \(G=\operatorname{GL}_1\), local class field theory is the local Langlands
correspondence: continuous
[[algebra-representation-theory/character|characters]] of \(F^\times\)
correspond to
one-dimensional representations of \(W_F\).  It is the abelian prototype for
[[langlands/local-langlands-correspondence|local Langlands]].  Its global
compatibility is recorded by
[[langlands-letter/knowls/ideles-artin-reciprocity-hecke-character|global Artin
reciprocity]].

## References

1. John Tate, “Number theoretic background,” in *Automorphic Forms,
   Representations and L-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 2, 1979.
2. Jean-Pierre Serre, *Local Fields*, Graduate Texts in Mathematics 67,
   Springer, 1979, Chapters XIII–XV.
