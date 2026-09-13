+++
id = "real-analysis/weighted-moment-projection"
title = "Projection removing one weighted moment"
kind = "definition"
summary = "Subtracting a fixed normalized bump removes an integral obstruction linearly."
aliases = ["normalized bump subtraction"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/weighted-radial-moment", "differential-geometry/bump-function", "linear-algebra/linear-map", "measure-theory/lebesgue-integral", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Fix a smooth compactly supported \(\rho\) in a positive radial interval with \(\int r^e\rho(r)\,dr=1\). The map
\[
P_ef=f-\rho\int r^ef(r)\,dr
\]
is a linear **weighted-moment projection**: its output has zero [[real-analysis/weighted-radial-moment|weighted moment]], and \(P_e^2=P_e\).

## Splitting an obstruction

The identity \(f=P_ef+\rho M_e(f)\) isolates the scalar obstruction to a supported primitive. With extra parameters, the obstruction is a function of those parameters. The bump is fixed independently of \(f\); making it depend on the current input would change the linearity and difference formulas. The support of the output lies in the union of the source support and the fixed bump support.
