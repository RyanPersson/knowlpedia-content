+++
id = "algebra-groups/pgl-psl-comparison"
title = "PGL–PSL comparison"
kind = "theorem"
summary = "Determinant modulo nth powers measures the difference between PGL_n(k) and PSL_n(k)."
aliases = ["determinant modulo nth powers", "PGL versus PSL", "PGL PSL exact sequence"]
domains = ["algebra-groups", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebra-groups/projective-general-linear-group", "algebra-groups/projective-special-linear-group", "linear-algebra/determinant", "algebra-groups/exact-sequence-groups"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(n\ge2\) and let \(k\) be a field. Determinant induces a well-defined surjective homomorphism
\[
\overline{\det}:\operatorname{PGL}_n(k)\longrightarrow
k^\times/(k^\times)^n,\qquad
[A]\longmapsto [\det A],
\]
whose kernel is the embedded [[algebra-groups/projective-special-linear-group|\(\operatorname{PSL}_n(k)\)]]. Hence there is a short exact sequence of abstract groups
\[
1\longrightarrow\operatorname{PSL}_n(k)
\longrightarrow\operatorname{PGL}_n(k)
\xrightarrow{\ \overline{\det}\ }
k^\times/(k^\times)^n
\longrightarrow1.
\]

## Why the determinant descends

Replacing \(A\) by another representative \(\lambda A\) of its projective class multiplies the determinant by \(\lambda^n\), so its class modulo \(n\)-th powers is unchanged. Surjectivity follows from
\[
\det\operatorname{diag}(a,1,\ldots,1)=a.
\]
If \(\det A=\lambda^n\), then \(\lambda^{-1}A\in\operatorname{SL}_n(k)\) and represents the same projective class. This proves the kernel statement.

## Important fields

For \(k=\mathbb C\), every nonzero complex number is an \(n\)-th power, so
\[
\operatorname{PGL}_n(\mathbb C)=\operatorname{PSL}_n(\mathbb C).
\]
For \(k=\mathbb R\), the quotient is trivial when \(n\) is odd and has two elements when \(n\) is even. Therefore
\[
\operatorname{PGL}_n(\mathbb R)=\operatorname{PSL}_n(\mathbb R)
\quad\text{for odd }n,
\]
whereas \(\operatorname{PSL}_n(\mathbb R)\) has index \(2\) in \(\operatorname{PGL}_n(\mathbb R)\) for even \(n\). In particular, \(\operatorname{PSL}_2(\mathbb R)\ne\operatorname{PGL}_2(\mathbb R)\).

For a [[algebra-fields-galois/finite-field|finite field]] \(\mathbb F_q\), the quotient has order \(\gcd(n,q-1)\), since \(\mathbb F_q^\times\) is cyclic. Thus equality is controlled by arithmetic in the ground field, not by notation.

## Scope warning

This exact sequence concerns groups of \(k\)-valued matrices modulo scalar matrices. It should not be confused with an exact sequence of [[algebraic-geometry-foundations/group-scheme|group schemes]] followed blindly by \(k\)-points: taking rational points of a quotient need not be right-exact.

## References

1. James S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, Cambridge University Press, 2017. [Author-maintained text](https://www.jmilne.org/math/CourseNotes/ala.html). Relevant: central quotients and classical groups.
2. Roger W. Carter, *Simple Groups of Lie Type*, Wiley, 1972. [Publisher record](https://doi.org/10.1002/9781118033093). Relevant: Chapter 1, projective linear groups over finite fields.
