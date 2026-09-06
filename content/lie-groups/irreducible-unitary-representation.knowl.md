+++
id = "lie-groups/irreducible-unitary-representation"
title = "Irreducible unitary representation"
kind = "definition"
summary = "An irreducible unitary representation has no nonzero proper closed invariant subspace."
aliases = ["topologically irreducible representation", "irreducible Hilbert representation"]
domains = ["lie-groups", "harmonic-analysis"]
prerequisites = ["lie-groups/strongly-continuous-unitary-representation", "linear-algebra/hilbert-space", "lie-groups/invariant-closed-subspace-unitary-representation", "linear-algebra/orthogonal-complement"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\pi:G\to U(H)\) be a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representation]]
on a nonzero
[[linear-algebra/hilbert-space|Hilbert space]]. It is **irreducible** if its
only [[lie-groups/invariant-closed-subspace-unitary-representation|closed
invariant subspaces]]
are \(\{0\}\) and \(H\). Closedness is essential in
infinite-dimensional Hilbert spaces: the definition is topological, not
purely algebraic. Because every \(\pi(g)\) is unitary and
\(\pi(g)^{-1}=\pi(g^{-1})\), a closed invariant subspace is automatically
reducing, so its [[linear-algebra/orthogonal-complement|orthogonal complement]]
is invariant as well.

## Commutant characterization

The representation is irreducible if and only if every bounded operator
\(T\) satisfying \(T\pi(g)=\pi(g)T\) for all \(g\in G\) is a scalar multiple
of the identity. Equivalently, the [[operator-algebras/commutant|commutant]] of
\(\pi(G)\) is \(\mathbb C I\). This is the unitary form of
[[algebra-representation-theory/schurs-lemma|Schur's lemma]]. A nontrivial
invariant subspace yields a nonscalar commuting
[[linear-algebra/orthogonal-projection|orthogonal projection]], while
the spectral projections of a nonscalar self-adjoint operator in the
commutant recover a nontrivial invariant subspace.

## Examples and reducible cases

Every one-dimensional unitary representation is irreducible. The trivial
representation on \(\mathbb C\) is the simplest example. A nontrivial
orthogonal direct sum \(\pi_1\oplus\pi_2\) is reducible because each summand is
a proper closed invariant subspace. An [[algebra-representation-theory/irreducible-representation|irreducible representation]] cannot have
two orthogonal nonzero invariant summands.

## Conventions and scope

**Warning.** This notion differs from irreducibility of an arbitrary
finite-dimensional linear representation only in settings where topology
matters. It should also be distinguished from factorial or primary
representations, whose commutants may contain nonscalar operators even when
their centers are trivial.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.1 on invariant subspaces, irreducibility, and Schur's lemma.
