+++
id = "langlands-letter/knowls/euler-product-and-local-factor"
title = "Euler product and determinant local L-factor"
kind = "definition"
summary = "Unramified and Weil-Deligne local L-factors and their incomplete global Euler product."
aliases = ["euler-product-and-local-factor", "Euler Product and Determinant Local \\(L\\)-Factor"]
domains = ["langlands-letter"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "harmonic-analysis/unramified-representation-p-adic-group", "langlands/satake-parameter", "langlands/l-group", "langlands-letter/knowls/semisimple-element-and-class", "algebra-groups/conjugacy-class", "langlands-letter/knowls/frobenius-unramified"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 1
legacy_source_path = "langlands-letter/knowls/euler-product-and-local-factor.md"
section_mode = "progressive"
+++

Let \(F_v\) be a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] with residue cardinality \(q_v\), let
\(\pi_v\) be
[[harmonic-analysis/unramified-representation-p-adic-group|unramified]] with
[[langlands/satake-parameter|Satake parameter]] \(c(\pi_v)\), and let

\[
r:{}^LG\longrightarrow\operatorname{GL}(V_r)
\]

be a finite-dimensional algebraic representation of the
[[langlands/l-group|\(L\)-group]]. The **unramified local
\(L\)-factor** is

\[
L_v(s,\pi_v,r)
=
\det\!\left(
1-r(c(\pi_v))q_v^{-s}\mid V_r
\right)^{-1}.
\]

It depends only on the
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]]
[[algebra-groups/conjugacy-class|conjugacy class]] and on the chosen
[[langlands-letter/knowls/frobenius-unramified|Frobenius]] and normalization
conventions.

## Euler product

For a [[langlands/automorphic-representation|global automorphic
representation]]
\(\pi=\bigotimes_v'\pi_v\), written as a
[[langlands/restricted-tensor-product-automorphic-representation|restricted
tensor product]], let \(S\) contain the
archimedean places and all places where the data are ramified. The
**incomplete Euler product** is

\[
L^S(s,\pi,r)=\prod_{v\notin S}L_v(s,\pi_v,r).
\]

It converges absolutely in a right half-plane in the standard automorphic
settings. A completed \(L\)-function includes specified ramified factors and
archimedean [[langlands/local-gamma-factor|gamma factors]].

## Ramified Weil-Deligne factor

Suppose the composite of a local parameter with \(r\) gives the
[[langlands/weil-deligne-representation|Weil–Deligne representation]]
\((\rho_{v,r},N_{v,r})\). With
[[langlands-letter/knowls/frobenius-unramified|arithmetic Frobenius]] in the
displayed
formula, one common convention is

\[
L_v(s,\pi_v,r)
=
\det\!\left(
1-q_v^{-s}\rho_{v,r}(\operatorname{Frob}_v)
\;\middle|\;
(\ker N_{v,r})^{I_v}
\right)^{-1}.
\]

Using [[langlands-letter/knowls/frobenius-unramified|geometric Frobenius]]
replaces the operator by its inverse. Different normalizations of
[[langlands/local-langlands-correspondence|local Langlands]] can also insert
a norm twist.

## What the letter could not yet encode

The letter's unramified determinant formula is foundational, but a canonical
ramified factor needs the later Weil–Deligne and local Langlands
formalism. Equality of almost-all unramified factors is weaker than full
local compatibility because it does not recover the
[[algebra-fields-galois/inertia-subgroup|inertia action]] or
[[langlands/weil-deligne-representation|monodromy]].

## References

1. Pierre Deligne, “Les constantes des équations fonctionnelles des
   fonctions \(L\),” in *Modular Functions of One Variable II*, 1973.
2. A. Borel, “Automorphic \(L\)-functions,” Proc. Sympos. Pure Math. 33,
   part 2, 1979.
