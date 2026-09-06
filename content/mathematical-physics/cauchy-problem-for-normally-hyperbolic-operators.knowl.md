+++
id = "mathematical-physics/cauchy-problem-for-normally-hyperbolic-operators"
title = "Cauchy problem for normally hyperbolic operators"
kind = "theorem"
summary = "Compactly supported source and Cauchy data determine a unique smooth solution with finite propagation on a globally hyperbolic spacetime."
aliases = ["Cauchy theorem for normally hyperbolic operators", "well-posedness of the normally hyperbolic Cauchy problem"]
domains = ["mathematical-physics", "partial-differential-equations", "differential-geometry"]
prerequisites = ["mathematical-physics/normally-hyperbolic-operator", "differential-geometry/globally-hyperbolic-spacetime", "differential-geometry/cauchy-hypersurface", "mathematical-physics/connection-form-of-a-normally-hyperbolic-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(P:\Gamma^\infty(E)\to\Gamma^\infty(E)\) be a [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic operator]] on a vector bundle over a [[differential-geometry/globally-hyperbolic-spacetime|globally hyperbolic spacetime]]. Let \(\Sigma\) be a smooth spacelike [[differential-geometry/cauchy-hypersurface|Cauchy hypersurface]] with future-directed unit normal \(\nu\). For
\[
f\in\Gamma^\infty_c(E),\qquad
u_0,u_1\in\Gamma^\infty_c(E|_\Sigma),
\]
there is a unique \(u\in\Gamma^\infty(E)\) satisfying
\[
Pu=f,\qquad
u|_\Sigma=u_0,\qquad
\nabla^E_\nu u|_\Sigma=u_1,
\]
where \(\nabla^E\) is the connection determined by the [[mathematical-physics/connection-form-of-a-normally-hyperbolic-operator|connection form of \(P\)]].

The solution obeys finite propagation:
\[
\operatorname{supp}u
\subseteq
J\!\left(\operatorname{supp}f\cup
\operatorname{supp}u_0\cup
\operatorname{supp}u_1\right),
\qquad
J(A)=J^+(A)\cup J^-(A).
\]
Thus existence, uniqueness, and causal support are global consequences of global hyperbolicity, not of the local principal-symbol condition alone.

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: Theorem 3.2.11.
