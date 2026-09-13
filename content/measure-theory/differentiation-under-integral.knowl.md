+++
id = "measure-theory/differentiation-under-integral"
title = "Differentiation under an integral sign"
kind = "theorem"
summary = "An integrable bound on parameter derivatives justifies passing a derivative through an integral."
aliases = ["differentiation under the integral sign", "parameter differentiation under an integral"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/integrable-majorant", "measure-theory/dominated-convergence-theorem", "real-analysis/mean-value-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(I\) be an open real interval and \(F(t,x)\) measurable in \(x\). Suppose outside a fixed null set, \(F(\cdot,x)\) is \(C^1\) on \(I\), and \(F(t_0,\cdot)\in L^1(X,\mu)\) for some \(t_0\in I\). Suppose each compact subinterval \(J\subset I\) has an [[measure-theory/integrable-majorant|integrable majorant]] \(g_J\) with \(|\partial_tF(t,x)|\le g_J(x)\) for all \(t\in J\). Then
\[
\frac{d}{dt}\int_X F(t,x)\,d\mu(x)=\int_X\partial_tF(t,x)\,d\mu(x).
\]

## Justification and higher orders

The mean value theorem bounds a difference quotient by a majorant on a slightly larger parameter interval. Dominated convergence then passes its limit through the integral. Applying the same argument to derivatives proves the \(C^k\) version when derivatives through order \(k\) have local integrable majorants. A moving integration domain contributes boundary terms and is not covered by this fixed-domain statement.
