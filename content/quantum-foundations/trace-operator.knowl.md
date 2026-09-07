+++
id = "quantum-foundations/trace-operator"
title = "Trace of an Operator"
kind = "knowl"
summary = "A basis-independent scalar associated to a linear operator, equal to the sum of diagonal entries or eigenvalues in finite dimension."
aliases = ["trace-operator", "Trace of an Operator"]
domains = ["quantum-foundations"]
legacy_source_path = "quantum-foundations/trace-operator.md"
prerequisites = ["functional-analysis/trace-class-operator", "linear-algebra/hilbert-space", "linear-algebra/inner-product", "linear-algebra/orthonormal-basis"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

Let \(A:H\to H\) be a [[functional-analysis/trace-class-operator|trace-class operator]] on a complex [[linear-algebra/hilbert-space|Hilbert space]], using the [[linear-algebra/inner-product|inner product]] convention linear in its first argument. For any [[linear-algebra/orthonormal-basis|orthonormal basis]] \((e_j)_{j\in J}\), the **trace** is
\[
\operatorname{Tr}(A)=\sum_{j\in J}\langle A e_j,e_j\rangle.
\]
The sum is absolutely convergent and independent of the basis. For an arbitrary index set, it is the limit over finite subsets; at most countably many summands are nonzero. In finite dimension every linear operator is trace-class, and this formula equals the [[linear-algebra/trace|matrix trace]].

## Equivalent descriptions (finite dimension)

- If \(A\) is represented by a matrix \((A_{ij})\) in any basis, then \(\operatorname{Tr}(A)=\sum_i A_{ii}\).
- \(\operatorname{Tr}(A)\) equals the sum of eigenvalues of \(A\), counted with algebraic multiplicity.


## Properties

For trace-class operators \(A,B\) on \(H\) and scalars \(\alpha,\beta\):

- **Linearity:** \(\operatorname{Tr}(\alpha A+\beta B)=\alpha\operatorname{Tr}(A)+\beta\operatorname{Tr}(B)\).
- **Cyclic property:** \(\operatorname{Tr}(AB)=\operatorname{Tr}(BA)\).
- **Unitary invariance:** if \(U\) is unitary, then \(\operatorname{Tr}(U^\ast A U)=\operatorname{Tr}(A)\).
- **Positivity:** if \(A\) is positive semidefinite, then \(\operatorname{Tr}(A)\ge 0\).


The cyclic identity also holds when one factor is trace-class and the other is bounded; both products are then trace-class.

## Quantum expectation values

For a [[quantum-foundations/density-operator|density operator]] \(\rho\) and a bounded self-adjoint observable \(A\),
\[
\mathbb E_\rho[A]=\operatorname{Tr}(\rho A).
\]
For an unbounded observable, additional domain and integrability conditions are needed.

## Positive operators outside trace class

For a bounded positive operator \(A\), the same sum of nonnegative diagonal entries defines an extended trace in \([0,\infty]\), independent of the basis. Finiteness is equivalent to trace-class membership. An arbitrary bounded operator need not have a trace.


## References

1. Dan-Virgil Voiculescu, *Math 209: Von Neumann Algebras*, notes by Leonard Tomczak, UC Berkeley, Spring 2024. [Lecture notes](https://math.berkeley.edu/~ltomczak/notes/Spring2024/VNA_Notes.pdf), §4, pp. 7–8, Proposition 4.1 and the singular-value expansion.
