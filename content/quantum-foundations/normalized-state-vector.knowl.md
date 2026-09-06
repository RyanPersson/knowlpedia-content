+++
id = "quantum-foundations/normalized-state-vector"
title = "Normalized state vector"
kind = "knowl"
summary = "A unit vector representing a pure quantum state up to multiplication by a phase."
aliases = ["normalized state vector", "unit state vector"]
domains = ["quantum-foundations", "linear-algebra"]
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/unit-sphere"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **normalized state vector** in a complex [[linear-algebra/hilbert-space|Hilbert space]] \(H\) is a vector \(\psi\in H\) with \(\lVert\psi\rVert=1\). It lies on the [[linear-algebra/unit-sphere|unit sphere]].

In quantum mechanics, \(\psi\) and \(e^{i\theta}\psi\) represent the same pure state, because all transition probabilities depend only on squared inner-product magnitudes. The phase-independent state is equivalently represented by the [[quantum-foundations/rank-one-projector|rank-one projector]] \(|\psi\rangle\langle\psi|\).
