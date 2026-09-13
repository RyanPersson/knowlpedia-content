+++
id = "harmonic-analysis/principal-value-singular-integral"
title = "Principal-value singular integral"
kind = "definition"
summary = "An integral operator defined by removing a neighborhood of its diagonal and taking a limit."
aliases = ["singular integral operator"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/integral-operator", "real-analysis/cauchy-principal-value", "linear-algebra/euclidean-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a kernel singular at \(x=y\), a **principal-value singular integral** is an operator represented, on a stated class of inputs, by
\[
Tf(x)=\lim_{\varepsilon\downarrow0}\int_{|x-y|>\varepsilon}K(x,y)f(y)\,dy.
\]
This is the radial-truncation version of a [[real-analysis/cauchy-principal-value|principal value]]. Convergence must be specified, for example pointwise almost everywhere or in a norm.

## Cancellation and scope

The limit can exist although the untruncated integral is not absolutely convergent near the diagonal. Symmetry or mean cancellation often supplies this convergence. A size estimate \(|K(x,y)|\le C|x-y|^{-n}\) alone is insufficient: a positive kernel of this size diverges logarithmically on a positive constant near \(x\). Distributional formulas for singular operators may also include a local multiplication term in addition to the principal-value integral.
