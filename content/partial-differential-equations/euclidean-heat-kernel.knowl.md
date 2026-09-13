+++
id = "partial-differential-equations/euclidean-heat-kernel"
title = "Euclidean heat kernel"
kind = "definition"
summary = "The normalized Gaussian that propagates the heat equation on Euclidean space."
aliases = ["heat kernel", "Gaussian heat kernel"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/heat-equation", "real-analysis/gaussian-integral", "real-analysis/exponential-function", "linear-algebra/euclidean-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(t>0\) and \(x\in\mathbb R^n\), the **Euclidean heat kernel** with diffusivity \(\nu>0\) is
\[
G_\nu(t,x)=(4\pi\nu t)^{-n/2}\exp\!\left(-\frac{|x|^2}{4\nu t}\right).
\]
It is positive, has integral one in \(x\), and solves the [[partial-differential-equations/heat-equation|heat equation]] for positive time.

## Normalization and concentration

The Gaussian integral proves the mass normalization, and direct differentiation proves \(\partial_tG_\nu=\nu\Delta G_\nu\). Its scaling is \(G_\nu(t,x)=(\nu t)^{-n/2}G_1(1,x/\sqrt{\nu t})\). For each fixed \(\delta>0\), the integral over \(|x|>\delta\) tends to zero as \(t\downarrow0\). The time-zero limit is a point mass in the distributional sense, not an ordinary integrable function.

## References

- [Hunter, The Heat and Schrödinger Equations, §§5.1–5.3](https://www.math.ucdavis.edu/~hunter/pdes/ch5.pdf).
