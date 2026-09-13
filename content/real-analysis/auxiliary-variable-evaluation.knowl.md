+++
id = "real-analysis/auxiliary-variable-evaluation"
title = "Evaluation along an auxiliary map"
kind = "definition"
summary = "Composition of a function of independent physical and periodic auxiliary variables with a prescribed auxiliary map."
aliases = ["auxiliary phase evaluation", "auxiliary phase map"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["shared-foundations/composition-of-functions", "real-analysis/periodic-function", "real-analysis/chain-rule-multivariable"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(F(x,Y)\) be smooth and \(\mathbb Z^k\)-periodic in the independent auxiliary variable \(Y\), and let \(\Psi:U\subset\mathbb R^n\to\mathbb R^k\) be smooth. **Evaluation along the auxiliary map** is the [[shared-foundations/composition-of-functions|composition]]
\[
F^\sharp(x)=F(x,\Psi(x)).
\]
Replacing \(\Psi\) by an integer translate leaves \(F^\sharp\) unchanged. Compatible local lifts therefore also define this operation for a map into a torus.

## Derivatives after evaluation

The [[real-analysis/chain-rule-multivariable|chain rule]] gives
\[
\partial_{x_j}F^\sharp=
\left(\partial_{x_j}F+\sum_{a=1}^k
\partial_{x_j}\Psi_a\,\partial_{Y_a}F\right)_{Y=\Psi(x)}.
\]
The first derivative on the right holds \(Y\) fixed. For \(\Psi(r,t)=v_r h(r)+v_t t\), the evaluated radial and time derivatives are represented before restriction by \(\partial_r+h'(r)v_r\cdot\nabla_Y\) and \(\partial_t+v_t\cdot\nabla_Y\). Auxiliary periodicity need not yield physical spatial periodicity. Auxiliary averaging is performed before restriction unless explicitly stated otherwise.
