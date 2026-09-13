+++
id = "real-analysis/chain-rule-for-iterated-torus-variables"
title = "Chain rule for iterated torus variables"
kind = "theorem"
summary = "Integer matrix iterations amplify auxiliary directional derivatives by their action on the direction vector."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/auxiliary-variable-evaluation", "topology/integer-matrix-torus-cover", "linear-algebra/eigenvector", "real-analysis/chain-rule-multivariable"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(Y(x)\in\mathbb T^n\) be smooth and \(F(x,H)\) smooth and periodic in \(H\). For a fixed integer \(i\ge0\), define
\[
u(x)=F(x,J^iY(x)).
\]
The [[real-analysis/chain-rule-multivariable|chain rule]] gives
\[
\partial_{x_a}u=\left(\partial_{x_a}F+
(J^i\partial_{x_a}Y)\cdot\nabla_HF\right)_{H=J^iY(x)}.
\]
Local lifts of \(Y\) give the same answer because \(J\) is integral and \(F\) is periodic.

## Eigenvector directions

If \(Y(r,t)=v_rh(r)+v_tt\) and \(Jv_r=\lambda_rv_r\), \(Jv_t=\lambda_tv_t\), then the represented derivatives are \(\partial_r+\lambda_r^i h'(r)v_r\cdot\nabla_H\) and \(\partial_t+\lambda_t^i v_t\cdot\nabla_H\). The discrete level \(i\) and all sheet labels are held fixed. A level selected by a floor function is not a differentiable variable; separate smooth band formulas must be combined with their cutoffs.
