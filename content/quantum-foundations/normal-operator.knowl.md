+++
id = "quantum-foundations/normal-operator"
title = "Normal operator"
kind = "knowl"
summary = "A bounded operator that commutes with its adjoint."
aliases = ["normal operator", "normal operators"]
domains = ["quantum-foundations", "linear-algebra", "analysis"]
prerequisites = ["linear-algebra/operator-invariant-subspace"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

A bounded operator \(T\) on a complex Hilbert space is **normal** if it commutes with its adjoint:
\[
TT^*=T^*T.
\]
Self-adjoint, unitary, and orthogonal projection operators are normal. In finite dimension, normality is equivalent to unitary diagonalizability.

The spectral theorem extends this structure to infinite-dimensional Hilbert spaces through a projection-valued spectral measure. This extra structure implies that a non-scalar normal operator on a Hilbert space has nontrivial [[linear-algebra/operator-invariant-subspace|closed invariant subspaces]].
