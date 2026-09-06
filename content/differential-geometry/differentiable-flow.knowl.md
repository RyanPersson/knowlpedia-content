+++
id = "differential-geometry/differentiable-flow"
title = "Differentiable flow"
kind = "definition"
summary = "A C1 action of the real line on a manifold by differentiable time maps."
domains = ["differential-geometry", "dynamical-systems"]
prerequisites = ["fiber-bundles/smooth-manifold", "real-analysis/differentiable-map", "shared-foundations/real-numbers", "shared-foundations/composition"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

Let \(N\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. A **differentiable flow** on \(N\) is a map \(\varphi:\mathbb R\times N\to N\) that is continuously differentiable in local manifold charts. Write \(\varphi_t(x)=\varphi(t,x)\). The required flow laws are
\[
\varphi_0=\operatorname{id}_N,\qquad
\varphi_{t+s}=\varphi_t\circ\varphi_s\quad(s,t\in\mathbb R).
\]
## Time maps and local flows

Consequently each time map is invertible, with continuously differentiable inverse \(\varphi_{-t}\).

This definition is global in time: all real \(t\) are allowed. A local flow only has time maps on suitable open subsets of \(\mathbb R\times N\).

## Reference

[Ko Honda, Differential Geometry Course Notes, §30](https://www.math.ucla.edu/~honda/math225a/revised%20course%20notes.pdf).
