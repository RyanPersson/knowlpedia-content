+++
id = "operator-algebras/properly-infinite-von-neumann-algebra"
title = "Properly infinite von Neumann algebra"
kind = "definition"
summary = "A properly infinite von Neumann algebra is one whose identity is equivalent to two orthogonal subprojections of itself."
aliases = ["properly infinite W*-algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

A [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\) is
**properly infinite** when its identity \(1_M\) is a properly infinite
projection: there are orthogonal projections \(p_1,p_2\leq1_M\) and partial
isometries \(v_1,v_2\in M\) such that
\[
v_i^*v_i=1_M,\qquad v_iv_i^*=p_i\quad(i=1,2).
\]
Equivalently, \(1_M\) contains two orthogonal subprojections, each
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann
equivalent]] to \(1_M\). This property is stronger than the
identity merely being [[operator-algebras/infinite-projection|infinite]] in a
general \(C^*\)-algebra, although the projection theory of von Neumann
algebras supplies powerful equivalent central criteria.

## Central characterization

A von Neumann algebra is properly infinite if and only if every nonzero
central projection is infinite, equivalently if it has no nonzero finite
central direct summand. In terms of the type decomposition, precisely the
[[operator-algebras/type-i-infinity-factor|type \(\mathrm I_\infty\)]],
type \(\mathrm{II}_\infty\), and type \(\mathrm{III}\) central summands may
occur. This characterization is part of the comparison theory of projections
[Kadison–Ringrose, §6.3](https://bookstore.ams.org/GSM/16).

## Isometries and amplification

The partial isometries in the core are isometries with orthogonal range
projections. By iterating the construction, one obtains countably many
orthogonal subprojections equivalent to the identity when the relevant
decomposition is countable. Proper infiniteness is consequently stable under
matrix amplification, and \(M\) absorbs finite matrix factors up to von
Neumann algebra isomorphism under the usual spatial identifications.

## Examples and non-examples

For every infinite-dimensional Hilbert space \(H\), \(B(H)\) is properly
infinite: split an orthonormal basis into two subsets of the same cardinality
and use the resulting isometries.
[[operator-algebras/type-ii-infinity-factor|Type
\(\mathrm{II}_\infty\)]] and
[[operator-algebras/type-iii-factor|type \(\mathrm{III}\) factors]] are also
properly infinite. By contrast,
\(M_n(\mathbb C)\),
[[operator-algebras/finite-von-neumann-algebra|finite von Neumann algebras]],
and type
\(\mathrm{II}_1\) factors are not, because their identities are finite.

## Conventions and scope

**Warning.** “Properly infinite algebra” here refers to a unital von Neumann
algebra through its identity projection. For nonunital \(C^*\)-algebras,
proper infiniteness is formulated in several nonequivalent ways, often using
positive elements, multiplier algebras, or stabilization; those conventions
should not be imported without qualification.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [AMS record](https://bookstore.ams.org/GSM/16). Relevant: §§6.3 and 6.5 on infinite projections and the type decomposition.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V, §1 on finite and properly infinite von Neumann algebras.
