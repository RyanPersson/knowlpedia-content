---
title: "Grand-canonical number fluctuation identity"
description: "In the grand canonical ensemble, particle-number fluctuations equal the μ-derivative of the mean: Var(N) = (1/β) ∂⟨N⟩/∂μ = (1/β²) ∂² ln Ξ/∂μ²."
---

## Statement
In the {{< knowl id="grand-canonical-ensemble" section="stat-mech" text="grand canonical ensemble" >}} with grand partition function
$$
\Xi(\beta,\mu)=\mathrm{Tr}\,\exp\!\big(-\beta(H-\mu N)\big),
$$
the particle-number variance satisfies
$$
\mathrm{Var}(N)\;=\;\frac{1}{\beta}\,\frac{\partial}{\partial \mu}\langle N\rangle
\;=\;\frac{1}{\beta^2}\,\frac{\partial^2}{\partial \mu^2}\ln \Xi(\beta,\mu).
$$

## Key hypotheses
- The grand canonical state exists for the given $(\beta,\mu)$ and is differentiable in $\mu$.
- Differentiation under the trace/integral is justified.

## Conclusions
- Number susceptibility (response of $\langle N\rangle$ to $\mu$) equals a fluctuation:
  $\partial_\mu\langle N\rangle = \beta\,\mathrm{Var}(N)$.
- This is the particle-number analog of canonical fluctuation identities (compare {{< knowl id="prop-fluctuation-response-equivalence" text="fluctuation–response equivalence" >}}).

## Proof idea / significance
From $\partial_\mu\ln\Xi=\beta\langle N\rangle$ (see {{< knowl id="prop-grand-canonical-particle-number" section="thermodynamics" text="grand-canonical particle number identity" >}}), differentiate once more in $\mu$:
$\partial_\mu^2\ln\Xi = \beta\,\partial_\mu\langle N\rangle$.
A direct differentiation of the expectation also gives $\partial_\mu\langle N\rangle=\beta\,\mathrm{Var}(N)$ by the same covariance algebra as in the canonical case. This connects compressibility-like responses to equilibrium density fluctuations.
