+++
id = "fluid-dynamics/kinetic-energy"
title = "Kinetic energy of an incompressible velocity field"
kind = "definition"
summary = "Half the squared spatial L2 norm when density is normalized to one."
aliases = ["fluid kinetic energy", "finite-energy velocity"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "measure-theory/lp-norm", "linear-algebra/euclidean-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

With constant density normalized to one, the **kinetic energy** of a [[fluid-dynamics/velocity-field|velocity field]] on \(\Omega\) at time \(t\) is
\[
E(t)=\frac12\int_\Omega|u(t,x)|^2\,dx
=\frac12\|u(t,\cdot)\|_{L^2(\Omega)}^2.
\]
It is finite exactly when the velocity belongs to spatial \(L^2\). For physical constant density \(\rho\), multiply the expression by \(\rho\).

## Uniform energy bounds

[[fluid-dynamics/bounded-kinetic-energy|Uniformly bounded kinetic energy]] specifies a bound uniform in time. This alone does not bound spatial derivatives or the pointwise magnitude of velocity. Energy identities and inequalities use the equation and appropriate boundary or decay assumptions in addition to this definition.

## Energy estimates

See the [[fluid-dynamics/kinetic-energy-identity|global energy identity]], [[fluid-dynamics/kinetic-energy-inequality|energy inequality]], and [[fluid-dynamics/viscous-dissipation|viscous dissipation]].
