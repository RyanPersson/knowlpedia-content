+++
id = "mathematical-physics/cauchy-problem-for-the-lorentzian-dirac-operator"
title = "Cauchy problem for the Lorentzian Dirac operator"
kind = "theorem"
summary = "Initial spinor data on a smooth spacelike Cauchy hypersurface determine a unique Lorentzian Dirac solution with causal propagation."
aliases = ["Lorentzian Dirac Cauchy theorem", "well-posedness of the Dirac equation on globally hyperbolic spacetimes"]
domains = ["mathematical-physics", "partial-differential-equations", "differential-geometry"]
prerequisites = ["differential-geometry/lorentzian-dirac-operator", "differential-geometry/globally-hyperbolic-spacetime", "differential-geometry/cauchy-hypersurface", "mathematical-physics/dirac-equation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(D_g\) be the
[[differential-geometry/lorentzian-dirac-operator|Lorentzian Dirac operator]]
on a spinor bundle \(S\to M\) over a
[[differential-geometry/globally-hyperbolic-spacetime|globally hyperbolic
spacetime]]. Let \(\Sigma\subset M\) be a smooth spacelike
[[differential-geometry/cauchy-hypersurface|Cauchy hypersurface]]. For every
compactly supported smooth source \(f\in\Gamma^\infty_c(S)\) and compactly
supported smooth initial spinor
\(\psi_0\in\Gamma^\infty_c(S|_\Sigma)\), there is a unique smooth spinor
\(\psi\in\Gamma^\infty(S)\) satisfying
\[
D_g\psi=f,
\qquad
\psi|_\Sigma=\psi_0.
\]

The solution has finite propagation speed:
\[
\operatorname{supp}\psi
\subseteq
J\!\left(\operatorname{supp}f\cup\operatorname{supp}\psi_0\right).
\]
Thus the Lorentzian [[mathematical-physics/dirac-equation|Dirac equation]] has one freely prescribed spinor trace on
\(\Sigma\), unlike the two traces required by a second-order normally
hyperbolic equation.

The same conclusion holds for Dirac operators with smooth zeroth-order terms,
including a constant mass term. Such operators also have unique
[[mathematical-physics/advanced-and-retarded-green-operators|advanced and
retarded Green operators]] on a globally hyperbolic spacetime.

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on
   Lorentzian Manifolds and Quantization*, European Mathematical Society,
   2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §3.4.
