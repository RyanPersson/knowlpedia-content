+++
id = "complex-analysis/holomorphic-logarithm"
title = "Holomorphic logarithm of a nonvanishing function"
kind = "definition"
summary = "A branch L with exp(L)=f, available on a simply connected domain for a zero-free holomorphic function."
aliases = ["analytic logarithm", "logarithm branch"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["differential-geometry/holomorphic-map", "real-analysis/exponential-function", "complex-analysis/cauchy-integral-theorem", "topology/simply-connected-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **holomorphic logarithm** of a nonvanishing [[differential-geometry/holomorphic-map|holomorphic function]] \(f\) on a domain \(\Omega\) is a holomorphic \(L\) satisfying \(e^{L(z)}=f(z)\). If \(\Omega\) is simply connected, such a logarithm exists. Choosing its value \(L(z_0)\) at one point fixes the branch.

## Construction

The function \(f'/f\) is holomorphic. On a simply connected domain it has a primitive, so define
\[
L(z)=L(z_0)+\int_{z_0}^z\frac{f'(w)}{f(w)}\,dw,
\qquad e^{L(z_0)}=f(z_0).
\]
The derivative of \(fe^{-L}\) is zero and its value at \(z_0\) is one, proving the claim. Any two branches on a connected domain differ by a constant in \(2\pi i\mathbb Z\). Nonvanishing alone does not suffice on arbitrary domains; \(f(z)=z\) on a punctured disc has no single-valued holomorphic logarithm there.

## References

- [Dan Romik, Complex Analysis, §13](https://www.math.ucdavis.edu/~romik/data/uploads/teaching/math205a-2018/complex-analysis-2018.pdf).
