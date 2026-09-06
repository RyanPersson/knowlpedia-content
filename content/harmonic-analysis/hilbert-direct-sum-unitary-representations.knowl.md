+++
id = "harmonic-analysis/hilbert-direct-sum-unitary-representations"
title = "Hilbert direct sum of unitary representations"
kind = "definition"
summary = "The unitary representation obtained by acting coordinatewise on the Hilbert direct sum of representation spaces."
aliases = ["orthogonal direct sum of representations"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
prerequisites = ["topology/topological-group", "lie-groups/strongly-continuous-unitary-representation", "linear-algebra/hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]], and for each \(i\in I\) let \(\pi_i:G\to\mathcal U(\mathcal H_i)\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] on a complex [[linear-algebra/hilbert-space|Hilbert space]]. Their **Hilbert direct sum** is the representation
\[
\bigoplus_{i\in I}\pi_i:G\longrightarrow
\mathcal U\left(\bigoplus_{i\in I}\mathcal H_i\right)
\]
defined by
\[
\left(\bigoplus_i\pi_i\right)(g)(\xi_i)_i
=\bigl(\pi_i(g)\xi_i\bigr)_i,
\]
where \(\bigoplus_i\mathcal H_i\) consists of families satisfying \(\sum_i\lVert\xi_i\rVert^2<\infty\). The coordinatewise operator is unitary and the resulting representation is strongly continuous.

## Why continuity is preserved

Every vector in the Hilbert sum can be approximated in norm by vectors with finite support. On a finite-support vector, strong continuity follows from that of finitely many summands. Unitarity gives the uniform bound
\[
\left\lVert\left(\bigoplus_i\pi_i\right)(g)\right\rVert=1,
\]
so the finite-support approximation extends continuity to every vector. This argument works for an arbitrary index set; each individual vector has at most countably many nonzero coordinates.

## Examples and decomposition

The sum \(\pi\oplus\sigma\) is the basic two-summand example. Repeating one representation \(n\) times records finite multiplicity, while a countable sum can record infinite multiplicity. Each coordinate space \(\mathcal H_i\) is a closed [[linear-algebra/operator-invariant-subspace|invariant subspace]], and the coordinate projection is an intertwining operator. By contrast, an algebraic direct sum is generally incomplete and is not itself a Hilbert-space representation.

## Conventions and scope

The Hilbert direct sum is a discrete construction. It should not be confused with a direct integral of representations, where summands vary over a [[measure-theory/measure-space|measure space]] and vectors are square-integrable measurable fields. No countability assumption on \(I\) is required for the definition, although separability of the sum imposes restrictions on the nonzero summands.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.1 on unitary representations and direct sums.
