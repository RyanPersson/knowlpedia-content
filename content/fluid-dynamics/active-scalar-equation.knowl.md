+++
id = "fluid-dynamics/active-scalar-equation"
title = "Active scalar equation"
kind = "definition"
summary = "A transport equation whose advecting velocity is determined by the transported scalar."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/transport-equation", "shared-foundations/function", "real-analysis/divergence"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **active scalar equation** couples a [[partial-differential-equations/transport-equation|transport equation]]
\[
\partial_t\theta+u\cdot\nabla\theta=F
\]
to a specified [[shared-foundations/function|rule]] \(u=\mathcal T[\theta]\) determining velocity from the scalar. The rule may include solving an elliptic equation, and often imposes [[real-analysis/divergence|zero divergence]] \(\operatorname{div}u=0\). The domain, data, and operator \(\mathcal T\) are part of the model.

## Feedback

Changing the scalar changes the velocity that transports it. This distinguishes active transport from a passive scalar transported by a separately prescribed velocity. Diffusion or fractional diffusion may also be added.
