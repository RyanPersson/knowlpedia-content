+++
id = "operator-algebras/type-i-infinity-factor"
title = "Type I∞ factor"
kind = "definition"
summary = "A type I-infinity factor is a type I von Neumann factor acting on an infinite-dimensional Hilbert space."
aliases = ["infinite type I factor"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

A **type \(\mathrm I_\infty\) factor** is a
[[operator-algebras/type-i-factor|type I factor]] that is isomorphic, as a von
Neumann algebra, to \(B(H)\) for an infinite-dimensional complex
[[linear-algebra/hilbert-space|Hilbert space]] \(H\). Equivalently, it is a
type I factor whose identity is an
[[operator-algebras/infinite-projection|infinite projection]], or whose
maximal families of mutually orthogonal equivalent [[operator-algebras/minimal-projection|minimal projections]] are
infinite.
The subscript \(\infty\) distinguishes this case from the finite-dimensional
type \(\mathrm I_n\) factors \(M_n(\mathbb C)\). No separability hypothesis is
part of the definition: the Hilbert-space dimension may be any infinite
cardinal.

## Classification and projection structure

Every type I factor is \(B(H)\) for a Hilbert space \(H\), unique up to
dimension. Minimal projections in \(B(H)\) are precisely rank-one
projections, and a maximal orthogonal family of them corresponds to an
[[linear-algebra/orthonormal-basis|orthonormal basis]]. Thus the cardinality of such a family recovers
\(\dim H\), and the infinite cardinals distinguish the nonseparable
isomorphism classes
[Takesaki, Chapter V, §1](https://doi.org/10.1007/978-1-4612-6188-9).

## Proper infiniteness and traces

An infinite-dimensional \(H\) decomposes as \(H\cong H\oplus H\). The two
coordinate embeddings give isometries in \(B(H)\) with orthogonal ranges, so
every type \(\mathrm I_\infty\) factor is a
[[operator-algebras/properly-infinite-von-neumann-algebra|properly infinite
von Neumann algebra]]. The usual
[[operator-algebras/operator-trace|operator trace]] is faithful, normal, and
semifinite but takes value \(\infty\) at the identity. Hence the algebra is
semifinite without being finite.

## Examples and boundaries

The algebra \(B(\ell^2(\mathbb N))\) is the separable type
\(\mathrm I_\infty\) factor. More generally, \(B(\ell^2(I))\) is type
\(\mathrm I_\infty\) for every infinite set \(I\). The algebra
\(\ell^\infty(I)\) is type I but not a factor when \(|I|>1\), because its
center is nontrivial. A type \(\mathrm{II}_\infty\) factor is properly
infinite and semifinite but has no minimal projections, so it is not type I.

## Conventions and scope

**Warning.** The infinity symbol records infinite Hilbert-space dimension, not
a new numerical value of the type parameter. Authors working only with
separable preduals may use “the type \(\mathrm I_\infty\) factor” for
\(B(\ell^2)\); without that standing hypothesis there are distinct factors
\(B(H)\) for different infinite dimensions.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V, §1 on the classification of type I factors.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [AMS record](https://bookstore.ams.org/GSM/16). Relevant: §6.5 on type I factors and properly infinite factors.
