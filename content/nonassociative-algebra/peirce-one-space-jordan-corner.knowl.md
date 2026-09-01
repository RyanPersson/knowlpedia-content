+++
id = "nonassociative-algebra/peirce-one-space-jordan-corner"
title = "Peirce-one Jordan corner"
kind = "construction"
summary = "The Peirce 1-space of an idempotent, a unital Jordan subalgebra with that idempotent as its unit."
aliases = ["Peirce one space", "Jordan corner", "Peirce 1-space"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/jordan-algebra", "nonassociative-algebra/jordan-subalgebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For an idempotent \(e\) in a [[nonassociative-algebra/jordan-algebra|Jordan algebra]] \(J\), the **Peirce-one corner** is
\[
J_1(e)=\{x\in J:e\circ x=x\}.
\]
It is a [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] of \(J\), and \(e\) is its unit. Notice that the
defining equation is \(e\circ x=x\), not \(e\circ x=1\).

## Hermitian \(3\)-by-\(3\) case

Let \(\mathbb K\) be one of the normed real division algebras
\(\mathbb R,\mathbb C,\mathbb H,\mathbb O\), and let
\(J=H_3(\mathbb K)\). If \(\ell\in J\) is an idempotent of matrix trace \(2\),
then
\[
J_1(\ell)\cong H_2(\mathbb K)
\]
as a unital Jordan algebra. After an automorphism takes
\(\ell\) to \(E_{11}+E_{22}\), this corner consists exactly of matrices
\[
\begin{pmatrix}
\alpha&x&0\\
x^*&\beta&0\\
0&0&0
\end{pmatrix},
\qquad \alpha,\beta\in\mathbb R,\quad x\in\mathbb K.
\]

Conversely, every [[nonassociative-algebra/jordan-subalgebra|Jordan
subalgebra]] of \(H_3(\mathbb K)\) isomorphic to
\(H_2(\mathbb K)\) is \(J_1(\ell)\) for a unique trace-two idempotent
\(\ell\): namely, the unit of that subalgebra viewed inside \(J\).

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026, Lemmas 7–10. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
2. Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society, 1968, Chapter III, §1. [Publisher record](https://doi.org/10.1090/coll/039).
