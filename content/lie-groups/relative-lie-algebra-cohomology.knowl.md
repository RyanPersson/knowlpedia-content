+++
id = "lie-groups/relative-lie-algebra-cohomology"
title = "Relative Lie algebra cohomology"
kind = "definition"
summary = "Cohomology of a Lie algebra relative to a subalgebra, computed by equivariant alternating cochains on the quotient."
aliases = ["(g,K)-cohomology", "relative (g,K)-cohomology", "relative Lie algebra cohomology H(g,K;V)"]
domains = ["lie-groups", "algebra-homological", "langlands"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "lie-groups/lie-subalgebra", "algebra-modules/module", "algebra-homological/cochain-complex"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathfrak g\) be a [[lie-groups/lie-algebra|Lie algebra]], let
\(\mathfrak k\subseteq\mathfrak g\) be a
[[lie-groups/lie-subalgebra|subalgebra]], and let \(V\) be a
[[algebra-modules/module|module]] over \(\mathfrak g\) with a compatible
action of a group \(K\) having Lie algebra \(\mathfrak k\). The following
[[algebra-homological/cochain-complex|cochain complex]] is the **relative Lie
algebra cochain complex**:

\[
C^q(\mathfrak g,K;V)=
\operatorname{Hom}_K
\!\left(\bigwedge^q(\mathfrak g/\mathfrak k),V\right),
\]

with the Chevalley–Eilenberg differential.  Its cohomology is
\(H^q(\mathfrak g,K;V)\), the **relative Lie algebra cohomology** or
**\((\mathfrak g,K)\)-cohomology** of \(V\).

For a disconnected \(K\), using \(K\)-equivariant rather than merely
\(\mathfrak k\)-equivariant cochains retains the component-group action.

## Geometric interpretation

When \(G\) is a real reductive group with
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact
subgroup]] \(K\), the
complex models \(G\)-invariant differential forms on the symmetric space
\(G/K\) with coefficients in the
[[fiber-bundles/local-system|local system]] determined by \(V\).  This
connects representation theory with the cohomology of locally symmetric
spaces.

## Automorphic use

An [[langlands/automorphic-representation|automorphic representation]] is
[[langlands/cohomological-automorphic-representation|cohomological]] when its
archimedean [[lie-groups/harish-chandra-module|Harish–Chandra module]], after
tensoring with a finite-dimensional algebraic coefficient representation, has
nonzero relative Lie algebra cohomology.

## References

1. Armand Borel and Nolan Wallach, *Continuous Cohomology, Discrete
   Subgroups, and Representations of Reductive Groups*, second edition,
   Mathematical Surveys and Monographs 67, AMS, 2000, Chapter I.
2. David A. Vogan Jr. and Gregg J. Zuckerman, “Unitary representations with
   nonzero cohomology,” *Compositio Mathematica* 53 (1984), 51–90.
   [Numdam](https://www.numdam.org/item/CM_1984__53_1_51_0/).
