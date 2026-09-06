+++
id = "algebra-groups/projective-special-linear-group"
title = "Projective special linear group"
kind = "definition"
summary = "The special linear group modulo its scalar center."
aliases = ["PSL", "unimodular projective group", "projective unimodular group"]
domains = ["algebra-groups", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["lie-groups/special-linear-group", "algebra-groups/quotient-group", "algebra-groups/normal-subgroup", "linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(n\ge2\) and let \(k\) be a field. The **projective special linear group** is
\[
\operatorname{PSL}_n(k)
:=\operatorname{SL}_n(k)/Z(\operatorname{SL}_n(k)).
\]
The center consists exactly of scalar matrices
\[
Z(\operatorname{SL}_n(k))
=\{\lambda I_n:\lambda\in k^\times,\ \lambda^n=1\}.
\]

## Projective realization

The inclusion \(\operatorname{SL}_n(k)\hookrightarrow\operatorname{GL}_n(k)\) followed by the quotient to the [[algebra-groups/projective-general-linear-group|projective general linear group]] has kernel \(Z(\operatorname{SL}_n(k))\). It therefore identifies \(\operatorname{PSL}_n(k)\) with a [[algebra-groups/normal-subgroup|normal subgroup]] of \(\operatorname{PGL}_n(k)\), acting faithfully on \(\mathbb P^{n-1}(k)\).

This is a definition of the abstract group of \(k\)-points. The central quotient of the corresponding [[algebraic-geometry-foundations/algebraic-group|algebraic group]] and its \(k\)-points require care over non-algebraically closed fields; the present page makes no assertion that taking \(k\)-points commutes with every quotient construction.

## Comparison with \(\operatorname{PGL}\)

Over an [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]], every nonzero scalar has an \(n\)-th root, and \(\operatorname{PSL}_n(k)=\operatorname{PGL}_n(k)\) as subgroups of projective transformations. Over a general field they may differ; the precise quotient is \(k^\times/(k^\times)^n\).

## References

1. James S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, Cambridge University Press, 2017. [Author-maintained text](https://www.jmilne.org/math/CourseNotes/ala.html). Relevant: \(\operatorname{SL}_n\), centers, and central quotients.
2. Jean-Pierre Serre, *Linear Representations of Finite Groups*, Springer, 1977. [Publisher record](https://doi.org/10.1007/978-1-4684-9458-7). Relevant: projective linear groups as standard finite-group examples.
