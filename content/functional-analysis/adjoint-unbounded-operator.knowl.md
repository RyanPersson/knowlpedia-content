+++
id = "functional-analysis/adjoint-unbounded-operator"
title = "Adjoint of a densely defined operator"
kind = "definition"
summary = "The closed operator determined by the vectors on which an unbounded operator's inner-product pairing is bounded."
aliases = ["unbounded adjoint", "Hilbert-space operator adjoint"]
domains = ["functional-analysis", "operator-theory"]
section_mode = "progressive"
prerequisites = ["functional-analysis/densely-defined-operator", "linear-algebra/hilbert-space", "functional-analysis/riesz-representation-hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T:\mathcal D(T)\subseteq H\to K\) be a
[[functional-analysis/densely-defined-operator|densely defined operator]]
between complex [[linear-algebra/hilbert-space|Hilbert spaces]], with inner
products linear in the first variable. The **adjoint** \(T^*\) has domain
\[
\mathcal D(T^*)=
\left\{y\in K:\exists z\in H\ \text{such that}\
\langle Tx,y\rangle_K=\langle x,z\rangle_H
\ \text{for all }x\in\mathcal D(T)\right\},
\]
and \(T^*y=z\). Density of \(\mathcal D(T)\) makes \(z\) unique. Equivalently,
\(y\in\mathcal D(T^*)\) exactly when the functional
\(x\mapsto\langle Tx,y\rangle_K\) is bounded in the \(H\)-norm; the
[[functional-analysis/riesz-representation-hilbert-space|Riesz
representation theorem]] then supplies \(T^*y\).

## Closedness and closability

The adjoint \(T^*\) is always closed, although its domain need not be dense.
The original operator \(T\) is closable exactly when
\(\mathcal D(T^*)\) is dense in \(K\). In that case its
[[functional-analysis/closure-of-operator|closure]] satisfies
\[
\overline T=T^{**}.
\]
These identities include equality of domains as well as equality of the
operator actions.

## Domain-sensitive algebra

Adjoints reverse products only with domain qualifications. For densely
defined \(S\) and \(T\) such that \(ST\) is densely defined, one generally
has
\[
(ST)^*\supseteq T^*S^*,
\]
and equality requires additional hypotheses. Likewise, the formal
integration-by-parts expression for a differential operator does not by
itself determine the adjoint: boundary terms and the chosen domain determine
\(\mathcal D(T^*)\).

## Symmetry and self-adjointness

For \(T:\mathcal D(T)\subseteq H\to H\), symmetry means
\(T\subseteq T^*\), including \(\mathcal D(T)\subseteq\mathcal D(T^*)\).
Self-adjointness requires the stronger equality \(T=T^*\), especially
\(\mathcal D(T)=\mathcal D(T^*)\). A symmetric differential operator on a
small test domain can therefore fail to be self-adjoint even when its formal
expression is real.

## References

- [Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Chapter 1 (Springer, 2012)](https://doi.org/10.1007/978-94-007-4753-1)
- [Tosio Kato, *Perturbation Theory for Linear Operators*, Chapter V, §3 (Springer, 1995)](https://doi.org/10.1007/978-3-642-66282-9)
