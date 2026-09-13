+++
id = "partial-differential-equations/newtonian-fundamental-solution-three-dimensions"
title = "Newtonian fundamental solution in three dimensions"
kind = "theorem"
summary = "One over four pi times radius is a distributional fundamental solution of minus the Laplacian."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/poisson-equation", "functional-analysis/dirac-delta-distribution", "functional-analysis/distributional-derivative", "differential-geometry/stokes-theorem", "real-analysis/pi", "measure-theory/locally-integrable-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

In \(\mathbb R^3\), the locally integrable function
\[
\Gamma(x)=\frac1{4\pi|x|}\quad(x\ne0)
\]
satisfies \(-\Delta\Gamma=\delta_0\) in distributions, where \(\delta_0\) is the [[functional-analysis/dirac-delta-distribution|Dirac delta]]. It is the **Newtonian fundamental solution of \(-\Delta\)** in three dimensions.

## Flux verification

Away from zero, the radial Laplacian gives \(\Delta\Gamma=0\). Integrate by parts against a test function outside the ball of radius \(\varepsilon\). The inner boundary term involving \(\Gamma\nabla\varphi\) tends to zero; the term involving \(\partial_r\Gamma=-1/(4\pi\varepsilon^2)\) tends to \(\varphi(0)\). Thus \(\langle-\Delta\Gamma,\varphi\rangle=\varphi(0)\).

## References

- [Hunter, Laplace equation, §2.6](https://www.math.ucdavis.edu/~hunter/pdes/ch2.pdf).
