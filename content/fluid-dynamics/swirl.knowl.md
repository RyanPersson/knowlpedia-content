+++
id = "fluid-dynamics/swirl"
title = "Swirl component of a cylindrical velocity"
kind = "definition"
summary = "The azimuthal velocity component tangent to circles around the chosen axis."
aliases = ["azimuthal velocity", "tangential cylindrical velocity"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "real-analysis/cylindrical-coordinates", "linear-algebra/inner-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **swirl component** is the scalar \(u_\theta=u\cdot e_\theta\) in [[real-analysis/cylindrical-coordinates|cylindrical coordinates]]
\[
u=u_r e_r+u_\theta e_\theta+u_z e_z.
\]
Its vector contribution \(u_\theta e_\theta\) is tangent to circles about the chosen axis. A flow is **without swirl** when \(u_\theta=0\).

## Related quantities

The [[fluid-dynamics/angular-velocity|angular velocity]] is \(u_\theta/r\), and the [[fluid-dynamics/specific-angular-momentum|specific angular momentum]] about the axis is \(r u_\theta\). These differ from the linear azimuthal velocity by factors of radius. Some authors use “swirl” for \(r u_\theta\); a formula or explicit convention resolves that terminology.

Axisymmetry permits swirl. It requires independence of \(\theta\) in the cylindrical components, not that the azimuthal component vanish.

## References

- [Ben Pineau, Notes for Beale–Kato–Majda Blowup Criterion and Some Applications, axisymmetric Euler section](https://math.berkeley.edu/~sjoh/2020-spring-rs/pdfs/pineau_fluid_presentation.pdf).
