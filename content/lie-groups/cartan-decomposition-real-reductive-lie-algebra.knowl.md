+++
id = "lie-groups/cartan-decomposition-real-reductive-lie-algebra"
title = "Cartan decomposition of a real reductive Lie algebra"
kind = "definition"
summary = "The decomposition of a real reductive Lie algebra into the two eigenspaces of a Cartan involution."
aliases = ["k plus p decomposition", "infinitesimal Cartan decomposition"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Given a [[lie-groups/cartan-involution-real-lie-algebra|Cartan involution]]
\(\theta\) of a [[lie-groups/reductive-lie-algebra|real reductive Lie
algebra]] \(\mathfrak g\), its **Cartan decomposition** is the vector-space
direct sum
\[
\mathfrak g=\mathfrak k\oplus\mathfrak p,\qquad
\mathfrak k=\ker(\theta-1),\quad \mathfrak p=\ker(\theta+1).
\]
Because \(\theta\) is a [[lie-groups/lie-algebra-automorphism|Lie algebra automorphism]], the brackets satisfy
\[
[\mathfrak k,\mathfrak k]\subseteq\mathfrak k,\qquad
[\mathfrak k,\mathfrak p]\subseteq\mathfrak p,\qquad
[\mathfrak p,\mathfrak p]\subseteq\mathfrak k.
\]
Thus \(\mathfrak k\) is a [[lie-groups/lie-subalgebra|Lie subalgebra]], whereas \(\mathfrak p\) is generally
not. The decomposition is orthogonal for the positive inner product associated
with \(\theta\).

## Compact and noncompact directions

The subalgebra \(\mathfrak k\) is maximally compactly embedded and integrates,
under the usual group hypotheses, to a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact
subgroup]] \(K\). The space \(\mathfrak p\) models the tangent space at the
base point of the homogeneous space \(G/K\). The bracket inclusions are the
infinitesimal algebraic signature of its symmetric-space geometry
[Helgason, Chapter V](https://doi.org/10.1090/gsm/034).

## Example

For \(\mathfrak g=\mathfrak{gl}_n(\mathbb R)\) and
\(\theta(X)=-X^{\mathsf T}\),
\[
\mathfrak k=\mathfrak{so}(n),\qquad
\mathfrak p=\{X:X^{\mathsf T}=X\}.
\]
Exponentiating \(\mathfrak p\) produces the positive-definite symmetric
matrices. The resulting group-level statement is the familiar polar
decomposition and is a model for the
[[lie-groups/global-cartan-decomposition|global Cartan decomposition]].

## Terminological distinction

This \( \mathfrak k\oplus\mathfrak p\) decomposition should not be confused
with a root-space decomposition relative to a Cartan subalgebra. A maximal
abelian subspace \(\mathfrak a\subseteq\mathfrak p\) instead gives the
[[lie-groups/restricted-root-system|restricted root system]], which records
how the noncompact directions decompose under \(\operatorname{ad}\mathfrak a\).

## References

1. A. W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002. [Publisher record](https://link.springer.com/book/9780817642594). Relevant: Chapter VI, §2.
2. S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, American Mathematical Society, 2001. [DOI record](https://doi.org/10.1090/gsm/034). Relevant: Chapter V on symmetric decompositions.
