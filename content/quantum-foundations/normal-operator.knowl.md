+++
id = "quantum-foundations/normal-operator"
title = "Normal operator"
kind = "knowl"
summary = "A [[functional-analysis/bounded-linear-operator|bounded operator]] that commutes with its adjoint."
aliases = ["normal operator", "normal operators"]
domains = ["quantum-foundations", "linear-algebra", "analysis"]
prerequisites = ["quantum-foundations/bounded-operator-hilbert"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A bounded operator \(T\) on a complex [[linear-algebra/hilbert-space|Hilbert space]] is **normal** if it commutes with its [[functional-analysis/adjoint-bounded-operator|adjoint]]:
\[
TT^*=T^*T.
\]
[[quantum-foundations/self-adjoint-operator-observable|Self-adjoint]], [[functional-analysis/unitary-operator|unitary]], and [[linear-algebra/orthogonal-projection|orthogonal projection]] operators are normal. In finite dimension, normality is equivalent to unitary diagonalizability.

The spectral theorem extends this structure to infinite-dimensional [[linear-algebra/hilbert-space|Hilbert spaces]] through a projection-valued [[functional-analysis/projection-valued-measure|spectral measure]]. This extra structure implies that a non-scalar normal operator on a Hilbert space has nontrivial [[linear-algebra/operator-invariant-subspace|closed invariant subspaces]].
