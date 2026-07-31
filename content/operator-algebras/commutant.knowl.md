+++
id = "operator-algebras/commutant"
title = "Commutant"
kind = "definition"
summary = "The algebra of bounded operators that commute with every operator in a specified set."
aliases = ["centralizer algebra", "operator commutant"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(\mathcal H\) be a [[linear-algebra/hilbert-space|Hilbert space]] and let \(S\) be a subset of the [[operator-algebras/bounded-operator-cstar-algebra|algebra \(\mathcal B(\mathcal H)\) of bounded operators]] on \(\mathcal H\). The **commutant** of \(S\) is
\[
S'=\{T\in\mathcal B(\mathcal H):TA=AT\text{ for every }A\in S\}.
\]
Thus \(S'\) records all bounded symmetries of the operator family \(S\). The [[operator-algebras/bicommutant|bicommutant]] is \(S''=(S')'\). This definition applies to any set of operators; \(S\) need not itself be an algebra, self-adjoint, or closed in any operator topology.

## Basic properties

The commutant is a unital [[operator-algebras/involutive-algebra|\(*\)-subalgebra]] of \(\mathcal B(\mathcal H)\) when \(S=S^*\); without that hypothesis it is still a unital algebra but need not be closed under adjoints. It is closed in both the [[operator-algebras/weak-operator-topology|weak]] and [[operator-algebras/strong-operator-topology|strong operator topologies]]. Inclusion reverses: \(S\subseteq T\) implies \(T'\subseteq S'\), and always \(S\subseteq S''\).

## Bicommutants and operator algebras

The [[operator-algebras/von-neumann-bicommutant-theorem|von Neumann bicommutant theorem]] says that for a unital self-adjoint subalgebra \(A\subseteq\mathcal B(\mathcal H)\), the bicommutant \(A''\) equals both its strong-operator and weak-operator closures. This makes commutants a central bridge between algebraic relations and operator-topological closure.

## Examples

The commutant of all scalar multiples of the identity is \(\mathcal B(\mathcal H)\). Conversely, \(\mathcal B(\mathcal H)'=\mathbb C I\). If \(P\) is an [[linear-algebra/orthogonal-projection|orthogonal projection]], then \(\{P\}'\) consists of the operators preserving both \(\operatorname{ran}P\) and \(\ker P\), equivalently the block-diagonal operators for \(\mathcal H=\operatorname{ran}P\oplus\ker P\).

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §§1–2 on commutants and the bicommutant theorem.
