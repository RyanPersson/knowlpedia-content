+++
id = "catalog/finite-groups/elementary/sl-2-q"
title = "Finite special linear group SL_2(q)"
kind = "definition"
summary = "Determinant-one matrices over F_q."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-fields-galois/finite-field", "algebra-groups/group", "linear-algebra/determinant"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(q=p^f\), with \(p\) prime and \(f\geq1\) an integer, and choose the [[algebra-fields-galois/finite-field|finite field]] \(\mathbb F_q\). The **special linear group \(\mathrm{SL}_{2}(q)\)** is the [[algebra-groups/group|group]] of [[linear-algebra/determinant|determinant-one]] \(2\times 2\) matrices over \(\mathbb F_q\), with matrix multiplication.

## Order

The group order is \(q(q^2-1)\). The determinant map from the [[catalog/finite-groups/elementary/gl-2-q|general linear group]] onto \(\mathbb F_q^\times\) has this group as kernel. Dividing the general linear group order by \(q-1\) gives the formula.

## Simplicity conditions

For odd \(q\), the proper nontrivial center \(\{I,-I\}\) prevents simplicity. For even \(q\), the center is trivial and the group equals \(\mathrm{PSL}_2(q)\), which is simple for \(q\geq4\). The remaining case \(q=2\) is [[catalog/finite-groups/elementary/sym-3|\(S_3\)]]. Thus simplicity holds exactly when \(q\) is even and \(q\geq4\).

## Field and category convention

The parameter \(q\) must be a prime power. This is a finite abstract group; the field and its [[linear-algebra/vector-space|vector space]] supply a construction, rather than a vector-space structure on the matrix group itself.

## Determinant sequence

The inclusion into the general linear group and the determinant give an exact sequence
\[
1\longrightarrow\mathrm{SL}_{2}(q)\longrightarrow\mathrm{GL}_{2}(q)\xrightarrow{\det}\mathrm{GL}_1(q)\longrightarrow1.
\]
The diagonal matrix with entries \(a,1,\ldots,1\) maps to any prescribed \(a\in\mathbb F_q^\times\), proving surjectivity. In size one, this is the identity map on \(\mathbb F_q^\times\), with trivial kernel.

## References

- [Peter J. Cameron, Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), §2.1, Theorems 2.2–2.3, pp. 15–16: orders, determinant and scalar kernels; §2.4, Theorem 2.10, pp. 20–22: simplicity.
