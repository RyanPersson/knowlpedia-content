+++
id = "harmonic-analysis/uniqueness-of-continuous-fourier-series"
title = "Uniqueness of Fourier coefficients for continuous periodic functions"
kind = "theorem"
summary = "A continuous periodic function with every Fourier coefficient zero vanishes identically."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/fourier-coefficient", "real-analysis/uniform-continuity", "real-analysis/geometric-series"]
+++

If a continuous periodic function \(f:\mathbb R\to\mathbb C\) has all [[harmonic-analysis/fourier-coefficient|Fourier coefficients]] zero, then \(f=0\).

## Proof

Rescale the period to one. For \(N\ge1\) let \(K_N(t)=N^{-1}|\sum_{j=0}^{N-1}e^{2\pi ijt}|^2\). It is nonnegative, has integral one over one period by integrating the expanded square, and its expansion is a finite sum of exponentials. Consequently \(\int_{-1/2}^{1/2} f(x-t)K_N(t)\,dt=0\) for every \(x\), by the assumed coefficients.

Given \(\epsilon>0\), [[real-analysis/uniform-continuity|uniform continuity]] on a period gives \(0<\delta<1/2\) with \(|f(x-t)-f(x)|<\epsilon\) for \(|t|\le\delta\). On \(\delta\le|t|\le1/2\), summing the [[real-analysis/geometric-series|geometric series]] gives \(K_N(t)\le1/(N\sin^2(\pi\delta))\). The difference between the integral and \(f(x)\) is bounded by \(\epsilon+2\|f\|_\infty/(N\sin^2(\pi\delta))\). Taking \(N\) to infinity and then \(\epsilon\) to zero gives \(f(x)=0\).
