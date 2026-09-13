+++
id = "harmonic-analysis/oscillatory-modulation"
title = "Oscillatory modulation"
kind = "definition"
summary = "Multiplication of a coefficient by a rapidly varying complex phase factor."
aliases = ["high-frequency modulation"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/wave-amplitude", "real-analysis/chain-rule-multivariable", "real-analysis/product-rule", "real-analysis/laplacian"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **oscillatory modulation** of a coefficient \(a\) by a phase \(\Phi\) is \(a e^{i\kappa\Phi}\). For smooth \(a,\Phi\), the product and chain rules give
\[
\partial_j(ae^{i\kappa\Phi})
=e^{i\kappa\Phi}(\partial_ja+i\kappa a\partial_j\Phi).
\]
Thus estimates on the [[harmonic-analysis/wave-amplitude|amplitude]] alone do not control derivatives of the full wave independently of \(\kappa\).

## Second derivatives

Componentwise for a vector amplitude,
\[
\Delta(ae^{i\kappa\Phi})=e^{i\kappa\Phi}
\left(\Delta a+2i\kappa\nabla\Phi\cdot\nabla a
+i\kappa(\Delta\Phi)a-\kappa^2|\nabla\Phi|^2a\right).
\]
For example, \(\varepsilon\sin(x/\varepsilon)\) is small in value but has order-one first derivative. Frequency powers and amplitude powers must both be included when estimating a modulated field.
