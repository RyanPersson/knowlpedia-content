+++
id = "fluid-dynamics/centripetal-acceleration"
title = "Centripetal acceleration for circular motion"
kind = "definition"
summary = "The inward normal acceleration v²/r required by motion along a circle."
aliases = ["centripetal force per unit mass"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["real-analysis/cylindrical-coordinates", "real-analysis/chain-rule", "fluid-dynamics/angular-velocity"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For motion along a circle of fixed radius \(r>0\), the **centripetal acceleration** is the inward radial component
\[
a_r=-\frac{v_\theta^2}{r}=-r\Omega^2.
\]
Indeed, differentiating \(v_\theta e_\theta\) gives the radial term \(v_\theta\dot\theta(-e_r)\), and \(v_\theta=r\dot\theta\). A changing speed also gives a tangential acceleration.

## Radial pressure balance

For a stationary inviscid purely circular flow \(u=V(r)e_\theta\) with no external force, the radial momentum equation is
\[
\partial_rp=\frac{V(r)^2}{r}.
\]
The pressure therefore increases radially outward, so the pressure acceleration \(-\nabla p\) points inward. This sign follows from the inertial-frame material acceleration.
