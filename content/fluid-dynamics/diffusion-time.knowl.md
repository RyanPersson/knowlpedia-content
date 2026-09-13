+++
id = "fluid-dynamics/diffusion-time"
title = "Viscous diffusion time scale"
kind = "definition"
summary = "The characteristic time L²/ν for viscosity to act across a length L."
aliases = ["diffusion time"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/viscosity", "shared-foundations/real-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For length \(L>0\) and [[fluid-dynamics/viscosity|kinematic viscosity]] \(\nu>0\), the **viscous diffusion time scale** is
\[
t_{\mathrm{diff}}=\frac{L^2}{\nu}.
\]
Balancing \(\partial_tu\) against \(\nu\Delta u\) at spatial scale \(L\) gives \(U/t_{\mathrm{diff}}\) of size \(\nu U/L^2\), yielding this scale.

## Interpretation

This is a characteristic scale, not an exact decay time for every solution. A Fourier mode of wave number magnitude \(k\) under pure diffusion decays like \(e^{-\nu k^2t}\), with decay time \((\nu k^2)^{-1}\); a convention for wavelength introduces corresponding numerical factors.
