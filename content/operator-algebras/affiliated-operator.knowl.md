+++
id = "operator-algebras/affiliated-operator"
title = "Operator affiliated with a von Neumann algebra"
kind = "definition"
summary = "A closed densely defined operator whose domain and action are invariant under every unitary in the commutant."
aliases = ["affiliated operator"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]]. A
[[functional-analysis/densely-defined-operator|densely defined operator]]
\(T\) on \(H\) that is
[[functional-analysis/closed-linear-operator|closed]] is **affiliated with \(M\)**,
written \(T\eta M\), if every unitary \(u\) in the
[[operator-algebras/commutant|commutant]] \(M'\) preserves
\(\operatorname{Dom}(T)\) and
\[
Tu\xi=uT\xi\qquad(\xi\in\operatorname{Dom}(T)).
\]
Equivalently, \(uTu^*=T\) as unbounded operators for every unitary
\(u\in M'\). Affiliation therefore extends the relation \(T\in M\) from
bounded operators to closed unbounded operators while retaining invariance
under all symmetries commuting with \(M\).

## Spectral characterization

If \(T\) is self-adjoint, then \(T\eta M\) exactly when every
[[functional-analysis/spectral-projection|spectral projection]] of \(T\)
belongs to \(M\). More generally, for the polar
decomposition \(T=v|T|\), affiliation is equivalent to \(v\in M\) together
with affiliation of \(|T|\). These criteria turn an unbounded commutation
condition into bounded operator-algebra data.

## Examples and non-examples

Every bounded \(T\in M\) is affiliated with \(M\). For
\(M=L^\infty(X,\mu)\) acting by multiplication on \(L^2(X,\mu)\), a
[[measure-theory/measurable-function|measurable function]] defines an
affiliated multiplication operator on its maximal \(L^2\)-domain. In
contrast, a closed operator whose spectral projections do not lie in \(M\)
is not affiliated, even if some bounded functions of that operator happen
to belong to \(M\).

## Role in noncommutative integration

Affiliated operators supply the unbounded observables and measurable
operators used in noncommutative integration. Additional conditions such as
\(\tau\)-measurability control the size of the domain relative to a trace;
affiliation alone imposes no integrability, boundedness, or finite-trace
condition. This distinction is essential for constructions such as
[[operator-algebras/tau-compact-operator|\(\tau\)-compact operators]].

## References

1. Edward Nelson, “Notes on Non-Commutative Integration,” *Journal of Functional Analysis* 15 (1974), 103–116. [DOI record](https://doi.org/10.1016/0022-1236%2874%2990014-7). Relevant: §§1–2 on affiliated and measurable operators.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V on unbounded operators affiliated with von Neumann algebras.
