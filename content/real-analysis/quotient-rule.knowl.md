+++
id = "real-analysis/quotient-rule"
title = "Quotient rule"
kind = "definition"
summary = "Differentiation of f/g at a point where g is nonzero."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/product-rule", "real-analysis/chain-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If \(f,g\) are differentiable at \(x\) and \(g(x)\ne0\), then \(g\) stays nonzero near \(x\) and
\[
\left(\frac fg\right)'(x)=\frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2}.
\]
This follows by applying the [[real-analysis/product-rule|product rule]] to \(f\cdot g^{-1}\) and the chain rule to the reciprocal. The same formula holds for each partial derivative.

## Vanishing denominators

The formula does not define a quotient at a zero of \(g\). A separate extension argument may remove a particular singularity, for example \(r^{-1}\partial_r a(r^2)=2a'(r^2)\) for smooth \(a\). Such cancellation must be established before claiming regularity on the axis.
