+++
id = "operator-algebras/trace-cstar-algebra"
title = "Trace on a C*-algebra"
kind = "definition"
summary = "A bounded positive linear functional on a C*-algebra that is invariant under cyclic permutation of two factors."
aliases = ["C*-trace", "positive trace", "tracial functional"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/positive-linear-functional", "operator-algebras/tracial-weight"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**bounded trace on \(A\)** is a
[[operator-algebras/positive-linear-functional|positive linear functional]]
\(\tau:A\to\mathbb C\) satisfying
\[
\tau(ab)=\tau(ba)\qquad(a,b\in A).
\]
Equivalently, \(\tau(x^*x)=\tau(xx^*)\) for every \(x\in A\). Boundedness and
norm continuity are included here because \(\tau\) is a positive functional
on all of \(A\). A [[operator-algebras/tracial-state|tracial state]] is a trace
of norm one. Some sources also call an extended-valued [[operator-algebras/tracial-weight|tracial weight]] on
\(A_+\) a trace; such an object must have its domain,
lower-semicontinuity, and density assumptions stated separately and is not the
bounded notion defined above.

## Equivalent invariance

For a bounded positive functional, the tracial identity is equivalent to
invariance under inner unitary conjugation:
\[
\tau(uau^*)=\tau(a)
\]
for every unitary \(u\) in the unitization of \(A\). On positive elements it
also implies that Murray–von Neumann
[[operator-algebras/murray-von-neumann-equivalence|equivalent projections]]
have equal trace. These statements express that a trace records size without
depending on a choice of coordinates, while positivity prevents cancellation
on \(A_+\).

## Examples and existence

The normalized matrix trace \(a\mapsto n^{-1}\operatorname{Tr}(a)\) is the
unique tracial state on \(M_n(\mathbb C)\). For a commutative \(C^*\)-algebra,
every positive linear functional is automatically tracial. In contrast,
\(B(H)\) for infinite-dimensional \(H\) has no tracial state: its canonical
operator trace is unbounded and takes \(+\infty\) at the identity. Thus the
existence of a tracial state is a genuine restriction on a \(C^*\)-algebra.

## Extended traces and scope

An extended trace is commonly formulated as a weight
\(\tau:A_+\to[0,+\infty]\) satisfying
\(\tau(x^*x)=\tau(xx^*)\). Authors may additionally require it to be densely
defined, lower semicontinuous in norm, semifinite, or normal when \(A\) is a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]]. None of those
continuity and domain properties follows from the tracial identity alone. The
matrix/operator trace and a trace on an abstract algebra should therefore not
be identified without specifying their ambient algebra and domains.

## References

1. Bruce Blackadar, Operator Algebras: Theory of \(C^*\)-Algebras and von Neumann Algebras, Springer, 2006. [DOI record](https://doi.org/10.1007/978-1-4612-0949-3). Relevant: §II.6 on traces, tracial states, and dimension functions.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: the chapters on densely defined lower-semicontinuous traces and weights.
