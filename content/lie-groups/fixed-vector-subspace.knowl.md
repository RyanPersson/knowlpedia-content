+++
id = "lie-groups/fixed-vector-subspace"
title = "Fixed-vector subspace"
kind = "definition"
summary = "The subspace of a representation on which every group or Lie-algebra element acts trivially."
aliases = ["invariant-vector subspace", "space of invariants", "fixed vectors", "G-invariants"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
+++

For a [[lie-groups/representation-of-a-lie-group|representation]] \(\rho:G\to\operatorname{GL}(V)\), the **fixed-vector subspace**, or **space of invariants**, is
\[
V^G=\{v\in V:\rho(g)v=v\text{ for every }g\in G\}.
\]
For a [[lie-groups/representation-of-a-lie-algebra|Lie-algebra representation]] \(d\rho:\mathfrak g\to\mathfrak{gl}(V)\), it is
\[
V^{\mathfrak g}=\{v\in V:d\rho(X)v=0\text{ for every }X\in\mathfrak g\}.
\]
Both are linear subspaces and subrepresentations carrying the trivial action.

## Universal description

The fixed space can be written as an intersection of kernels,
\[
V^G=\bigcap_{g\in G}\ker(\rho(g)-I),
\qquad
V^{\mathfrak g}=\bigcap_{X\in\mathfrak g}\ker(d\rho(X)).
\]
Equivalently, \(V^G\) is naturally the space \(\operatorname{Hom}_G(\mathbf1,V)\) of equivariant maps from the trivial one-dimensional representation. Thus \(\dim V^G\) is the [[lie-groups/multiplicity-of-an-irreducible-representation|multiplicity]] of the trivial representation whenever \(V\) is completely reducible.

## Compact-group averaging

If \(G\) is compact and \(V\) is a continuous finite-dimensional representation, normalized Haar measure defines the Reynolds projection
\[
P(v)=\int_G\rho(g)v\,dg.
\]
It satisfies \(P^2=P\) and \(\operatorname{im}P=V^G\). This turns the abstract invariant subspace into a computable direct summand.

## Group versus Lie algebra

Every group-fixed vector is fixed infinitesimally. If \(G\) is connected, then
\[
V^G=V^{\mathfrak g}.
\]
For disconnected \(G\), the equality can fail because \(V^{\mathfrak g}\) only records invariance under the identity component. The remaining component group may act nontrivially on \(V^{\mathfrak g}\).

The term “invariant vector” means a fixed vector. It should not be confused with an invariant subspace, whose individual vectors may move within that subspace.

## References

1. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015, Chapters 4 and 11. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3).
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapter IV. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
