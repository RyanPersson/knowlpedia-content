+++
id = "operator-algebras/finite-normal-trace"
title = "Finite normal trace on a von Neumann algebra"
kind = "definition"
summary = "A normal tracial weight on a von Neumann algebra whose value at the identity is finite."
aliases = ["finite normal tracial weight"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/tracial-weight", "operator-algebras/normal-weight"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a unital [[operator-algebras/von-neumann-algebra|von Neumann
algebra]]. A **finite normal trace** on \(M\) is a
[[operator-algebras/tracial-weight|tracial weight]]
\(\tau:M_+\to[0,+\infty]\) that is
[[operator-algebras/normal-weight|normal]] and satisfies
\[
\tau(1)<\infty.
\]
Finiteness at the identity implies \(\tau(x)<\infty\) for every
\(x\in M_+\), so \(\tau\) extends uniquely to a bounded normal positive linear
functional on \(M\) satisfying \(\tau(ab)=\tau(ba)\). Faithfulness and
normalization are not part of the definition: they must be imposed separately
when the trace is meant to detect every positive element or be a state.

## Equivalent bounded formulation

Equivalently, a finite normal trace is a normal
[[operator-algebras/positive-linear-functional|positive linear functional]]
\(\tau:M\to\mathbb C\) satisfying
\[
\tau(ab)=\tau(ba)\qquad(a,b\in M).
\]
Its norm is \(\|\tau\|=\tau(1)\). Dividing a nonzero finite normal trace by
\(\tau(1)\) produces a normal
[[operator-algebras/tracial-state|tracial state]], but it does not repair a
failure of faithfulness. Thus the positive-cone weight and bounded-functional
formulations are equivalent.

## Examples and consequences

The normalized matrix trace \(n^{-1}\operatorname{Tr}\) is a faithful finite
normal trace on \(M_n(\mathbb C)\). Integration against a finite measure gives
a finite normal trace on the
[[operator-algebras/commutative-von-neumann-algebra|commutative von Neumann algebra]]
\(L^\infty(X,\mu)\). On \(B(H)\) for infinite-dimensional \(H\), the canonical
operator trace is normal, semifinite, and faithful but not finite because
\(\operatorname{Tr}(1)=+\infty\).

A [[operator-algebras/von-neumann-algebra|von Neumann algebra]] admitting a faithful finite normal trace is finite, but
the zero functional is a finite normal trace on every von Neumann algebra.
Faithfulness is therefore essential in any trace-based characterization of
finite algebras.

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, AMS, 1997. [AMS record](https://bookstore.ams.org/GSM-16). Relevant: §7.2 on finite traces and normal traces.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on traces and finite von Neumann algebras.
