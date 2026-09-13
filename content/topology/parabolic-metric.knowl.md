+++
id = "topology/parabolic-metric"
title = "Parabolic metric on space-time"
kind = "definition"
summary = "A space-time metric in which a time separation has the size of its square root."
aliases = ["parabolic distance", "parabolic cylinder"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/metric", "linear-algebra/euclidean-norm", "real-analysis/nonnegative-square-root"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **parabolic metric** on \(\mathbb R^n\times\mathbb R\) is
\[
d_p((x,t),(y,s))=\max\{|x-y|,\sqrt{|t-s|}\}.
\]
The triangle inequality follows from the Euclidean triangle inequality and \(\sqrt{a+b}\le\sqrt a+\sqrt b\). The map \((x,t)\mapsto(\lambda x,\lambda^2t)\) multiplies this distance by \(\lambda>0\).

## Balls and scaling

A ball of radius \(r\) is \(B_r(x)\times(t-r^2,t+r^2)\). Its space-time Lebesgue volume is a dimensional constant times \(r^{n+2}\). A backward cylinder uses \(B_r(x)\times(t-r^2,t)\); it respects the same space-time scaling but is not a metric ball centered at \((x,t)\).
