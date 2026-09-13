+++
id = "harmonic-analysis/oscillatory-phase"
title = "Oscillatory phase"
kind = "definition"
summary = "A real-valued function used as the argument of a complex exponential."
aliases = ["phase function"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "real-analysis/exponential-function", "real-analysis/class-ck-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **oscillatory phase** is a real-valued [[shared-foundations/function|function]] \(\Phi(t,x)\) appearing in a factor \(e^{i\kappa\Phi(t,x)}\), with a fixed nonzero frequency parameter \(\kappa\). Smooth phases permit differentiation by the chain rule. The exponential depends on \(\kappa\Phi\) modulo \(2\pi\).

## Locally defined phases

On a periodic domain the exponential can be globally defined even when a real-valued phase exists only in local charts. Two local phases give the same exponential on an overlap if their difference lies in \((2\pi/\kappa)\mathbb Z\). For continuous lifts on a connected overlap this integer difference is constant.

[[real-analysis/auxiliary-variable-evaluation|Evaluating a field along an auxiliary map]] is a separate composition operation. Averaging in independent auxiliary variables before this composition need not equal averaging the composed physical field.
