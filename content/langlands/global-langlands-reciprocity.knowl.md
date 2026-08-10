+++
id = "langlands/global-langlands-reciprocity"
title = "Global Langlands reciprocity"
kind = "knowl"
summary = "The conjectural relation between global arithmetic parameters and automorphic representations."
aliases = ["global Langlands correspondence", "Langlands reciprocity conjecture", "nonabelian reciprocity"]
domains = ["langlands", "number-theory", "representation-theory"]
section_mode = "progressive"
+++

**Global Langlands reciprocity** is the conjectural principle that arithmetic
[[langlands/global-langlands-parameter|global Langlands parameters]] for a
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
\(G\) organize
[[langlands/automorphic-representation|automorphic representations]] of
\(G(\mathbb A_F)\), with compatible
localizations, \(L\)-functions, and multiplicities.

It is a program of correspondences rather than one unconditional bijection.

## Abelian case

For \(G=\operatorname{GL}_1\), global class field theory identifies
characters of the idèle class group

\[
F^\times\backslash\mathbb A_F^\times
\]

with one-dimensional representations of the abelianized global [[algebra-fields-galois/galois-group|Galois group]],
subject to the chosen reciprocity and Frobenius normalization. This is the
abelian model for the general principle.

## General linear groups

For \(\operatorname{GL}_n\), the expected primitive correspondence relates
[[langlands/cuspidal-automorphic-representation|cuspidal automorphic representations]] to irreducible \(n\)-dimensional global
parameters. Over number fields this includes several different coefficient
realizations and is known only in important families. Over global function
fields, Drinfeld and Laurent Lafforgue proved the correspondence for
\(\operatorname{GL}_n\), and Vincent Lafforgue constructed a broad
automorphic-to-Galois parameterization for reductive groups.

## General reductive groups

For a general \(G\), a parameter determines local packets rather than a
single representation. A global packet is assembled from local members, and
a multiplicity formula selects which restricted tensor products occur in the
[[langlands/discrete-automorphic-spectrum|discrete spectrum]]. Endoscopy and
[[langlands/arthur-parameter|Arthur parameters]] refine this statement.

## Required compatibilities

The conjecture includes more than matching sets. It should preserve:

- localization at every place;
- unramified [[langlands/satake-parameter|Satake parameters]];
- global and local \(L\)- and \(\varepsilon\)-factors;
- central characters and duality;
- functorial transfer under homomorphisms of \(L\)-groups.

A result proving only one direction or only equality of almost-all
unramified parameters should be named accordingly.

## References

1. Robert P. Langlands, “Problems in the theory of automorphic forms,” in
   *Lectures in Modern Analysis and Applications III*, 1970.
   [IAS copy](https://publications.ias.edu/sites/default/files/problems-in-the-theory-of-automorphic-forms_rpl.pdf).
2. Laurent Lafforgue, “Chtoucas de Drinfeld et correspondance de Langlands,”
   *Inventiones Mathematicae* 147 (2002), 1–241.
   [DOI](https://doi.org/10.1007/s002220100174).
3. Vincent Lafforgue, “Chtoucas pour les groupes réductifs et paramétrisation
   de Langlands globale,” *JAMS* 31 (2018), 719–891.
   [arXiv](https://arxiv.org/abs/1209.5352).
