+++
id = "harmonic-analysis/pulse-envelope"
title = "Pulse envelope"
kind = "definition"
summary = "A positive scalar function used to bound the amplitude of a localized pulse."
aliases = []
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/exponential-function", "real-analysis/antiderivative", "asymptotics/uniform-parameter-estimate"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **pulse envelope** is a positive function \(P(v)\) used in a bound such as \(|a(v)|\le C P(v)\) for a pulse amplitude. For a prescribed continuous net growth rate \(g\) and reference point \(v_0\), one useful choice is
\[
P(v)=\exp\left(\int_{v_0}^{v}g(s)\,ds\right).
\]
Then \(P(v_0)=1\) and \(P'=gP\). The [[real-analysis/exponential-function|exponential]] is positive, so ratios \(P(v)/P(w)\) are well-defined.

## Growth followed by decay

If \(g\) is positive before \(v_0\) and negative afterward, this envelope has a maximum at \(v_0\). In an amplitude equation \(g\) can represent amplification minus viscous damping. Bounds for each derivative of \(a\) must still be proved separately; an envelope inequality on values does not imply smoothness of \(a/P\) or a zero extension at an endpoint.
