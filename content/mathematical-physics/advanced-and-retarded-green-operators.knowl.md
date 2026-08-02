+++
id = "mathematical-physics/advanced-and-retarded-green-operators"
title = "Advanced and retarded Green operators"
kind = "definition"
summary = "Two-sided Green operators on compactly supported sections whose outputs have future- or past-causal support."
aliases = ["causal Green operators", "advanced Green operator", "retarded Green operator"]
domains = ["mathematical-physics", "partial-differential-equations"]
section_mode = "progressive"
+++

Let \(P:\Gamma^\infty(E)\to\Gamma^\infty(E)\) be a differential operator on a time-oriented [[differential-geometry/lorentzian-manifold|Lorentzian manifold]]. A **future Green operator** \(G^+\) and a **past Green operator** \(G^-\) are linear maps
\[
G^\pm:\Gamma^\infty_c(E)\longrightarrow\Gamma^\infty(E)
\]
such that, for every compactly supported smooth section \(f\),
\[
P G^\pm f=f,\qquad G^\pm P f=f,
\]
and
\[
\operatorname{supp}(G^\pm f)\subseteq J^\pm(\operatorname{supp}f).
\]
Here \(J^\pm\) are the [[differential-geometry/chronological-and-causal-future|causal future and past]].

These are often called the **advanced** and **retarded** Green operators. Naming conventions for “advanced” and “retarded” vary, so the signs and causal support conditions above fix the meaning unambiguously in this collection.

The [[mathematical-physics/existence-of-advanced-and-retarded-green-operators|Green-operator existence theorem]] supplies a unique pair for every [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic operator]] on a [[differential-geometry/globally-hyperbolic-spacetime|globally hyperbolic spacetime]].

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: Definition 3.4.1.
