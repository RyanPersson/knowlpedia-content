+++
id = "catalog/finite-groups/elementary/sl-1-q"
title = "Finite special linear group SL_1(q)"
kind = "definition"
summary = "Determinant-one matrices over F_q."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-fields-galois/finite-field", "algebra-groups/group", "linear-algebra/determinant"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(q=p^f\), with \(p\) prime and \(f\geq1\) an integer, and choose the [[algebra-fields-galois/finite-field|finite field]] \(\mathbb F_q\). The **special linear group \(\mathrm{SL}_{1}(q)\)** is the [[algebra-groups/group|group]] of [[linear-algebra/determinant|determinant-one]] \(1\times 1\) matrices over \(\mathbb F_q\), with matrix multiplication.

## Order

The group order is \(1\). The determinant map from the [[catalog/finite-groups/elementary/gl-1-q|general linear group]] onto \(\mathbb F_q^\times\) has this group as kernel. Dividing the general linear group order by \(q-1\) gives the formula.

## Simplicity conditions

The only one by one matrix with determinant one is \((1)\). Thus this group is trivial for every \(q\), and the trivial group is not simple.

## Field and category convention

The parameter \(q\) must be a prime power. This is a finite abstract group; the field and its [[linear-algebra/vector-space|vector space]] supply a construction, rather than a vector-space structure on the matrix group itself.

## Determinant sequence

The inclusion into the general linear group and the determinant give an exact sequence
\[
1\longrightarrow\mathrm{SL}_{1}(q)\longrightarrow\mathrm{GL}_{1}(q)\xrightarrow{\det}\mathrm{GL}_1(q)\longrightarrow1.
\]
The diagonal matrix with entries \(a,1,\ldots,1\) maps to any prescribed \(a\in\mathbb F_q^\times\), proving surjectivity. In size one, this is the identity map on \(\mathbb F_q^\times\), with trivial kernel.

## References

- [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §2.1, Theorems 2.2–2.3, pp. 15–16: orders, determinant and scalar kernels; §2.4, Theorem 2.10, pp. 20–22: simplicity.
