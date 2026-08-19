+++
id = "harmonic-analysis/poisson-kernel-upper-half-plane"
title = "Poisson kernel of the upper half-plane"
kind = "definition"
summary = "The positive unit-mass kernel that harmonically extends boundary data from the real line to the upper half-plane."
aliases = ["upper-half-plane Poisson kernel", "Poisson kernel on H"]
domains = ["harmonic-analysis", "complex-analysis", "partial-differential-equations"]
section_mode = "progressive"
+++

For \(y>0\), the **Poisson kernel of the upper half-plane** is
\[
P_y(t)=\frac1\pi\frac{y}{t^2+y^2},\qquad t\in\mathbb R.
\]
It is positive, integrates to \(1\), and is
[[complex-analysis/harmonic-function|harmonic]] as a function of
\(t+iy\in\mathbb H\).

## Approximate identity

As \(y\downarrow0\), the family \(P_y\) concentrates at the origin. Therefore
\(P_y*f\to f\) in standard \(L^p\) regimes and at Lebesgue points. The
convolution \(P_y*f\) is the
[[harmonic-analysis/poisson-extension-upper-half-plane|Poisson extension]] of
\(f\).

## Scaling

\(P_y(t)=y^{-1}P_1(t/y)\). This scaling explains the equivalent formula
\(\int f(x+ty)/(1+t^2)\,dt/\pi\) used in linewise extensions.

## References

1. Elias M. Stein and Rami Shakarchi, *Complex Analysis*, Princeton University Press, 2003. [DOI record](https://doi.org/10.1515/9781400831159).
