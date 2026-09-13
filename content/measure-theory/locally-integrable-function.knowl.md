+++
id = "measure-theory/locally-integrable-function"
title = "Locally integrable function"
kind = "definition"
summary = "A measurable function integrable on every compact subset of its Euclidean open domain."
aliases = ["local integrability", "L1loc"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/lebesgue-integrable-function", "measure-theory/lebesgue-measure", "topology/compact-set", "topology/open-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A measurable scalar or finite-dimensional vector-valued function \(f\) on an open set \(U\subseteq\mathbb R^n\) is **locally integrable**, written \(f\in L^1_{\mathrm{loc}}(U)\), if
\[
\int_K |f(x)|\,dx<\infty
\quad\text{for every [[topology/compact-set|compact]] }K\subset U.
\]
Here \(|f|\) is absolute value or the Euclidean norm. As with [[measure-theory/lp-space|Lebesgue spaces]], functions are identified almost everywhere.

## Local versus global

The constant function one lies in \(L^1_{\mathrm{loc}}(\mathbb R^n)\) but not in \(L^1(\mathbb R^n)\). Every continuous function is locally integrable, and Hölder's inequality gives \(L^p_{\mathrm{loc}}\subseteq L^1_{\mathrm{loc}}\) for \(p\ge1\). Local integrability is sufficient to integrate \(f\) against any smooth compactly supported test function, giving a regular distribution.
