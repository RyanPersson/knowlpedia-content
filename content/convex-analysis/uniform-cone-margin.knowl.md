+++
id = "convex-analysis/uniform-cone-margin"
title = "Uniform directional margin inside a cone"
kind = "definition"
summary = "Normalized vectors in a compact subset of an open cone stay a positive distance from its boundary even when their magnitudes vanish."
aliases = ["strict cone margin", "positive directional margin"]
domains = ["convex-analysis"]
section_mode = "progressive"
prerequisites = ["convex-analysis/convex-cone", "linear-algebra/unit-vector", "convex-analysis/distance-function-to-a-set", "topology/compact-set", "topology/extreme-value-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal C\subset\mathbb R^n\setminus\{0\}\) be open and invariant under positive scaling. A family of nonzero vectors \(T(x)\) has a **uniform directional margin** in \(\mathcal C\) if
\[
\operatorname{dist}\!\left(\frac{T(x)}{|T(x)|},\mathbb R^n\setminus\mathcal C\right)\ge\delta>0
\]
for every parameter \(x\). The condition concerns the [[linear-algebra/unit-vector|unit direction]], not a lower bound on \(|T(x)|\).

## Compactness and vanishing amplitudes

If the normalized direction extends continuously to a compact parameter set with values in \(\mathcal C\), its distance from the closed complement has a positive minimum. Hence the margin can persist while \(T\) tends to zero at a boundary. A relative perturbation \(|\Delta T|\le\varepsilon|T|\), for sufficiently small \(\varepsilon\) depending on the margin, keeps the perturbed vector inside the cone. An absolute perturbation bound alone does not give this conclusion near zero.
