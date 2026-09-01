+++
id = "differential-geometry/causal-curve"
title = "Causal curve"
kind = "definition"
summary = "A curve in a time-oriented Lorentzian manifold whose tangent vectors are everywhere future-directed or everywhere past-directed and nonspacelike."
aliases = ["nonspacelike curve"]
domains = ["differential-geometry", "mathematical-physics"]
prerequisites = ["differential-geometry/lorentzian-manifold", "differential-geometry/time-orientation", "differential-geometry/chronological-and-causal-future"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,g)\) be a [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] with a [[differential-geometry/time-orientation|time orientation]]. A piecewise \(C^1\) curve \(\gamma:I\to M\) is **future-directed causal** if, wherever \(\dot\gamma\) exists and is nonzero,
\[
g(\dot\gamma,\dot\gamma)\leq 0
\]
and \(\dot\gamma\) lies in the chosen future cone. A **past-directed causal curve** is defined using the past cone. Either is called a **causal curve**.

A causal curve is **timelike** if \(g(\dot\gamma,\dot\gamma)<0\) wherever its tangent is nonzero, and **null** if \(g(\dot\gamma,\dot\gamma)=0\). Definitions using locally Lipschitz curves impose the same condition almost everywhere and include the piecewise-smooth curves used here.

Future-directed causal and timelike curves define the [[differential-geometry/chronological-and-causal-future|causal and chronological relations]] on spacetime.

## References

1. Barrett O'Neill, *Semi-Riemannian Geometry With Applications to Relativity*, Academic Press, 1983. [Publisher record](https://doi.org/10.1016/C2009-0-03118-3). Relevant: Chapter 14.
2. Ettore Minguzzi, “Lorentzian causality theory,” *Living Reviews in Relativity* 22 (2019), article 3. [Journal record](https://doi.org/10.1007/s41114-019-0019-x).
