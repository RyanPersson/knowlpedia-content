+++
id = "lie-groups/weak-strong-continuity-equivalence-unitary-representations"
title = "Weak and strong continuity for unitary representations"
kind = "theorem"
summary = "For a unitary representation, continuity of all matrix coefficients, of diagonal coefficients, and of all orbit maps are equivalent."
aliases = ["weak continuity theorem", "continuity of matrix coefficients"]
domains = ["lie-groups", "harmonic-analysis", "functional-analysis"]
prerequisites = ["topology/topological-group", "algebra-groups/group-homomorphism", "linear-algebra/hilbert-space", "lie-groups/strongly-continuous-unitary-representation", "harmonic-analysis/coefficient-function", "operator-algebras/weak-operator-topology", "operator-algebras/strong-operator-topology"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]] and let
\(\pi:G\to U(H)\) be a [[algebra-groups/group-homomorphism|group homomorphism]]
on a [[linear-algebra/hilbert-space|Hilbert space]]. The following
conditions are equivalent:

1. \(\pi\) is [[lie-groups/strongly-continuous-unitary-representation|strongly continuous]];
2. every [[harmonic-analysis/coefficient-function|matrix coefficient]]
   \(g\mapsto\langle\pi(g)\xi,\eta\rangle\) is continuous; and
3. every diagonal coefficient
   \(g\mapsto\langle\pi(g)\xi,\xi\rangle\) is continuous.

In conditions 2 and 3, it is enough to require continuity at the identity.
Thus weak operator continuity and strong operator continuity agree for
unitary representations, even though the
[[operator-algebras/weak-operator-topology|weak operator topology]] and
[[operator-algebras/strong-operator-topology|strong operator topology]] differ
on general operator families.

## Proof mechanism

Strong continuity immediately implies coefficient continuity. Polarization
recovers all coefficients from diagonal ones. Conversely, unitarity gives
\[
\lVert\pi(g)\xi-\xi\rVert^2
=2\lVert\xi\rVert^2-
2\operatorname{Re}\langle\pi(g)\xi,\xi\rangle,
\]
so continuity of the diagonal coefficient at the identity forces continuity
of the [[fiber-bundles/orbit-map|orbit map]] there. Translation then gives continuity at every group
element.

## Why unitarity matters

The fixed norm \(\lVert\pi(g)\xi\rVert=\lVert\xi\rVert\) turns weak convergence
of an orbit to \(\xi\) into norm convergence through the displayed identity.
Without a uniform norm-preserving hypothesis, weak continuity of an
operator-valued homomorphism need not imply strong continuity by this
argument.

## Conventions and scope

Here "weakly continuous" refers to continuity of every scalar matrix
coefficient, not to
[[harmonic-analysis/weak-containment-unitary-representations|weak containment]]
of representations. No local compactness or finite-dimensionality assumption
on \(G\) or \(H\) is needed.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: the opening discussion of §3.1 on equivalent continuity conditions.
