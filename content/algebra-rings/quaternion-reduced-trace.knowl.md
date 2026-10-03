+++
id = "algebra-rings/quaternion-reduced-trace"
title = "Reduced trace in a quaternion algebra"
kind = "definition"
summary = "The scalar obtained by adding a quaternion to its standard conjugate."
aliases = ["quaternion reduced trace", "reduced trace of a quaternion"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-algebra", "algebra-rings/quaternion-conjugation"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

The **reduced trace** of \(x\) in a [[algebra-rings/quaternion-algebra|quaternion algebra]] \(B\) over a field \(F\) of characteristic different from two is
\[
\operatorname{trd}(x)=x+\bar x\in F,
\]
where \(\bar x\) is [[algebra-rings/quaternion-conjugation|standard conjugation]]. In a presentation \(B=(a,b)_F\), one has
\[
\operatorname{trd}(x_0+x_1i+x_2j+x_3ij)=2x_0.
\]

## Trace identities

The map is \(F\)-linear and satisfies \(\operatorname{trd}(xy)=\operatorname{trd}(yx)\). Together with the [[algebra-rings/quaternion-reduced-norm|reduced norm]], it gives the identity
\[
x^2-\operatorname{trd}(x)x+\operatorname{nrd}(x)=0.
\]
This follows by expanding and using \(x\bar x=\bar xx\).

## Two different traces

In \(M_2(F)\), reduced trace is ordinary matrix trace. On the four-dimensional vector space \(B\), however, the linear operator \(L_x:y\mapsto xy\) has ordinary trace \(2\operatorname{trd}(x)\). Reduced trace should not be confused with the trace of that regular representation.

The kernel is the space of [[algebra-rings/pure-quaternion|pure quaternions]].

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), §3.3, reduced trace and norm.
