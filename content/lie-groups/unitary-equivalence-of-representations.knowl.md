+++
id = "lie-groups/unitary-equivalence-of-representations"
title = "Unitary equivalence of representations"
kind = "definition"
summary = "Two unitary representations are unitarily equivalent when a unitary operator intertwines their actions."
aliases = ["equivalent unitary representations"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(\pi_1:G\to U(H_1)\) and \(\pi_2:G\to U(H_2)\) be
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representations]]
of the same
[[topology/topological-group|topological group]]. They are
**unitarily equivalent** if there is a [[functional-analysis/unitary-operator|unitary operator]]
\(U:H_1\to H_2\) such that
\[
U\pi_1(g)=\pi_2(g)U\qquad\text{for every }g\in G.
\]
Thus a unitary equivalence is an invertible
[[lie-groups/intertwining-operator-unitary-representations|intertwining
operator]]
that also preserves
[[linear-algebra/inner-product|inner products]]. It identifies the two actions
after an isometric change of Hilbert-space coordinates, rather than asserting
that their operators are literally equal on one fixed space.

## Invariants

A unitary equivalence carries closed invariant subspaces of \(H_1\) to closed
invariant subspaces of \(H_2\). It therefore preserves irreducibility,
orthogonal direct-sum decompositions, multiplicities, and
[[harmonic-analysis/coefficient-function|coefficient functions]] after vectors
are transported by \(U\). The integrated representations also have the same
[[linear-algebra/operator-norm|operator norms]] and corresponding kernels.

## Equivalence relation and classes

Identity operators, adjoints, and compositions show that unitary equivalence
is an [[shared-foundations/equivalence-relation|equivalence relation]].
Representation theory normally classifies
unitary representations up to this relation. In particular, the
[[harmonic-analysis/unitary-dual|unitary dual]]
of a [[topology/locally-compact-group|locally compact group]] consists of
unitary-equivalence classes of
[[lie-groups/irreducible-unitary-representation|irreducible unitary representations]]; see
[Folland, §3.1](https://doi.org/10.1201/B19172).

## Conventions and scope

For unitary representations, a bounded invertible intertwiner does imply
unitary equivalence: the unitary factor in its polar decomposition still
intertwines the actions. The original intertwiner itself need not be unitary.
Equality of characters or of selected coefficient functions does not, without
an appropriate classification theorem, constitute the definition of unitary
equivalence.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.1 on unitary representations, intertwiners, and equivalence.
