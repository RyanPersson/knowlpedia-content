+++
id = "functional-analysis/singular-values"
title = "Singular values of a compact operator"
kind = "definition"
summary = "The decreasing eigenvalue sequence of the absolute value of a compact Hilbert-space operator."
aliases = ["s-numbers", "singular-value sequence", "approximation numbers"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/compact-operator", "linear-algebra/hilbert-space", "real-analysis/absolute-value"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(T:H\to K\) be a
[[linear-algebra/compact-operator|compact operator]] between [[linear-algebra/hilbert-space|Hilbert spaces]].
Its [[real-analysis/absolute-value|absolute value]] is the positive compact operator
\[
|T|=(T^*T)^{1/2}\quad\text{on }H.
\]
The **singular values** \(s_1(T)\geq s_2(T)\geq\cdots\geq0\) are the nonzero
eigenvalues of \(|T|\), repeated according to multiplicity and arranged in
nonincreasing order, followed by zeros when appropriate. Equivalently, for
\(n\geq1\),
\[
s_n(T)=\inf\{\|T-F\|:\operatorname{rank}(F)<n\}.
\]
This approximation-number formulation also fixes the zero tail and remains
unambiguous when \(H\) or \(K\) is not separable.

## Fundamental properties

The first singular value is the [[linear-algebra/operator-norm|operator norm]]:
\(s_1(T)=\|T\|\). Compactness is equivalent to
\(s_n(T)\to0\) when the zero tail is included, and
\(s_n(T)=s_n(T^*)\) for every \(n\). Unitary changes of coordinates on the
source or target do not alter the sequence. These facts make singular values
the coordinate-free infinite-dimensional analogue of the singular values of
a matrix.

## Approximation and ideal estimates

The formula using rank-\(<n\) operators measures the best possible
operator-norm approximation of \(T\) by low-rank maps. It implies, for bounded
operators \(A\) and \(B\),
\[
s_n(ATB)\leq\|A\|\,s_n(T)\,\|B\|.
\]
Hence decay conditions on the sequence define two-sided operator ideals.
Summability of \((s_n(T))\) gives the trace-class and Schatten conditions,
while weaker rates lead to [[operator-algebras/weak-schatten-ideal|weak Schatten ideals]].

## Examples and boundary cases

For the diagonal operator
\(T(x_1,x_2,\ldots)=(\lambda_1x_1,\lambda_2x_2,\ldots)\) on
\(\ell^2\), with \(\lambda_n\to0\), the singular values are the numbers
\(|\lambda_n|\) rearranged in decreasing order. A rank-\(r\) operator has
\(s_n(T)=0\) for \(n>r\). A bounded diagonal operator whose diagonal entries
do not tend to zero is not compact, so it does not have a singular-value
sequence tending to zero in this sense.

## References

1. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., American Mathematical Society, 2005. [DOI record](https://doi.org/10.1090/surv/120). Relevant: §§1–2 on singular values, approximation numbers, and ideal inequalities.
2. Israel Gohberg and Mark Krein, *Introduction to the Theory of Linear Nonselfadjoint Operators*, American Mathematical Society, 1969. [AMS record](https://bookstore.ams.org/mmono-18). Relevant: Chapter II on characteristic numbers of compact operators.
