+++
id = "langlands-letter/knowls/ideles-artin-reciprocity-hecke-character"
title = "Ideles, Hecke Characters, and Artin Reciprocity"
kind = "knowl"
summary = "The idele class group, its Hecke characters, and its relation to abelian Galois theory through Artin reciprocity."
aliases = ["ideles-artin-reciprocity-hecke-character", "Ideles, Hecke Characters, and Artin Reciprocity"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/ideles-artin-reciprocity-hecke-character.md"
+++

For a number field \(K\), the **idele group** is
\[
\mathbb I_K:=\prod_v' K_v^\times,
\]
the restricted product with respect to \(\mathcal O_v^\times\) at finite places \(v\). The **idele class group** is \(C_K:=K^\times\backslash\mathbb I_K\).

A **Hecke character** (Grössencharakter) is a continuous homomorphism \(\chi:C_K\to\mathbb C^\times\). Its Hecke \(L\)-function is given, in its half-plane of absolute convergence, by the Euler product \(L(s,\chi)=\prod_v L_v(s,\chi_v)\).

**Artin reciprocity** gives a continuous surjection
\[
C_K\longrightarrow \operatorname{Gal}(K^{\mathrm{ab}}/K)
\]
whose kernel is the identity component of \(C_K\). Thus the profinite completion of \(C_K\) is canonically isomorphic to \(\operatorname{Gal}(K^{\mathrm{ab}}/K)\), subject to the chosen arithmetic or geometric Frobenius normalization.

## Remarks

In the letter, this realizes abelian Artin \(L\)-series as \(L\)-series of Hecke characters (example (iii)).
