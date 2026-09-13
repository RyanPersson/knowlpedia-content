+++
id = "real-analysis/laplacian"
title = "Euclidean Laplacian"
kind = "definition"
summary = "The sum of the unmixed second Cartesian partial derivatives."
aliases = ["Laplace operator", "vector Laplacian"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/partial-derivative", "real-analysis/class-ck-map", "shared-foundations/finite-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **Euclidean Laplacian** of a [[real-analysis/class-ck-map|\(C^2\)]] scalar function is
\[
\Delta f=\sum_{i=1}^n\partial_{x_i}^2 f.
\]
For a vector field it acts on Cartesian components: \((\Delta u)_i=\Delta u_i\). This convention has Fourier symbol \(-|\xi|^2\) when derivatives have symbol \(i\xi\).

## Cylindrical coordinates

For scalar functions on \(r>0\), set
\[
L=\partial_r^2+r^{-1}\partial_r+r^{-2}\partial_\theta^2+\partial_z^2.
\]
Then \(\Delta f=Lf\). For cylindrical vector components,
\[
\begin{aligned}
(\Delta u)_r&=Lu_r-r^{-2}u_r-2r^{-2}\partial_\theta u_\theta,\\
(\Delta u)_\theta&=Lu_\theta-r^{-2}u_\theta+2r^{-2}\partial_\theta u_r,\\
(\Delta u)_z&=Lu_z.
\end{aligned}
\]
These follow by applying \(L\) to \(u_r e_r+u_\theta e_\theta+u_z e_z\) and differentiating the frame. Applying the scalar formula separately to moving components would omit the displayed terms.

## References

- [Arthur Mattuck, MIT 18.02SC, The Del Operator](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/a5910abd3b1b31bdb0c26ff1e0185ef2_MIT18_02SC_MNotes_v15.1.pdf).
- [MIT 6.013, Differential operators in cylindrical and spherical coordinates](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-fall-2005/59e100001186c03a19ca3361dcd3b240_formula_sheet2.pdf).
