+++
id = "operator-algebras/pure-state-irreducible-gns"
title = "Pure states and irreducible GNS representations"
kind = "theorem"
summary = "A state is pure exactly when its GNS representation is irreducible."
aliases = ["pure iff GNS irreducible", "GNS purity criterion"]
domains = ["operator-algebras", "representation-theory"]
section_mode = "progressive"
+++

**GNS purity criterion.** Let \(\varphi\) be a
[[operator-algebras/state-cstar-algebra|state]] on a \(C^*\)-algebra \(A\), and
let \((\pi_\varphi,H_\varphi,\xi_\varphi)\) be its
[[operator-algebras/gns-construction|GNS representation]]. Then
\(\varphi\) is a
[[operator-algebras/pure-state-cstar-algebra|pure state]] if and only if
\(\pi_\varphi\) is an
[[operator-algebras/irreducible-cstar-representation|irreducible
representation]]. Consequently, convex indecomposability of a state is
equivalent to the absence of nontrivial closed invariant subspaces in its
canonical cyclic representation. Neither side asserts that \(\varphi\) or
\(\pi_\varphi\) is faithful.

## Proof mechanism

If a nontrivial projection lies in the
[[operator-algebras/commutant|commutant]] \(\pi_\varphi(A)'\), its two
orthogonal components split the vector functional into a nontrivial convex
combination. Conversely, a
[[operator-algebras/positive-linear-functional|positive functional]] dominated
by \(\varphi\) is represented by a positive contraction in that commutant; a
nontrivial convex decomposition therefore produces a nonscalar commutant.
[[algebra-representation-theory/schurs-lemma|Schur's lemma]],
\(\pi_\varphi(A)'=\mathbb C I\), completes the equivalence.

## Converse realization

Let \(\pi:A\to\mathcal B(H)\) be irreducible and let \(\xi\neq0\). Then \(\xi\)
is cyclic, and after normalization its
[[operator-algebras/vector-state|vector state]] is pure. The pointed GNS
representation of that state is unitarily equivalent to
\((\pi,H,\xi/\|\xi\|)\). Hence every [[algebra-representation-theory/irreducible-representation|irreducible representation]] is obtained,
up to unitary equivalence, from a pure state and a choice of nonzero vector.

## Distinctions

**Warning.** Purity is relative to the full state space of \(A\). Restricting a
pure state to a \(C^*\)-subalgebra can make it mixed, and a mixed state can
still be represented by a single vector in a reducible representation.
Normality is a separate order-continuity property available when the algebra
is a [[operator-algebras/von-neumann-algebra|von Neumann algebra]].

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Theorem 3.3.8 on pure states and irreducible GNS representations.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 3 on pure states, cyclic representations, and commutants.
