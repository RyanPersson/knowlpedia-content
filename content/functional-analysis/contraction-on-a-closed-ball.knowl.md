+++
id = "functional-analysis/contraction-on-a-closed-ball"
title = "Contraction criterion on a closed norm ball"
kind = "proposition"
summary = "Separate quantitative conditions ensuring that a map preserves a complete ball and contracts it."
aliases = ["invariant ball for contraction", "self-map ball criterion"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/banach-space", "real-analysis/banach-fixed-point-theorem", "topology/closed-ball"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[linear-algebra/banach-space|Banach space]], \(r>0\), and \(B=\{x:\|x-x_0\|\le r\}\). Suppose \(T:B\to X\) satisfies
\[
\|T(x)-T(y)\|\le q\|x-y\|,\qquad q<1,
\quad
\|T(x_0)-x_0\|\le(1-q)r.
\]
Then \(T(B)\subseteq B\), since \(\|T(x)-x_0\|\le qr+(1-q)r\). The ball is complete, so the [[real-analysis/banach-fixed-point-theorem|contraction theorem]] gives a unique fixed point in it.

## Small-parameter form

For \(T(x)=x_0+\varepsilon N(x)\), it suffices that \(|\varepsilon|\sup_B\|N\|\le r\) and \(|\varepsilon|\operatorname{Lip}_B N<1\). A contraction estimate without the self-map condition is insufficient to apply the theorem on the ball.
