+++
id = "catalog/lie-groups/so-identity-p-q-r"
title = "Identity component SO0(p,q)"
kind = "definition"
summary = "The connected identity component of the real special orthogonal matrix group of signature (p,q)."
aliases = ["SO0(p,q)", "SO_0(p,q)", "SO⁺(p,q)", "connected indefinite special orthogonal group"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["catalog/lie-groups/so-p-q-r", "lie-groups/identity-component-of-a-lie-group"]
dependency_heuristic = "lie-groups-table-semantic-core-v1"
dependency_review_count = 1
+++

For integers \(p,q\ge0\) with \(p+q\ge1\), the **connected special orthogonal group**
\[
\operatorname{SO}_0(p,q):=\operatorname{SO}(p,q)^\circ
\]
is the [[lie-groups/identity-component-of-a-lie-group|identity component]] of the real matrix group
[[catalog/lie-groups/so-p-q-r|\(\operatorname{SO}(p,q)\)]]. Explicitly, it consists of matrices joined to the identity by a continuous path inside
\[
\{A\in\operatorname{GL}(p+q,\mathbb R):
A^{\mathsf T}I_{p,q}A=I_{p,q},\ \det A=1\},
\qquad I_{p,q}=\operatorname{diag}(-I_p,I_q).
\]
The parameter \(p\) counts negative directions. Multiplication and inversion are the inherited matrix operations; \(\operatorname{SO}^{+}(p,q)\) is another notation for this same identity component.

## Dimension and compactness

The identity component is an open [[lie-groups/normal-lie-subgroup|normal Lie subgroup]], so it has the same
[[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]] and dimension as the full group:
\[
\mathfrak{so}(p,q)=\{X:X^{\mathsf T}I_{p,q}+I_{p,q}X=0\},
\qquad
\dim_{\mathbb R}\operatorname{SO}_0(p,q)=\frac{(p+q)(p+q-1)}2.
\]
Indeed, \(X\mapsto I_{p,q}X\) identifies these tangent matrices with skew-symmetric matrices, whose entries above the diagonal are independent.

If \(p=0\) or \(q=0\), the group is compact \(\operatorname{SO}(p+q)\).
If \(p,q>0\), the group is noncompact: on one negative and one positive
coordinate, the matrices
\[
\begin{pmatrix}\cosh t&\sinh t\\\sinh t&\cosh t\end{pmatrix},\qquad t\in\mathbb R,
\]
extended by the identity on the remaining coordinates, form an unbounded continuous path through the identity.

## Split orthogonal examples

The Lie algebra of \(\operatorname{SO}_0(r,r+1)\) is split of type \(B_r\),
and that of \(\operatorname{SO}_0(r,r)\) is split of type \(D_r\).
The visual table uses \(r\ge2\) for \(B_r\) and \(r\ge4\) for \(D_r\),
with real dimensions \(r(2r+1)\) and \(r(2r-1)\), respectively.
These entries specify connected matrix groups. Their Lie-algebra types alone
do not specify a global covering or a [[lie-groups/central-quotient-of-a-lie-group|central quotient]].

The fixed specialization \(p=1,q=3\) is the
[[lie-groups/proper-orthochronous-lorentz-group|proper orthochronous Lorentz group]].

## References

1. [Pavel Etingof, *Lie Groups and Lie Algebras* (MIT lecture notes)](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §2.4, Proposition 2.6, pp. 21–22 (identity components); §6.1, p. 38 (orthogonal matrix groups); §41.2, pp. 219–220 (split orthogonal Lie algebras). The signature convention here counts negative directions first; exchanging the two entries gives an isomorphic group.
