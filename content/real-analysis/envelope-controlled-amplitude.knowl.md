+++
id = "real-analysis/envelope-controlled-amplitude"
title = "Envelope-controlled amplitude"
kind = "definition"
summary = "A smooth coefficient whose derivatives obey prescribed pointwise spatial and temporal envelopes."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/weighted-coefficient-class", "real-analysis/nonnegative-square-root", "real-analysis/modulus-on-c"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Use the domain and parameters of a [[real-analysis/weighted-coefficient-class|weighted coefficient class]], and fix an additional pointwise envelope \(0<P(x)\le1\). An **envelope-controlled amplitude** of order \(\alpha\), denoted here by \(a\in\mathcal A^\alpha(w,P)\), satisfies for every \(I\),
\[
|\partial_x^I a_{\varepsilon,\lambda}(x)|
\le C_I\varepsilon^\alpha\Lambda_\varepsilon^{m_I}
\sqrt{w(x)}\,\delta(x)^{-n_I}P(x),
\]
with the same uniformity convention and a common parameter domain. Complex amplitudes are measured by their modulus.

## Scope of an amplitude bound

The estimate controls the coefficient before any oscillatory exponential is attached. Differentiating a full oscillatory field also differentiates its phase. The inequality does not assert smoothness of \(a/P\), divisibility by a cutoff, or smooth zero extension across a temporal endpoint. Such properties require their own hypotheses. No derivative of \(P\) is taken when reading this pointwise bound.
