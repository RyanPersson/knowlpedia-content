+++
id = "differential-geometry/globally-hyperbolic-spacetime"
title = "Globally hyperbolic spacetime"
kind = "definition"
summary = "A strongly causal Lorentzian spacetime whose causal diamonds are compact, equivalently one admitting Cauchy hypersurfaces."
aliases = ["global hyperbolicity", "globally hyperbolic Lorentzian manifold"]
domains = ["differential-geometry", "mathematical-physics", "partial-differential-equations"]
section_mode = "progressive"
+++

A time-oriented [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] \((M,g)\) is **globally hyperbolic** if it is strongly causal and every causal diamond
\[
J^+(p)\cap J^-(q)
\]
is compact. Here \(J^+(p)\) and \(J^-(q)\) are the points reachable from \(p\), or able to reach \(q\), by future-directed causal curves. Strong causality rules out causal curves that return arbitrarily close to their starting event. Together the two conditions exclude closed causal curves and prevent causal influence between two events from escaping to infinity and returning.

## Cauchy hypersurfaces

A **Cauchy hypersurface** is a subset met exactly once by every inextendible timelike curve. A spacetime is globally hyperbolic if and only if it admits a Cauchy hypersurface. Moreover, it admits a smooth spacelike Cauchy hypersurface and a smooth splitting
\[
M\cong\mathbb R\times\Sigma,\qquad
g=-\beta\,dt^2+h_t,
\]
where \(\beta>0\) and each \(h_t\) is a Riemannian metric on \(\Sigma\). Each slice \(\{t\}\times\Sigma\) can be chosen to be Cauchy.

## Role in hyperbolic equations

Global hyperbolicity is the standard geometric hypothesis for a global Cauchy
theory. On such a spacetime, a
[[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic
operator]] has unique advanced and retarded Green operators, and smooth
compactly supported initial data on a Cauchy hypersurface determine a unique
smooth solution. The analogous Lorentzian
[[mathematical-physics/dirac-equation|Dirac equation]] also has a well-posed
Cauchy problem.

These conclusions are not consequences of local Lorentzian signature alone. Removing global hyperbolicity can destroy existence, uniqueness, or causal support properties even though the differential operator has the same local principal symbol.

## Examples and non-examples

[[mathematical-physics/minkowski-spacetime|Minkowski spacetime]] is globally hyperbolic; each constant-time hyperplane is Cauchy. The static cylinder \(\mathbb R\times\Sigma\) with metric \(-dt^2+h\), for complete Riemannian \((\Sigma,h)\), is globally hyperbolic. A spacetime with a closed timelike curve is not causal and therefore not globally hyperbolic.

## References

1. Antonio N. Bernal and Miguel Sánchez, “Smoothness of time functions and the metric splitting of globally hyperbolic spacetimes,” *Communications in Mathematical Physics* 257 (2005), 43–50. [Journal record](https://doi.org/10.1007/s00220-005-1346-1).
2. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §§1.3 and 3.2.
