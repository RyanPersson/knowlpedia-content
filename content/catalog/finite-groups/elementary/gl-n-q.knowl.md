+++
id = "catalog/finite-groups/elementary/gl-n-q"
title = "Finite general linear group GL_n(q)"
kind = "definition"
summary = "Invertible matrices over F_q."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-fields-galois/finite-field", "algebra-groups/group", "linear-algebra/matrix-inverse"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(q=p^f\), with \(p\) prime and \(f\geq1\) an integer, and choose the [[algebra-fields-galois/finite-field|finite field]] \(\mathbb F_q\). Let \(n\geq1\) be an integer. The **general linear group \(\mathrm{GL}_{n}(q)\)** is the [[algebra-groups/group|group]] of [[linear-algebra/matrix-inverse|invertible]] \(n\times n\) matrices over \(\mathbb F_q\), with matrix multiplication.

## Order

The group order is \(\prod_{j=0}^{n-1}(q^n-q^j)\). For an [[linear-algebra/matrix-inverse|invertible matrix]], choose ordered linearly independent columns: after \(j\) choices, precisely \(q^j\) vectors are forbidden for the next column.

## Simplicity conditions

In size one the group is \(\mathbb F_q^\times\), cyclic of order \(q-1\), and hence simple exactly when \(q-1\) is prime. For size at least two and \(q>2\), the determinant has a proper nontrivial kernel, so simplicity fails. At \(q=2\), general and [[catalog/finite-groups/elementary/sl-n-q|special linear groups]] coincide: size two gives \(S_3\), while every size at least three is simple.

## Field and category convention

The parameter \(q\) must be a prime power. This is a finite abstract group; the field and its [[linear-algebra/vector-space|vector space]] supply a construction, rather than a vector-space structure on the matrix group itself.

## References

- [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §2.1, Theorems 2.2–2.3, pp. 15–16: orders, determinant and scalar kernels; §2.4, Theorem 2.10, pp. 20–22: simplicity.
