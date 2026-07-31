+++
id = "mathematical-physics/conformal-coupling-of-a-scalar-field"
title = "Conformal coupling of a scalar field"
kind = "definition"
summary = "The scalar-curvature coupling that makes the massless wave equation conformally covariant."
aliases = ["conformally coupled scalar field", "conformal scalar coupling", "conformal wave operator"]
domains = ["mathematical-physics", "partial-differential-equations", "differential-geometry"]
section_mode = "progressive"
+++

On an \(n\)-dimensional pseudo-Riemannian manifold with \(n\geq3\), the **conformally coupled scalar operator** in the convention
\(\Box_g=-\operatorname{tr}_g\nabla d\) is
\[
L_g=\Box_g+\frac{n-2}{4(n-1)}\operatorname{Scal}_g,
\]
where \(\operatorname{Scal}_g\) is the [[differential-geometry/scalar-curvature|scalar curvature]]. The **conformally coupled massless scalar equation** is \(L_g\phi=0\).

If \(\widetilde g=\Omega^2g\) for a positive smooth function \(\Omega\), then
\[
L_{\widetilde g}\!\left(\Omega^{-(n-2)/2}\phi\right)
=\Omega^{-(n+2)/2}L_g\phi.
\]
This covariance distinguishes the coefficient
\[
\xi_n=\frac{n-2}{4(n-1)}
\]
from the minimally coupled value \(\xi=0\). A nonzero mass term breaks this conformal covariance.

## References

1. Robert M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics*, University of Chicago Press, 1994. [Publisher record](https://doi.org/10.7208/chicago/9780226870274.001.0001). Relevant: Chapter 4.
