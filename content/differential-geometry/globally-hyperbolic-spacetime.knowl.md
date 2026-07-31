+++
id = "differential-geometry/globally-hyperbolic-spacetime"
title = "Globally hyperbolic spacetime"
kind = "definition"
summary = "A strongly causal spacetime in which every causal diamond is compact."
aliases = ["global hyperbolicity", "globally hyperbolic Lorentzian manifold"]
domains = ["differential-geometry", "mathematical-physics", "partial-differential-equations"]
section_mode = "progressive"
+++

A time-oriented [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] \((M,g)\) is **globally hyperbolic** if it is [[differential-geometry/strong-causality|strongly causal]] and every [[differential-geometry/causal-diamond|causal diamond]]
\[
J^+(p)\cap J^-(q)
\]
is compact.

The [[differential-geometry/global-hyperbolicity-and-cauchy-hypersurfaces|Cauchy-hypersurface characterization]] and the [[differential-geometry/smooth-splitting-of-globally-hyperbolic-spacetimes|smooth splitting theorem]] are equivalent global descriptions and consequences, not additional clauses in this definition. Global hyperbolicity is also the geometric hypothesis in the [[mathematical-physics/cauchy-problem-for-normally-hyperbolic-operators|global Cauchy theorem]] for normally hyperbolic operators.

## Examples and non-examples

[[mathematical-physics/minkowski-spacetime|Minkowski spacetime]] is globally hyperbolic; each constant-time hyperplane is a [[differential-geometry/cauchy-hypersurface|Cauchy hypersurface]]. The static cylinder \(\mathbb R\times\Sigma\) with metric \(-dt^2+h\), for complete Riemannian \((\Sigma,h)\), is globally hyperbolic. A spacetime with a closed timelike curve is not strongly causal and therefore is not globally hyperbolic.

## References

1. Antonio N. Bernal and Miguel Sánchez, “Smoothness of time functions and the metric splitting of globally hyperbolic spacetimes,” *Communications in Mathematical Physics* 257 (2005), 43–50. [Journal record](https://doi.org/10.1007/s00220-005-1346-1).
2. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §§1.3 and 3.2.
