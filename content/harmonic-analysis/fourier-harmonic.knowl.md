+++
id = "harmonic-analysis/fourier-harmonic"
title = "Fourier harmonic"
kind = "definition"
summary = "A single integer-multiple frequency in a periodic Fourier expansion."
aliases = ["Fourier mode"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-character", "harmonic-analysis/fourier-coefficient"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **\(m\)-th Fourier harmonic** of a one-dimensional periodic function is its component \(\widehat f(m)e^{im\theta}\), for an angular coordinate of period \(2\pi\). The term harmonic can also refer to the [[harmonic-analysis/fourier-character|character]] \(e^{im\theta}\) itself. For real-valued functions, the \(m\) and \(-m\) components combine to a real sinusoidal component.

## Several frequencies

On a unit \(d\)-torus the harmonic index is \(m\in\mathbb Z^d\), and the component is \(\widehat f(m)e^{2\pi i m\cdot x}\). In an ansatz \(a_m e^{ikm\Phi}\), the integer harmonic multiplier \(m\) is distinct from a chosen carrier parameter \(k\). Fourier harmonics are frequency components; they are generally not harmonic functions in the sense \(\Delta f=0\).
