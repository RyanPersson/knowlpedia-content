+++
id = "fiber-bundles/smooth-g-valued-cech-1-cocycle"
title = "Smooth G-valued Čech 1-cocycle"
kind = "definition"
summary = "Smooth transition functions on double overlaps satisfying the identity, inverse, and triple-overlap cocycle laws."
aliases = ["principal bundle Čech cocycle", "nonabelian transition cocycle", "G-valued 1-cocycle"]
domains = ["fiber-bundles", "topology"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/lie-group", "fiber-bundles/cocycle-condition-for-transition-functions"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]], let
\(\mathcal U=\{U_i\}_{i\in I}\) be an open cover, and let \(G\) be a
[[fiber-bundles/lie-group|Lie group]]. A **smooth \(G\)-valued Čech
\(1\)-cocycle** on \(\mathcal U\) is a family of smooth maps

\[
g_{ij}:U_i\cap U_j\longrightarrow G
\]

satisfying

\[
g_{ii}=e,
\qquad
g_{ji}=g_{ij}^{-1},
\qquad
g_{ik}=g_{ij}g_{jk}
\]

on every overlap on which the expressions are defined. The last equality is
the [[fiber-bundles/cocycle-condition-for-transition-functions|cocycle
condition]] on triple intersections.

## From local sections

Choose local sections \(s_i:U_i\to P\) of a
[[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]]. There is a unique
map \(g_{ij}\) on each double overlap such that

\[
s_j(x)=s_i(x)g_{ij}(x).
\]

Associativity of the action gives \(g_{ik}=g_{ij}g_{jk}\). Replacing the local
sections by \(s_i'=s_i h_i\), where \(h_i:U_i\to G\), changes the cocycle by

\[
g_{ij}'=h_i^{-1}g_{ij}h_j.
\]

This is [[fiber-bundles/equivalence-of-cocycles|equivalence of cocycles]], or a
change of local trivialization.

## Gluing a principal bundle

Conversely, a cocycle glues the disjoint union
\(\bigsqcup_i(U_i\times G)\) by

\[
(x,a)_i\sim(x,g_{ij}(x)^{-1}a)_j.
\]

The cocycle law makes this relation transitive. The quotient is a smooth
principal \(G\)-bundle locally trivialized over the \(U_i\). Equivalent
cocycles give isomorphic bundles.

## Abelian and nonabelian behavior

If \(G\) is abelian, cocycles multiply pointwise and form an abelian group. For
general \(G\), pointwise multiplication need not preserve the cocycle law; the
natural classification is therefore a pointed set and, before taking
isomorphism classes, a groupoid. See
[[fiber-bundles/nonabelian-cech-h1-principal-bundles|nonabelian Čech
\(H^1\)]].

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: bundles described by coordinate functions and their equivalence.
2. Jean-Luc Brylinski, *Loop Spaces, Characteristic Classes and Geometric Quantization*, Birkhäuser, 1993. [DOI record](https://doi.org/10.1007/978-0-8176-4731-5). Relevant: Čech cocycles and bundles.
