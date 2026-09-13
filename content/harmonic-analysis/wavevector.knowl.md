+++
id = "harmonic-analysis/wavevector"
title = "Local wavevector"
kind = "definition"
summary = "The spatial gradient of the full angular phase of an oscillatory field."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/oscillatory-phase", "real-analysis/gradient"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For the factor \(e^{i\Psi(t,x)}\), the **local wavevector** is
\[
k(t,x)=\nabla_x\Psi(t,x).
\]
If \(\Psi=\kappa\Phi\) with constant \(\kappa\), then \(k=\kappa\nabla\Phi\). The [[real-analysis/gradient|gradient]] points normally to the local constant-phase surfaces where it is nonzero.

## Plane waves and conventions

For \(e^{i(k_0\cdot x-\omega t)}\), the wavevector is the constant \(k_0\). In the convention \(e^{2\pi i\xi\cdot x}\), it is \(2\pi\xi\). Thus a Fourier frequency measured in cycles per unit length and an angular wavevector differ by \(2\pi\).
