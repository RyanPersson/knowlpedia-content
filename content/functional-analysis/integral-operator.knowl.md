+++
id = "functional-analysis/integral-operator"
title = "Integral operator with a measurable kernel"
kind = "definition"
summary = "A linear operator defined by integration against a kernel K(x,y)."
aliases = ["integral kernel", "kernel operator", "Volterra integral operator"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["measure-theory/lebesgue-integral", "measure-theory/measurable-function", "linear-algebra/linear-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **integral operator** with kernel \(K\) has the form
\[
(Tf)(x)=\int_Y K(x,y)f(y)\,d\nu(y)
\]
on a specified class of functions for which the integral exists. This **kernel** is a function of two variables; it is distinct from the nullspace of a linear map.

## A direct bound

If \(K\) is jointly measurable and \(\sup_x\int|K(x,y)|\,d\nu(y)\le M\), then \(\|Tf\|_{\sup}\le M\|f\|_{\sup}\) on bounded measurable functions. For essential norms, use the corresponding almost-everywhere row bound on sigma-finite product spaces. A formula alone does not establish boundedness on a chosen function space; its kernel estimates do.

## Examples

On \(\mathbb R^n\), taking \(K(x,y)=k(x-y)\) gives convolution. An integral \(\int_a^tK(t,s)f(s)\,ds\) is a Volterra operator and respects the time ordering \(s\le t\).
