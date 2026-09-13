+++
id = "harmonic-analysis/carrier-frequency"
title = "Carrier frequency parameter"
kind = "definition"
summary = "A selected base oscillation rate whose integer multiples label the harmonics of an ansatz."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/oscillatory-phase", "harmonic-analysis/fourier-harmonic"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

In an expansion \(\sum_m a_m e^{i\kappa m\Phi}\), the chosen positive number \(\kappa\) is a **carrier frequency parameter**. The integer \(m\) is the harmonic multiplier; \(\kappa m\Phi\) is the full phase. This convention separates the common rapid oscillation scale from its [[harmonic-analysis/fourier-harmonic|harmonics]].

## Periodicity and physical scale

If \(\Phi=p\theta+\Phi_0\) with \(\theta\) of period \(2\pi\) and \(\Phi_0\) independent of \(\theta\), then \(e^{i\kappa\Phi}\) is angularly periodic precisely when \(\kappa p\in\mathbb Z\). The physical wavevector of harmonic \(m\) is \(\kappa m\nabla\Phi\). A carrier parameter, a dyadic localization scale, and the physical wavenumber serve different roles.
