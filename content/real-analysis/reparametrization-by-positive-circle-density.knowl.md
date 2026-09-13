+++
id = "real-analysis/reparametrization-by-positive-circle-density"
title = "Circle reparametrization by a positive density"
kind = "theorem"
summary = "Integrating a positive normalized periodic density gives an orientation-preserving circle diffeomorphism."
aliases = ["density reparametrization of a loop"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/periodic-function", "real-analysis/fundamental-theorem-of-calculus-i", "real-analysis/implicit-function-theorem", "real-analysis/substitution-rule", "topology/flat-torus"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(\rho\) be a smooth positive \(1\)-periodic function with \(\int_0^1\rho(s)\,ds=1\). Define
\[
\Phi(\theta)=\int_0^\theta\rho(s)\,ds.
\]
Then \(\Phi'=\rho>0\) and \(\Phi(\theta+1)=\Phi(\theta)+1\), so \(\Phi\) induces a smooth invertible map of the [[topology/flat-torus|unit circle]] with a smooth inverse.

## Changing an average

For \(g(\phi)=f(\Phi^{-1}(\phi))\), substitution yields
\[
\int_0^1g(\phi)\,d\phi=\int_0^1 f(\theta)\rho(\theta)\,d\theta.
\]
Thus the parameter speed changes how long a loop spends at each of its values. If the density depends smoothly on a compact parameter set and has a common positive lower bound, the inverse reparametrizations depend smoothly on those parameters, with bounded derivatives at every fixed order. A vanishing density would require a separate inverse-regularity analysis.
