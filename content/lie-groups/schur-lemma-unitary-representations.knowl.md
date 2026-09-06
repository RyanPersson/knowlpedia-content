+++
id = "lie-groups/schur-lemma-unitary-representations"
title = "Schur's lemma for unitary representations"
kind = "theorem"
summary = "An irreducible complex unitary representation has only scalar bounded operators in its commutant."
aliases = ["unitary Schur lemma", "commutant criterion for irreducibility"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "lie-groups/irreducible-unitary-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi\) be a unitary representation of a group \(G\) on a nonzero complex
[[linear-algebra/hilbert-space|Hilbert space]] \(\mathcal H\). **Schur's lemma for unitary representations**
states that \(\pi\) is
[[lie-groups/irreducible-unitary-representation|irreducible]] if and only if
every bounded operator \(T\) satisfying
\[
T\pi(g)=\pi(g)T\qquad(g\in G)
\]
is a scalar multiple of the identity. Equivalently, the commutant
\(\pi(G)'\) equals \(\mathbb C I\). Here irreducibility means that
\(\mathcal H\) has no nonzero proper closed invariant subspace. No
finite-dimensionality, compactness, or local compactness hypothesis on \(G\)
is required.

## Proof mechanism

If a closed subspace is invariant under a unitary representation, its
[[linear-algebra/orthogonal-complement|orthogonal complement]] is invariant, so the corresponding orthogonal
projection lies in the commutant. Conversely, for a self-adjoint operator in
the commutant, every spectral projection also commutes with \(\pi(G)\).
Irreducibility forces all these projections to be \(0\) or \(I\), hence the
operator is scalar. Applying this to the real and imaginary parts of an
arbitrary commutant element proves the theorem.

## Intertwiners between irreducibles

Let \(\pi\) and \(\sigma\) be irreducible unitary representations and let
\(T\) be a bounded
[[lie-groups/intertwining-operator-unitary-representations|intertwining
operator]] from \(\pi\) to \(\sigma\). Then \(T=0\), or \(T\) is a positive
scalar multiple of a unitary intertwiner. Thus inequivalent irreducibles admit
no nonzero bounded intertwiner; if \(\pi=\sigma\), every such \(T\) is scalar.
This follows by applying the commutant statement to \(T^*T\) and \(TT^*\).

## Conventions and scope

**Warning.** Over a real Hilbert space the commutant of an irreducible
orthogonal representation can be isomorphic to \(\mathbb R\), \(\mathbb C\),
or the quaternions, so the complex scalar conclusion does not carry over
unchanged. For nonunitary infinite-dimensional representations, algebraic
irreducibility and topological irreducibility also require separate
hypotheses.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §3.1, especially Theorem 3.5.
2. Jacques Dixmier, \(C^*\)-Algebras, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapter 2 on representations and commutants.
