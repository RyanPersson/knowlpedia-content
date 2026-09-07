+++
id = "functional-analysis/trace-class-operator"
title = "Trace-Class Operator"
kind = "knowl"
summary = "A bounded operator on a Hilbert space whose singular values are summable."
aliases = ["trace-class-operator", "Trace-Class Operator"]
domains = ["functional-analysis"]
legacy_source_path = "shale-paper/trace-class-operator.md"
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/compact-operator", "functional-analysis/singular-values", "real-analysis/convergent-series"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

Let \(H\) be a [[linear-algebra/hilbert-space|Hilbert space]]. A [[linear-algebra/compact-operator|compact operator]] \(X:H\to H\) is **trace-class** if its [[functional-analysis/singular-values|singular values]] are summable:
\[
\|X\|_1:=\sum_{n=1}^{\infty}s_n(X)<\infty.
\]
The singular values include multiplicities and a zero tail for finite-rank operators. The displayed sum is the **trace norm**.

## Trace

For a trace-class operator, the [[quantum-foundations/trace-operator|operator trace]] is defined and independent of the orthonormal basis. Equivalently, \(\|X\|_1=\operatorname{Tr}|X|\), with the positive operator trace interpreted as a possibly infinite sum before imposing finiteness.

## Remarks


The principal properties used in Shale's paper are:

- The [[functional-analysis/fredholm-determinant-trace-log|Fredholm determinant]] is defined for operators of the form \(I+X\) with \(X\) trace-class.


## Examples


- On \(\ell^2\), \(\mathrm{diag}(a_n)\) is trace-class iff \(\sum_n |a_n|<\infty\).

## References

1. Dan-Virgil Voiculescu, *Math 209: Von Neumann Algebras*, notes by Leonard Tomczak, UC Berkeley, Spring 2024. [Lecture notes](https://math.berkeley.edu/~ltomczak/notes/Spring2024/VNA_Notes.pdf), §4, pp. 7–8, Proposition 4.1 and the singular-value expansion.
