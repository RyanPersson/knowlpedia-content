+++
id = "linear-algebra/linearized-squared-amplitude-inverse"
title = "Linearized inverse for squared amplitudes"
kind = "theorem"
summary = "A positive amplitude representation provides a linear inverse for signed target increments, with an exact quadratic remainder."
aliases = ["signed quadratic target correction"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/positive-quadratic-realization", "linear-algebra/right-inverse", "real-analysis/linearization", "linear-algebra/hadamard-product"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(Q(a)=H(a\odot a)\) with \(H\) invertible and all \(a_j>0\), its derivative is \(DQ(a)[h]=2H(a\odot h)\). Therefore the linear map
\[
L\Sigma=\frac12\operatorname{diag}(a)^{-1}H^{-1}\Sigma
\]
is an inverse for this [[real-analysis/linearization|linearization]]:
\[
DQ(a)[L\Sigma]=\Sigma.
\]
It accepts arbitrary signed increments \(\Sigma\).

## Exact remaining error

The complete update satisfies
\[
Q(a+L\Sigma)=Q(a)+\Sigma+H\bigl((L\Sigma)\odot(L\Sigma)\bigr).
\]
The final quadratic term must be retained. The linear identity does not assert that an arbitrary signed finite target is exactly realizable by nonnegative squared amplitudes. In repeated linear corrections the matrix and base amplitudes in \(L\) must be kept at the values used to define that operator, unless a new linearization is explicitly chosen.
