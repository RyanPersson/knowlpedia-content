+++
id = "mathematical-physics/existence-of-advanced-and-retarded-green-operators"
title = "Existence of advanced and retarded Green operators"
kind = "theorem"
summary = "A normally hyperbolic operator on a globally hyperbolic spacetime has unique future and past Green operators."
aliases = ["existence of causal Green operators", "Green hyperbolicity of normally hyperbolic operators"]
domains = ["mathematical-physics", "partial-differential-equations"]
prerequisites = ["mathematical-physics/normally-hyperbolic-operator","differential-geometry/globally-hyperbolic-spacetime","mathematical-physics/advanced-and-retarded-green-operators"]
dependency_review_count = 1
section_mode = "progressive"
+++

Every [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic operator]] on a vector bundle over a [[differential-geometry/globally-hyperbolic-spacetime|globally hyperbolic spacetime]] has unique future and past [[mathematical-physics/advanced-and-retarded-green-operators|Green operators]] \(G^+\) and \(G^-\).

For each compactly supported source \(f\), the section \(G^+f\) is the unique solution of \(Pu=f\) supported in \(J^+(\operatorname{supp}f)\), and \(G^-f\) is the unique solution supported in \(J^-(\operatorname{supp}f)\). Their difference
\[
G=G^+-G^-
\]
solves the homogeneous equation after applying \(P\) and is called the causal propagator.

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: Corollary 3.4.3.
