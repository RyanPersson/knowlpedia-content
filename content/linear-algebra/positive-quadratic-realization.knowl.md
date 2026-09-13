+++
id = "linear-algebra/positive-quadratic-realization"
title = "Positive realization by squared amplitudes"
kind = "theorem"
summary = "An invertible linear combination of squared amplitudes realizes targets with positive inverse coordinates."
aliases = ["squared-amplitude representation"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quadratic-map", "linear-algebra/matrix-inverse", "linear-algebra/hadamard-product", "real-analysis/nonnegative-square-root", "real-analysis/class-ck-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an invertible real \(m\times m\) matrix \(H\), define the [[linear-algebra/quadratic-map|quadratic map]]
\[
Q(a)=H(a\odot a).
\]
If \(y=H^{-1}T\) has strictly positive components, then \(a_j=\sqrt{y_j}>0\) gives \(Q(a)=T\). This selects the positive amplitude branch uniquely.

## Parameters and boundary behavior

If \(H,T\) depend smoothly on parameters and the inverse coordinates remain positive, the selected amplitudes are smooth by matrix inversion and the smoothness of the positive square root. At a boundary where a coordinate tends to zero, smoothness of its square root needs additional control. A nonnegative smooth function can have a nonsmooth square root; positivity in the interior alone does not settle extension through the boundary.
