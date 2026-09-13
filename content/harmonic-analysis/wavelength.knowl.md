+++
id = "harmonic-analysis/wavelength"
title = "Wavelength"
kind = "definition"
summary = "The spatial distance for a plane wave’s phase to advance by one full cycle."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/wavenumber", "linear-algebra/unit-vector"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a plane wave with nonzero angular wavevector \(k\), its **wavelength** in the direction \(k/|k|\) is
\[
\lambda=\frac{2\pi}{|k|}.
\]
Advancing by this distance changes \(k\cdot x\) by \(2\pi\), leaving the exponential unchanged. The [[harmonic-analysis/wavenumber|wavenumber]] is the reciprocal length with the angular factor included.

## Variable phase

Where \(\nabla\Psi\ne0\), \(2\pi/|\nabla\Psi|\) is a local wavelength from linearizing the phase. For a nonlinear phase it need not be an exact distance between successive crests over a finite interval. If the Fourier convention uses cycles per length \(|\xi|\), the corresponding wavelength is \(1/|\xi|\).
