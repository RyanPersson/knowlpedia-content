+++
id = "fluid-dynamics/reynolds-number"
title = "Reynolds number"
kind = "definition"
summary = "The dimensionless ratio UL/ν comparing advective and viscous scales."
aliases = ["Reynolds ratio"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/viscosity", "shared-foundations/real-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Given characteristic speed \(U>0\), length \(L>0\), and [[fluid-dynamics/viscosity|kinematic viscosity]] \(\nu>0\), the **Reynolds number** is
\[
\mathrm{Re}=\frac{UL}{\nu}.
\]
It compares the characteristic advective acceleration \(U^2/L\) to the viscous acceleration \(\nu U/L^2\).

## Scale choices

The value depends on the chosen speed and length. In anisotropic or rotating flows, radial transport, azimuthal velocity, tube width, and radius can supply different scales and hence different Reynolds numbers. Each convention should be stated.

## Meaning of a large ratio

A large Reynolds number indicates that advection is large relative to viscosity at the selected scales. It does not by itself prove turbulence, instability, or singularity formation. Finer scales can still have substantial diffusion.
