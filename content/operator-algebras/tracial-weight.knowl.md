+++
id = "operator-algebras/tracial-weight"
title = "Tracial weight"
kind = "definition"
summary = "An extended positive weight whose values are unchanged when the two factors in an operator square are reversed."
aliases = ["trace weight"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/weight-on-von-neumann-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]].
A [[operator-algebras/weight-on-von-neumann-algebra|weight]]
\(\tau:M_+\to[0,+\infty]\) is **tracial** if
\[
\tau(x^*x)=\tau(xx^*)\qquad(x\in M).
\]
The equality is interpreted in the extended nonnegative reals, so either side
may be \(+\infty\). A **tracial weight** is such a weight, without any implied
normality, semifiniteness, faithfulness, or finiteness. In particular, the
tracial identity specifies symmetry under changing the order of the two
factors, while the regularity and domain properties commonly needed in von
Neumann algebra theory are independent additional hypotheses.

## Invariance and finite elements

Taking \(x=ua^{1/2}\), where \(u\) is unitary and \(a\in M_+\), shows that
\[
\tau(uau^*)=\tau(a).
\]
Thus a tracial weight is invariant under inner unitary conjugation. Its finite
positive domain
\[
\mathfrak m_\tau^+=\{a\in M_+:\tau(a)<\infty\}
\]
is hereditary and invariant under unitary conjugation. When
\(\tau(1)<\infty\), additivity and homogeneity extend \(\tau\) uniquely to a
bounded tracial
[[operator-algebras/positive-linear-functional|positive linear functional]]
on all of \(M\).

## Examples and distinctions

The usual operator trace on \(B(H)_+\), allowed to take \(+\infty\), is a
normal semifinite faithful tracial weight. Integration on
\(L^\infty(X,\mu)_+\) is tracial because the algebra is commutative. By
contrast, a [[operator-algebras/vector-state|vector state]] on \(B(H)\) is
generally not tracial: it can
distinguish \(x^*x\) from \(xx^*\).

A bounded [[operator-algebras/trace-cstar-algebra|trace on a
\(C^*\)-algebra]] is finite everywhere. A tracial weight may instead be
unbounded and extended-valued, so the two terms should not be treated as
aliases.

## Conventions and scope

Some authors use “trace” to mean a normal semifinite faithful tracial weight,
while others reserve “trace” for a bounded functional. Here “tracial” records
only the displayed symmetry. The adjectives normal, semifinite, faithful, and
finite must be stated explicitly whenever they are required.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on traces and the type decomposition of von Neumann algebras.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, AMS, 1997. [AMS record](https://bookstore.ams.org/GSM-16). Relevant: §7.2 on traces and weights.
