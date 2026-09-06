+++
id = "langlands/arthur-parameter"
title = "Arthur parameter"
kind = "knowl"
summary = "A bounded Langlands parameter enlarged by an additional algebraic SL2 factor."
aliases = ["A-parameter", "local Arthur parameter", "global Arthur parameter"]
domains = ["langlands", "representation-theory", "number-theory"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/local-field", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands/local-l-parameter", "algebra-groups/center-of-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(F\) be a
[[algebra-fields-galois/local-field|local field]] and
\(G\) a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]]. A **local Arthur parameter** is an admissible
[[langlands/local-l-parameter|\(L\)-homomorphism]]

\[
\psi:L_F\times\operatorname{SL}_2(\mathbb C)
\longrightarrow {}^L G
\]

such that the restriction to \(L_F\) is bounded modulo the
[[algebra-groups/center-of-group|center]] and the
restriction to the displayed \(\operatorname{SL}_2(\mathbb C)\) is
algebraic. Parameters are considered up to \(\widehat G\)-conjugacy.

## Two SL2 factors at a nonarchimedean place

If the [[langlands/weil-deligne-group|local Langlands group]] is written

\[
L_F=W_F\times\operatorname{SL}_2(\mathbb C),
\]

then an Arthur parameter has **two** \(\operatorname{SL}_2\)-factors: the
Deligne factor already present in \(L_F\) and the additional Arthur factor.
The latter records controlled nontemperedness.

## Associated Langlands parameter

An Arthur parameter gives an ordinary local parameter by inserting the norm
cocharacter into the Arthur factor:

\[
\varphi_\psi(w)
=
\psi\!\left(
w,
\begin{pmatrix}
|w|^{1/2}&0\\
0&|w|^{-1/2}
\end{pmatrix}
\right),
\]

with the evident extension over the Deligne factor and with \(|w|\)
depending on the stated reciprocity convention. If the Arthur
\(\operatorname{SL}_2\) is trivial, the associated parameter is tempered;
for nonarchimedean \(F\), this is the parameter-side condition corresponding
to a [[harmonic-analysis/tempered-representation-p-adic-group|tempered
representation]].

## Global form

A general [[langlands/global-langlands-parameter|global Langlands group]] is
conjectural over
[[algebra-fields-galois/number-field|number fields]]. In the
classification of classical groups, global Arthur parameters are therefore
encoded concretely as formal
[[langlands/isobaric-automorphic-representation|isobaric sums]]

\[
\psi=\boxplus_i\,\pi_i[d_i],
\]

where the \(\pi_i\) are suitable self-dual
[[langlands/cuspidal-automorphic-representation|cuspidal automorphic
representations]] of general linear groups and \([d_i]\) denotes the
\(d_i\)-dimensional [[algebra-representation-theory/irreducible-representation|irreducible representation]] of
\(\operatorname{SL}_2(\mathbb C)\), subject to dimension, parity, and
ellipticity conditions.

## Role

The parameter determines an [[langlands/a-packet|\(A\)-packet]] and a
component group. A global character of that component group enters the
[[langlands/arthur-multiplicity-formula|Arthur multiplicity formula]].
This formalism captures both cuspidal and
[[langlands/residual-automorphic-spectrum|residual]] discrete automorphic
representations.

## Status

Arthur parameters and packets are theorems for major classical families,
including Arthur's symplectic and orthogonal classification and Mok's
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split]]
unitary classification. Their expected general form for every
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] remains conjectural.

## References

1. James Arthur, *The Endoscopic Classification of Representations:
   Orthogonal and Symplectic Groups*, AMS Colloquium Publications 61, 2013.
   [AMS](https://bookstore.ams.org/COLL/61).
2. James Arthur, “Unipotent automorphic representations: conjectures,”
   *Astérisque* 171–172 (1989), 13–71.
   [Numdam](https://www.numdam.org/item/AST_1989__171-172__13_0/).
