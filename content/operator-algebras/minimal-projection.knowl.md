+++
id = "operator-algebras/minimal-projection"
title = "Minimal projection"
kind = "definition"
summary = "A nonzero projection in a von Neumann algebra that has no nonzero proper subprojection."
aliases = ["atomic projection"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]].
A **minimal projection** is a nonzero projection \(p\in M\) such that every
projection \(q\in M\) with \(q\leq p\) satisfies \(q=0\) or \(q=p\). Here
\(q\leq p\) means \(pq=qp=q\). Equivalently,
\[
pMp=\mathbb Cp.
\]
Minimality is relative to the ambient algebra \(M\): the same operator may be
minimal in one von Neumann subalgebra and not in a larger one. A minimal
projection need not be central, and it should not be confused with a minimal
central projection.

## Equivalent formulations

The corner \(pMp\) is itself a von Neumann algebra with identity \(p\).
Spectral projections show that it has no projections other than \(0\) and
\(p\) exactly when every self-adjoint element of the corner is scalar,
yielding \(pMp=\mathbb Cp\). In a concrete algebra on \(H\), a rank-one
[[linear-algebra/orthogonal-projection|orthogonal projection]] is minimal in \(B(H)\). Higher-rank projections are not,
because a one-dimensional subspace of their range gives a proper nonzero
subprojection.

## Relation to factor type

Every [[operator-algebras/type-i-factor|type I factor]] contains minimal projections: under an isomorphism with
\(B(K)\), they correspond to rank-one projections. Type II and type III
factors contain no minimal projections
[Takesaki, Chapter V, §1].
For a general [[operator-algebras/type-i-von-neumann-algebra|type I von Neumann algebra]], a diffuse center can prevent the
existence of minimal projections, so the factor statement must not be promoted
to all type I algebras.

## Conventions and scope

“Atomic projection” is commonly synonymous with minimal projection, while an
**abelian projection** only requires \(pMp\) to be commutative and can be much
weaker. In a general \(C^*\)-algebra, \(pAp=\mathbb Cp\) is often taken as the
definition of a minimal projection. The subprojection condition is equivalent
to it for von Neumann algebras, as used here, but not merely from the absence
of projections in an arbitrary unital \(C^*\)-corner.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V, §1 on minimal projections and type I structure.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [AMS record](https://doi.org/10.1090/gsm/016). Relevant: Chapter 6 on projections, factors, and type decomposition.
