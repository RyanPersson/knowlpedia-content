+++
id = "catalog/finite-groups/elementary/sl-n-q"
title = "Finite special linear group SL_n(q)"
kind = "definition"
summary = "Determinant-one matrices over F_q."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-fields-galois/finite-field", "algebra-groups/group", "linear-algebra/determinant"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(q=p^f\), with \(p\) prime and \(f\geq1\) an integer, and choose the [[algebra-fields-galois/finite-field|finite field]] \(\mathbb F_q\). Let \(n\geq1\) be an integer. The **special linear group \(\mathrm{SL}_{n}(q)\)** is the [[algebra-groups/group|group]] of [[linear-algebra/determinant|determinant-one]] \(n\times n\) matrices over \(\mathbb F_q\), with matrix multiplication.

## Order

The group order is \(\frac{1}{q-1}\prod_{j=0}^{n-1}(q^n-q^j)\). The determinant map from the [[catalog/finite-groups/elementary/gl-n-q|general linear group]] onto \(\mathbb F_q^\times\) has this group as kernel. Dividing the general linear group order by \(q-1\) gives the formula.

## Simplicity conditions

In size one the group is trivial. For size \(m\geq2\), the center is \(\{\lambda I:\lambda^m=1\}\), of order \(\gcd(m,q-1)\). Its quotient is \(\mathrm{PSL}_m(q)\), which is simple except at \((m,q)=(2,2),(2,3)\). Thus the special linear group itself is simple exactly when its center is trivial and these two exceptions are absent.

## Field and category convention

The parameter \(q\) must be a prime power. This is a finite abstract group; the field and its [[linear-algebra/vector-space|vector space]] supply a construction, rather than a vector-space structure on the matrix group itself.

## Determinant sequence

The inclusion into the general linear group and the determinant give an exact sequence
\[
1\longrightarrow\mathrm{SL}_{n}(q)\longrightarrow\mathrm{GL}_{n}(q)\xrightarrow{\det}\mathrm{GL}_1(q)\longrightarrow1.
\]
The diagonal matrix with entries \(a,1,\ldots,1\) maps to any prescribed \(a\in\mathbb F_q^\times\), proving surjectivity. In size one, this is the identity map on \(\mathbb F_q^\times\), with trivial kernel.

## References

- [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §2.1, Theorems 2.2–2.3, pp. 15–16: orders, determinant and scalar kernels; §2.4, Theorem 2.10, pp. 20–22: simplicity.
