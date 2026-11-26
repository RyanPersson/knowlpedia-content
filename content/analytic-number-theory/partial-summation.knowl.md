+++
id = "analytic-number-theory/partial-summation"
title = "Partial summation"
kind = "definition"
summary = "A finite summation-by-parts identity relating a weighted sum to partial sums of its coefficients."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["shared-foundations/finite-sum"]
+++

For a sequence \(a_n\) put \(A(t)=\sum_{1\le n\le t}a_n\). If \(w\) is continuously differentiable on \([1,x]\), **partial summation** rewrites a [[shared-foundations/finite-sum|finite sum]] as
\[
\sum_{1\le n\le x}a_n w(n)=A(x)w(x)-\int_1^x A(t)w'(t)\,dt.
\]
Indeed \(w(n)=w(x)-\int_n^x w'(t)\,dt\), and interchanging the finite sum and the integral gives the formula.

## A weight that vanishes at the cutoff

For \(w(t)=1/t-1/x\), \(w(x)=0\) and \(-w'(t)=1/t^2\). The weighted sum equals \(\int_1^x A(t)t^{-2}\,dt\).
