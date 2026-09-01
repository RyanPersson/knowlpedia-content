+++
id = "linear-algebra/orthogonal-projection"
title = "Orthogonal projection"
kind = "knowl"
summary = "The bounded linear operator projecting a Hilbert space onto a closed subspace along its orthogonal complement."
aliases = ["orthogonal projection", "orthogonal projector"]
domains = ["linear-algebra", "quantum-foundations"]
prerequisites = ["linear-algebra/closed-linear-subspace", "linear-algebra/hilbert-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

Let \(M\) be a [[linear-algebra/closed-linear-subspace|closed linear subspace]] of a [[linear-algebra/hilbert-space|Hilbert space]] \(H\). The decomposition \(H=M\oplus M^\perp\) defines the **orthogonal projection** \(P_M:H\to H\) by \(P_M(m+n)=m\).

It is the unique bounded operator satisfying \(P_M^2=P_M\), \(P_M^*=P_M\), and \(\operatorname{range}(P_M)=M\). Conversely, the range of every self-adjoint idempotent bounded operator is a closed subspace.
