+++
id = "differential-geometry/strong-causality"
title = "Strong causality"
kind = "definition"
summary = "The condition that every event has arbitrarily small neighborhoods which causal curves cannot leave and then re-enter."
aliases = ["strongly causal spacetime", "strong causality condition"]
domains = ["differential-geometry", "mathematical-physics"]
section_mode = "progressive"
prerequisites = ["differential-geometry/lorentzian-manifold", "differential-geometry/causal-curve"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A time-oriented [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] \((M,g)\) is **strongly causal at** \(p\in M\) if every neighborhood \(U\) of \(p\) contains a neighborhood \(V\) of \(p\) such that no [[differential-geometry/causal-curve|causal curve]] intersects \(V\) in a disconnected set. It is **strongly causal** if it is strongly causal at every point.

Equivalently, each point has arbitrarily small causally convex neighborhoods: if both endpoints of a causal curve lie in such a neighborhood, the whole curve lies there. Strong causality excludes closed causal curves and also excludes “almost closed” causal curves that repeatedly return arbitrarily close to an event.

Strong causality, together with compactness of every [[differential-geometry/causal-diamond|causal diamond]], is the definition of a [[differential-geometry/globally-hyperbolic-spacetime|globally hyperbolic spacetime]] used in this collection.

## References

1. Robert M. Wald, *General Relativity*, University of Chicago Press, 1984. [Publisher record](https://doi.org/10.7208/chicago/9780226870373.001.0001). Relevant: §8.3.
2. Ettore Minguzzi, “Lorentzian causality theory,” *Living Reviews in Relativity* 22 (2019), article 3. [Journal record](https://doi.org/10.1007/s41114-019-0019-x).
