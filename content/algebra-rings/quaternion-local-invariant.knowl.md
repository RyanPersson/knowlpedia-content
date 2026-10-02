+++
id = "algebra-rings/quaternion-local-invariant"
title = "Local Brauer invariant of a quaternion algebra"
kind = "definition"
summary = "The value zero or one-half modulo integers associated with a split or division quaternion algebra over a local field."
aliases = ["quaternion local invariant", "local invariant of a quaternion algebra"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/brauer-group", "algebra-fields-galois/local-field", "algebra-rings/quaternion-algebra"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

For a [[algebra-rings/quaternion-algebra|quaternion algebra]] \(B\) over a [[algebra-fields-galois/local-field|local field]] \(F\) of characteristic different from two, its **local Brauer invariant** is
\[
\operatorname{inv}_F(B)=
\begin{cases}
0 & B\cong M_2(F),\\
\tfrac12\pmod{\mathbb Z} & B\text{ is a division algebra},
\end{cases}
\qquad\text{in }\mathbb Q/\mathbb Z.
\]

It is the restriction of the local invariant map on the [[algebra-rings/brauer-group|Brauer group]]. For \(F=\mathbb C\), only the value zero occurs.

## Sign versus additive invariant

When \(\operatorname{char}F\ne2\), the [[algebra-rings/hilbert-symbol|Hilbert symbol]] of a presentation takes the value \(+1\) for invariant zero and \(-1\) for invariant \(\tfrac12\). The additive invariant is not the sign itself.

## Global consistency

For a quaternion algebra over a [[algebra-fields-galois/number-field|number field]] \(K\), the invariants of \(B\otimes_KK_v\) sum to zero in \(\mathbb Q/\mathbb Z\). This expresses the even parity of the [[algebra-rings/quaternion-ramification|ramification set]].

The rational Hamilton algebra has local invariant \(\tfrac12\) at \(2\) and at \(\infty\), and zero elsewhere. Their sum is \(1\), which is zero modulo \(\mathbb Z\).

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Remark 13.4.3 and Remark 14.6.10, especially the quaternion specialization following (14.6.11).
