+++
id = "langlands-letter/knowls/ideles-artin-reciprocity-hecke-character"
title = "Ideles, Hecke characters, and Artin reciprocity"
kind = "knowl"
summary = "The idele class group, its continuous quasicharacters, and the global reciprocity map to the abelianized Galois group."
aliases = ["ideles-artin-reciprocity-hecke-character", "Ideles, Hecke Characters, and Artin Reciprocity"]
domains = ["langlands-letter"]
prerequisites = ["algebra-fields-galois/number-field", "langlands-letter/knowls/adeles-restricted-product", "algebra-representation-theory/character"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "langlands-letter/knowls/ideles-artin-reciprocity-hecke-character.md"
section_mode = "progressive"
+++

Let \(F\) be a
[[algebra-fields-galois/number-field|number field]].
Its **idele group** is the
[[langlands-letter/knowls/adeles-restricted-product|restricted product]]

\[
\mathbb A_F^\times
=
\prod_v'F_v^\times
\]

with respect to \(\mathcal O_v^\times\) at the finite places, and its
**idele class group** is

\[
C_F=F^\times\backslash\mathbb A_F^\times.
\]

A **Hecke character** or Grössencharakter is a continuous
[[algebra-representation-theory/character|quasicharacter]]
\(\chi:C_F\to\mathbb C^\times\).

## Hecke L-function

Writing \(\chi=\bigotimes_v'\chi_v\) as a restricted tensor product, the
Hecke [[langlands-letter/knowls/euler-product-and-local-factor|\(L\)-function]]
has local
factors. At an unramified finite place,

\[
L_v(s,\chi_v)
=
\left(1-\chi_v(\varpi_v)q_v^{-s}\right)^{-1},
\]

with the inverse altered if the
[[langlands/local-class-field-theory|local reciprocity map]] uses the
opposite [[langlands-letter/knowls/frobenius-unramified|Frobenius
convention]].

## Artin reciprocity

Global class field theory supplies a continuous reciprocity map

\[
\operatorname{Art}_F:C_F
\longrightarrow
\operatorname{Gal}(F^{\mathrm{ab}}/F).
\]

For a number field it is surjective with kernel the identity component
\(C_F^\circ\), so it induces an isomorphism from the profinite completion of
\(C_F\) to the abelianized
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]].
Some authors send a local [[algebra-commutative/dvr|uniformizer]] to
arithmetic Frobenius and others to geometric Frobenius.

Finite-order Hecke characters therefore correspond to finite-order
one-dimensional Galois characters. Algebraic Hecke characters give
[[langlands/compatible-system-of-galois-representations|compatible
one-dimensional \(\ell\)-adic characters]] after choosing
coefficient embeddings.

## Modern placement

This is the \(G=\operatorname{GL}_1\) case of
[[langlands/global-langlands-reciprocity|global Langlands reciprocity]].
Packets are singletons, and the nonabelian complications of endoscopy and
multiplicity do not appear.

## Relation to the letter

The letter uses reciprocity to reinterpret abelian Artin \(L\)-series as
Hecke \(L\)-series. Its proposed nonabelian correspondences generalize this
local-to-global pattern rather than the group structure of \(C_F\) itself.

## References

1. John Tate, “Fourier analysis in number fields and Hecke's zeta
   functions,” in *Algebraic Number Theory*, 1967.
2. Jürgen Neukirch, *Class Field Theory*, Springer, 1986.
