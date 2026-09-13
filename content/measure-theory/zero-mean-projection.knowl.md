+++
id = "measure-theory/zero-mean-projection"
title = "Projection onto zero-mean functions"
kind = "definition"
summary = "The linear operation subtracting a function’s normalized average."
aliases = []
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/zero-mean-function", "linear-algebra/linear-map", "measure-theory/measure-space", "linear-algebra/vector-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For \(0<\mu(X)<\infty\), the **zero-mean projection** is
\[
P_0f=f-\frac{1}{\mu(X)}\int_X f\,d\mu.
\]
It is linear, its output has [[measure-theory/zero-mean-function|zero mean]], and \(P_0^2=P_0\). It removes exactly the constant component.

## Norms and parameters

On \(L^2(X,\mu)\), it is the orthogonal projection onto the complement of the constants, and \(\|P_0f\|_2\le\|f\|_2\). For \(1\le p\le\infty\), Hölder's inequality gives \(\|P_0f\|_p\le2\|f\|_p\). The notation must specify \(X\) and \(\mu\); averaging only an auxiliary variable leaves the remaining variables as parameters.
