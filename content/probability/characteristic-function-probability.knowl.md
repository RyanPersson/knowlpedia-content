+++
id = "probability/characteristic-function-probability"
title = "Characteristic function"
kind = "knowl"
summary = "The complex-valued function t ↦ E[exp(i t X)] associated with a real-valued random variable."
aliases = ["characteristic-function-probability", "Characteristic function"]
domains = ["probability"]
prerequisites = ["probability/random-variable"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "probability/characteristic-function-probability.md"
+++

The **characteristic function** of a real-valued [[probability/random-variable|random variable]] \(X\) is the function \(\varphi_X:\mathbb R\to\mathbb C\) defined by
\[
\varphi_X(t)=\mathbb E[e^{itX}].
\]

## Remarks

The expectation always exists because \(|e^{itX}|=1\). The characteristic function determines the [[probability/distribution-law|distribution]] of \(X\). It is related to the [[probability/moment-generating-function|moment-generating function]] when the latter exists near \(0\).

## Examples

- If \(X\sim\mathcal N(\mu,\sigma^2)\), then \(\varphi_X(t)=\exp(i\mu t-\tfrac12\sigma^2t^2)\).
- If \(X\sim\operatorname{Bernoulli}(p)\), then \(\varphi_X(t)=(1-p)+pe^{it}\).
