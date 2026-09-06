+++
id = "nonassociative-algebra/complex-qubit-jordan-algebra"
title = "Complex-qubit Jordan algebra"
kind = "definition"
summary = "The four-dimensional Euclidean Jordan algebra of Hermitian two-by-two complex matrices."
aliases = ["complex qubit Jordan algebra", "qubit Jordan algebra", "h_2(C)"]
domains = ["nonassociative-algebra", "quantum-foundations"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/euclidean-jordan-algebra", "quantum-foundations/qubit"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **complex-qubit Jordan algebra** is
\[
\mathfrak h_2(\mathbb C)
=\{X\in M_2(\mathbb C):X^*=X\},
\qquad
X\circ Y=\frac12(XY+YX).
\]
It is the four-dimensional real
[[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]]
of observables of a complex [[quantum-foundations/qubit|two-level quantum system]].

## Pauli and spin-factor descriptions

Every \(X\in\mathfrak h_2(\mathbb C)\) is uniquely
\[
X=\lambda I+u_1\sigma_1+u_2\sigma_2+u_3\sigma_3,
\qquad (\lambda,u)\in\mathbb R\oplus\mathbb R^3,
\]
where the \(\sigma_i\) are the Pauli matrices. Their anticommutation relations
give the spin-factor product, so
\[
\mathfrak h_2(\mathbb C)\cong J(\mathbb R^3).
\]
It is therefore a simple
[[nonassociative-algebra/spin-factor-jordan-algebra|spin factor]] of rank \(2\).

## Spectrum and states

The eigenvalues of \(X=\lambda I+u\cdot\sigma\) are
\(\lambda\pm\|u\|\). Thus \(X\) is positive exactly when
\(\lambda\geq\|u\|\). A density matrix has the Bloch representation
\[
\rho=\frac12(I+r\cdot\sigma),\qquad \|r\|\leq1.
\]

## Embedding in a qutrit algebra

The upper-left \(2\times2\) corner is a [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] of
\(\mathfrak h_3(\mathbb C)\). This inclusion is not unital: it sends
\(I_2\) to \(\operatorname{diag}(1,1,0)\), rather than to \(I_3\).

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778).
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
