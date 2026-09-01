+++
id = "shale-paper/trace-class-operator"
title = "Trace-Class Operator"
kind = "knowl"
summary = "A bounded operator on a Hilbert space whose singular values are summable."
aliases = ["trace-class-operator", "Trace-Class Operator"]
domains = ["shale-paper"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "shale-paper/trace-class-operator.md"
+++

Let \(H\) be a Hilbert space and \(X:H\to H\) a bounded operator. The operator \(X\) is **trace-class** if
\[
\lVert X\rVert_1:=\operatorname{tr}(|X|)<\infty,
\]
equivalently, if the singular values of \(X\) are summable.

## Remarks

The principal properties used in Shale's paper are:

- The trace \(\mathrm{tr}(X)\) is well-defined and basis-independent.
- The [[shale-paper/fredholm-determinant-trace-log|Fredholm determinant]] is defined for operators of the form \(I+X\) with \(X\) trace-class.

## Examples

- On \(\ell^2\), \(\mathrm{diag}(a_n)\) is trace-class iff \(\sum_n |a_n|<\infty\).
