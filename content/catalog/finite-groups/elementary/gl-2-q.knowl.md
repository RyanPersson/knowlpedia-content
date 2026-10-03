+++
id = "catalog/finite-groups/elementary/gl-2-q"
title = "Finite general linear group GL_2(q)"
kind = "definition"
summary = "Invertible matrices over F_q."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-fields-galois/finite-field", "algebra-groups/group", "linear-algebra/matrix-inverse"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(q=p^f\), with \(p\) prime and \(f\geq1\) an integer, and choose the [[algebra-fields-galois/finite-field|finite field]] \(\mathbb F_q\). The **general linear group \(\mathrm{GL}_{2}(q)\)** is the [[algebra-groups/group|group]] of [[linear-algebra/matrix-inverse|invertible]] \(2\times 2\) matrices over \(\mathbb F_q\), with matrix multiplication.

## Order

The group order is \((q^2-1)(q^2-q)\). For an [[linear-algebra/matrix-inverse|invertible matrix]], choose ordered linearly independent columns: after \(j\) choices, precisely \(q^j\) vectors are forbidden for the next column.

## Simplicity conditions

For \(q>2\), the determinant map onto \(\mathbb F_q^\times\) has a proper nontrivial kernel, the [[catalog/finite-groups/elementary/sl-2-q|special linear group]]. For \(q=2\), this group is isomorphic to [[catalog/finite-groups/elementary/sym-3|\(S_3\)]], whose alternating subgroup is proper nontrivial normal. Thus \(\mathrm{GL}_2(q)\) is never simple.

## Field and category convention

The parameter \(q\) must be a prime power. This is a finite abstract group; the field and its [[linear-algebra/vector-space|vector space]] supply a construction, rather than a vector-space structure on the matrix group itself.

## References

- [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §2.1, Theorems 2.2–2.3, pp. 15–16: orders, determinant and scalar kernels; §2.4, Theorem 2.10, pp. 20–22: simplicity.
