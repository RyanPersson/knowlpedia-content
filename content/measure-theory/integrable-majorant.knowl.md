+++
id = "measure-theory/integrable-majorant"
title = "Integrable majorant for a family"
kind = "definition"
summary = "A single integrable function controlling every member of a parameterized family almost everywhere."
aliases = ["integrable domination", "dominating integrable function"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/l1-function", "measure-theory/almost-everywhere", "shared-foundations/function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **integrable majorant** for a [[shared-foundations/function|parameterized family]] \(f_\lambda\) is a nonnegative \(g\in L^1(X,\mu)\) such that \(|f_\lambda(x)|\le g(x)\) almost everywhere for every relevant parameter \(\lambda\). To use a pointwise limit argument, specify the exceptional null sets and, when necessary, a common null set for the parameter neighborhood.

## Uniform control for limits

For a sequence converging almost everywhere, this hypothesis permits [[measure-theory/dominated-convergence-theorem|dominated convergence]]. Having a bound \(\int|f_\lambda|\le C\) alone is weaker: the functions \(f_n=n\mathbf1_{(0,1/n)}\) converge to zero almost everywhere on \((0,1)\) but their integrals stay one.

## Parameter derivatives

For differentiation under an integral, the relevant majorant usually bounds the parameter derivative throughout a neighborhood, so that it also bounds the difference quotients by the mean value theorem.
