+++
id = "measure-theory/zero-mean-function"
title = "Zero-mean function"
kind = "definition"
summary = "An integrable function whose integral in the specified averaging variables vanishes."
aliases = []
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/lebesgue-integrable-function", "measure-theory/lebesgue-integral", "measure-theory/measure-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

On a [[measure-theory/measure-space|measure space]] \((X,\mu)\) with \(0<\mu(X)<\infty\), an integrable scalar or finite-dimensional vector-valued function \(f\) is **zero mean** if
\[
\int_X f\,d\mu=0.
\]
Equivalently, its normalized average \(\mu(X)^{-1}\int_X f\,d\mu\) vanishes. Vector integrals are interpreted componentwise.

## Variables are part of the definition

A family \(f(x,y)\) can have zero mean in \(y\) for each fixed \(x\), without being independent of \(x\). On a periodic cell, zero mean is equivalent to vanishing of the [[harmonic-analysis/zero-fourier-mode|zero Fourier coefficient]]. Changing the measure or the averaging variables can change whether the condition holds.
