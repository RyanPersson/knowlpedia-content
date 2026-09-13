+++
id = "partial-differential-equations/newtonian-potential"
title = "Newtonian potential in three dimensions"
kind = "definition"
summary = "Convolution with the fundamental solution gives a solution of a Poisson equation."
aliases = ["Newtonian convolution potential"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/newtonian-fundamental-solution-three-dimensions", "harmonic-analysis/convolution-on-locally-compact-group", "functional-analysis/test-function-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(f\in C_c^\infty(\mathbb R^3)\), its **Newtonian potential** is
\[
u(x)=(\Gamma*f)(x)=\int_{\mathbb R^3}\frac{f(y)}{4\pi|x-y|}\,dy.
\]
The kernel \(\Gamma\) is the [[partial-differential-equations/newtonian-fundamental-solution-three-dimensions|fundamental solution of \(-\Delta\)]].

## Equation and regularity

The kernel is locally integrable and the source is compactly supported. Distributional differentiation gives \(-\Delta u=f\). Derivatives can be transferred to \(f\), making \(u\) smooth and the equality classical. At large \(|x|\), \(u=O(|x|^{-1})\). Other sources require their own convergence conditions; the displayed integral is not automatically finite for every distribution or every integrable function at every point.

## References

- [Hunter, Laplace equation, §2.6](https://www.math.ucdavis.edu/~hunter/pdes/ch2.pdf).
